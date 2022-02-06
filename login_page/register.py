from re import L
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from turtle import width
from unicodedata import name
from PIL import Image,ImageTk

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('Register')
        self.root.geometry('1550x800+0+0')

    #Bg-Img
        bg_img=Image.open(r'C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\login_page\images_login\thought-good-morning-messages-LoveSove.jpg')
        bg_img=bg_img.resize((1550,800),Image.ANTIALIAS)
        self.photo_bg_img=ImageTk.PhotoImage(bg_img)

        f_lbl=Label(self.root,image=self.photo_bg_img)
        f_lbl.place(x=0,y=0,width=1550,height=800)




if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()