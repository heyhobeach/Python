import tkinter as tk

pokectmonlist=[]
current_num=0

class Pokectmon:
    def __init__(self,id,name,type_,imgpath="Pichu.png"):
        self.id = id
        self.name=name
        self.type_=type_
        self.imgpath=imgpath
        self.img=None
        pokectmonlist.append(self)

    def ShowInfo(self):
        print(f'도감 번호 : {self.id} \n 이름 : {self.name} \n 묘사 : {self.type_} ')


def GUIClear(gui):
    for widget in gui.winfo_children():
        widget.destroy()
    
def DrawGUI(gui,num):
    id_label=tk.Label(gui,text=pokectmonlist[num].id)
    name_label=tk.Label(gui,text=pokectmonlist[num].name)
    type_lable=tk.Label(gui,text=pokectmonlist[num].type_)
    if pokectmonlist[num].img is None:
        pokectmonlist[num].img=tk.PhotoImage(file=pokectmonlist[num].imgpath)
    img_lable=tk.Label(gui,image=pokectmonlist[num].img)
    left_button=tk.Button(gui,text="<-",command=LeftButtonEvent)
    right_button=tk.Button(gui,text="->",command=RightButtonEvent)
    left_button.pack(side="left")
    right_button.pack(side="right")
    id_label.pack()
    name_label.pack()
    type_lable.pack()
    img_lable.pack()
    
def LeftButtonEvent():
    global current_num
    current_num-=1
    GUIClear(gui)
    DrawGUI(gui,current_num)
def RightButtonEvent():
    global current_num
    current_num+=1
    GUIClear(gui)
    DrawGUI(gui,current_num)




#id = 이상해꽃.id
#print(id)
#print(pokectmonlist[0].id)
#pokectmonlist[0].ShowInfo()
#
#포켓몬이름목록 = ["이상해꽃", "파이리", "꼬부기", "피카츄"]
#포켓몬도감번호목록 = [3, 4, 7, 25]
#포켓몬속성목록 = ["풀", "불", "물", "전기"]
#
#
#이상해꽃이름 = "이상해꽃"
#파이리이름 ="파이리"
#꼬부기이름 ="꼬부기"
#피카츄이름 ="피카츄"
#이상해꽃도감번호 =3
#파이리도감번호=4
#꼬부기도감번호=7
#피카츄도감번호=25
#이상해꽃속성="풀"
#파이리속성="불"
#꼬부기속성="물"
#피카츄속성="전기"
"""
... 
다양한 다른 내용들의 피카츄 이름

"""

이상해꽃 = Pokectmon(3, "이상해꽃", "풀","Venusaur.png")
파이리 = Pokectmon(4, "파이리", "불","Charmander.png")
꼬부기 = Pokectmon(7, "꼬부기", "물","Squirtle.png")
피카츄 = Pokectmon(25, "피카츄", "전기","pikachu.png")

gui=tk.Tk()
gui.title("포켓몬 도감")
gui.geometry("500x500")
DrawGUI(gui,current_num)

gui.mainloop()
