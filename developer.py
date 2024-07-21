from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x600+0+0")
        self.root.title("face Recognition system")

        title_lbl=Label(self.root,text="DEVELOPER",font=("Helvetica",34,"bold"),bg="white",fg="blue",)
        title_lbl.place(x=0,y=0,width=1400,height=45)

        img_top=Image.open(r"C:\Users\Hp\Desktop\Face_recognizationsystem\photos\developer1.jpeg")
        img_top=img_top.resize((1350,638),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=5,y=55,width=1350,height=638)


        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=925,y=0,width=430,height=475)

        img_top1=Image.open(r"C:\Users\Hp\Desktop\Face_recognizationsystem\photos\developer3.jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=230,y=0,width=200,height=200)

        #developer info
        dev_label=Label(main_frame,text="Hii!! Bhavya here",font=("Helvetica",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)


        dev_label=Label(main_frame,text="Developer of this project",font=("Helvetica",13,"bold"),bg="white")
        dev_label.place(x=0,y=40)


        img2=Image.open(r"C:\Users\Hp\Desktop\Face_recognizationsystem\photos\developer2.png")
        img2=img2.resize((420,260),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=420,height=260)

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()