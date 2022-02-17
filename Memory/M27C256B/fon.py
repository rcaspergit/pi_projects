import sys
from time import sleep


args = sys.argv[1:]
data = open(args[0],"rb")
data.seek(0x2010)


def build_string_line(inbyte):
    outstring = ""
    littlec = ""
    for i in range(8):
        bit = (inbyte>>i)&1
        if (bit == 1):
            littlec = "*"
        else:
            littlec = " "
        outstring += littlec
    return outstring

for i in range(1024):
    bytes = data.read(16)
    for j in range(16):
        img_line = build_string_line(bytes[j])
        print ("                  " + img_line)    
    sleep(0.5)

data.close()


