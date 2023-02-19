import numpy as n 
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
plain_text = list(input("Entar to plain text : ").upper())
key = list(input("Entar to encrytion key : ").upper())
def len_key(plain_text,key):
    new_key = []
    len_text = len(plain_text)
    while len(new_key) <= len_text:
        if len_text == len(new_key):
            break
        for  k in key :
            if len_text == len(new_key):
                break
            new_key.append(k)
    return new_key
def ind_pl(plain_text):
    numper = []
    x=0
    for pl in plain_text:
        x=0
        for le in letters:
            
            if le == pl:
                pl_index = x
                numper.append(pl_index)
            x=x+1
    return numper
def ind_key(plain_text,key1):
    numper = []
    z=0
    key = len_key(plain_text,key1)
    for k in key:
        z=0
        for le in letters:
            if le == k:
                key_index=z
                numper.append(key_index)
            z=z+1
    return numper
def vagenir(plain_text,letters,key1):
    text=[]
    ind_key1=ind_key(plain_text,key1)
    ind_pl1=ind_pl(plain_text)
    for x in range(len(ind_pl1)):
        cipher_key = ((ind_key1[x]+ind_pl1[x])%26)
        text.append(letters[cipher_key])
        tex = "".join(text)
    print(tex)

vagenir(plain_text,letters,key)
