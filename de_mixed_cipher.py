cipher_text_usar =list(input("Entar to cipher text : ").upper())
key=list(input("Entar to key: ").upper())
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
def key_usar(letters,key): # لي ترتيف احرف المفتاح دون تكرير الذي يدخله المستخدم
    key_letters = []
    for k in key :
        for le in letters:
            if k == le  and k not in key_letters:
                key_letters.append(k)
    return key_letters
def key_system(letters,key):# لي ترتيب احرفا لتي يدخلها المستخدم مع باقي الحرف بي الترتيب
    key_letters =list(key)
    for k in key:
        for le in letters:
            if le not in key_letters:
                key_letters.append(le)
    return key_letters
def plain_text_usar (letters,cipher_text,key):
    plain_text =[]
    for ciph in cipher_text:
        x=0
        for k in key:
            if ciph ==k :
                plain_text.append(letters[x])
            x=x+1
    finel_plain_text ="".join(plain_text)
    return finel_plain_text
t1 = key_usar(letters,key)
t2 = key_system(letters,t1)
t3 = plain_text_usar (letters,cipher_text_usar,t2)

print(t3)