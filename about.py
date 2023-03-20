#About
#Only Background Image Is Use
from tkinter import *




about_root=Toplevel()


about_root.geometry("600x480")
about_root.title("About")
about_root.minsize(width="600",height="480")
about_root.maxsize(width="600",height="480")

#Image
image1= PhotoImage(file="about.gif")
label_for_image= Label(about_root, image=image1)
label_for_image.pack()
