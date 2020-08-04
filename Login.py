from tkinter import *
import tkinter.messagebox as mb
import mysql.connector
main = Tk()

def chk():
    conn = mysql.connector.connect(host="localhost",user="root",password="",db="Rest")
    cr=conn.cursor()
    user = e1.get()
    pwd = e2.get()

   
    cr.execute("select * from login where usr='"+user+"'and pwd='"+pwd+"'")
    if(cr.fetchone()):
        main.destroy()
        import billings
    else:
        mb.showinfo("Success","data not match")   
     


main.config(bg = "black")
main.title("Login Page")
main.geometry("600x500+100+50")
Label(main,text="User ID", fg="White",bg="Black",font=("Arial",20)).grid(row=0,column=0)
Label(main,text="Password", fg="White",bg="Black",font=("Arial",20)).grid(row=1,column=0)
e1 = Entry(main)
e1.grid(row=0,column=2)
e2 = Entry(main,show="*")
e2.grid(row = 1, column = 2)
Button(main,text="Sign In",command=chk).grid(row =3 , column= 2)
Button(main,text="Cancel").grid(row = 3,column=1)

main.mainloop()