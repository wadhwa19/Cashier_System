#!/usr/bin/env python
# coding: utf-8

# In[150]:


import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox as msg
import random


# In[197]:


a=tk.Tk()
a.title('CASHIER SYSTEM')
a.geometry('600x800')
background=ImageTk.PhotoImage(Image.open('C:\\Users\\wadhw\\Downloads\\menu2.png'))
l4=tk.Label(image=background)
l4.place(x=0,y=0)
l2=tk.Label(a,text=' Mac-Cafe',font='broadway 20',fg='maroon',bg='white')
l2.grid(row=0,column=2)
l1=tk.Label(a,text='Enter your meal card number :',font='times 10 bold',fg='black',bg='white')
l1.grid(row=2,column=1)
def name_and_balance():
    names=['Jake','Myra','Leo','Summer','Mario','Lily','Ryan','Nick']
    name=random.choice(names)
    msg.showinfo('Meal Card Details',f'Hello {name}, welcome to Mac-Cafe!\n Your current balance is $3000\n Please click on "OK" to place your order')
b2=tk.Button(a,text='Next',fg='maroon',bg='gold',font='times 10 bold',command=name_and_balance)
b2.grid(row=2,column=3)
l3=tk.Label(a,text='MENU',font='broadway 15 bold',fg='gold',bg='white')
l3.place(x=250,y=70)
e1=tk.Entry(a)
e1.grid(row=2,column=2)
l5=tk.Label(a,text=' Soft Serve-$5',font='times 10 bold',fg='black',bg='white')
l6=tk.Label(a,text=' Lemonade-$3',font='times 10 bold',fg='black',bg='white')
l7=tk.Label(a,text='Chicken burger-$7',font='times 10 bold',fg='black',bg='white')
l8=tk.Label(a,text='Fries-$4',font='times 10 bold',fg='black',bg='white')
l9=tk.Label(a,text='Popsicle-$3',font='times 10 bold',fg='black',bg='white')
l10=tk.Label(a,text='Pizza-$9',font='times 10 bold',fg='black',bg='white')
l11=tk.Label(a,text='Omlette-$6',font='times 10 bold',fg='black',bg='white')
l12=tk.Label(a,text='Coffee-$3',font='times 10 bold',fg='black',bg='white')
l13=tk.Label(a,text='Salami Sandwhich-$6',font='times 10 bold',fg='black',bg='white')
l14=tk.Label(a,text='Cupcake-$4',font='times 10 bold',fg='black',bg='white')
l15=tk.Label(a,text='Taco-$9',font='times 10 bold',fg='black',bg='white')
l16=tk.Label(a,text='Hot dog-$5',font='times 10 bold',fg='black',bg='white')
l5.place(x=80,y=170)
l6.place(x=200,y=170)
l7.place(x=350,y=170)
l8.place(x=500,y=170)
l9.place(x=80,y=360)
l10.place(x=200,y=360)
l11.place(x=350,y=360)
l12.place(x=500,y=360)
l13.place(x=80,y=550)
l14.place(x=200,y=550)
l15.place(x=350,y=550)
l16.place(x=500,y=550)
s1=tk.Spinbox(a,from_=0,to=10,width=2)
s1.place(x=80,y=185)
s2=tk.Spinbox(a,from_=0,to=10,width=2)
s2.place(x=200,y=185)
s3=tk.Spinbox(a,from_=0,to=10,width=2)
s3.place(x=350,y=185)
s4=tk.Spinbox(a,from_=0,to=10,width=2)
s4.place(x=500,y=185)
s5=tk.Spinbox(a,from_=0,to=10,width=2)
s5.place(x=80,y=380)
s6=tk.Spinbox(a,from_=0,to=10,width=2)
s6.place(x=200,y=380)
s7=tk.Spinbox(a,from_=0,to=10,width=2)
s7.place(x=350,y=380)
s8=tk.Spinbox(a,from_=0,to=10,width=2)
s8.place(x=500,y=380)
s9=tk.Spinbox(a,from_=0,to=10,width=2)
s9.place(x=80,y=570)
s10=tk.Spinbox(a,from_=0,to=10,width=2)
s10.place(x=200,y=570)
s11=tk.Spinbox(a,from_=0,to=10,width=2)
s11.place(x=350,y=570)
s12=tk.Spinbox(a,from_=0,to=10,width=2)
s12.place(x=500,y=570)

def bill():
    cb=int(s3.get())*7
    ss=int(s1.get())*5
    l=int(s2.get())*3
    f=int(s4.get())*4
    pp=int(s5.get())*3
    p=int(s6.get())*9
    o=int(s7.get())*6
    c=int(s8.get())*3
    sals=int(s9.get())*6
    cc=int(s10.get())*4
    t=int(s11.get())*9
    hd=int(s12.get())*5
    amount=int(cb+ss+l+f+pp+p+o+c+sals+cc+t+hd)
    tax=(amount*18)/100
    total=int(tax+amount)
    balance=int(3000-amount)
    msg.showinfo('Payment Reciept',f'\t MAC-CAFE\t \n Subtotal=${amount}\nTax(%18)=${tax}\nTotal Amount=${total}\nYour Balance =${balance}\nThank you for shopping with us:)\nHave a nice day!')
b1=tk.Button(a,text='Place Order',fg='maroon',bg='gold',font='times 15',command=bill)
b1.place(x=250,y=600)
a.mainloop()


# In[196]:





# In[ ]:





# In[ ]:




