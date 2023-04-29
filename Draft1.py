def Encrypt(key):
    try:
        path = "plain.png"
        print('Key for encryption : ', key)
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()
        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values ^ key
        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
        print('Encryption Done...')
    except Exception:
        print('Error caught : ', Exception.__name__)

def Decrypt(key):
    try:
        path ="plain.png"
        print('The path of file : ', path)
        print('Key for Decryption : ', key)
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()
        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values ^ key
        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
        print('Decryption Done...')
    except Exception:
        print('Error caught : ', Exception.__name__)
import numpy as np
np.random.seed(177013)
arr1 = np.random.randint(10, size=(10))
arr2=[]
n=int(input("Enter n:"))
x=int(input("Enter x:"))
r=int(input("Enter r:"))
while(n!=0):
    arr2.append(abs(x))
    x=x*r*(1-r)
    n=n-1
array=np.convolve(arr1, arr2)
print(array)
array.flatten()
key=1
for i in array:
    key^=i
print("1: Encrypt\n2:Decrypt\n0: Exit")
ch=1
while(ch in [1, 2]):
    ch=int(input("Enter Choice"))
    if(ch==1):
        Encrypt(key)
    elif(ch==2):
        Decrypt(key)
    else:
        print("Exit")
