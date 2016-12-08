f = open('mapper_output.txt','r')

for line in f:
    print line.lower(),
    
f.close()