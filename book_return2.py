from tkinter import *
import pymysql
import tkinter.messagebox as mb
import pandas as pd
import numpy as np
# Import Data
books = pd.read_csv('books.csv')
circulations_train = pd.read_csv('circulations-train.csv')
circulations_valid = pd.read_csv('circulations-valid.csv')
# Specify usable column in books 
bk = books[['item_no','bib_no','language','location','title','subject','author']]
# Adjust columns in circulation_valid
circulations_valid.head()
cirval = circulations_valid.drop(columns=['id','patron_hint'])
cirval = pd.merge(cirval, bk[['bib_no','subject']], on='bib_no', how='inner')
# Split date and time but keep only date
cirval[['tx_date', 'tx_time']] = cirval['tx_date'].str.split(' ', expand=True)
cirval.drop('tx_time', axis=1, inplace=True)
cirval[['due_date', 'due_time']] = cirval['due_date'].str.split(' ', expand=True)
cirval.drop('due_time', axis=1, inplace=True)

# Change datatype from object to datetime
cirval['tx_date'] = pd.to_datetime(cirval['tx_date'])
cirval['due_date'] = pd.to_datetime(cirval['due_date'])

# calculate duration between 'tx_date' and 'due_date' and store in 'duration' column
cirval['duration'] = (cirval['due_date'] - cirval['tx_date']).dt.days.astype(float)
# Consider English books only
bk_eng = bk[bk['language']=='eng']
cirval_eng = cirval[cirval['language']=='eng']
# For exist users
## Count number of duplicated time that users borrow the book
user_count = cirval_eng.groupby('patron_no')['subject'].value_counts()
## Count amount of distinct type of book that users borrow
user_count = cirval_eng.groupby('patron_no')['subject'].nunique().sort_values(ascending=False)
# List of existing members
member_list = cirval_eng['patron_no'].drop_duplicates().reset_index(drop=True).astype(str)


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
        for_member = cirval_eng[cirval_eng['patron_no']==ans].reset_index(drop=True)
        temp_list1 = list(for_member['bib_no'].drop_duplicates())
        temp_list2 = list(for_member['subject'].drop_duplicates())
        for i in temp_list1:
               bk_for_rec = bk_eng[bk_eng['bib_no'] != str(i) ]
        bk_for_rec = bk_for_rec[bk_for_rec['subject'].isin(temp_list2)]
        print(bk_for_rec.head(10))

        




root=Toplevel()



root.geometry("900x550")







#Main Frame
stu_main_frame=Frame(root,height="550",width="900")
stu_main_frame.place(x=0,y=0)

#Image
image1= PhotoImage(file="return_book2.gif")
label_for_image= Label(stu_main_frame, image=image1)
label_for_image.pack()


#Entry And Labels
#Left
return_book_id=Entry(root,bd="5")
return_book_id.place(x=425,y=185)

return_stu_id=Entry(root,bd="5")
return_stu_id.place(x=425,y=270)

return_book_name=Entry(root,bd="5")
return_book_name.place(x=425,y=350)

return_student_name=Entry(root,bd="5")
return_student_name.place(x=425,y=430)
#Right
return_course_entry=Entry(root,bd="5")
return_course_entry.place(x=720,y=185)

return_branch_entry=Entry(root,bd="5")
return_branch_entry.place(x=720,y=270)

date_of_return_entry=Entry(root,bd="5")
date_of_return_entry.place(x=720,y=350)

#Buttons

#Button Frame
btn_frame=Frame(stu_main_frame,bg="#b0a897",height="65",width="430")
btn_frame.place(x=450,y=470)


return_insert=Button(btn_frame,text="Insert",bg="black",fg="white",bd="5",font="arial 12 bold",command=return_insert)
return_insert.place(x=20,y=10)

return_delete=Button(btn_frame,text="Delete",bg="black",fg="white",bd="5",font="arial 12 bold",command=return_delete)
return_delete.place(x=125,y=10)

return_clear=Button(btn_frame,text="Clear",bg="black",fg="white",bd="5",font="arial 12 bold",command=clear)
return_clear.place(x=230,y=10)

return_close=Button(btn_frame,text="Close",bg="black",fg="white",bd="5",font="arial 12 bold",command=return_close)
return_close.place(x=330,y=10)





root.mainloop()

