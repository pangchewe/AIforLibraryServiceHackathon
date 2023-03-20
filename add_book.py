from tkinter import *
import pymysql
import tkinter.messagebox as mb




def add_book_close():
        add_book_close_ques=mb.askquestion("Close","Are You Sure ?")
        if add_book_close_ques=="yes":
            root.destroy()


def add_book_clear():
    book_id.delete(0,END)
    book_name.delete(0,END)
    book_isbn.delete(0,END)
    book_publisher.delete(0,END)
    book_edition.delete(0,END)
    book_price.delete(0,END)
    book_page.delete(0,END)
    




def delete():
        id1=book_id.get()
        name=book_name.get()
        book_isbn1=book_isbn.get()
        publisher=book_publisher.get()
        edition=book_edition.get()
        price=book_price.get()
        page=book_page.get()
        con=pymysql.connect(host="localhost",user="root",password="123",db="library")
        cursor=con.cursor()
        cursor.execute("delete from add_book where Book_ID='"+book_id.get()+"'")
        ques=mb.askquestion("Delete","Are You Sure You Want To Delete Data")
        if ques=="yes":
                cursor.execute("commit");
                mb.showinfo("Deleted","Data Sucessfully Deleted")


def insert():
        id1=book_id.get()
        name=book_name.get()
        book_isbn1=book_isbn.get()
        publisher=book_publisher.get()
        edition=book_edition.get()
        price=book_price.get()
        page=book_page.get()
        con=pymysql.connect(host="localhost",user="root",password="123",db="library")
        cursor=con.cursor()
        cursor.execute("insert into add_book values('"+id1 +"','"+ name+"','"+book_isbn1+"','"+publisher+"','"+edition +"','"+price+"','"+ page +"')")
        cursor.execute("commit");

        mb.showinfo("Inserted","Data Sucessfully Inserted")



root=Toplevel()


root.geometry("900x550")



#Main Frame
main_frame=Frame(root,bg="#d5d8de",height="550",width="900")
main_frame.place(x=0,y=0)

#Image
image1= PhotoImage(file="add_book.gif")
label_for_image= Label(main_frame, image=image1)
label_for_image.pack()







#Entry And Labels
#Left
book_id=Entry(root,bd="5")
book_id.place(x=425,y=185)

book_name=Entry(root,bd="5")
book_name.place(x=425,y=270)


book_isbn=Entry(root,bd="5")
book_isbn.place(x=425,y=350)


book_publisher=Entry(root,bd="5")
book_publisher.place(x=425,y=430)

#Right
book_edition=Entry(root,bd="5")
book_edition.place(x=720,y=185)


book_price=Entry(root,bd="5")
book_price.place(x=720,y=270)


book_page=Entry(root,bd="5")
book_page.place(x=720,y=350)


#Buttons
#btn Frame
btn_frame=Frame(main_frame,bg="#b0a897",height="65",width="430")
btn_frame.place(x=450,y=470)

insert=Button(btn_frame,text="Insert",bg="black",fg="white",bd="5",font="arial 12 bold",command=insert)
insert.place(x=40,y=10)

delete=Button(btn_frame,text="Delete",bg="black",fg="white",bd="5",font="arial 12 bold",command=delete)
delete.place(x=135,y=10)

add_book_clear=Button(btn_frame,text="Clear",bg="black",fg="white",bd="5",font="arial 12 bold",command=add_book_clear)
add_book_clear.place(x=230,y=10)

add_book_close=Button(btn_frame,text="Close",bg="black",fg="white",bd="5",font="arial 12 bold",command=add_book_close)
add_book_close.place(x=330,y=10)




root.mainloop()
