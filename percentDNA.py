count = 0.00


line=open("DNA.txt").read()
for x in range (0,len(line)):
        if(line[x]== 'G' or line[x]== 'C'):
            count = count + 1

print "The file contains", count, "C and G"
percent = (count/len(line))*100
print "The percentage of CG to DNA is", percent, "is"
