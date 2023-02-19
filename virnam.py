inp_bits = int(input("Enter the number of bits: "))
# plain_text=list(input("Entar to plain text : ").upper())
def bit_list(inp_bits):
    num=1
    list_bits=[]
    for i in range(inp_bits+1) :
        list_bits.append(num)
        num=num*2
    return list_bits
def text_list_index(plain_text):
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    list_text_indax=[]
    text=""
    for i in range(len(plain_text)):
        for l in range(len(letters)):
            if letters[l] == plain_text[i] :
                list_text_indax.append(l)
    return list_text_indax
def list_01(text_list_index,bit_list):
    text_list_index=text_list_index
    bit_list=bit_list
    x=0
    lis_01 = []
    for i in bit_list:
        if i<=text_list_index[x]:
            bit=i-text_list_index[x]
            lis_01.append(1)
        else:
            lis_01.append(0)
    print(lis_01)
# list_01(text_list_index(plain_text),bit_list(inp_bits))
a=bit_list(inp_bits)
print(a)