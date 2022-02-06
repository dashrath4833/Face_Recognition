from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
import os
import numpy as np
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Face Recognition System')
        # TITLE:
        title_lbl = Label(self.root,text="DEVELOPER INFORMATION",font=('times new roman',35,'bold'),bg='white',fg='red')
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #IMAGE:
        img_top = Image.open(r"C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\dev.jpg")
        img_top = img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=47,width=1530,height=720)

        #Frame
        main_frame = Frame(f_lbl,bd=2,bg='white',relief=RIDGE)
        main_frame.place(x=1000,y=0,width=522,height=500)

        #Developer image:
        img_developer = Image.open(r"C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\Dash_ki_pic.jpeg")
        img_developer = img_developer.resize((200,150),Image.ANTIALIAS)
        self.photoimg_developer = ImageTk.PhotoImage(img_developer)

        f_lbl = Label(main_frame,image=self.photoimg_developer)
        f_lbl.place(x=300,y=0,width=200,height=150)

        #DEVELOPER INFO
        dev_label = Label(main_frame,text='Name: Dashrath Singh Kavia',font=('times new roman',13,'bold'),bg='white',fg='black')
        dev_label.place(x=0,y=5)
        dev_label = Label(main_frame,text='Class: B.Tech Final Year',font=('times new roman',13,'bold'),bg='white',fg='black')
        dev_label.place(x=0,y=40)
        dev_label = Label(main_frame,text='Phone No: 9145999212',font=('times new roman',13,'bold'),bg='white',fg='black')
        dev_label.place(x=0,y=80)
        dev_label = Label(main_frame,text='Address: Sewapura Jaipur',font=('times new roman',13,'bold'),bg='white',fg='black')
        dev_label.place(x=0,y=120)
        dev_label = Label(main_frame,text='Technologies: Python, Python DSA, NodeJs, ExpressJs, Mongoose.',font=('times new roman',13,'bold'),bg='white',fg='black')
        dev_label.place(x=0,y=160)
        dev_label = Label(main_frame,text='Sports That I Love: Cricket, Chess',font=('times new roman',13,'bold'),bg='white',fg='black')
        dev_label.place(x=0,y=200)
        dev_label = Label(main_frame,text='Activities that I Like: Driving, Listening Songs',font=('times new roman',13,'bold'),bg='white',fg='black')
        dev_label.place(x=0,y=240)

if __name__ == '__main__':
    root=Tk()
    obj=Developer(root)
    root.mainloop()