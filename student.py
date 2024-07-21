from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x600+0+0")
        self.root.title("face Recognition system")

        # *******variables******
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_stdname=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio=StringVar()
        

        
 #img 1
        img=Image.open(r"C:\Users\ankur\Downloads\Face_recognizationsystem (1)\Face_recognizationsystem\photos\s2.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=130)

#img2
        img1=Image.open(r"C:\Users\ankur\Downloads\Face_recognizationsystem (1)\Face_recognizationsystem\photos\s1.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=450,height=130)

#img3
        img2=Image.open(r"C:\Users\ankur\Downloads\Face_recognizationsystem (1)\Face_recognizationsystem\photos\s3.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=500,height=130)

#bg image
        img3=Image.open(r"C:\Users\ankur\Downloads\Face_recognizationsystem (1)\Face_recognizationsystem\photos\bg.jpg")
        img3=img3.resize((1350,600),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1350,height=600)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("Helvetica",34,"bold"),bg="white",fg="red",)
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1330,height=505)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Helvetica",12,"bold"))
        Left_frame.place(x=15,y=10,width=655,height=1100)

        img_left=Image.open(r"C:\Users\ankur\Downloads\Face_recognizationsystem (1)\Face_recognizationsystem\photos\left.jpg")
        img_left=img_left.resize((655,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=655,height=130)
        
       
                

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("Helvetica",12,"bold"))
        current_course_frame.place(x=5,y=135,width=640,height=100)

# DEpartment
        dep_label=Label(current_course_frame,text="Department",font=("Helvetica",10,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("Helvetica",10,"bold"),state="read only",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("Helvetica",10,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Helvetica",10,"bold"),state="read only",width=20)
        course_combo["values"]=("Select Course","BE","BA","B.sc")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("Helvetica",10,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("Helvetica",10,"bold"),state="read only",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("Helvetica",10,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("Helvetica",10,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Semester1","Semester2","Semester3","Semester4","Semester5","Semester6")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #class student
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("Helvetica",12,"bold"))
        class_student_frame.place(x=5,y=240,width=640,height=260)
        
        #studentid
        studentID_label=Label(class_student_frame,text="Student_ID",font=("Helvetica",10,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("Helvetica",10,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #student name
        studentname_label=Label(class_student_frame,text="Student Name",font=("Helvetica",10,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_stdname,width=20,font=("Helvetica",10,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        # class division
        class_div_label=Label(class_student_frame,text="Class Division",font=("Helvetica",10,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("Helvetica",10,"bold"),state="read only",width=18)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll no
        roll_no_label=Label(class_student_frame,text="Roll No.",font=("Helvetica",10,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("Helvetica",10,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender
        gender_label=Label(class_student_frame,text="Gender",font=("Helvetica",10,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Helvetica",10,"bold"),state="read only",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #dob
        dob_label=Label(class_student_frame,text="DOB",font=("Helvetica",10,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("Helvetica",10,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        email_label=Label(class_student_frame,text="Email",font=("Helvetica",10,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("Helvetica",10,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phonr no
        phone_label=Label(class_student_frame,text="Phone No:",font=("Helvetica",10,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("Helvetica",10,"bold"))
        class_div_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #Address
        address_label=Label(class_student_frame,text="Address:",font=("Helvetica",10,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("Helvetica",10,"bold"))
        class_div_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #teacher name
        teacher_label=Label(class_student_frame,text="Teacher",font=("Helvetica",10,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("Helvetica",10,"bold"))
        class_div_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio,text="No Photo sample",value="No")
        radiobtn2.grid(row=5,column=1)

        #save
        save_btn=Button(class_student_frame,text="Save",command=self.add_data,width="10",font=("Helvetica",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=6,column=0)

        #update
        update_btn=Button(class_student_frame,text="Update",command=self.update_data,width="10",font=("Helvetica",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=6,column=1)

        #delete
        delete_btn=Button(class_student_frame,text="Delete",command=self.delete_data,width="10",font=("Helvetica",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=6,column=2)

        #reset
        reset_btn=Button(class_student_frame,text="Reset",command=self.reset_data,width="10",font=("Helvetica",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=6,column=3)

        #phto sample
        take_photo_btn=Button(class_student_frame,text="Sample",command=self.generate_dataset,width="8",font=("Helvetica",10,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=6,column=4)


        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Helvetica",12,"bold"))
        Right_frame.place(x=675,y=10,width=645,height=1100)

        img_right=Image.open(r"C:\Users\ankur\Downloads\Face_recognizationsystem (1)\Face_recognizationsystem\photos\right.jpg")
        img_right=img_right.resize((645,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=0,y=0,width=645,height=130)


        #**********searching system*************

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Helvetica",12,"bold"))
        Search_frame.place(x=5,y=135,width=630,height=100)

        search_label=Label(Search_frame,text="Search By",font=("Helvetica",10,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("Helvetica",10,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll No","Phone No","StudentID","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=20,font=("Helvetica",10,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #search
        search_btn=Button(Search_frame,text="Search",width="10",font=("Helvetica",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=1,column=3,padx=4)

        #showall
        showall_btn=Button(Search_frame,text="Show All",width="10",font=("Helvetica",10,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=1,column=5,padx=5)

      # *************table**********
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=250,width=630,height=215)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="dep")
        self.student_table.heading("course",text="course")
        self.student_table.heading("year",text="year")
        self.student_table.heading("sem",text="semester")
        self.student_table.heading("id",text="std_id")
        self.student_table.heading("name",text="std_name")
        self.student_table.heading("div",text="div")
        self.student_table.heading("roll",text="roll")
        self.student_table.heading("gender",text="gender")
        self.student_table.heading("dob",text="dob")
        self.student_table.heading("email",text="email")
        self.student_table.heading("phone",text="phone")
        self.student_table.heading("address",text="address")
        self.student_table.heading("teacher",text="teacher")
        self.student_table.heading("photo",text="photosample")
        
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=120)
        self.student_table.column("course",width=120)
        self.student_table.column("year",width=120)
        self.student_table.column("sem",width=120)
        self.student_table.column("id",width=120)
        self.student_table.column("name",width=120)
        self.student_table.column("div",width=120)
        self.student_table.column("roll",width=120)
        self.student_table.column("gender",width=120)
        self.student_table.column("dob",width=120)
        self.student_table.column("email",width=120)
        self.student_table.column("phone",width=120)
        self.student_table.column("address",width=120)
        self.student_table.column("teacher",width=120)
        self.student_table.column("photo",width=120)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stdname.get()== "" or self.var_std_id.get()== "":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    

                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_std_id.get(),
                                                                                                self.var_stdname.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radio.get()

                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("sucess","student details has been added sucessfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    # ******fetch data*******
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
        my_cursor=conn.cursor()   
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                    self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ******get cursor******
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]), 
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_stdname.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio.set(data[14])

    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stdname.get()==" " or self.var_std_id.get()==" ":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student detail",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,stdname=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where std_id=%s",(
                                        
                                                                                                                                                                              self.var_dep.get(), 
                                                                                                                                                                              self.var_course.get(),
                                                                                                                                                                              self.var_year.get(),
                                                                                                                                                                              self.var_semester.get(),
                                                                                                                                                                              self.var_stdname.get(),
                                                                                                                                                                              
                                                                                                                                                                              self.var_roll.get(),
                                                                                                                                                                              self.var_gender.get(),
                                                                                                                                                                              self.var_dob.get(),
                                                                                                                                                                              self.var_email.get(),
                                                                                                                                                                              self.var_phone.get(),
                                                                                                                                                                              self.var_address.get(),
                                                                                                                                                                              self.var_teacher.get(),
                                                                                                                                                                              self.var_radio.get(),
                                                                                                                                                                              self.var_std_id.get(),

                                                                                                                                                                        ))                                  
                else:
                     if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 
    # delete function
    def delete_data(self):
        if self.var_std_id.get()=="": 
             messagebox.showerror("Error","Student id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete",parent=self.root)
                if delete>0:
                      conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                      my_cursor=conn.cursor()
                      sql="delete from student where std_id=%s"
                      val=(self.var_std_id.get(),)
                      my_cursor.execute(sql,val)
                else:
                     if not delete:
                        return 

                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Delete","Successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)},parent=self.root")
    # reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course") 
        self.var_year.set("Select Year") 
        self.var_semester.set("Select Semester") 
        self.var_std_id.set(" ") 
        self.var_stdname.set(" ") 
        self.var_div.set("Select") 
        self.var_roll.set(" ") 
        self.var_gender.set("Select") 
        self.var_dob.set(" ") 
        self.var_email.set(" ") 
        self.var_phone.set(" ") 
        self.var_address.set(" ")
        self.var_teacher.set(" ")         


#**************** generate data set or take photo sample *************
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_stdname.get()== "" or self.var_std_id.get()== "":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                        id+=1
                my_cursor.execute("Update student set dep=%s,course=%s,year=%s,semester=%s,stdname=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s where std_id=%s",(
                                        
                                                                                                                                                                              self.var_dep.get(),
                                                                                                                                                                              self.var_course.get(),
                                                                                                                                                                              self.var_year.get(),
                                                                                                                                                                              
                                                                                                                                                                              self.var_semester.get(),
                                                                                                                                                                              self.var_stdname.get(),
                                                                                                                                                                              
                                                                                                                                                                              self.var_roll.get(),
                                                                                                                                                                              self.var_gender.get(),
                                                                                                                                                                              self.var_dob.get(),
                                                                                                                                                                              self.var_email.get(),
                                                                                                                                                                              self.var_phone.get(),
                                                                                                                                                                              self.var_address.get(),
                                                                                                                                                                              self.var_teacher.get(), 
                                                                                                                                                                              self.var_std_id.get()==id+1 

                                                                                                                                                                         )) 
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load perdefined data on face frontals from opencv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling factorial=1.3
                        #minimum neighor=5

                        for (x,y,w,h) in faces:
                                face_cropped=img[y:y+h,x:x+w]
                                return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                                img_id+=1
                                face=cv2.resize(face_cropped(my_frame),(450,450))
                                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                                cv2.imwrite(file_name_path,face)
                                cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                                break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating Data sets completed!!")
            except Exception as es:
             messagebox.showerror("Error",f"Due To:{str(es)},parent=self.root")
        

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()