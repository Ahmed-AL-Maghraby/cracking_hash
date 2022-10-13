#Python Script For crack hash With the Brute Force
# By : Ahmed Kamal
from hashlib import *
from  sys import *
print ("Crack Hash Algorithm : MD5 | SHA1 | SHA512 |SHA256 | SHA224 | SHA384")
hash_value = str(input("Enter the hash value > "))
word__list_path = str(input("Enter ther path of Word List > "))
word_list = open(word__list_path,mode='r')
if len(hash_value) == 32:
    for line in word_list:
        line = line.strip()
        if md5(line.encode()).hexdigest() == hash_value:
            print("================\nHash Type : MD5\nYour password is : \"",line,"\"\n================")
elif len(hash_value) == 40:
    for line in word_list:
        line = line.strip()
        if sha1(line.encode()).hexdigest() == hash_value:
            print("================\nHash Type : SHA1\nYour password is : \"",line,"\"\n================")
elif len(hash_value) == 128:
    for line in word_list:
        line = line.strip()
        if sha512(line.encode()).hexdigest() == hash_value:
            print("================\nHash Type : SHA512\nYour password is : \"",line,"\"\n================")
elif len(hash_value) == 56:
    for line in word_list:
        line = line.strip()
        if sha224(line.encode()).hexdigest() == hash_value:
            print("================\nHash Type : SHA224\nYour password is : \"",line,"\"\n================")
elif len(hash_value) == 96:
    for line in word_list:
        line = line.strip()
        if sha384(line.encode()).hexdigest() == hash_value:
            print("================\nHash Type : SHA384\nYour password is : \"",line,"\"\n================")
elif len(hash_value) == 64:
    for line in word_list:
        line = line.strip()
        if sha256(line.encode()).hexdigest() == hash_value:
            print("================\nHash Type : SHA256\nYour password is : \"",line,"\"\n================")
else :
    print("Invaled value")
