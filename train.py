from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from student import Student
import os
import numpy as np
import cv2
class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Face Recognition System')
        #TITLE:
        title_lbl = Label(self.root,text="TRAIN DATASET",font=('times new roman',35,'bold'),bg='white',fg='red')
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #TOP IMAGE:
        img_top = Image.open(r'C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\facialrecognition.png')
        img_top = img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1530,height=325)

        # button
        b1_1=Button(self.root,text='Train Data',command=self.train_classifier,cursor='hand2',font=('times new roman',30,'bold'),bg='Green',fg='white')
        b1_1.place(x=0,y=380,width=1530,height=40)

        #BOTTOM IMAGE:
        img_bottom = Image.open(r'C:\Users\dashrath singh\OneDrive\Desktop\Student_Management_System_tinkter\college_images\teaser.png')
        img_bottom = img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)

        # data_dir=('data')
        # # print(type(data_dir))
        # print(os.listdir(data_dir))
        # print(os.path.join(data_dir,os.listdir(data_dir)[0]))

    def train_classifier(self):
        data_dir=('data')
        path=[os.path.join(data_dir,file1) for file1 in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #To convert an image into grayscale image using different method.
            image_np=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            # x=os.path.split(image)
            # print(x)
            # print((image[0]))
            # print(image_np)
            # print(id)
            faces.append(image_np)
            ids.append(id)
            cv2.imshow('Training',image_np)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #Train the classifier and save it.
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write('classifier.xml')
        cv2.destroyAllWindows()
        messagebox.showinfo('Information','Training Dataset Completed.')








if __name__ == '__main__':
    root=Tk()
    obj=Train(root)
    root.mainloop()