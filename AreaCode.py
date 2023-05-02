import sys

if sys.argv[1] == "-s":
    name = ""
    for x in sys.argv[2:]:
        name = name + x
    f = open(name +"list.txt", "w")
    for x in sys.argv[2:]:
        areacode = x
        for y in range(1000000):
            if y > 99999:
                f.write(areacode+str(y)+"\n")
            elif y > 9999:
                f.write(areacode+"0"+str(y)+"\n")
            elif y > 999:
                f.write(areacode+"00"+str(y)+"\n")
            elif y > 99:
                f.write(areacode+"000"+str(y)+"\n")
            elif y > 9:
                f.write(areacode+"0000"+str(y)+"\n")
            else:
                f.write(areacode+"00000"+str(y)+"\n")
    f.close()
else:
    for x in sys.argv[1:]:
        areacode = x
        f = open(areacode +"list.txt", "w")
        for y in range(1000000):
            if y > 99999:
                f.write(areacode+str(y)+"\n")
            elif y > 9999:
                f.write(areacode+"0"+str(y)+"\n")
            elif y > 999:
                f.write(areacode+"00"+str(y)+"\n")
            elif y > 99:
                f.write(areacode+"000"+str(y)+"\n")
            elif y > 9:
                f.write(areacode+"0000"+str(y)+"\n")
            else:
                f.write(areacode+"00000"+str(y)+"\n")
        f.close()