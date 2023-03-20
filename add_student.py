from tkinter import *
import pymysql
import tkinter.messagebox as mb



def stu_close():
        stu_ques=mb.askquestion("Close","Are You Sure ?")
        if stu_ques=="yes":
                add_stu_root.destroy()

                
def stu_clear():
        stu_id.delete(0,END)
        stu_name.delete(0,END)
        father_entry.delete(0,END)
        course_entry.delete(0,END)
        branch_entry.delete(0,END)
        semester_entry.delete(0,END)
        year_entry.delete(0,END)
    

def stu_delete():
        stu_id1=stu_id.get()
        stu_name1=stu_name.get()
        father=father_entry.get()
        course=course_entry.get()
        branch=branch_entry.get()
        semester=semester_entry.get()
        year=year_entry.get()
        con=pymysql.connect(host="localhost",user="root",password="123",db="library")
        cursor=con.cursor()
        cursor.execute("delete from add_student where student_id='"+stu_id.get()+"'")
        ques=mb.askquestion("Delete","Are You Sure You Want To Delete Data")
        if ques=="yes":
                cursor.execute("commit");
                mb.showinfo("Deleted","Data Sucessfully Deleted")


def stu_insert():
        stu_id1=stu_id.get()
        stu_name1=stu_name.get()
        father=father_entry.get()
        course=course_entry.get()
        branch=branch_entry.get()
        semester=semester_entry.get()
        year=year_entry.get()
        con=pymysql.connect(host="localhost",user="root",password="123",db="library")
        cursor=con.cursor()
        cursor.execute("insert into add_student values('"+stu_id1 +"','"+ stu_name1+"','"+father+"','"+course+"','"+branch +"','"+semester+"','"+ year +"')")
        cursor.execute("commit");
        mb.showinfo("Inserted","Data Sucessfully Inserted")


add_stu_root=Toplevel()


add_stu_root.geometry("900x550")
add_stu_root.minsize(width=900,height=550)
add_stu_root.maxsize(width=900,height=550)







#Main Frame
stu_main_frame=Frame(add_stu_root,bg="#d5d8de",height="550",width="900")
stu_main_frame.place(x=0,y=0)


#Image
image1= PhotoImage(file="stu5.gif")
label_for_image= Label(stu_main_frame, image=image1)
label_for_image.pack()



#Entry And Labels
#Left
stu_id=Entry(add_stu_root,bd="5")
stu_id.place(x=425,y=185)


stu_name=Entry(add_stu_root,bd="5")
stu_name.place(x=425,y=270)


father_entry=Entry(add_stu_root,bd="5")
father_entry.place(x=425,y=350)


course_entry=Entry(add_stu_root,bd="5")
course_entry.place(x=425,y=430)

#Right
branch_entry=Entry(add_stu_root,bd="5")
branch_entry.place(x=720,y=180)


year_entry=Entry(add_stu_root,bd="5")
year_entry.place(x=720,y=270)


semester_entry=Entry(add_stu_root,bd="5")
semester_entry.place(x=720,y=350)


#Button Frame
btn_frame=Frame(stu_main_frame,bg="#b0a897",height="65",width="430")
btn_frame.place(x=450,y=470)


student_insert=Button(btn_frame,text="Insert",bg="black",fg="white",bd="5",font="arial 12 bold",command=stu_insert)
student_insert.place(x=20,y=10)

student_delete=Button(btn_frame,text="Delete",bg="black",fg="white",bd="5",font="arial 12 bold",command=stu_delete)
student_delete.place(x=125,y=10)

student_clear=Button(btn_frame,text="Clear",bg="black",fg="white",bd="5",font="arial 12 bold",command=stu_clear)
student_clear.place(x=230,y=10)

student_close=Button(btn_frame,text="Close",bg="black",fg="white",bd="5",font="arial 12 bold",command=stu_close)
student_close.place(x=330,y=10)


add_stu_root.mainloop()

