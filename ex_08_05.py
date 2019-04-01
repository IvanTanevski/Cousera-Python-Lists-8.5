fname = input("Enter file name: ")
try:
    fhandle = open(fname)
except:
    print("File not found!")
    quit()

count = 0
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        print(words[1])
        count += 1
    
print("There were", count, "lines in the file with From as the first word")
