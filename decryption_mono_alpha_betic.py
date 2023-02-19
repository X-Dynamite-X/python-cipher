key= ["A","B","C","D","e","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
    #   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25   

cipher_text = list(input("Entar to cipher text: ").upper())
letters = ["Z","W","A","B","C","X","P","D","Q","R","J","K","U","V","E","F","H","I","T","Y","G","L","M","N","O","S"," "]
        #   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25   

def decryption_mono_alpha_betic(cipher_text,letters,key):
    plin_text_list =[]
    for cipy in cipher_text:
        x=0
        for le in letters:
            if le == cipy:
                plin_text_list.append(key[x])
                break
            x=x+1
    text = "".join(plin_text_list)
    print(text)

decryption_mono_alpha_betic(cipher_text,letters,key)