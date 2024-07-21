from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x600+0+0")
        self.root.title("Attendence management system")

        # variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_data=StringVar()
        self.var_atten_attendance=StringVar()







 #img 1
        img=Image.open(r"C:\Users\Hp\Desktop\Face_recognizationsystem\photos\attendence1.jpg")
        img=img.resize((675,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=10,y=0,width=675,height=190)

#img2
        img1=Image.open(r"C:\Users\Hp\Desktop\Face_recognizationsystem\photos\attendence2.jpg")
        img1=img1.resize((675,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=685,y=0,width=675,height=190)

#bg image
        img3=Image.open(r"C:\Users\Hp\Desktop\Face_recognizationsystem\photos\bg.jpg")
        img3=img3.resize((1350,600),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=10,y=130,width=1350,height=600)

#title
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("Helvetica",34,"bold"),bg="white",fg="red",)
        title_lbl.place(x=0,y=10,width=1530,height=35)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=60,width=1340,height=500)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("Helvetica",12,"bold"))
        Left_frame.place(x=15,y=10,width=655,height=435)

        img_left=Image.open(r"C:\Users\Hp\Desktop\Face_recognizationsystem\photos\attendence3.jpg")
        img_left=img_left.resize((655,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=655,height=130)

        #inside frame
        left_inside_frame=Frame(Left_frame,bd=2,bg="white",relief=RIDGE)
        left_inside_frame.place(x=3,y=135,width=643,height=275)

        #ID
        id_label=Label(left_inside_frame,text="Student ID:",font=("Helvetica",10,"bold"),bg="white")
        id_label.grid(row=0,column=0,padx=10,sticky=W)

        id_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("Helvetica",10,"bold"))
        id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll
        roll_label=Label(left_inside_frame,text="Roll:",font=("Helvetica",10,"bold"),bg="white")
        roll_label.grid(row=0,column=3,padx=10,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("Helvetica",10,"bold"))
        atten_roll.grid(row=0,column=4,padx=10,pady=5,sticky=W)

        #name
        name_label=Label(left_inside_frame,text="Name:",font=("Helvetica",10,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("Helvetica",10,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #department
        dep_label=Label(left_inside_frame,text="Department",font=("Helvetica",10,"bold"),bg="white")
        dep_label.grid(row=1,column=3,padx=10,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("Helvetica",10,"bold"))
        atten_dep.grid(row=1,column=4,padx=10,pady=5,sticky=W)

        #time
        time_label=Label(left_inside_frame,text="Time",font=("Helvetica",10,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("Helvetica",10,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #date
        date_label=Label(left_inside_frame,text="Date:",font=("Helvetica",10,"bold"),bg="white")
        date_label.grid(row=2,column=3,padx=10,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_data,font=("Helvetica",10,"bold"))
        atten_date.grid(row=2,column=4,padx=10,pady=5,sticky=W)

        #status
        status_label=Label(left_inside_frame,text="Attendence Status:",font=("Helvetica",10,"bold"),bg="white")
        status_label.grid(row=3,column=0,padx=10,sticky=W)

        self.status_combo=ttk.Combobox(left_inside_frame,font=("Helvetica",10,"bold"),state="readonly",width=18,textvariable=self.var_atten_attendance)
        self.status_combo["values"]=("Status","Present","Absent")
        self.status_combo.current(0)
        self.status_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #down inside frame
        btn_frame=Frame(Left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=7,y=300,width=635,height=30)

         #import
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width="18",font=("Helvetica",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=6,column=0)

        #update
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width="18",font=("Helvetica",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=6,column=1)

        #delete
        delete_btn=Button(btn_frame,text="Update",width="19",font=("Helvetica",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=6,column=2)

        #reset
        reset_btn=Button(btn_frame,text="Reset",width="19",command=self.reset_data,font=("Helvetica",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=6,column=3) 
        
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Helvetica",12,"bold"))
        Right_frame.place(x=675,y=10,width=655,height=435)

         # table freame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=3,y=0,width=645,height=410)

        #scroll bar and table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.Attendence_table=ttk.Treeview(table_frame,column=("ID","Roll","Name","Department","Time","Date","Attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Attendence_table.xview)
        scroll_y.config(command=self.Attendence_table.yview)

        self.Attendence_table.heading("ID",text="Student ID")
        self.Attendence_table.heading("Roll",text="Roll No.")
        self.Attendence_table.heading("Name",text="Name")
        self.Attendence_table.heading("Department",text="Department")
        self.Attendence_table.heading("Time",text="Time")
        self.Attendence_table.heading("Date",text="Date")
        self.Attendence_table.heading("Attendence",text="Attendence Status")

        self.Attendence_table["show"]="headings"

        self.Attendence_table.column("ID",width=130)
        self.Attendence_table.column("Roll",width=130)
        self.Attendence_table.column("Name",width=130)
        self.Attendence_table.column("Department",width=130)
        self.Attendence_table.column("Time",width=130)
        self.Attendence_table.column("Date",width=130)
        self.Attendence_table.column("Attendence",width=130)

        self.Attendence_table.pack(fill=BOTH,expand=1)

        self.Attendence_table.bind("<ButtonRelease>",self.get_cursor)

        #fetch data
    def fetchdata(self,rows):


            self.Attendence_table.delete(*self.Attendence.get_children())
            for i in rows:
                    self.Attendence_table.insert("",END,values=i)
#import
    def importCsv(self):
             global mydata
             mydata.clear()
             fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root) 
             with open(fln) as myfile:
                     csvread=csv.reader(myfile,delimiter=",")
                     for i in csvread:
                             mydata.append(i)
                             self.fetchdata(mydata)  
#export
    def exportCsv(self):
            try:
                    if len(mydata)<1:
                            messagebox.showerror("No Data","No Data found tp export",parent=self.root)
                            return False
                    fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)  
                    with open(fln,mode="w",newline="") as myfile:
                            exp_write=csv.writer(myfile,delimiter=",") 
                            for i in mydata:
                                    exp_write.writerow(i)
                                    messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"sucessfully")
            except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root) 
    def get_cursor(self):
            cursor_row=self.Attendence_table.focus()
            content=self.Attendence_table.item(cursor_row)
            rows=content['values']
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6])

    def reset_data(self):
            self.var_atten_id.set(" ")
            self.var_atten_roll.set(" ")
            self.var_atten_name.set(" ")
            self.var_atten_dep.set(" ")
            self.var_atten_time.set(" ")
            self.var_atten_date.set(" ")
            self.var_atten_attendance.set(" ")


        







if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()