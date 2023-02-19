import os
import pandas as pan
def  key():
    key = str(input("Entar to key: ")).upper()
    letters = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    key_n=[]
    for k in key :
        if k == "J":
            key_n.append("I")
        else :
            key_n.append(k)
    list0 = []
    for k in key_n:
        for le in letters:
            if k == le and le not in list0:
                list0.append(k)
    for k in list0:
        for le in letters:
            if le not in list0 :
                list0.append(le)
    list1  = []
    list2  = []
    list3  = [] 
    list4  = [] 
    list5  = []
    for  z in range(0,5):
        list1.append(list0[z])
        list2.append(list0[z+5])
        list3.append(list0[z+10])
        list4.append(list0[z+15])
        list5.append(list0[z+20])
    cube = pan.DataFrame([list1,list2,list3,list4,list5])
    print(cube)
    return cube
def en_beliver(plain,key):
    x=0
    p = []
    for z in range(len(plain)):
        if plain[x] != plain[x-1] and x>0 :
            p.append(plain[x])
        elif x==0:
            p.append(plain[x])
        else:
            p.append("X")
            p.append(plain[x])
        x=x+1
    if len(p)%2==1:
        p.append("X")
    lop = int(len(p)/2) 
    x = 0
    c1 = 0
    c2 = 0
    r1 = 0
    r2 = 0
    index_plain = []
    for i in range(lop):
        for col1 in range(5):
            for rows1 in range(5):
                if key[col1][rows1] == p[x]:
                    c1 = col1
                    r1 = rows1
                    break
        for col2 in range(5):
            for rows2 in range(5):
                if key[col2][rows2] == p[x+1]:
                    c2 = col2
                    r2 = rows2
                    break
        if c1 == c2 :
            index_plain.append(key[c1][(r1+1%5)])
            index_plain.append(key[c2][(r2+1)%5])
        elif r1 == r2 :
            index_plain.append(key[(c1+1%5)][r1])
            index_plain.append(key[(c2+1)%5][r2])
        else:
            index_plain.append(key[c2][r1])
            index_plain.append(key[c1][r2])
        x=x+2
    cipher_text = "".join(index_plain)
    print(f"\ncipher text >> {cipher_text}\n")
def de_beliver(cipher_text,key):
    x=0
    c1 = 0
    c2 = 0
    r1 = 0
    r2 = 0
    index_cipher =[]
    for ciph_len in range(int(len(cipher_text)/2)):
        for col1 in range(5):
            for row1 in range(5):
                if key[col1][row1] == cipher_text[x]:
                    c1 = col1
                    r1 = row1
                    break
        for col2 in range(5):
            for row2 in range(5):
                if key[col2][row2] == cipher_text[x+1]:
                    c2 = col2
                    r2 = row2
                    break
        if c1 == c2 :
            index_cipher.append(key[c1][(r1-1)%5])
            index_cipher.append(key[c2][(r2-1)%5])
            
            
        elif r1 == r2 :
            index_cipher.append(key[(c1-1)%5][r1])
            index_cipher.append(key[(c2-1)%5][r2])
            
            
        else :
            index_cipher.append(key[c2][r1])
            index_cipher.append(key[c1][r2])
            
        x=x+2
    plain_text = "".join(index_cipher)
    print(plain_text)
# key = key()
try:
    print("[1] decryption")
    print("[2] encryption")
    cheese = int(input("Entar to type Cheese :"))
    key = key()
    while 1:
        if cheese == 1 :
            text = list(input("\nEntar to text : ").upper())
            en_beliver(text,key)
        elif cheese == 2 :
            cypher_text = list (input("\nEntar to ciopher text : ").upper())
            de_beliver(cypher_text,key)
except KeyboardInterrupt as e :
    print("\nexit done ! ")