plain_text = list(input("Entar to text: ").upper())
key = int(input("Entar to key: "))
def cissar(plain_text,key):
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    text=[]
    x=0
    for pl in plain_text:
        x=0
        if ord(pl) == 32:
            text.append(pl)
        for le in letters:
            if le == pl:
                cipher_key = (x+key)%26
                text.append(letters[cipher_key])
                break
            x=x+1
    tex = "".join(text)
    print(tex)
cissar(plain_text,key)

