from tkinter import *
import pymysql
import tkinter.messagebox as mb


def book_issue_close():
        issue_ques=mb.askquestion("Close","Are You Sure ?")
        if issue_ques=="yes":
            issue_root.destroy()


def book_issue_clear():
    return_book_id.delete(0,END)
    return_stu_id.delete(0,END)
    return_book_name.delete(0,END)
    return_student_name.delete(0,END)
    return_course_entry.delete(0,END)
    return_branch_entry.delete(0,END)
    date_of_return_entry.delete(0,END)



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


issue_root=Toplevel()
issue_root.title("Issue Book")

issue_root.geometry("900x550")
issue_root.title("Book Issue")
issue_root.minsize(width="900",height="550")
issue_root.maxsize(width="900",height="550")








#Main Frame
return_main_frame=Frame(issue_root,bg="#d5d8de",height="550",width="900")
return_main_frame.place(x=0,y=0)



#Image
image1= PhotoImage(file="issue_book.gif")
label_for_image= Label(return_main_frame, image=image1)
label_for_image.pack()



#Entry And Labels
#Left
return_book_id=Entry(issue_root,bd="5")
return_book_id.place(x=425,y=185)

return_stu_id=Entry(issue_root,bd="5")
return_stu_id.place(x=425,y=270)


return_book_name=Entry(issue_root,bd="5")
return_book_name.place(x=425,y=350)


return_student_name=Entry(issue_root,bd="5")
return_student_name.place(x=425,y=430)

#Right
return_course_entry=Entry(issue_root,bd="5")
return_course_entry.place(x=720,y=185)


return_branch_entry=Entry(issue_root,bd="5")
return_branch_entry.place(x=720,y=270)


date_of_return_entry=Entry(issue_root,bd="5")
date_of_return_entry.place(x=720,y=350)



#Buttons

#Button Frame
btn_frame=Frame(return_main_frame,bg="#b0a897",height="65",width="430")
btn_frame.place(x=450,y=470)


return_insert=Button(btn_frame,text="Insert",bg="black",fg="white",bd="5",font="arial 12 bold",command=return_insert)
return_insert.place(x=20,y=10)

return_delete=Button(btn_frame,text="Delete",bg="black",fg="white",bd="5",font="arial 12 bold",command=return_delete)
return_delete.place(x=125,y=10)

return_clear=Button(btn_frame,text="Clear",bg="black",fg="white",bd="5",font="arial 12 bold",command=book_issue_clear)
return_clear.place(x=230,y=10)

return_close=Button(btn_frame,text="Close",bg="black",fg="white",bd="5",font="arial 12 bold",command=book_issue_close)
return_close.place(x=330,y=10)



issue_root.mainloop()

