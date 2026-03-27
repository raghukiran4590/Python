import subprocess
import getpass
from aiofiles import stderr

principal = "AF35861@us.ad.wellpoint.com"
print(f"Obtaining Kerberos TGT for {principal}...")
try:
    # Example using a password (less secure)
    password = getpass.getpass(f"Enter password for {principal}: ")
    kinit_command = ['kinit', principal]
    # process = subprocess.Popen(kinit_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # stdout, stderr = process.communicate(input=password)
    
    # Example using a keytab file (recommended for scripts)
    # keytab_path = "/path/to/your/user.keytab"
    # kinit_command = ['kinit', '-kt', keytab_path, principal]
    # Ensure the keytab file has secure permissions.
    
    result = subprocess.run(kinit_command, input=password, capture_output=True, text=True, check=True)
    # result.wait()

    if result.returncode == 0:
        print("Kerberos ticket obtained successfully.")
    else:
        print(f"kinit failed. Stderr: {result.stderr}")

except subprocess.CalledProcessError as e:
    print(f"kinit failed: {e.stderr}")
    exit()
