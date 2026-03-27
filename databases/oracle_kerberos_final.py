"""
oracle_kerberos_final.py
========================
Connect to Oracle using Kerberos/CMU-AD via cx_Oracle thick mode.

Prerequisites:
  1. pip install cx_Oracle
  2. Run script — prompts for password and runs okinit automatically
"""
import os
import sys
import getpass
import subprocess
import cx_Oracle

# =============================================================================
# CONFIGURATION
# =============================================================================
ORACLE_CLIENT = r"c:\oracle19c_64\WINDOWS.X64_193000_client_home\bin"
OKINIT_PATH   = r"c:\oracle19c_64\WINDOWS.X64_193000_client_home\bin\okinit.exe"
KRB5_CCACHE   = r"C:\Users\af60385\krb5cc_AF60385"
KRB5_CONF     = r"C:\oracle19c_64\WINDOWS.X64_193000_client_home\network\admin\krb5.conf"
PRINCIPAL     = "AF60385@US.AD.WELLPOINT.COM"

# Must be set BEFORE makedsn()
os.environ["TNS_ADMIN"] = r"c:\oracle19c_64\WINDOWS.X64_193000_client_home\network\admin"

DB_HOST    = "ihubtopo-u-01.internal.das"
DB_PORT    = 1525
DB_SERVICE = "topou"
DSN        = cx_Oracle.makedsn(DB_HOST, DB_PORT, service_name=DB_SERVICE)

# =============================================================================
def validate():
    ok = True
    print("\n[CHECK] Validating...")
    for label, path in [("Oracle Client", ORACLE_CLIENT),
                        ("okinit",        OKINIT_PATH),
                        ("krb5.conf",     KRB5_CONF)]:
        exists = os.path.exists(path)
        print(f"  [{'OK' if exists else 'MISSING'}] {label}: {path}")
        if not exists:
            ok = False

    sqlnet = os.path.join(os.environ["TNS_ADMIN"], "sqlnet.ora")
    if os.path.exists(sqlnet):
        with open(sqlnet) as f:
            content = f.read().upper()
        if "KERBEROS5" in content:
            print(f"  [OK] sqlnet.ora   : KERBEROS5 found")
        else:
            print(f"  [WARN] sqlnet.ora : KERBEROS5 not found")
            print(f"         Add: SQLNET.AUTHENTICATION_SERVICES = (KERBEROS5)")
            ok = False
    else:
        print(f"  [MISSING] sqlnet.ora: {sqlnet}")
        ok = False

    if not ok:
        sys.exit(1)

# =============================================================================
def run_okinit(principal):
    """
    Obtain Kerberos TGT using Oracle's okinit.
    Writes ticket cache to FILE:KRB5_CCACHE — compatible with cx_Oracle.
    Note: okinit may not accept stdin password on all systems.
    If it fails, run  okinit <principal>  manually then re-run this script.
    """
    print(f"\n[okinit] Obtaining Kerberos TGT for {principal}...")
    password = getpass.getpass(f"[okinit] Enter AD password for {principal}: ")

    try:
        result = subprocess.run(
            [OKINIT_PATH, principal],
            input=password,
            capture_output=True,
            text=True
        )
        # Check cache was written regardless of return code
        if os.path.exists(KRB5_CCACHE) and os.path.getsize(KRB5_CCACHE) > 0:
            print(f"[okinit] TGT obtained. Cache: FILE:{KRB5_CCACHE} ({os.path.getsize(KRB5_CCACHE)} bytes)")
        else:
            stderr_msg = result.stderr.strip() if result.stderr else "no output"
            print(f"[okinit] FAILED: {stderr_msg}")
            print(f"\n  okinit may require an interactive terminal.")
            print(f"  Run manually then re-run script:  okinit {principal}")
            sys.exit(1)

    except FileNotFoundError:
        print(f"[okinit] ERROR: not found at {OKINIT_PATH}")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"[okinit] FAILED: {e.stderr}")
        sys.exit(1)

# =============================================================================
def connect_oracle():
    print(f"\n[DB]  Connecting via cx_Oracle thick mode (Kerberos)...")
    print(f"[DB]  DSN   : {DSN}")
    print(f"[DB]  Cache : FILE:{KRB5_CCACHE}")

    cx_Oracle.init_oracle_client(lib_dir=ORACLE_CLIENT)

    # Empty string triggers Kerberos/external auth (cx_Oracle 8.x)
    # Use "" not "/" — cx_Oracle does not interpret "/" like sqlplus
    conn = cx_Oracle.connect("", dsn=DSN)
    print("[DB]  *** Connected successfully! ***\n")
    return conn

# =============================================================================
def run_queries(conn):
    queries = [
        ("Authenticated identity", "SELECT SYS_CONTEXT('USERENV','AUTHENTICATED_IDENTITY') FROM DUAL"),
        ("Session user",           "SELECT SYS_CONTEXT('USERENV','SESSION_USER') FROM DUAL"),
        ("Auth method",            "SELECT SYS_CONTEXT('USERENV','AUTHENTICATION_METHOD') FROM DUAL"),
        ("DB name",                "SELECT NAME, DB_UNIQUE_NAME FROM V$DATABASE"),
    ]
    print("=" * 60)
    print("  Verification Queries")
    print("=" * 60)
    cursor = conn.cursor()
    for label, sql in queries:
        try:
            cursor.execute(sql)
            row = cursor.fetchone()
            if row:
                print(f"  {label:<30}: {' | '.join(str(c) for c in row)}")
        except Exception as e:
            print(f"  {label:<30}: ERROR - {e}")
    cursor.close()
    conn.close()
    print("\n[DONE] Connection closed.")

# =============================================================================
def main():
    print("=" * 60)
    print("  Oracle Kerberos (CMU-AD) Connection Test")
    print("  Engine : cx_Oracle 8.x thick mode (Oracle Client oci.dll)")
    print("  Auth   : Kerberos via okinit -> FILE: ticket cache")
    print("=" * 60)

    validate()
    run_okinit(PRINCIPAL)

    try:
        conn = connect_oracle()
        run_queries(conn)
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print(f"\n[DB ERROR] {error.message}")
        print("\n  Diagnosis:")
        print("  ORA-01005/01017 : sqlnet.ora not loaded or missing KERBEROS5")
        print("  ORA-12638       : Ticket expired — re-run okinit")
        print("  ORA-01017       : CMU external_name mismatch in dba_users")
        print("  DPI-1047        : oci.dll not found — check ORACLE_CLIENT path")
        sys.exit(1)

if __name__ == "__main__":
    main()