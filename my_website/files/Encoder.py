import re
import matplotlib.pyplot as plt
import PIL
import os
import numpy
import binascii
def encode():
    img = plt.imread("C:\Users\hssteam\Desktop\Jonah.JPG")
    width = len(img[0])
    heigth = len(img)
    secret_message = raw_input("What is the secret message? ")
    new_secret_message = "".join(format(ord(x), 'b') for x in secret_message) #Converts message into binary, got off internet
    new_secret_message_list = [new_secret_message for new_secret_message in re.split(r'(\w{2})', new_secret_message) if new_secret_message] #Splits the message in binary into a list of strings of two, copied off internet
    
    blue_value_list=[]
    
    for x in range(len(img[0])): #algorithm to get all the binary blue values in a list of the image
        for y in range(len(img)):
            blue_value_list.append(bin(img[y,x,2]))
    
    new_blue_value_list =[]
    
    for item in blue_value_list:
        for i in new_secret_message_list:
            new_blue_value_list.append(item[0:8]+i)
    j = 0
    for x in range(len(img[0])): 
        for y in range(len(img)):
            img[y][x][2] = int(new_blue_value_list[j],2)
            j= j + 1
    fig,ax=plt.subplots(1,1)
    ax.imshow(img)
    fig.show()
    new_img = PIL.Image.fromarray(img)
    new_img.save("encoded_image.png")
    return new_img
    
            
    
 
def decode():
    img = plt.imread("encoded_image.png")
    blue_value_list=[]
    for x in range(len(img[0])): #algorithm to get all the binary blue values in a list of the image
        for y in range(len(img)):
            blue_value_list.append(bin(int(img[y][x][2]*256)))
    for i in blue_value_list:
        blue_value_list[7:]
        decoded_message = int(i, 2) 
        binascii.unhexlify('%x' % decoded_message)
    print decoded_message
        
   

decode()


      
         