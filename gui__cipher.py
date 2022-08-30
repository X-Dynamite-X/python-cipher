#!/usr/bin/python3
import flet as f
from flet import ElevatedButton, Row, TextField,Page,Text,Icon,icons,AppBar,AlertDialog, ElevatedButton, OutlinedButton
from flet import * 
import pandas as pan


def main(page: Page):

    def en_caesar (plain_text,key):
        letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        key=int(key)
        cipher_list = []
        for pl in  list(plain_text.upper()):
            x=0
            if ord(pl) == 32:
                cipher_list.append(pl)
            for l in letters:
                if l == pl :
                    cipher_key = (x+key)%26
                    cipher_list.append(letters[cipher_key])
                    break
                x=x+1
        cipher_text="".join(cipher_list)
        return cipher_text
    def de_caesar(cipher,key):
        letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        plain_list = []
        key =int(key)
        for ci in  list(cipher.upper()):
            x=0
            if ord(ci) == 32:
                plain_list.append(ci)
            for l in letters:
                if l == ci :
                    cipher_key = (x-key)%26
                    plain_list.append(letters[cipher_key])
                    break
                x=x+1
        plain_text="".join(plain_list)
        return plain_text
    ############ (شفرة فحينير  vigener ) ############
    def loop_key_vigener(plain_text,key):
        loop_list_key = []
        while len(plain_text) >= len(loop_list_key):
            if  len(plain_text) == len(loop_list_key):
                break
            for k in key :
                if  len(plain_text) == len(loop_list_key):
                    break
                loop_list_key.append(k)
        return loop_list_key
    def index_text(text):
        letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        ind = []
        for te in text:
            x = 0
            for le in letters:
                if le == te :
                    index_text = x
                    ind.append(index_text)
                x=x+1
        return ind
    def index_key(text,key):
        key_index = []
        letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        key = loop_key_vigener(text,key)
        for k in key : 
            x=0
            for le in letters:
                if le ==k:
                    key_ind=x
                    key_index.append(key_ind)
                x=x+1
        return key_index
    def en_vigener(plain_text,key):
        letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        cipher_list=[]
        plain_text = list(plain_text.upper())
        key =list(key.upper())
        ind_key1 = index_key(plain_text,key)
        ind_text = index_text(plain_text)
        for i in range(len(ind_text)):
            cipher_ind = ((ind_text[i]+ind_key1[i])%26)
            cipher_list.append(letters[cipher_ind])
        cipher_text ="".join(cipher_list)
        return cipher_text
    def de_vigener(cipher_text,key):
        letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        plin_list=[]
        cipher_text = list(cipher_text.upper())
        key =list(key.upper())
        ind_key1 = index_key(cipher_text,key)
        ind_text = index_text(cipher_text)
        for i in range(len(ind_text)):
            cipher_ind = ((ind_text[i]-ind_key1[i])%26)
            plin_list.append(letters[cipher_ind])
        plin_text ="".join(plin_list)
        return plin_text
    ############ (شفرة الخلطي  mixed ) ############ 
    def key_list(key,letters):
        key_list = []
        for k in key:
            for le in letters:
                if le == k and k not in key_list:
                    key_list.append(k)
        return key_list
    def key_finesh(key,letters):
        key_list = list(key)
        for k in key_list:
            for le in letters:
                if le not in key_list:
                    key_list.append(le)
        return key_list
    def en_mixed(plain_text,key):
        letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        plain_text = list(plain_text.upper())
        key =list(key.upper())
        key_lis = key_list(key,letters)
        finesh_key = key_finesh(key_lis,letters)
        cipher_list = []
        for plain in plain_text:
            x=0
            for le in letters:
                if plain == le :
                    cipher_list.append(finesh_key[x])
                x=x+1
        cipher_text="".join(cipher_list)
        return cipher_text
    def de_mixed(cipher_text,key):
        letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        cipher_text = list(cipher_text.upper())
        key =list(key.upper())
        key_lis = key_list(key,letters)
        finesh_key = key_finesh(key_lis,letters)
        plain_list = []
        for cipher in cipher_text:
            x=0
            for k in finesh_key:
                if cipher == k :
                    plain_list.append(letters[x])
                x=x+1
        plain_text="".join(plain_list)
        return plain_text
    ############ ( شفرة بيلايفير  beliver ) ############
    def key_matrex(key,letters):
        key_input = []
        for k in key :
            if k == "J":
                key_input.append("I")
            else:
                key_input.append(k)
        key_list0=[]
        for k in key_input:
            for le in letters:
                if k  == le  and  le not in key_list0:
                    key_list0.append(le)
        for k in key_list0:
            for le in letters:
                if le not in key_list0 :
                    key_list0.append(le)
        key_list1 = []
        key_list2 = []
        key_list3 = []
        key_list4 = []
        key_list5 = []
        for i in range(0,5):
            key_list1.append(key_list0[i])
            key_list2.append(key_list0[i+5])
            key_list3.append(key_list0[i+10])
            key_list4.append(key_list0[i+15])
            key_list5.append(key_list0[i+20])
        matrex_key = pan.DataFrame([key_list1,key_list2,key_list3,key_list4,key_list5])
        return matrex_key
    def en_beliver(plain_text,key):
        letters = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        plain_text = list(plain_text.upper())
        key0 =list(key.upper())
        key =key_matrex(key0,letters)
        x = 0
        plain_list = []
        for i in range(len(plain_text)):
            if plain_text != plain_text[x-1]and x>0:
                plain_list.append(plain_text[x])
            elif x==0:
                plain_list.append(plain_text[x])
            else:
                plain_list.append("X")
                plain_list.append(plain_text[x])
            x=x+1
        if len(plain_list)%2 ==1:
            plain_list.append("X")
        loop=int(len(plain_list)/2)
        x = 0
        c1 = 0
        c2 = 0
        r1 = 0
        r2 = 0
        index_cipher = []
        for i in range(loop):
            for col1 in range(5):
                for row1 in range(5):
                    if key[col1][row1] == plain_list[x]:
                        c1 = col1
                        r1 = row1
                        break
            for col2 in range(5):
                for row2 in range(5):
                    if key[col2][row2] == plain_list[x+1]:
                        c2 = col2
                        r2 = row2
                        break
            if c1 == c2 :
                index_cipher.append(key[c1][(r1+1)%5])
                index_cipher.append(key[c2][(r2+1)%5])
            elif r1 == r2 :
                index_cipher.append(key[(c1+1)%5][r1])
                index_cipher.append(key[(c2+1)%5][r2])
            else:
                index_cipher.append(key[c2][r1])
                index_cipher.append(key[c1][r2])
            x=x+2
        cipher_text= "".join(index_cipher)
        return cipher_text
    def de_beliver(cipher_text,key0):
        letters = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        cipher_text = list(cipher_text.upper())
        key0 =list(key0.upper())
        key =key_matrex(key0,letters)
        x=0
        c1 = 0
        c2 = 0
        r1 = 0
        r2 = 0
        plain_list = [] 
        loop =int(len(cipher_text)/2)
        for lis_plain in range(loop):
            for col1 in  range(5):
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
                plain_list.append(key[c1][(r1-1)%5])
                plain_list.append(key[c2][(r2-1)%5])
                
                
            elif r1 == r2 :
                plain_list.append(key[(c1-1)%5][r1])
                plain_list.append(key[(c2-1)%5][r2])
                
                
            else :
                plain_list.append(key[c2][r1])
                plain_list.append(key[c1][r2])
            x=x+2
        plain_text="".join(plain_list)
        return plain_text
    page.bgcolor="black"
    page.window_height
    page.window_width
    # page.window_min_height=600
    # page.window_min_width=600
    page.title = "Flet counter example"
    page.vertical_alignment = "center"
    page.appbar=AppBar(
        leading=Icon(icons.LOCK,color="#17730d",size=50),
        title=Text("cryptography"),
        center_title=True,
        actions=[Icon(icons.LOCK,color="#17730d",size=50)],
        bgcolor="#700c0d"
                    )
    def choice_1(e):
        choos1=choice1.value
        choos2=choice2.value
        if choos1 == "encryption":
            if choos2 == "caesar":
                cipher_text=en_caesar(usar_text.value,key.value)
            elif choos2 == "vigener":
                cipher_text=en_vigener(usar_text.value,key.value)
            elif choos2 == "mixed":
                cipher_text=en_mixed(usar_text.value,key.value)
            elif choos2 == "beliver":
                cipher_text=en_beliver(usar_text.value,key.value)
            text=Text(f"{cipher_text}",color="red",size=17)
            page.add(Row([Text("thes cipher text: ",color="red",size=25)],alignment="center"))
        else:
            if choos2 == "caesar":
                plain_text=de_caesar(usar_text.value,key.value)
            elif choos2 == "vigener":
                plain_text=de_vigener(usar_text.value,key.value)
            elif choos2 == "mixed":
                plain_text=de_mixed(usar_text.value,key.value)
            elif choos2 == "beliver":
                plain_text=de_beliver(usar_text.value,key.value) 
            text=Text(f"{plain_text}",color="red",size=17)
            page.add(Row([Text("thes plain text: ",color="red",size=25)],alignment="center"))
        page.add(Column([text]))
        page.update()
        page.controls.pop(-1)
        page.controls.pop(-1)

    page.auto_scroll=False
    page.scroll="auto"
    choice1 = RadioGroup(content=Row([
    Radio(value="encryption", label="encryption"),
    Radio(value="decryption", label="decryption"),],alignment="center"))
    choice2 = RadioGroup(content=Row([
    Radio(value="caesar", label="caesar"),
    Radio(value="vigener", label="vigener"),
    Radio(value="mixed", label="mixed"),
    Radio(value="beliver", label="beliver"),
    ],alignment="center"))
    submit = ElevatedButton(text='Submit',width=100, on_click=choice_1,bgcolor="#700c0d",color="#fffffe")
    page.add(choice1,choice2)
    usar_text = TextField(label="Entar to text: ",width=300,color="#700c0d",border_radius=30,text_size=17,border_color="#700c0d",min_lines=1,max_lines=10) 
    key = TextField(label="Entar to key: ",width=300,color="#700c0d",border_radius=30,text_size=17,border_color="#700c0d",min_lines=1,max_lines=10)
    page.add(Row([usar_text,key],alignment="center"))
    page.add(Row([submit],alignment="center"))
    def page_resize(e):
        print("New page size:", page.window_width, page.window_height)
    page.on_resize = page_resize
    def window_event(e):
        if e.data == "close":
            page.dialog = confirm_dialog
            confirm_dialog.open = True
            page.update()
    page.window_prevent_close = True
    page.on_window_event = window_event
    def yes_click(e):
        page.window_destroy()
    def no_click(e):
        confirm_dialog.open = False
        page.update()
    confirm_dialog = AlertDialog(
        modal=True,
        title=Text("Please confirm"),
        content=Text("Do you really want to exit this app?"),
        actions=[
            ElevatedButton("Yes", on_click=yes_click),
            OutlinedButton("No", on_click=no_click),
        ],
        actions_alignment="end",
    )
    page.add()


app(target=main,port=8001)

