def read_txt(fn):
    with open(fn) as f:
        print(f.read())
    
def read_txt_by_line(fn):
    with open(fn) as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')
            line = f.readline()

def write_txt(fn, text):
    with open(fn, 'w', encoding='utf-8') as f:
        f.write("\n")
        f.write(text)


def append_txt(fn, text):
    with open(fn, 'a', encoding='utf-8') as f:
        f.write(text)


# read_txt('./read_file.py')
# read_txt_by_line('./read_file.py')
# write_txt('./test.txt', 'Hello, world!')
append_txt('./test.txt', '\nHello, Raghu!')