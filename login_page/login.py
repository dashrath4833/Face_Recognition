from re import L
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from turtle import width
from unicodedata import name
from PIL import Image,ImageTk

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title('Login')
        self.root.geometry('1550x800+0+0')

        #Bgimg:
        bg_img=Image.open(r'C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\login_page\images_login\hackers2.jpg')
        bg_img=bg_img.resize((1550,800),Image.ANTIALIAS)
        self.photo_bg_img=ImageTk.PhotoImage(bg_img)

        f_lbl=Label(self.root,image=self.photo_bg_img)
        f_lbl.place(x=0,y=0,width=1550,height=800)

        #Frame:
        frame=Frame(f_lbl,bg='black')
        frame.place(x=610,y=170,width=340,height=450)

        #Image1:
        img1=Image.open(r'C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\login_page\images_login\LoginIconAppl.png')
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photo_img1=ImageTk.PhotoImage(img1)

        f_lbl1=Label(image=self.photo_img1,bg='black',borderwidth=0)
        f_lbl1.place(x=730,y=175,width=100,height=100)

        #Starting Label:
        get_start = Label(frame,text='Get Started',font=('times new roman',20,'bold'),bg='black',fg='white')
        get_start.place(x=97,y=100)

        #Username Label
        username = Label(frame,text='Username',font=('times new roman',15,'bold'),bg='black',fg='white')
        username.place(x=70,y=155)

        #Username_Entry_fill:
        self.user_entry=ttk.Entry(frame,width=20,font=('times new roman',15,'bold'))
        self.user_entry.place(x=70,y=190)

        
        #password Label
        passwd = Label(frame,text='Passsword',font=('times new roman',15,'bold'),bg='black',fg='white')
        passwd.place(x=70,y=225)
        #Password_Entry_fill:
        self.passwd_entry=ttk.Entry(frame,width=20,font=('times new roman',15,'bold'))
        self.passwd_entry.place(x=70,y=260)


        #Button_Frame
        #Login Button:
        button_frame = Frame(frame,bd=2,bg='black')
        button_frame.place(x=80,y=300,width=300,height=40)

        login_btn=Button(button_frame,command=self.login1,text='Login',font=('times new roman',12,'bold'),bg='red',fg='white',width=19,activeforeground='white',activebackground='red')
        login_btn.grid(row=0,column=0)


        #New User Register
        button_frame1 = Frame(frame,bg='black')
        button_frame1.place(x=80,y=350,width=300,height=40)
        
        new_user_btn=Button(button_frame1,text='New User Register',font=('times new roman',12,'bold'),bg='black',fg='white',width=19,activeforeground='white',activebackground='black')
        new_user_btn.grid(row=0,column=0)

        #Forgot Password:
        button_frame2 = Frame(frame,bd=2,bg='black')
        button_frame2.place(x=80,y=395,width=300,height=40)

        forgot_pswd_btn=Button(button_frame2,text='Forgot Password',font=('times new roman',12,'bold'),bg='black',fg='white',width=19,activeforeground='white',activebackground='black')
        forgot_pswd_btn.grid(row=0,column=0)


    #Function for login button:
    def login1(self):
        if self.user_entry.get()=='' or self.passwd_entry.get()=='':
            messagebox.showerror('Error','All fields should be filled.')
        elif(self.user_entry.get()=='cap' and self.passwd_entry.get()=='ash'):
            messagebox.showinfo('Success','Welcome Here!!!')
        else:
            messagebox.showerror('Error','Invalid username or password!!!')


if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()

