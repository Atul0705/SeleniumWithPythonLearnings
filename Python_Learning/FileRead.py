file = open('test.txt')
# print(file.read(7)) #to print chars
# print(file.readline())  #to print whole line

line = file.readline()      #if 100 of line present then use this while loop
while line != "":
    print(line)
    line = file.readline()


file.close()
