ItemInCart = 0
#1st method
 #if ItemInCart !=2 :
    #raise Exception("Test case failed")

#2nd Method

assert (ItemInCart == 0)

try:
    with open('file.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("Hello im still printable")