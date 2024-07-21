from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np




class Face:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x600+0+0")
        self.root.title("Face Recognition system")

        title_lbl=Label(self.root,text="FACE RECOGNITON",font=("Helvetica",34,"bold"),bg="white",fg="red",)
        title_lbl.place(x=0,y=0,width=1400,height=45)

        img_top=Image.open(r"C:\Users\Hp\Desktop\Face_recognizationsystem\photos\face1.jpg")
        img_top=img_top.resize((675,600),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=10,y=55,width=675,height=600)

        img_bottom=Image.open(r"C:\Users\Hp\Desktop\Face_recognizationsystem\photos\face2.jpg")
        img_bottom=img_bottom.resize((670,600),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=675,y=55,width=670,height=600)

         #button
        b1_1=Button(self.root,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("Helvetica","10","bold"),bg="#728FCE",fg="white")
        b1_1.place(x=933,y=580,width=150,height=40)
    # attendence
    def mark_attendence(self,i,r,n,d):
        with open("bhavya.csv","r+",newlinw="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:$S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


    #face recognition

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="0000",database="face_recognizer")
                my_cursor=conn.cursor()


                my_cursor.execute("select stdname from student where std_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select roll from student where std_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select dep from student where std_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select std_id from student where std_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)


                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y,-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y,-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            if cv2.waitKey(1)==13:
                break
            cv2.VideoCapture.release()
            cv2.destroyAllWindows()
 
if __name__ == "__main__":
    root=Tk()
    obj=Face(root)
    root.mainloop()