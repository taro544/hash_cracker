import os
import hashlib

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

words = []
z = 0
file_location = "/home/shp/Desktop/hashcracker/kelimeler.txt"
the_file = open(file_location,"r")
readed = the_file.read().split("\n")
words.extend(readed)
list_lenght = len(words)

main_hash = input("Main hash :")

for i in range(list_lenght):
    byte_message = bytes(words[i], 'utf-8')
    current_hash = hashlib.md5(byte_message).hexdigest()
    #print(current_hash)

    if current_hash == main_hash:
        cls()
        print("Your hash is :"+main_hash)
        print("Your word is :"+words[i])
        break
    z+=1
    if z == list_lenght and current_hash != main_hash:
        print("Did not find")
