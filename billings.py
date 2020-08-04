from tkinter import *
import random
import tkinter.messagebox
import time;
import datetime

root = Tk()
root.geometry("1400x750+0+0")
root.title("Cafe Management System")
root.configure(background="black")


Tops = Frame (root, width = 1350, height=100,bd=14,relief="raise")
Tops.pack(side=TOP)
lblInfo=Label(Tops, font=('arial',70,'bold'),text="    Cafe Billing System    ",bd=10)
lblInfo.grid(row=1,column=0)





f1 = Frame (root, width = 900, height=650,bd=8,relief="raise")
f1.pack(side=LEFT)
f2 = Frame (root, width = 440, height=650,bd=8,relief="raise")
f2.pack(side=RIGHT)

f1a = Frame (f1, width = 900, height=330,bd=8,bg='#bf7c58',relief="raise")
f1a.pack(side=TOP)
f2a = Frame (f1, width = 900, height=320,bd=6,bg='#bf7c58',relief="raise")
f2a.pack(side=BOTTOM)

ft2 = Frame(f2,width = 440, height = 650, bd = 12,bg='#bf7c58', relief = "raise")
ft2.pack(side=TOP)
fb2 = Frame(f2,width = 440, height = 50, bd = 16,bg='#bf7c58', relief = "raise")
fb2.pack(side=BOTTOM)

f1aa = Frame (f1a, width = 400, height=330,bd=16,bg='#bf7c58',relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a,width = 400, height = 330, bd = 16,bg='#bf7c58', relief = "raise")
f1ab.pack(side=RIGHT)

f2aa = Frame (f2a, width = 450, height=330,bd=14,bg='#bf7c58',relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a,width = 450, height = 330, bd = 14,bg='#bf7c58', relief = "raise")
f2ab.pack(side=RIGHT)

Tops.config(background="black")
f1.config(background="black")
f2.config(background="black")
#==================================METHODS=================================

def qExit():
    qExit= tkinter.messagebox.askyesno("Quit System","Do you want to quit?")
    if qExit>0:
        root.destroy()
        return

def Reset():
    E_Latte.set("0")
    E_Cappucino.set("0") 
    E_Espresso.set("0") 
    E_Iced_Latte.set("0") 
    E_Tea.set("0") 
    E_Lemonade.set("0") 
    E_Hot_Chocolate.set("0") 
    E_Iced_Tea.set("0") 

    E_Pineapple.set("0") 
    E_Black_Forest.set("0") 
    E_Chocolate.set("0") 
    E_ButterScotch.set("0") 
    E_Cheese.set("0") 
    E_Red_Velvet.set("0") 
    E_White_Forest.set("0") 
    E_Coffee_Cake.set("0")

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostOfDrinks.set("")
    CostOfCakes.set("")
    ServiceCharge.set("")
    txtReciept.delete("1.0",END)

    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")

    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")

    txtLatte.config(state=DISABLED)
    txtCappuccino.config(state=DISABLED)
    txtEspresso.config(state=DISABLED)
    txtIcedLatte.config(state=DISABLED)
    txtTea.config(state=DISABLED)
    txtLemonade.config(state=DISABLED)
    txtHotChocolate.config(state=DISABLED)
    txtIcedTea.config(state=DISABLED)

    txtPineapple_Cake.config(state=DISABLED)
    txtBf_Cake.config(state=DISABLED)
    txtChocolate_Cake.config(state=DISABLED)
    txtBS_Cake.config(state=DISABLED)
    txtCheese_Cake.config(state=DISABLED)
    txtRV_Cake.config(state=DISABLED)
    txtWF_Cake.config(state=DISABLED)
    txtCoffee_Cake.config(state=DISABLED)

def chkbutton_value():
    if (var1.get() == 1):
        txtLatte.configure(state= NORMAL)
    elif var1.get()== 0:
        txtLatte.configure(state= DISABLED)
        E_Latte.set("0")
    if (var2.get() == 1):
        txtCappuccino.configure(state= NORMAL)
    elif var2.get()== 0:
        txtCappuccino.configure(state= DISABLED)
        E_Cappucino.set("0")
    if (var3.get() == 1):
        txtEspresso.configure(state= NORMAL)
    elif var3.get()== 0:
        txtEspresso.configure(state= DISABLED)
        E_Espresso.set("0")
    if (var4.get() == 1):
        txtIcedLatte.configure(state= NORMAL)
    elif var4.get()== 0:
        txtIcedLatte.configure(state= DISABLED)
        E_Iced_Latte.set("0")
    if (var5.get() == 1):
        txtTea.configure(state= NORMAL)
    elif var5.get()== 0:
        txtTea.configure(state= DISABLED)
        E_Tea.set("0")
    if (var6.get() == 1):
        txtLemonade.configure(state= NORMAL)
    elif var6.get()== 0:
        txtLemonade.configure(state= DISABLED)
        E_Lemonade.set("0")
    if (var7.get() == 1):
        txtHotChocolate.configure(state= NORMAL)
    elif var7.get()== 0:
        txtHotChocolate.configure(state= DISABLED)
        E_Hot_Chocolate.set("0")
    if (var8.get() == 1):
        txtIcedTea.configure(state= NORMAL)
    elif var8.get()== 0:
        txtIcedTea.configure(state= DISABLED)
        E_Iced_Tea.set("0")
    if (var9.get() == 1):
        txtPineapple_Cake.configure(state= NORMAL)
    elif var9.get()== 0:
        txtPineapple_Cake.configure(state= DISABLED)
        E_Pineapple.set("0")
    if (var10.get() == 1):
        txtBf_Cake.configure(state= NORMAL)
    elif var10.get()== 0:
        txtBf_Cake.configure(state= DISABLED)
        E_Black_Forest.set("0")
    if (var11.get() == 1):
        txtChocolate_Cake.configure(state= NORMAL)
    elif var11.get()== 0:
        txtChocolate_Cake.configure(state= DISABLED)
        E_Chocolate.set("0")
    if (var12.get() == 1):
        txtBS_Cake.configure(state= NORMAL)
    elif var12.get()== 0:
        txtBS_Cake.configure(state= DISABLED)
        E_ButterScotch.set("0")
    if (var13.get() == 1):
        txtCheese_Cake.configure(state= NORMAL)
    elif var13.get()== 0:
        txtCheese_Cake.configure(state= DISABLED)
        E_Cheese.set("0")
    if (var14.get() == 1):
        txtRV_Cake.configure(state= NORMAL)
    elif var14.get()== 0:
        txtRV_Cake.configure(state= DISABLED)
        E_Red_Velvet.set("0")
    if (var15.get() == 1):
        txtWF_Cake.configure(state= NORMAL)
    elif var15.get()== 0:
        txtWF_Cake.configure(state= DISABLED)
        E_White_Forest.set("0")
    if (var16.get() == 1):
        txtCoffee_Cake.configure(state= NORMAL)
    elif var16.get()== 0:
        txtCoffee_Cake.configure(state= DISABLED)
        E_Coffee_Cake.set("0")


def CostOfItem():

    # Item1=float(E_Latte.get() * int(cr.execute("select * from items where name = 'Latte'").fetchone()[2]))
    # Item2=float(E_Cappucino.get() * int(cr.execute("select * from items where name = 'Cappucino'").fetchone()[2]) )
    # Item3=float(E_Espresso.get() * int(cr.execute("select * from items where name = 'Espresso'").fetchone()[2]))
    # Item4=float(E_Iced_Latte.get() * int(cr.execute("select * from items where name = 'Iced_Latte'").fetchone()[2]))
    # Item5=float(E_Tea.get() * int( cr.execute("select * from items where name = 'Tea'").fetchone()[2]))
    # Item6=float(E_Lemonade.get() * int(cr.execute("select * from items where name = 'Lemonade'").fetchone()[2]))
    # Item7=float(E_Hot_Chocolate.get() * int(cr.execute("select * from items where name = 'Hot_Chocolate'").fetchone[2]))
    # Item8=float(E_Iced_Tea.get() * int(cr.execute("select * from items where name = 'Iced_Tea'").fetchone()[2]))

    # Item9=float(E_Pineapple.get() * int(cr.execute("select * from items where name = 'Pineapple_Cake'").fetchone()[2]))
    # Item10=float(E_Black_Forest.get() * int(cr.execute("select * from items where name = 'Black_Forest_Cake'").fetchone()[2]))
    # Item11=float(E_Chocolate.get()  * int(cr.execute("select * from items where name = 'Chocolate_Cake'").fetchone()[2]))
    # Item12=float(E_ButterScotch.get() * int(cr.execute("select * from items where name = 'Butterscotch_Cake'").fetchone()[2]))
    # Item13=float(E_Cheese.get() * int(cr.execute("select * from items where name = 'Cheese_Cake'").fetchone()[2]))
    # Item14=float(E_Red_Velvet.get() * int(cr.execute("select * from items where name = 'Red_Velvet_Cake'").fetchone()[2]))
    # Item15=float(E_White_Forest.get() * int(cr.execute("select * from items where name = 'White_Forest_Cake'").fetchone()[2]))
    # Item16=float(E_Coffee_Cake.get() * int(cr.execute("select * from items where name = 'Coffee_Cake'").fetchone()[2]))


    Item1=float(E_Latte.get())
    Item2=float(E_Cappucino.get())
    Item3=float(E_Espresso.get())
    Item4=float(E_Iced_Latte.get())
    Item5=float(E_Tea.get())
    Item6=float(E_Lemonade.get())
    Item7=float(E_Hot_Chocolate.get())
    Item8=float(E_Iced_Tea.get())

    Item9=float(E_Pineapple.get())
    Item10=float(E_Black_Forest.get())
    Item11=float(E_Chocolate.get())
    Item12=float(E_ButterScotch.get())
    Item13=float(E_Cheese.get())
    Item14=float(E_Red_Velvet.get())
    Item15=float(E_White_Forest.get())
    Item16=float(E_Coffee_Cake.get())

    PriceOfDrinks = (Item1*120) + (Item2*199) + (Item3*205) + (Item4*189) + (Item5*199) + (Item6*140) + (Item7*160) + (Item8 * 129)
    PriceOfCakes = (Item9 * 135) + (Item10 * 220) + (Item11*199) + (Item12 * 149) + (Item13 * 180) + (Item14 * 160) + (Item15 * 180 ) + (Item16 * 250) 

    DrinksPrice = "Rs.",str('%.2f'%(PriceOfDrinks))
    CakesPrice = "Rs.",str('%.2f'%(PriceOfCakes))
    CostOfCakes.set(CakesPrice)
    CostOfDrinks.set(DrinksPrice)
    SC="Rs.",str('%.2f'%(159))
    ServiceCharge.set(SC)

    SubTotalOfItems = "Rs.",str('%.2f'%(PriceOfDrinks + PriceOfCakes+ 159))
    SubTotal.set(SubTotalOfItems)

    Tax="Rs.",str('%.2f'%((PriceOfCakes + PriceOfDrinks + 159) * 0.18))
    PaidTax.set(Tax)
    TT = ((PriceOfDrinks + PriceOfCakes + 159)* 0.18)
    TC = "Rs.",str('%.2f'%(PriceOfDrinks + PriceOfCakes + 159 + TT))
    TotalCost.set(TC)


def Reciept():
    txtReciept.delete("1.0",END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Reciept_Ref.set("Bill " + randomRef)

    txtReciept.insert(END,'Reciept Ref:\t\t\t'+ Reciept_Ref.get() + '\t\t' + DateOfOrder.get()+ '\n')
    txtReciept.insert(END,'Item\t\t\t\t\t'+ "Cost Of Items\n\n")
    txtReciept.insert(END,'Latte: \t\t\t\t\t'+ E_Latte.get()+"\n")
    txtReciept.insert(END,'Cappuccino: \t\t\t\t\t'+ E_Cappucino.get()+"\n")
    txtReciept.insert(END,'Espresso: \t\t\t\t\t'+ E_Espresso.get()+"\n")
    txtReciept.insert(END,'Iced Latte: \t\t\t\t\t'+ E_Iced_Latte.get()+"\n")
    txtReciept.insert(END,'Tea: \t\t\t\t\t'+ E_Tea.get()+"\n")
    txtReciept.insert(END,'Lemonade: \t\t\t\t\t'+ E_Lemonade.get()+"\n")
    txtReciept.insert(END,'Hot Chocolate: \t\t\t\t\t'+ E_Hot_Chocolate.get()+"\n")
    txtReciept.insert(END,'Iced Tea: \t\t\t\t\t'+ E_Iced_Tea.get()+"\n")
    txtReciept.insert(END,'Pineapple Cake: \t\t\t\t\t'+ E_Pineapple.get()+"\n")
    txtReciept.insert(END,'Black Forest Cake: \t\t\t\t\t'+ E_Black_Forest.get()+"\n")
    txtReciept.insert(END,'Chocolate Cake: \t\t\t\t\t'+ E_Chocolate.get()+"\n")
    txtReciept.insert(END,'Butterscotch Cake: \t\t\t\t\t'+ E_ButterScotch.get()+"\n")
    txtReciept.insert(END,'Cheese Cake: \t\t\t\t\t'+ E_Cheese.get()+"\n")
    txtReciept.insert(END,'Red Velvet Cake: \t\t\t\t\t'+ E_Red_Velvet.get()+"\n")
    txtReciept.insert(END,'White Forest Cake: \t\t\t\t\t'+ E_White_Forest.get()+"\n")
    txtReciept.insert(END,'Coffee Cake: \t\t\t\t\t'+ E_Coffee_Cake.get()+"\n")
    txtReciept.insert(END,'Cost Of Drinks: \t\t'+ CostOfDrinks.get() +  '\nTax Paid:\t\t'+PaidTax.get()+"\n")
    txtReciept.insert(END,'Cost Of Cakes: \t\t'+ CostOfCakes.get()+ '\nSubTotal:\t\t' +SubTotal.get()+"\n")
    txtReciept.insert(END,'Service Charge: \t\t'+ ServiceCharge.get()+ '\nTotal Cost:\t\t' + TotalCost.get() + "\n")



#==================================VARIABLES=================================

var1 = IntVar()
var1.set("0")
var2 = IntVar()
var2.set("0")
var3 = IntVar()
var3.set("0")
var4 = IntVar()
var4.set("0")
var5 = IntVar()
var5.set("0")
var6 = IntVar()
var6.set("0")
var7 = IntVar()
var7.set("0")
var8 = IntVar()
var8.set("0")

var9 = IntVar()
var9.set("0")
var10 = IntVar()
var10.set("0")
var11 = IntVar()
var11.set("0")
var12 = IntVar()
var12.set("0")
var13 = IntVar()
var13.set("0")
var14 = IntVar()
var14.set("0")
var15 = IntVar()
var15.set("0")
var16 = IntVar()
var16.set("0")

DateOfOrder=StringVar()
Reciept_Ref=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostOfCakes=StringVar()
CostOfDrinks=StringVar()
ServiceCharge=StringVar()
txtReciept=StringVar()

E_Latte=StringVar()
E_Cappucino=StringVar()
E_Espresso=StringVar()
E_Iced_Latte=StringVar()
E_Tea=StringVar()
E_Lemonade=StringVar()
E_Hot_Chocolate=StringVar()
E_Iced_Tea=StringVar()

E_Pineapple=StringVar()
E_Black_Forest=StringVar()
E_Chocolate=StringVar()
E_ButterScotch=StringVar()
E_Cheese=StringVar()
E_Red_Velvet=StringVar()
E_White_Forest=StringVar()
E_Coffee_Cake=StringVar()

PaidTax.set("")
SubTotal.set("")
TotalCost.set("")
CostOfDrinks.set("")
CostOfCakes.set("")
ServiceCharge.set("")
txtReciept.set("")

E_Latte.set("0")
E_Cappucino.set("0") 
E_Espresso.set("0") 
E_Iced_Latte.set("0") 
E_Tea.set("0") 
E_Lemonade.set("0") 
E_Hot_Chocolate.set("0") 
E_Iced_Tea.set("0") 

E_Pineapple.set("0") 
E_Black_Forest.set("0") 
E_Chocolate.set("0") 
E_ButterScotch.set("0") 
E_Cheese.set("0") 
E_Red_Velvet.set("0") 
E_White_Forest.set("0") 
E_Coffee_Cake.set("0") 

DateOfOrder.set(time.strftime("%d/%m/%Y"))


# ============================COLUMN1=============================


Latte = Checkbutton(f1aa, text="Latte \t", variable = var1, onvalue= 1, offvalue=0,bg='#bf7c58',font=('arial',18,'bold'),command=chkbutton_value).grid(row=0,column=0,sticky=W)
Cappuccino = Checkbutton(f1aa, text="Cappuccino \t", variable = var2, onvalue= 1,bg='#bf7c58', offvalue=0,font=('arial',18,'bold'),command=chkbutton_value).grid(row=1,column=0,sticky=W)
Espresso = Checkbutton(f1aa, text="Espresso \t", variable = var3, onvalue= 1,bg='#bf7c58', offvalue=0,font=('arial',18,'bold'),command=chkbutton_value).grid(row=2,column=0,sticky=W)
Iced_latte = Checkbutton(f1aa, text="Iced Latte \t", variable = var4, onvalue= 1,bg='#bf7c58', offvalue=0,font=('arial',18,'bold'),command=chkbutton_value).grid(row=3,column=0,sticky=W)
Tea = Checkbutton(f1aa, text="Tea \t", variable = var5, onvalue= 1, offvalue=0,bg='#bf7c58',font=('arial',18,'bold'),command=chkbutton_value).grid(row=4,column=0,sticky=W)
Lemonade = Checkbutton(f1aa, text="Lemonade \t", variable = var6, onvalue= 1,bg='#bf7c58', offvalue=0,font=('arial',18,'bold'),command=chkbutton_value).grid(row=5,column=0,sticky=W)
Hot_Chocolate = Checkbutton(f1aa, text="Hot Chocolate \t", variable = var7, onvalue= 1,bg='#bf7c58', offvalue=0,font=('arial',18,'bold'),command=chkbutton_value).grid(row=6,column=0,sticky=W)
Iced_Tea = Checkbutton(f1aa, text="Iced Tea \t", variable = var8, onvalue= 1,bg='#bf7c58', offvalue=0,font=('arial',18,'bold'),command=chkbutton_value).grid(row=7,column=0,sticky=W)

# ============================COLUMN2=============================
Pineapple = Checkbutton(f1ab, text="Pineapple Cake \t", variable = var9, onvalue= 1,bg='#bf7c58', offvalue=0,font=('arial',18,'bold'),command=chkbutton_value).grid(row=0,column=0,sticky=W)
Black_Forest = Checkbutton(f1ab, text="Black Forest Cake \t", variable = var10, onvalue= 1,bg='#bf7c58', offvalue=0,font=('arial',18,'bold'),command=chkbutton_value).grid(row=1,column=0,sticky=W)
Chocolate = Checkbutton(f1ab, text="Chocolate Cake \t", variable = var11, onvalue= 1,bg='#bf7c58', offvalue=0,font=('arial',18,'bold'),command=chkbutton_value).grid(row=2,column=0,sticky=W)
ButterScotch = Checkbutton(f1ab, text="ButterScotch Cake \t", variable = var12, onvalue= 1,bg='#bf7c58', offvalue=0,font=('arial',18,'bold'),command=chkbutton_value).grid(row=3,column=0,sticky=W)
Cheese = Checkbutton(f1ab, text="Cheese Cake \t", variable = var13, onvalue= 1, offvalue=0,bg='#bf7c58',font=('arial',18,'bold'),command=chkbutton_value).grid(row=4,column=0,sticky=W)
Red_Velvet = Checkbutton(f1ab, text="Red Velvet Cake \t", variable = var14, onvalue= 1,bg='#bf7c58', offvalue=0,font=('arial',18,'bold'),command=chkbutton_value).grid(row=5,column=0,sticky=W)
White_Forest = Checkbutton(f1ab, text="White Forest Cake \t", variable = var15, onvalue= 1,bg='#bf7c58', offvalue=0,font=('arial',18,'bold'),command=chkbutton_value).grid(row=6,column=0,sticky=W)
Coffee = Checkbutton(f1ab, text="Coffee Cake \t", variable = var16, onvalue= 1, offvalue=0,bg='#bf7c58',font=('arial',18,'bold'),command=chkbutton_value).grid(row=7,column=0,sticky=W)

# ========================ENTRY WIDGET FIR COLUMN1=====================

txtLatte=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Latte,state=DISABLED)
txtLatte.grid(row=0,column=1)
txtCappuccino=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Cappucino,state=DISABLED)
txtCappuccino.grid(row=1,column=1)
txtEspresso=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Espresso,state=DISABLED)
txtEspresso.grid(row=2,column=1)
txtIcedLatte=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Iced_Latte,state=DISABLED)
txtIcedLatte.grid(row=3,column=1)
txtTea=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Tea,state=DISABLED)
txtTea.grid(row=4,column=1)
txtLemonade=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Lemonade,state=DISABLED)
txtLemonade.grid(row=5,column=1)
txtHotChocolate=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Hot_Chocolate,state=DISABLED)
txtHotChocolate.grid(row=6,column=1)
txtIcedTea=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Iced_Tea,state=DISABLED)
txtIcedTea.grid(row=7,column=1)
# ========================ENTRY WIDGET FIR COLUMN2=====================
txtPineapple_Cake=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Pineapple,state=DISABLED)
txtPineapple_Cake.grid(row=0,column=1)
txtBf_Cake=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Black_Forest,state=DISABLED)
txtBf_Cake.grid(row=1,column=1)
txtChocolate_Cake=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Chocolate,state=DISABLED)
txtChocolate_Cake.grid(row=2,column=1)
txtBS_Cake=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_ButterScotch,state=DISABLED)
txtBS_Cake.grid(row=3,column=1)
txtCheese_Cake=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Cheese,state=DISABLED)
txtCheese_Cake.grid(row=4,column=1)
txtRV_Cake=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Red_Velvet,state=DISABLED)
txtRV_Cake.grid(row=5,column=1)
txtWF_Cake=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_White_Forest,state=DISABLED)
txtWF_Cake.grid(row=6,column=1)
txtCoffee_Cake=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Coffee_Cake,state=DISABLED)
txtCoffee_Cake.grid(row=7,column=1)


#===========================INFORMATION==========================

lblReciept = Label(ft2,font=('arial',12,'bold'),bg='#bf7c58',text="Reciept",bd=2)
lblReciept.grid(row=0,column=0,sticky=W)
txtReciept = Text(ft2,font=('arial',11,'bold'), bd=8, width=55)
txtReciept.grid(row=1,column=0)


#==========================ITEM INFORMATION===============================
lblCostOfDrinks=Label(f2aa,font=('arial',16,'bold'),bg='#bf7c58',text="Cost Of Drinks",bd=8)
lblCostOfDrinks.grid(row=0,column=0,sticky=W)
txtCostOfDrinks=Entry(f2aa,font=('arial',16,'bold'),bd=8,justify = 'left',textvariable=CostOfDrinks)
txtCostOfDrinks.grid(row=0,column=1,sticky=W)

lblCostOfCakes=Label(f2aa,font=('arial',16,'bold'),bg='#bf7c58',text="Cost Of Food",bd=8)
lblCostOfCakes.grid(row=1,column=0,sticky=W)
txtCostOfCakes=Entry(f2aa,font=('arial',16,'bold'),bd=8,justify = 'left',textvariable=CostOfCakes)
txtCostOfCakes.grid(row=1,column=1,sticky=W)

lblServiceCharge=Label(f2aa,font=('arial',16,'bold'),bg='#bf7c58',text="Service Charge",bd=8)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(f2aa,font=('arial',16,'bold'),bd=8,justify = 'left',textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1,sticky=W)


#==========================PAYMENT INFORMATION===============================

lblPaidTax=Label(f2ab,font=('arial',16,'bold'),bg='#bf7c58',text="Paid Tax",bd=8)
lblPaidTax.grid(row=0,column=0,sticky=W)
txtPaidTax=Entry(f2ab,font=('arial',16,'bold'),bd=8,justify = 'left',textvariable=PaidTax)
txtPaidTax.grid(row=0,column=1,sticky=W)

lblSubTotal=Label(f2ab,font=('arial',16,'bold'),bg='#bf7c58',text="Sub Total",bd=8)
lblSubTotal.grid(row=1,column=0,sticky=W)
txtSubTotal=Entry(f2ab,font=('arial',16,'bold'),bd=8,justify = 'left', textvariable=SubTotal)
txtSubTotal.grid(row=1,column=1,sticky=W)

lblTotalCost=Label(f2ab,font=('arial',16,'bold'),bg='#bf7c58',text="Total Cost",bd=8)
lblTotalCost.grid(row=2,column=0,sticky=W)
txtTotalCost=Entry(f2ab,font=('arial',16,'bold'),bd=8,justify = 'left',textvariable=TotalCost)
txtTotalCost.grid(row=2,column=1,sticky=W)



#==========================BUTTONS===============================

btnTotal = Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Total",bg='#bf586b',command=CostOfItem).grid(row=0,column=0)
btnReciept = Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Receipt",bg='#bf586b',command=Reciept).grid(row=0,column=1)
btnReset = Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Reset",bg='#bf586b',command=Reset).grid(row=0,column=2)
btnExit = Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Exit",bg='#bf586b',command=qExit).grid(row=0,column=3)




root.mainloop()
