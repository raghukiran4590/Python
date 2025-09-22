import os, fnmatch

def ends_with(fld, search):
    for fn in os.listdir(fld):
        if fn.endswith(search):
            print(fn)

def starts_with(fld, search):
    for fn in os.listdir(fld):
        if fn.startswith(search):
            print(fn)

def pattern_search(fld, search):
    for fn in os.listdir(fld):
        if fnmatch.fnmatch(fn, search):
            print(fn)



# ends_with("./", ".py")
# starts_with("../databases", "test")
pattern_search("./", "*file*.py")