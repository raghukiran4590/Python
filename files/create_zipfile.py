import zipfile

def create_zipfile(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt, zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            zipf.write(file, arcname=file.split('/')[-1])

def add_to_zipfile(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt) as archive:
        for f in files:
            lst = archive.namelist()
            if f not in lst:
                archive.write(f)
            else:
                print(f"File exists in zipfile : {f}")

def read_zip(zipf):
    with zipfile.ZipFile(zipf, 'r') as archive:
        lst = archive.namelist()
        for l in lst:
            zipinfo = archive.getinfo(l)
            print(f"{l} => { zipinfo.file_size} bytes, {zipinfo.compress_type} compress type, {zipinfo.compress_size} compress size")

def extract_file(zipf, fn, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extract(fn, path=path)

def extract_all(zipf, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extractall(path=path)

zip_files = ['./cleanup.py','./file_attributes.py','./glob_search.py']
files_to_add = ["./file_operations.py", "./glob_search.py", "./move_remaining.py"]

# create_zipfile('example.zip', zip_files, 'w')
# add_to_zipfile("./example.zip", files_to_add, 'a')
# read_zip("./example.zip")

# extract_file("./example.zip", "glob_search.py", "./extract")
extract_all("./example.zip", "./extractall")
