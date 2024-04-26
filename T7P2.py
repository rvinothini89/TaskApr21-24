#Program to read the contents of a file and display the file content in console
#function to read the file and print it. 
def fRead(fname):
    f = open(fname)
    for x in f:
        print(x)
fRead("names.txt")