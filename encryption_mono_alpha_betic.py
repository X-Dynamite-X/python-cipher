letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
plain_text = list(input("Entar to plain text: ").upper())
key =     ["Z","W","A","B","C","X","P","D","Q","R","J","K","U","V","E","F","H","I","T","Y","G","L","M","N","O","S"," "]
    #   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25   

def encryption_mono_alpha_betic(plain_text,letters,key):
    cipher_text_list =[]
    for plin in plain_text:
        x=0
        for le in letters:
            if le == plin:
                cipher_text_list.append(key[x])
                break
            x=x+1
    text = "".join(cipher_text_list)
    print(text)

encryption_mono_alpha_betic(plain_text,letters,key)