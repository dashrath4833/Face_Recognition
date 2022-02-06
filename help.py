from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
import os
import numpy as np
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Face Recognition System')
        # TITLE:
        title_lbl = Label(self.root,text="Reach Me Here",font=('times new roman',35,'bold'),bg='white',fg='green')
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #IMAGE:
        img_top = Image.open(r"C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\wp2551980.jpg")
        img_top = img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=47,width=1530,height=720)

        #Frame
        main_frame = Frame(f_lbl,bd=2,bg='white',relief=RIDGE)
        main_frame.place(x=440,y=150,width=800,height=50)

        dev_label = Label(main_frame,text='Email: dashrathsingh422233@gmail.com',font=('times new roman',20,'bold'),bg='white',fg='red')
        dev_label.place(x=170,y=7)

if __name__ == '__main__':
    root=Tk()
    obj=Help(root)
    root.mainloop()