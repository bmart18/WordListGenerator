
areacode="440"

f = open(areacode +"list.txt", "w")
for x in range(1000000):
    if x > 99999:
        f.write(areacode+str(x)+"\n")
    elif x > 9999:
        f.write(areacode+"0"+str(x)+"\n")
    elif x > 999:
        f.write(areacode+"00"+str(x)+"\n")
    elif x > 99:
        f.write(areacode+"000"+str(x)+"\n")
    elif x > 9:
        f.write(areacode+"0000"+str(x)+"\n")
    else:
        f.write(areacode+"00000"+str(x)+"\n")
f.close()