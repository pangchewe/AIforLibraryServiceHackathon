from tkinter import *
import pymysql
import tkinter.messagebox as mb






def return_delete():
        bookID=return_book_id.get()
        con=pymysql.connect(host="localhost",user="root",password="123",db="library")
        cursor=con.cursor()
        cursor.execute("delete from book_issue where student_id='"+return_book_id.get()+"'")
        ques=mb.askquestion("Delete","Are You Sure You Want To Delete Data")
        if ques=="yes":
                cursor.execute("commit");
                mb.showinfo("Deleted","Data Sucessfully Deleted")


def return_insert():
        bookID=return_book_id.get()
        studentID=return_stu_id.get()
        bookName=return_book_name.get()
        studentName=return_student_name.get()
        course=return_course_entry.get()
        branch=return_branch_entry.get()
        date=date_of_return_entry.get()
        con=pymysql.connect(host="localhost",user="root",password="123",db="library")
        cursor=con.cursor()
        cursor.execute("insert into book_issue values('"+bookID +"','"+ studentID+"','"+bookName+"','"+studentName+"','"+course +"','"+branch+"','"+ date +"')")
        cursor.execute("commit");
        mb.showinfo("Inserted","Data Sucessfully Inserted")


root=Tk()


root.geometry("600x480")


#Image
image1= PhotoImage(file="hh.gif")
label_for_image= Label(root, image=image1)
label_for_image.pack()



#Heading Frame And Heading
return_heading_frame=Frame(root,height="100",width="800",bg="black")
return_heading_frame.place(x=0,y=0)
stu=Label(return_heading_frame,text="return Book",fg="white",font="arial 30 bold",bg="black")
stu.place(x=200,y=20)


#Main Frame
return_main_frame=Frame(root,bg="#d5d8de",height="400",width="800")
return_main_frame.place(x=0,y=100)

image1= PhotoImage(file="hh.gif")
label_for_image= Label(return_main_frame, image=image1)
label_for_image.pack()


#btn_Main Frame
btn_frame=Frame(return_main_frame,bg="#b0a897",height="100",width="350")
btn_frame.place(x=150,y=270)

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
return_course_label.place(x=340,y=120)

return_branch_entry=Entry(root,bd="5")
return_branch_entry.place(x=430,y=190)
return_branch_label=Label(root,text="Branch",font="arial 12 bold",fg="white",bg="black")
return_branch_label.place(x=340,y=190)

date_of_return_entry=Entry(root,bd="5")
date_of_return_entry.place(x=430,y=260)
date_of_return_label=Label(root,text="Date Of Issue",font="arial 12 bold",fg="white",bg="black")
date_of_return_label.place(x=300,y=260)

#Buttons
return_insert=Button(btn_frame,text="Insert",bg="black",fg="white",bd="5",font="arial 12 bold",command=return_insert)
return_insert.place(x=40,y=30)

return_delete=Button(btn_frame,text="Delete",bg="black",fg="white",bd="5",font="arial 12 bold",command=return_delete)
return_delete.place(x=135,y=30)

return_close=Button(btn_frame,text="Close",bg="black",fg="white",bd="5",font="arial 12 bold")
return_close.place(x=250,y=30)



root.mainloop()

