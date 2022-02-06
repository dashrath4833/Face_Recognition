from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import tkinter
from PIL import Image, ImageTk
from student import Student
from train import Train
from attendance import Attendance
from developer import Developer
from help import Help
from face_recognition import Face_Recognition
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Face Recognition System')
        #firstimg
        img = Image.open(r'C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\Stanford.jpg')
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #secondimg
        img1 = Image.open(r'C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\facialrecognition.png')
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #thirdimg
        img2 = Image.open(r'C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\u.jpg')
        img2 = img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #bgimg
        img3 = Image.open(r'C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\bg1.jpg')
        img3 = img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #Title_Label:
        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=('times new roman',35,'bold'),bg='white',fg='red')
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #Student_button
        img4 = Image.open(r'C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\pexels-buro-millennial-1438072.jpg')
        img4 = img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details, cursor='hand2')
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text='Student Details',command=self.student_details, cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=200,y=300,width=220,height=40)

        #Detect_Face Button
        img5 = Image.open(r'C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\face_detector1.jpg')
        img5 = img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,command=self.Face_data,image=self.photoimg5,cursor='hand2')
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,command=self.Face_data,text='Face Detector',cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=500,y=300,width=220,height=40) 


        #Attendance Button
        img6 = Image.open(r'C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\smart-attendance.jpg')
        img6 = img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor='hand2',command=self.Attendance)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text='Attendance',cursor='hand2',command=self.Attendance,font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=800,y=300,width=220,height=40)


        #Help Desk Button
        img7 = Image.open(r'C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg')
        img7 = img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,command=self.help_me,image=self.photoimg7,cursor='hand2')
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text='Help Desk',command=self.help_me,cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=1100,y=300,width=220,height=40)


        #Train Face Button:
        img8 = Image.open(r'C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\Train.jpg')
        img8 = img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,command=self.train_the_data,image=self.photoimg8,cursor='hand2')
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,command=self.train_the_data,text='Train Data',cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=200,y=580,width=220,height=40)


        #Photos Button:
        img9 = Image.open(r'C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\pexels-pixabay-159740.jpg')
        img9 = img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor='hand2')
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text='Photos',command=self.open_img,cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=500,y=580,width=220,height=40)

        
        #Developer Button:
        img10 = Image.open(r'C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\Team-Management-Software-Development.jpg')
        img10 = img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,command=self.DeveloperInfo,image=self.photoimg10,cursor='hand2')
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text='Developer',command=self.DeveloperInfo,cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=800,y=580,width=220,height=40)


        #Exit Button:
        img11 = Image.open(r'C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\exit.jpg')
        img11 = img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img,command=self.iexit,image=self.photoimg11,cursor='hand2')
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text='Exit',command=self.iexit,cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=1100,y=580,width=220,height=40)


    
        
# ================>#FUNCTION BUTTONS:<========================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)

    def open_img(self):
        os.startfile('data')

    def train_the_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def Face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def Attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
     
    def DeveloperInfo(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_me(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    
    def iexit(self):
        self.iExit=tkinter.messagebox.askyesno('Face Recognition','Are you sure you want to exit?',parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


if __name__ == '__main__':
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()