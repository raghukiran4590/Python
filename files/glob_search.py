from pathlib import Path

def glob_match(fld, search) :
    # p = Path(fld).glob(search)
    p = Path(fld)
    for n in p.glob(search):
        print(n)

glob_match(".", "*_*")