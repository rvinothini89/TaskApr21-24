#Program to create a new file with current timestamp as data
import time
def newFile():
    #As the file is text file and accepts only string, typecasted timestamp to string
    #Creating text file name with current timestamp
    ts = time.time()
    ts = str(ts)
    fname = "myFile"+ts+".txt"
    f = open(fname,"x")    
    f.write(ts)
newFile()