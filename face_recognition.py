from distutils.command.config import config
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib.pyplot import gray
import mysql.connector
from student import Student
from train import Train
import os
import cv2
from time import strftime
from datetime import datetime
class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Recognising the face')

        #TITLE
        title_lbl = Label(self.root,text="FACE RECOGNISATION",font=('times new roman',35,'bold'),bg='white',fg='red')
        title_lbl.place(x=0,y=0,width=1530,height=50)


        #First Image
        img_first = Image.open(r"C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\face_detector1.jpg")
        img_first = img_first.resize((650,700),Image.ANTIALIAS)
        self.photoimg_first = ImageTk.PhotoImage(img_first)

        f_lbl = Label(self.root,image=self.photoimg_first)
        f_lbl.place(x=0,y=50,width=650,height=700)

        
        #Second Image
        img_second = Image.open(r"C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_second = img_second.resize((950,700),Image.ANTIALIAS)
        self.photoimg_second = ImageTk.PhotoImage(img_second)

        f_lbl = Label(self.root,image=self.photoimg_second)
        f_lbl.place(x=651,y=50,width=950,height=700)

        #Button in second image
        b1_1=Button(f_lbl,text='Face Recognisation',command=self.face_recognise,cursor='hand2',font=('times new roman',15,'bold'),bg='darkgreen',fg='white')
        b1_1.place(x=365,y=620,width=200,height=40)

#=================>Attendance System<====================================
    def mark_attendance(self,i,r,n,d):
        with open('attendance_register.csv','r+',newline='\n') as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((','))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                day_string=now.strftime('%d/%m/%Y')
                time_string=now.strftime('%H:%M:%S')
                f.writelines(f'\n{i},{r},{n},{d},{time_string},{day_string},Present')



#=================>Face recognisation Function<==========================
    def face_recognise(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf): #
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w]) #
                confidence=int((100*(1-predict/300)))
                conn=mysql.connector.connect(host='localhost',username='root',password='Amazon111@',database='face_recognition')
                my_cursor=conn.cursor()

                my_cursor.execute('select Name from student where Student_id='+str(id))
                n=my_cursor.fetchone()
                n='+'.join(n)

                my_cursor.execute('select Roll from student where Student_id='+str(id))
                r=my_cursor.fetchone()
                r='+'.join(r)

                my_cursor.execute('select Dep from student where Student_id='+str(id))
                d=my_cursor.fetchone()
                d='+'.join(d)

                my_cursor.execute('select Student_id from student where Student_id='+str(id))
                i=my_cursor.fetchone()
                i='+'.join(i)
                # print(n)
                # print(r)
                # print(d)
                # print(id)
                if confidence>79:
                    cv2.putText(img,f'Id:{i}',(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                    cv2.putText(img,f'Roll:{r}',(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                    cv2.putText(img,f'Name:{n}',(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                    cv2.putText(img,f'Department:{d}',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f'Unknown Face Detected',(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),'Face',clf)
            return img

        faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read('classifier.xml')
        
        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow('Welcome to Face Recognisation',img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()