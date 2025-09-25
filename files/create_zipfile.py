import zipfile

def create_zipfile(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt, zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            zipf.write(file, arcname=file.split('/')[-1])

zip_files = ['./cleanup.py','./file_attributes.py','./glob_search.py']

create_zipfile('example.zip', zip_files, 'w')
