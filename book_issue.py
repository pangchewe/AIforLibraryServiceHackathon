from tkinter import *
import pymysql
import tkinter.messagebox as mb


def return_close():
        close_ques=mb.askquestion("Close","Are You Sure ?")
        if close_ques=="yes":
            root.destroy()


def clear():
    return_book_id.delete(0,END)
    return_stu_id.delete(0,END)
    return_book_name.delete(0,END)
    return_student_name.delete(0,END)
    return_course_entry.delete(0,END)
    return_branch_entry.delete(0,END)
    date_of_return_entry.delete(0,END)
    



def return_delete():
        bookID_return=return_book_id.get()
        con=pymysql.connect(host="localhost",user="root",password="123",db="library")
        cursor=con.cursor()
        cursor.execute("delete from book_return2 where book_id='"+return_book_id.get()+"'")
        ques=mb.askquestion("Delete","Are You Sure You Want To Delete Data")
        if ques=="yes":
                cursor.execute("commit");
                mb.showinfo("Deleted","Data Sucessfully Deleted")


def return_insert():
        bookID_return=return_book_id.get()
        studentID_return=return_stu_id.get()
        bookName_return=return_book_name.get()
        studentName_return=return_student_name.get()
        course_return=return_course_entry.get()
        branch_return=return_branch_entry.get()
        date_return=date_of_return_entry.get()
        con=pymysql.connect(host="localhost",user="root",password="123",db="library")
        cursor=con.cursor()
        cursor.execute("insert into book_return2 values('"+bookID_return +"','"+ studentID_return+"','"+bookName_return+"','"+studentName_return+"','"+course_return +"','"+branch_return+"','"+ date_return +"')")
        cursor.execute("commit");
        mb.showinfo("Inserted ","Data Sucessfully Inserted")


root=Toplevel()



root.geometry("600x480")





#Heading Frame And Heading
return_heading_frame=Frame(root,height="100",width="800",bg="black")
return_heading_frame.place(x=0,y=0)
stu=Label(return_heading_frame,text="Return Book",fg="white",font="arial 30 bold",bg="black")
stu.place(x=200,y=20)


#Main Frame
stu_main_frame=Frame(root,height="400",width="800")
stu_main_frame.place(x=0,y=100)

#Image
image1= PhotoImage(file="about.gif")
label_for_image= Label(stu_main_frame, image=image1)
label_for_image.pack()


#Entry And Labels
#Left
return_book_id=Entry(root,bd="5")
return_book_id.place(x=150,y=120)
return_book_id_label=Label(root,text="Book ID",font="arial 12 bold",fg="white",bg="black")
return_book_id_label.place(x=30,y=120)

return_stu_id=Entry(root,bd="5")
return_stu_id.place(x=150,y=190)
return_stu_id_label=Label(root,text="Student ID",font="arial 12 bold",fg="white",bg="black")
return_stu_id_label.place(x=30,y=190)

return_book_name=Entry(root,bd="5")
return_book_name.place(x=150,y=260)
return_book_name_label=Label(root,text="Book Name",font="arial 12 bold",fg="white",bg="black")
return_book_name_label.place(x=30,y=260)

return_student_name=Entry(root,bd="5")
return_student_name.place(x=150,y=330)
return_student_name_label=Label(root,text="Student Name",font="arial 12 bold",fg="white",bg="black")
return_student_name_label.place(x=30,y=330)
#Right
return_course_entry=Entry(root,bd="5")
return_course_entry.place(x=430,y=120)
return_course_label=Label(root,text="Course",font="arial 12 bold",fg="white",bg="black")
return_course_label.place(x=330,y=120)

return_branch_entry=Entry(root,bd="5")
return_branch_entry.place(x=430,y=190)
return_branch_label=Label(root,text="Branch",font="arial 12 bold",fg="white",bg="black")
return_branch_label.place(x=330,y=190)

date_of_return_entry=Entry(root,bd="5")
date_of_return_entry.place(x=430,y=260)
date_of_return_label=Label(root,text="Date Of Return",font="arial 12 bold",fg="white",bg="black")
date_of_return_label.place(x=300,y=260)

#Buttons

#Button Frame
btn_frame=Frame(stu_main_frame,bg="#b0a897",height="100",width="430")
btn_frame.place(x=100,y=270)


return_insert=Button(btn_frame,text="Insert",bg="black",fg="white",bd="5",font="arial 12 bold",command=return_insert)
return_insert.place(x=20,y=30)

return_delete=Button(btn_frame,text="Delete",bg="black",fg="white",bd="5",font="arial 12 bold",command=return_delete)
return_delete.place(x=125,y=30)

return_clear=Button(btn_frame,text="Clear",bg="black",fg="white",bd="5",font="arial 12 bold",command=clear)
return_clear.place(x=230,y=30)

return_close=Button(btn_frame,text="Close",bg="black",fg="white",bd="5",font="arial 12 bold",command=return_close)
return_close.place(x=330,y=30)





root.mainloop()

