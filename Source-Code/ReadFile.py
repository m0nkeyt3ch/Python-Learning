def file_read(fname):
    txt = open(fname)
    print(txt.read())

fname = "text.txt"
file_read(fname)