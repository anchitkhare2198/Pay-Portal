from Tkinter import *
from tkMessageBox import *
import sqlite3
con=sqlite3.Connection('MyDb')
cur=con.cursor()

root4=Tk()
root4.title('Splash Screen')
#img=PhotoImage(file='C:\\Users\\171B033\\Desktop\\a.gif')
img=PhotoImage(file='ak33.gif')

def fun(e):
    root4.destroy()
    root=Tk()
    root.title('Pay Portal')
    #root.configure(background='Light Blue')
    root.geometry('300x600+0+0')
    root.resizable(0,0)
    #d=PhotoImage(file='E:\\project\\gif\\abcd.gif')
    d=PhotoImage(file='abcd.gif')
    Label(root,image=d).grid(row=0,column=0,columnspan=4)
    Label(root,text='\nPAY USING\n',fg='Black',font='Arial 20 bold').grid(row=1,column=2)
    v1=IntVar()
    #a=PhotoImage(file='E:\\project\\gif\\q.gif')
    a=PhotoImage(file='q.gif')
    Radiobutton(root,image=a,variable=v1,value=1).grid(row=3,column=2)
    #b=PhotoImage(file='E:\\project\\gif\\c.gif')
    b=PhotoImage(file='c.gif')
    Radiobutton(root,image=b,variable=v1,value=2).grid(row=4,column=2)
    #e=PhotoImage(file='E:\\project\\gif\\12.gif')
    e=PhotoImage(file='12.gif')
    Radiobutton(root,image=e,variable=v1,value=3).grid(row=5,column=2)

    #ima=PhotoImage(file='E:\\project\\gif\\B1.gif')

    def fun():
            #PayTm
            cur.execute("create table if not exists paytm(mob_no number primary key, card_no number(20), card_name varchar(20), cvv number(10), amount number(10))")
            if v1.get()==1:
                    root4=Tk()
                    root4.resizable(0,0)
                    
                    #root4.geometry('400x600')
                    #Pay Now
                    
                    def funt3():
                            
                            root1=Tk()
                            #root1.configure(background='Sky Blue')
                            Label(root1,text='WELCOME TO PAYTM',fg='Black',font='calibri 20',background='White').grid(row=1,column=1,columnspan=4)
                            root1.geometry('500x750+1+1')
                            root1.resizable(0,0)
                            
                            Label(root1,text='Enter Mobile Number',font='Arial 12 ').grid(row=2,column=1)
                            E=Entry(root1,width=12,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                            E.grid(row=2,column=2)
                            #root.destroy()                        
                            
                            a1=IntVar()
                            a2=IntVar()
                            a3=IntVar()
                            def funt():
                                    #Mobile Number
                                    #root4.destroy()
                                    a=int(E.get())
                                    c=0
                                    while a>0:
                                            a=a/10
                                            c=c+1
                                    if c!=10:
                                            showerror('ERROR','This field must have 10 digits\nPlease Enter Correct Mobile Number')
                                    
                                    
                                    else:
                                            #Card Details
                                            Label(root1,text='Enter your Card details',fg='Black',font='calibri 20').grid(row=4,column=1)
                                            #Card Number
                                            Label(root1,text='Enter Card Number',font='Arial 12').grid(row=6,column=1)
                                            a1=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a1.grid(row=6,column=2)
                                            def cno():
                                                    b1=int(a1.get())
                                                    c11=0
                                                    while b1>0:
                                                            b1=b1/10
                                                            c11=c11+1
                                                    if c11!=16:
                                                            showerror('ERROR','Invalid Account Number\nPlease Enter a Valid Account Number')
                                            Button(root1,text='Enter',command=cno,width=6,bd=5,bg='Light Blue').grid(row=7,column=2)

                                            #Card Holder's Name
                                            Label(root1,text='Enter card Holder Name',font='Arial 12').grid(row=8,column=1)
                                            a2=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a2.grid(row=8,column=2)
                                            def chn():
                                                    b2=a2.get()
                                            Button(root1,text='Enter',command=chn,width=6,bd=5,bg='Light Blue').grid(row=9,column=2)

                                            #CVV
                                            Label(root1,text='Enter CVV',font='Arial 12').grid(row=10,column=1)
                                            a3=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a3.grid(row=10,column=2)
                                            def cv():
                                                    b3=int(a3.get())
                                                    c12=0
                                                    while b3>0:
                                                            b3=b3/10
                                                            c12=c12+1
                                                    if c12!=3:
                                                            showerror('ERROR','Invalid CVV\nPlease Enter Correct CVV')    
                                            Button(root1,text='Enter',command=cv,width=6,bd=5,bg='Light Blue').grid(row=11,column=2)

                                            #Reciever's Details
                                            Label(root1,text='Enter Recievers Details',fg='Black',font='calibri 20').grid(row=12,column=1)
                                            #Reciever's Mobile Number
                                            Label(root1,text='Enter Mobile Number',font='Arial 12').grid(row=13,column=1)
                                            h=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            h.grid(row=13,column=2)
                                            def funt2():
                                                    a=int(h.get())
                                                    c=0
                                                    while a>0:
                                                            a=a/10
                                                            c=c+1
                                                    if c!=10:
                                                            showerror('ERROR','This field must have 10 digits\nPlease Enter Correct Mobile Number')
                                            Button(root1,text='Enter',command=funt2,width=6,bd=5,bg='Light Blue').grid(row=14,column=2)
            
                                            #Amount To Be Paid
                                            Label(root1,text='Enter Amount to be Paid',font='Arial 12').grid(row=15,column=1)
                                            i=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            i.grid(row=15,column=2)
                                            
                                
                                            
                                            def funtt():
                                                aa=int(i.get())                                                
                                            Button(root1,text='Enter',command=funtt,width=6,bd=5,bg='Light Blue').grid(row=16,column=2)
                                            


                                            

                                            #DBMS

                                            #insert
                                            def insert():
                                                    abh=int(0)
                                                    cur.execute("insert into paytm values(?,?,?,?,?)",(int(E.get()),int(a1.get()),a2.get(),int(a3.get()),abh))
                                                    con.commit()
                                                    showinfo('Information','Card Saved for further use')
                                            Button(root1,text='Save Card for further use',command=insert,width=19,bd=5,bg='Light Blue').grid(row=17,column=1)


                                            Label(root1,text='Enter mobile number to view saved cards',font='Arial 12').grid(row=19,column=1)
                                            d=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            d.grid(row=19,column=2)
                                            
                                            #show
                                            def show():
                                                    a=[(int(d.get()))]
                                                    cur.execute("select *from paytm where mob_no=?",a)
                                                    x=cur.fetchall()
                                                    showinfo('Result',x)
                                            Button(root1,text='Show Save Card',command=show,width=15,bd=5,bg='Light Blue').grid(row=20,column=2)

                                            

                                            #showall
                                            def showall():
                                                    cur.execute("select *from paytm")
                                                    x=cur.fetchall()
                                                    showinfo("Result",x)
                                            Button(root1,text='Show all saved Cards',command=showall,width=17,bd=5,bg='Light Blue').grid(row=22,column=2) 


                                             
                                            #delete all                                        
                                            def delete():
                                                    cur.execute("drop table paytm")
                                                    x=cur.fetchall()
                                                    Label(root1,text=x).grid(row=21,column=1)
                                                    showinfo('Information','All saved Cards are Deleted')
                                            Button(root1,text='Delete all saved cards',command=delete,width=17,bd=5,bg='Light Blue').grid(row=22,column=1)

                                            #PAY
                                            def abcd():
                                                    qq=int(E.get())
                                                    ff=int(i.get())
                                                    
                                                    cur.execute("select amount from paytm where mob_no=?",(qq,))
                                                    x=cur.fetchall()
                                                    if (len(x)==0):
                                                        showinfo('Information','This Mobile Number is Not Registered\nPlease Enter All valid details and press Save for further use to get yourelf Registered.')
                                                    else:
                                                        aa=x[0][0]
                                                        #print ff
                                                    
                                                        gg=(aa-ff)
                                                        #print gg                                                    
                                                        #f=[gg,qq]
                                                        #if kk==int(h.get()):
                                                        #   showError('Error','Please Enter Recievers Mobile Number')

                                                    

                                                        if len(h.get()) == 0:
                                                            showinfo("Error!", "Please Enter Recievers Mobile Number")

                                                        else:
                                                            if gg<0:
                                                                showinfo("Information","Insufficient Balace")
                                                            else:
                                                                cur.execute("update paytm set amount=? where mob_no=?",(gg,qq))
                                                                x=cur.fetchall()
                                                                #q1=int(0)
                                                                #q2=''
                                                                #q3=int(0)
                                                                #cur.execute("insert into paytm values(?,?,?,?,?)",(int(h.get()),q1,q2,q3,hh))
                                                                hh=int(h.get())
                                                                cur.execute("select amount from paytm where mob_no=?",(hh,))
                                                                y=cur.fetchall()
                                                                if (len(y)==0):                                                                    
                                                                    showinfo('Information','This Mobile Number is Not Registered\nPlease Enter All valid details and press Save for further use to get yourelf Registered.')

                                                                else:                                                                    
                                                                    aa=y[0][0]
                                                                    #print ff
                                                    
                                                                    gg=(aa+ff)
                                                                    #print gg
                                                                    #f=[gg,qq]
                                                                    cur.execute("update paytm set amount=? where mob_no=?",(gg,hh))
                                                                    x=cur.fetchall()
                                                                    showinfo('Information','Your Amount has been successfully Paid')                                                            
                                            Button(root1,text='PAY',command=abcd,width=6,bd=5,bg='Light Blue').grid(row=25,column=1,columnspan=5)

                                            #Passbook
                                            def abcd2():
                                                    root2=Tk()
                                                    root2.resizable(0,0)
                                                    
                                                    Label(root2,text='PASSBOOK',fg='Black',font='calibri 40',background='white').grid(row=1,column=1,columnspan=12)
                                                    Label(root2,text='Enter Mobile No').grid(row=2,column=1)
                                                    r=Entry(root2,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                                    r.grid(row=2,column=2)
                                                    def abcd3():
                                                            a=int(r.get())
                                                            aa=[int(r.get())]
                                                            c=0
                                                            while a>0:
                                                                    a=a/10
                                                                    c=c+1
                                                            if c!=10:
                                                                    showerror('ERROR','This field must have 10 digits\nPlease Enter Correct Mobile Number')
                                                            
                                                            
                                                            else:
                                                                cur.execute("select amount from paytm where mob_no=?",(aa))
                                                                x=cur.fetchall()
                                                                if (len(x)==0):
                                                                    showinfo('Information','Mobile Number Not Registered.')

                                                                else:
                                                                    ab=x[0][0]
                                                                    showinfo('Passbook',(('Total Amount is '),ab))                                                            
                                                    Button(root2,text='Enter',command=abcd3,width=6,bd=5,bg='Light Blue').grid(row=3,column=2)

                                                    #Quit
                                                    def abcd4():
                                                        ans=askyesnocancel('Quit','Are you sure you want to quit')
                                                        if ans==True:
                                                           root2.destroy()
                                                    Button(root2,text='Quit',command=abcd4,width=6,bd=5,bg='Light Blue').grid(row=4,column=1)
                                                    
                                                    root2.mainloop()
                                            Button(root1,text='Passbook',command=abcd2,width=7,bd=5,bg='Light Blue').grid(row=27,column=1)

                                            #Quit
                                            def abcd4():
                                                   ans=askyesnocancel('Quit','Are you sure you want to quit')                                              #      
                                                   if ans==True:
                                                       root1.destroy()
                                                       root4.destroy()
                                            Button(root1,text='Quit',command=abcd4,width=6,bd=5,bg='Light Blue').grid(row=27,column=2)
                                            
                            Button(root1,text='Enter',command=funt,width=6,bd=5,bg='Light Blue').grid(row=3,column=2)
                            root1.mainloop()
                    #abc2=PhotoImage(file='E:\\project\\gif\\p1.gif')
                    Button(root4,text='PayNow',command=funt3,font='Arial 20',width=9,height=3,bd=5,bg='Light Blue').grid(row=1,column=1)

                    def funt4():
                            #Add Money
                            root1=Tk()
                            
                            Label(root1,text='WELCOME TO PAYTM',fg='Black',font='calibri 20',background='white').grid(row=1,column=1,columnspan=4)
                            root1.geometry('500x650+1+1')
                            root1.resizable(0,0)

                            
                            Label(root1,text='Enter Mobile Number',font='Arial 12').grid(row=2,column=1)
                            E=Entry(root1,width=12,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                            E.grid(row=2,column=2)
                            #root.destroy()                        
                            
                            a1=IntVar()
                            a2=IntVar()
                            a3=IntVar()

                            
                            def funt():
                                    #Mobile Number
                                    #root4.destroy()
                                    a=int(E.get())
                                    c=0
                                    while a>0:
                                            a=a/10
                                            c=c+1
                                    if c!=10:
                                            showerror('ERROR','This field must have 10 digits\nPlease Enter Correct Mobile Number')
                                    
                                    else:
                                            #Card Details
                                            Label(root1,text='\n   Enter your Card details\n',fg='Black',font='calibri 20').grid(row=4,column=1)
                                            #Card Number
                                            Label(root1,text='Enter Card Number',font='Arial 12').grid(row=6,column=1)
                                            a1=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a1.grid(row=6,column=2)
                                            def cno():
                                                    b1=int(a1.get())
                                                    c11=0
                                                    while b1>0:
                                                            b1=b1/10
                                                            c11=c11+1
                                                    if c11!=16:
                                                            showerror('ERROR','Invalid Account Number\nPlease Enter a Valid Account Number')
                                            Button(root1,text='Enter',command=cno,width=6,bd=5,bg='Light Blue').grid(row=7,column=2)

                                            #Card Holder's Name
                                            Label(root1,text='Enter card Holder Name',font='Arial 12').grid(row=8,column=1)
                                            a2=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a2.grid(row=8,column=2)
                                            def chn():
                                                    b2=a2.get()
                                            Button(root1,text='Enter',command=chn,width=6,bd=5,bg='Light Blue').grid(row=9,column=2)

                                            #CVV
                                            Label(root1,text='Enter CVV',font='Arial 12').grid(row=10,column=1)
                                            a3=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a3.grid(row=10,column=2)
                                            def cv():
                                                    b3=int(a3.get())
                                                    c12=0
                                                    while b3>0:
                                                            b3=b3/10
                                                            c12=c12+1
                                                    if c12!=3:
                                                            showerror('ERROR','Invalid CVV\nPlease Enter Correct CVV')    
                                            Button(root1,text='Enter',command=cv,bd=5,width=6,bg='Light Blue').grid(row=11,column=2)
                                            
                                            #Amount to Add
                                            Label(root1,text='Enter Amount to Add',font='Arial 12').grid(row=13,column=1)
                                            i=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            i.grid(row=13,column=2)
                                            def ata():
                                                    a12=int(i.get())
                                            Button(root1,text='ADD',command=ata,width=6,bd=5,bg='Light Blue').grid(row=14,column=2)


                                            #DBMS

                                            #insert
                                            def insert():
                                                    
                                                    cur.execute("insert into paytm values(?,?,?,?,?)",(int(E.get()),int(a1.get()),a2.get(),int(a3.get()),int(i.get())))
                                                    con.commit()
                                                    showinfo('Information','Card Saved for further use\nYour Money has been added no need to press Add Money Button')
                                            Button(root1,text='Save Card for further use',command=insert,width=19,bd=5,bg='Light Blue').grid(row=15,column=1)

                                            Label(root1,text='Enter mobile number to view saved cards').grid(row=17,column=1)
                                            d=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            d.grid(row=17,column=2)
                                            

                                            #show
                                            def show():
                                                    a=[(int(d.get()))]
                                                    cur.execute("select *from paytm where mob_no=?",a)
                                                    x=cur.fetchall()
                                                    showinfo('Result',x)
                                            Button(root1,text='Show Save Card',command=show,width=17,bd=5,bg='Light Blue').grid(row=18,column=2)


                                            

                                            #showall                                        
                                            def showall():
                                                    cur.execute("select *from paytm")
                                                    x=cur.fetchall()
                                                    showinfo("Result",x)
                                            Button(root1,text='Show all saved Cards',command=showall,width=19,bd=5,bg='Light Blue').grid(row=18,column=1)


                                            #delete all                                        
                                            def delete():
                                                    cur.execute("drop table paytm")
                                                    x=cur.fetchall()
                                                    Label(root1,text=x).grid(row=20,column=1)
                                                    showinfo('Information','All saved Cards are Deleted')
                                            Button(root1,text='Delete all saved cards',command=delete,width=19,bd=5,bg='Light Blue').grid(row=22,column=1)

                                            

                                            #Add Money
                                            def abcd():
                                                    qq=int(E.get())
                                                    ff=int(i.get())
                                                    cur.execute("select amount from paytm where mob_no=?",(qq,))
                                                    x=cur.fetchall()
                                                    if (len(x)==0):
                                                        showinfo('Information','Mobile Number Not Registered\nPlease Enter all valid Details and Press Save for further use to get Registered.')

                                                    else:
                                                        aa=x[0][0]
                                                        #print ff
                                                    
                                                        gg=(aa+ff)
                                                        #print gg
                                                        #f=[gg,qq]
                                                        cur.execute("update paytm set amount=? where mob_no=?",(gg,qq))
                                                        x=cur.fetchall()
                                                        showinfo('Information','Your Amount has been successfully Added')
                                                    
                                            Button(root1,text='Add Money',command=abcd,width=12,bd=5,bg='Light Blue').grid(row=23,column=1,columnspan=5)


                                            #Passbook
                                            def abcd2():
                                                    root2=Tk()
                                                    root2.resizable(0,0)
                                                    
                                                    Label(root2,text='PASSBOOK',fg='Black',font='calibri 40',background='white').grid(row=1,column=1,columnspan=12)
                                                    Label(root2,text='Enter Mobile No').grid(row=2,column=1)
                                                    r=Entry(root2,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                                    r.grid(row=2,column=2)
                                                    def abcd3():
                                                            a=int(r.get())
                                                            aa=[int(r.get())]
                                                            c=0
                                                            while a>0:
                                                                    a=a/10
                                                                    c=c+1
                                                            if c!=10:
                                                                    showerror('ERROR','This field must have 10 digits\nPlease Enter Correct Mobile Number')
                                                            
                                                            
                                                            else:
                                                                cur.execute("select amount from paytm where mob_no=?",(aa))
                                                                x=cur.fetchall()
                                                                if (len(x)==0):
                                                                    showinfo('Information','Mobile Number Not Registered.')

                                                                else:
                                                                    ab=x[0][0]
                                                                    showinfo('Passbook',(('Total Amount is '),ab))
                                                    Button(root2,text='Enter',command=abcd3,width=6,bd=5,bg='Light Blue').grid(row=3,column=2)
                                                    #Quit
                                                    def abcd4():
                                                        ans=askyesnocancel('Quit','Are you sure you want to quit')
                                                        if ans==True:
                                                           root2.destroy()
                                                    Button(root2,text='Quit',command=abcd4,width=6,bd=5,bg='Light Blue').grid(row=4,column=1)
                                                    
                                                    root2.mainloop()
                                            Button(root1,text='Passbook',command=abcd2,width=7,bd=5,bg='Light Blue').grid(row=24,column=1)

                                            #Quit
                                            def abcd4():
                                                   ans=askyesnocancel('Quit','Are you sure you want to quit')
                                                   if ans==True:
                                                       root1.destroy()
                                                       root4.destroy()
                                            Button(root1,text='Quit',command=abcd4,width=6,bd=5,bg='Light Blue').grid(row=24,column=2)

                                            

                                            
                            Button(root1,text='Enter',command=funt,width=6,bd=5,bg='Light Blue').grid(row=3,column=2)                
                            root1.mainloop()
                    Button(root4,text='Add Money',command=funt4,font='Arial 20',width=9,height=3,bd=5,bg='Light Blue').grid(row=1,column=3)        
                    root4.mainloop()


                    
            elif v1.get()==2:
                    #BHIM
                    root4=Tk()
                    root4.resizable(0,0)
                    #root4.geometry('400x600')
                    #Pay Now
                    def funt3():                        
                            root1=Tk()
                            #root1.configure(background='Sky Blue')
                            Label(root1,text='WELCOME TO BHIM',fg='Black',font='calibri 20',background='White').grid(row=1,column=1,columnspan=4)
                            root1.geometry('500x750+1+1')
                            root1.resizable(0,0)
                            
                            Label(root1,text='Enter Mobile Number',font='Arial 12 ').grid(row=2,column=1)
                            E=Entry(root1,width=12,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                            E.grid(row=2,column=2)
                            #root.destroy()                        
                            
                            a1=IntVar()
                            a2=IntVar()
                            a3=IntVar()
                            def funt():
                                    #Mobile Number
                                    #root4.destroy()
                                    a=int(E.get())
                                    c=0
                                    while a>0:
                                            a=a/10
                                            c=c+1
                                    if c!=10:
                                            showerror('ERROR','This field must have 10 digits\nPlease Enter Correct Mobile Number')
                                    
                                    
                                    else:
                                            #Card Details
                                            Label(root1,text='Enter Your Card Details',fg='Black',font='calibri 20').grid(row=4,column=1)
                                            #Card Number
                                            Label(root1,text='Enter Card Number',font='Arial 12').grid(row=6,column=1)
                                            a1=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a1.grid(row=6,column=2)
                                            def cno():
                                                    b1=int(a1.get())
                                                    c11=0
                                                    while b1>0:
                                                            b1=b1/10
                                                            c11=c11+1
                                                    if c11!=16:
                                                            showerror('ERROR','Invalid Account Number\nPlease Enter a Valid Account Number')
                                            Button(root1,text='Enter',command=cno,width=6,bd=5).grid(row=7,column=2)

                                            #Card Holder's Name
                                            Label(root1,text='Enter Card Holder Name',font='Arial 12').grid(row=8,column=1)
                                            a2=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a2.grid(row=8,column=2)
                                            def chn():
                                                    b2=a2.get()
                                            Button(root1,text='Enter',command=chn,width=6,bd=5).grid(row=9,column=2)

                                            #CVV
                                            Label(root1,text='Enter CVV',font='Arial 12').grid(row=10,column=1)
                                            a3=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a3.grid(row=10,column=2)
                                            def cv():
                                                    b3=int(a3.get())
                                                    c12=0
                                                    while b3>0:
                                                            b3=b3/10
                                                            c12=c12+1
                                                    if c12!=3:
                                                            showerror('ERROR','Invalid CVV\nPlease Enter Correct CVV')    
                                            Button(root1,text='Enter',command=cv,width=6,bd=5).grid(row=11,column=2)

                                            #Reciever's Details
                                            Label(root1,text='Enter Recievers Details',fg='Black',font='calibri 20').grid(row=12,column=1)
                                            #Reciever's Mobile Number
                                            Label(root1,text='Enter Mobile Number',font='Arial 12').grid(row=13,column=1)
                                            h=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            h.grid(row=13,column=2)
                                            def funt2():
                                                    a=int(h.get())
                                                    c=0
                                                    while a>0:
                                                            a=a/10
                                                            c=c+1
                                                    if c!=10:
                                                            showerror('ERROR','This field must have 10 digits\nPlease Enter Correct Mobile Number')
                                            Button(root1,text='Enter',command=funt2,width=6,bd=5).grid(row=14,column=2)
            
                                            #Amount To Be Paid
                                            Label(root1,text='Enter Amount to be Paid',font='Arial 12').grid(row=15,column=1)
                                            i=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            i.grid(row=15,column=2)
                                            
                                
                                            
                                            def funtt():
                                                aa=int(i.get())                                                
                                            Button(root1,text='Enter',command=funtt,width=6,bd=5).grid(row=16,column=2)
                                            


                                            

                                            #DBMS

                                            #insert
                                            def insert():
                                                    abh=int(0)
                                                    cur.execute("insert into paytm values(?,?,?,?,?)",(int(E.get()),int(a1.get()),a2.get(),int(a3.get()),abh))
                                                    con.commit()
                                                    showinfo('Information','Card Saved for further use')
                                            Button(root1,text='Save Card for further use',command=insert,width=19,bd=5).grid(row=17,column=1)


                                            Label(root1,text='Enter Mobile Number To View Saved Cards',font='Arial 12').grid(row=19,column=1)
                                            d=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            d.grid(row=19,column=2)
                                            
                                            #show
                                            def show():
                                                    a=[(int(d.get()))]
                                                    cur.execute("select *from paytm where mob_no=?",a)
                                                    x=cur.fetchall()
                                                    showinfo('Result',x)
                                            Button(root1,text='Show Save Card',command=show,width=15,bd=5).grid(row=20,column=2)

                                            

                                            #showall
                                            def showall():
                                                    cur.execute("select *from paytm")
                                                    x=cur.fetchall()
                                                    showinfo("Result",x)
                                            Button(root1,text='Show all Saved Cards',command=showall,width=17,bd=5).grid(row=22,column=2) 


                                             
                                            #delete all                                        
                                            def delete():
                                                    cur.execute("drop table paytm")
                                                    x=cur.fetchall()
                                                    Label(root1,text=x).grid(row=21,column=1)
                                                    showinfo('Information','All saved Cards are Deleted')
                                            Button(root1,text='Delete all Saved Cards',command=delete,width=17,bd=5).grid(row=22,column=1)

                                            #PAY
                                            def abcd():
                                                    qq=int(E.get())
                                                    ff=int(i.get())
                                                    
                                                    cur.execute("select amount from paytm where mob_no=?",(qq,))
                                                    x=cur.fetchall()
                                                    if (len(x)==0):
                                                        showinfo('Information','This Mobile Number is Not Registered\nPlease Enter All valid details and press Save for further use to get yourelf Registered.')

                                                    else:
                                                        aa=x[0][0]
                                                        #print ff
                                                    
                                                        gg=(aa-ff)
                                                        

                                                        if len(h.get()) == 0:
                                                            showinfo("Error!", "Please Enter Recievers Mobile Number")

                                                        else:
                                                            if gg<0:
                                                                showinfo("Information","Insufficient Balace")
                                                            else:
                                                                cur.execute("update paytm set amount=? where mob_no=?",(gg,qq))
                                                                x=cur.fetchall()
                                                                #q1=int(0)
                                                                #q2=''
                                                                #q3=int(0)
                                                                #cur.execute("insert into paytm values(?,?,?,?,?)",(int(h.get()),q1,q2,q3,hh))
                                                                hh=int(h.get())
                                                                cur.execute("select amount from paytm where mob_no=?",(hh,))
                                                                y=cur.fetchall()
                                                                if (len(y)==0):                                                                    
                                                                    showinfo('Information','This Mobile Number is Not Registered\nPlease Enter All valid details and press Save for further use to get yourelf Registered.')

                                                                else:                                                                    
                                                                    aa=y[0][0]
                                                                    #print ff
                                                    
                                                                    gg=(aa+ff)
                                                                    #print gg
                                                                    #f=[gg,qq]
                                                                    cur.execute("update paytm set amount=? where mob_no=?",(gg,hh))
                                                                    x=cur.fetchall()
                                                                    showinfo('Information','Your Amount has been successfully Paid')
                                                    
                                            Button(root1,text='PAY',command=abcd,width=6,bd=5).grid(row=25,column=1,columnspan=5)

                                            #Passbook
                                            def abcd2():
                                                    root2=Tk()
                                                    root2.resizable(0,0)
                                                    Label(root2,text='PASSBOOK',fg='Black',font='calibri 40',background='white').grid(row=1,column=1,columnspan=8)
                                                    Label(root2,text='Enter Mobile No').grid(row=2,column=1)
                                                    r=Entry(root2,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                                    r.grid(row=2,column=2)
                                                    def abcd3():
                                                            a=int(r.get())
                                                            aa=[int(r.get())]
                                                            c=0
                                                            while a>0:
                                                                    a=a/10
                                                                    c=c+1
                                                            if c!=10:
                                                                    showerror('ERROR','This field must have 10 digits\nPlease Enter Correct Mobile Number')
                                                            
                                                            
                                                            else:
                                                                cur.execute("select amount from paytm where mob_no=?",(aa))
                                                                x=cur.fetchall()
                                                                if (len(x)==0):
                                                                    showinfo('Information','Mobile Number Not Registered.')

                                                                else:
                                                                    ab=x[0][0]
                                                                    showinfo('Passbook',(('Total Amount is '),ab))
                                                    Button(root2,text='Enter',command=abcd3,width=6,bd=5).grid(row=3,column=2)

                                                    #Quit
                                                    def abcd4():
                                                        ans=askyesnocancel('Quit','Are you sure you want to quit')
                                                        if ans==True:
                                                           root2.destroy()
                                                    Button(root2,text='Quit',command=abcd4,width=6,bd=5).grid(row=4,column=1)
                                                    
                                                    root2.mainloop()
                                            Button(root1,text='Passbook',command=abcd2,width=7,bd=5).grid(row=27,column=1)

                                            #Quit
                                            def abcd4():
                                                   ans=askyesnocancel('Quit','Are you sure you want to quit')                                              #      
                                                   if ans==True:
                                                       root1.destroy()
                                                       root4.destroy()
                                            Button(root1,text='Quit',command=abcd4,width=6,bd=5).grid(row=27,column=2)
                                            
                            Button(root1,text='Enter',command=funt,width=6,bd=5).grid(row=3,column=2)
                            root1.mainloop()
                    #abc2=PhotoImage(file='E:\\project\\gif\\p1.gif')
                    Button(root4,text='PayNow',command=funt3,font='Arial 20',width=9,height=3,bd=5).grid(row=1,column=1)


                    def funt4():
                            #Add Money
                            root1=Tk()
                            
                            Label(root1,text='WELCOME TO BHIM',fg='Black',font='calibri 20',background='white').grid(row=1,column=1,columnspan=4)
                            root1.geometry('500x650+1+1')
                            root1.resizable(0,0)

                            
                            Label(root1,text='Enter Mobile Number',font='Arial 12').grid(row=2,column=1)
                            E=Entry(root1,width=12,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                            E.grid(row=2,column=2)
                            #root.destroy()                        
                            
                            a1=IntVar()
                            a2=IntVar()
                            a3=IntVar()

                            
                            def funt():
                                    #Mobile Number
                                    #root4.destroy()
                                    a=int(E.get())
                                    c=0
                                    while a>0:
                                            a=a/10
                                            c=c+1
                                    if c!=10:
                                            showerror('ERROR','This field must have 10 digits\nPlease Enter Correct Mobile Number')
                                    
                                    else:
                                            #Card Details
                                            Label(root1,text='\n   Enter your Card details\n',fg='Black',font='calibri 20').grid(row=4,column=1)
                                            #Card Number
                                            Label(root1,text='Enter Card Number',font='Arial 12').grid(row=6,column=1)
                                            a1=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a1.grid(row=6,column=2)
                                            def cno():
                                                    b1=int(a1.get())
                                                    c11=0
                                                    while b1>0:
                                                            b1=b1/10
                                                            c11=c11+1
                                                    if c11!=16:
                                                            showerror('ERROR','Invalid Account Number\nPlease Enter a Valid Account Number')
                                            Button(root1,text='Enter',command=cno,width=6,bd=5).grid(row=7,column=2)

                                            #Card Holder's Name
                                            Label(root1,text='Enter Card Holder Name',font='Arial 12').grid(row=8,column=1)
                                            a2=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a2.grid(row=8,column=2)
                                            def chn():
                                                    b2=a2.get()
                                            Button(root1,text='Enter',command=chn,width=6,bd=5).grid(row=9,column=2)

                                            #CVV
                                            Label(root1,text='Enter CVV',font='Arial 12').grid(row=10,column=1)
                                            a3=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a3.grid(row=10,column=2)
                                            def cv():
                                                    b3=int(a3.get())
                                                    c12=0
                                                    while b3>0:
                                                            b3=b3/10
                                                            c12=c12+1
                                                    if c12!=3:
                                                            showerror('ERROR','Invalid CVV\nPlease Enter Correct CVV')    
                                            Button(root1,text='Enter',command=cv,width=6,bd=5).grid(row=11,column=2)
                                            
                                            #Amount to Add
                                            Label(root1,text='Enter Amount to Add',font='Arial 12').grid(row=13,column=1)
                                            i=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            i.grid(row=13,column=2)
                                            def ata():
                                                    a12=int(i.get())
                                            Button(root1,text='ADD',command=ata,width=6,bd=5).grid(row=14,column=2)


                                            #DBMS

                                            #insert
                                            def insert():
                                                    
                                                    cur.execute("insert into paytm values(?,?,?,?,?)",(int(E.get()),int(a1.get()),a2.get(),int(a3.get()),int(i.get())))
                                                    con.commit()
                                                    showinfo('Information','Card Saved for further use\nYour Money has been added no need to press Add Money Button')
                                            Button(root1,text='Save Card for further use',command=insert,width=19,bd=5).grid(row=15,column=1)

                                            Label(root1,text='Enter mobile number to view saved cards').grid(row=17,column=1)
                                            d=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            d.grid(row=17,column=2)
                                            

                                            #show
                                            def show():
                                                    a=[(int(d.get()))]
                                                    cur.execute("select *from paytm where mob_no=?",a)
                                                    x=cur.fetchall()
                                                    showinfo('Result',x)
                                            Button(root1,text='Show Save Card',command=show,width=17,bd=5).grid(row=18,column=2)


                                            

                                            #showall                                        
                                            def showall():
                                                    cur.execute("select *from paytm")
                                                    x=cur.fetchall()
                                                    showinfo("Result",x)
                                            Button(root1,text='Show all Saved Cards',command=showall,width=19,bd=5).grid(row=18,column=1)


                                            #delete all                                        
                                            def delete():
                                                    cur.execute("drop table paytm")
                                                    x=cur.fetchall()
                                                    Label(root1,text=x).grid(row=20,column=1)
                                                    showinfo('Information','All saved Cards are Deleted')
                                            Button(root1,text='Delete all Saved Cards',command=delete,width=19,bd=5).grid(row=22,column=1)

                                            

                                            #Add Money
                                            def abcd():
                                                    qq=int(E.get())
                                                    ff=int(i.get())
                                                    cur.execute("select amount from paytm where mob_no=?",(qq,))
                                                    x=cur.fetchall()
                                                    if (len(x)==0):
                                                        showinfo('Information','Mobile Number Not Registered\nPlease Enter all valid Details and Press Save for further use to get Registered.')

                                                    else:
                                                        aa=x[0][0]
                                                        print ff
                                                    
                                                        gg=(aa+ff)
                                                        print gg
                                                        #f=[gg,qq]
                                                        cur.execute("update paytm set amount=? where mob_no=?",(gg,qq))
                                                        x=cur.fetchall()
                                                        showinfo('Information','Your Amount has been successfully Added')
                                            Button(root1,text='Add Money',command=abcd,width=12,bd=5).grid(row=23,column=1,columnspan=5)


                                            #Passbook
                                            def abcd2():
                                                    root2=Tk()
                                                    root2.resizable(0,0)
                                                    
                                                    Label(root2,text='PASSBOOK',fg='Black',font='calibri 40',background='white').grid(row=1,column=1,columnspan=12)
                                                    Label(root2,text='Enter Mobile No').grid(row=2,column=1)
                                                    r=Entry(root2,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                                    r.grid(row=2,column=2)
                                                    def abcd3():
                                                            a=int(r.get())
                                                            aa=[int(r.get())]
                                                            c=0
                                                            while a>0:
                                                                    a=a/10
                                                                    c=c+1
                                                            if c!=10:
                                                                    showerror('ERROR','This field must have 10 digits\nPlease Enter Correct Mobile Number')
                                                            
                                                            
                                                            else:
                                                                cur.execute("select amount from paytm where mob_no=?",(aa))
                                                                x=cur.fetchall()
                                                                if (len(x)==0):
                                                                    showinfo('Information','Mobile Number Not Registered.')

                                                                else:
                                                                    ab=x[0][0]
                                                                    showinfo('Passbook',(('Total Amount is '),ab))
                                                    Button(root2,text='Enter',command=abcd3,width=6,bd=5).grid(row=3,column=2)

                                                    #Quit
                                                    def abcd4():
                                                        ans=askyesnocancel('Quit','Are you sure you want to quit')
                                                        if ans==True:
                                                           root2.destroy()
                                                    Button(root2,text='Quit',command=abcd4,width=6,bd=5).grid(row=4,column=1)
                                                    root2.mainloop()
                                            Button(root1,text='Passbook',command=abcd2,width=7,bd=5).grid(row=24,column=1)

                                            #Quit
                                            def abcd4():
                                                   ans=askyesnocancel('Quit','Are you sure you want to quit')
                                                   if ans==True:
                                                       root1.destroy()
                                                       root4.destroy()
                                            Button(root1,text='Quit',command=abcd4,width=6,bd=5).grid(row=24,column=2)

                                            

                                            
                            Button(root1,text='Enter',command=funt,width=6,bd=5).grid(row=3,column=2)                
                            root1.mainloop()
                    Button(root4,text='Add Money',command=funt4,font='Arial 20',width=9,height=3,bd=5).grid(row=1,column=3)        
                    root4.mainloop()



                    
            else:
                    #Phonepe
                    root4=Tk()
                    root4.resizable(0,0)
                    #root4.geometry('400x600')
                    #Pay Now
                    def funt3():                        
                            root1=Tk()
                            #root1.configure(background='White')
                            Label(root1,text='WELCOME TO PHONEPE',fg='Black',font='calibri 20',background='White').grid(row=1,column=1,columnspan=4)
                            root1.geometry('500x750+1+1')
                            root1.resizable(0,0)
                            
                            Label(root1,text='Enter Mobile Number',font='Arial 12 ').grid(row=2,column=1)
                            E=Entry(root1,width=12,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                            E.grid(row=2,column=2)
                            #root.destroy()                        
                            
                            a1=IntVar()
                            a2=IntVar()
                            a3=IntVar()
                            def funt():
                                    #Mobile Number
                                    #root4.destroy()
                                    a=int(E.get())
                                    c=0
                                    while a>0:
                                            a=a/10
                                            c=c+1
                                    if c!=10:
                                            showerror('ERROR','This field must have 10 digits\nPlease Enter Correct Mobile Number')
                                    
                                    
                                    else:
                                            #Card Details
                                            Label(root1,text='Enter your Card details',fg='Black',font='calibri 20').grid(row=4,column=1)
                                            #Card Number
                                            Label(root1,text='Enter Card Number',font='Arial 12').grid(row=6,column=1)
                                            a1=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a1.grid(row=6,column=2)
                                            def cno():
                                                    b1=int(a1.get())
                                                    c11=0
                                                    while b1>0:
                                                            b1=b1/10
                                                            c11=c11+1
                                                    if c11!=16:
                                                            showerror('ERROR','Invalid Account Number\nPlease Enter a Valid Account Number')
                                            Button(root1,text='Enter',command=cno,width=6,bd=5,fg='White',bg='Purple').grid(row=7,column=2)

                                            #Card Holder's Name
                                            Label(root1,text='Enter card Holder Name',font='Arial 12').grid(row=8,column=1)
                                            a2=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a2.grid(row=8,column=2)
                                            def chn():
                                                    b2=a2.get()
                                            Button(root1,text='Enter',command=chn,width=6,bd=5,fg='White',bg='Purple').grid(row=9,column=2)

                                            #CVV
                                            Label(root1,text='Enter CVV',font='Arial 12').grid(row=10,column=1)
                                            a3=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a3.grid(row=10,column=2)
                                            def cv():
                                                    b3=int(a3.get())
                                                    c12=0
                                                    while b3>0:
                                                            b3=b3/10
                                                            c12=c12+1
                                                    if c12!=3:
                                                            showerror('ERROR','Invalid CVV\nPlease Enter Correct CVV')    
                                            Button(root1,text='Enter',command=cv,width=6,bd=5,fg='White',bg='Purple').grid(row=11,column=2)

                                            #Reciever's Details
                                            Label(root1,text='Enter Recievers Details',fg='Black',font='calibri 20').grid(row=12,column=1)
                                            #Reciever's Mobile Number
                                            Label(root1,text='Enter Mobile Number',font='Arial 12').grid(row=13,column=1)
                                            h=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            h.grid(row=13,column=2)
                                            def funt2():
                                                    a=int(h.get())
                                                    c=0
                                                    while a>0:
                                                            a=a/10
                                                            c=c+1
                                                    if c!=10:
                                                            showerror('ERROR','This field must have 10 digits\nPlease Enter Correct Mobile Number')
                                            Button(root1,text='Enter',command=funt2,width=6,bd=5,fg='White',bg='Purple').grid(row=14,column=2)
            
                                            #Amount To Be Paid
                                            Label(root1,text='Enter Amount to be Paid',font='Arial 12').grid(row=15,column=1)
                                            i=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            i.grid(row=15,column=2)
                                            
                                
                                            
                                            def funtt():
                                                aa=int(i.get())                                                
                                            Button(root1,text='Enter',command=funtt,width=6,bd=5,fg='White',bg='Purple').grid(row=16,column=2)
                                            


                                            

                                            #DBMS

                                            #insert
                                            def insert():
                                                    abh=int(0)
                                                    cur.execute("insert into paytm values(?,?,?,?,?)",(int(E.get()),int(a1.get()),a2.get(),int(a3.get()),abh))
                                                    con.commit()
                                                    showinfo('Information','Card Saved for further use')
                                            Button(root1,text='Save Card for further use',command=insert,width=19,bd=5,fg='White',bg='Purple').grid(row=17,column=1)


                                            Label(root1,text='Enter mobile number to view saved cards',font='Arial 12').grid(row=19,column=1)
                                            d=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            d.grid(row=19,column=2)
                                            
                                            #show
                                            def show():
                                                    a=[(int(d.get()))]
                                                    cur.execute("select *from paytm where mob_no=?",a)
                                                    x=cur.fetchall()
                                                    showinfo('Result',x)
                                            Button(root1,text='Show Save Card',command=show,width=15,bd=5,fg='White',bg='Purple').grid(row=20,column=2)

                                            

                                            #showall
                                            def showall():
                                                    cur.execute("select *from paytm")
                                                    x=cur.fetchall()
                                                    showinfo("Result",x)
                                            Button(root1,text='Show all saved Cards',command=showall,width=17,bd=5,fg='White',bg='Purple').grid(row=22,column=2) 


                                             
                                            #delete all                                        
                                            def delete():
                                                    cur.execute("drop table paytm")
                                                    x=cur.fetchall()
                                                    Label(root1,text=x).grid(row=21,column=1)
                                                    showinfo('Information','All saved Cards are Deleted')
                                            Button(root1,text='Delete all saved cards',command=delete,width=17,bd=5,fg='White',bg='Purple').grid(row=22,column=1)

                                            #PAY
                                            def abcd():
                                                    qq=int(E.get())
                                                    ff=int(i.get())
                                                    
                                                    cur.execute("select amount from paytm where mob_no=?",(qq,))
                                                    x=cur.fetchall()
                                                    if (len(x)==0):
                                                        showinfo('Information','This Mobile Number is Not Registered\nPlease Enter All valid details and press Save for further use to get yourelf Registered.')

                                                    else:
                                                        aa=x[0][0]
                                                        #print ff
                                                    
                                                        gg=(aa-ff)
                                                        

                                                        if len(h.get()) == 0:
                                                            showinfo("Error!", "Please Enter Recievers Mobile Number")

                                                        else:
                                                            if gg<0:
                                                                showinfo("Information","Insufficient Balace")
                                                            else:
                                                                cur.execute("update paytm set amount=? where mob_no=?",(gg,qq))
                                                                x=cur.fetchall()
                                                                #q1=int(0)
                                                                #q2=''
                                                                #q3=int(0)
                                                                #cur.execute("insert into paytm values(?,?,?,?,?)",(int(h.get()),q1,q2,q3,hh))
                                                                hh=int(h.get())
                                                                cur.execute("select amount from paytm where mob_no=?",(hh,))
                                                                y=cur.fetchall()
                                                                if (len(y)==0):                                                                    
                                                                    showinfo('Information','This Mobile Number is Not Registered\nPlease Enter All valid details and press Save for further use to get yourelf Registered.')

                                                                else:                                                                    
                                                                    aa=y[0][0]
                                                                    #print ff
                                                    
                                                                    gg=(aa+ff)
                                                                    #print gg
                                                                    #f=[gg,qq]
                                                                    cur.execute("update paytm set amount=? where mob_no=?",(gg,hh))
                                                                    x=cur.fetchall()
                                                                    showinfo('Information','Your Amount has been successfully Paid')
                                                    
                                            Button(root1,text='PAY',command=abcd,width=6,bd=5,fg='White',bg='Purple').grid(row=25,column=1,columnspan=5)

                                            #Passbook
                                            def abcd2():
                                                    root2=Tk()
                                                    root2.resizable(0,0)
                                                    Label(root2,text='PASSBOOK',fg='Black',font='calibri 40',background='white').grid(row=1,column=1,columnspan=12)
                                                    Label(root2,text='Enter Mobile No').grid(row=2,column=1)
                                                    r=Entry(root2,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                                    r.grid(row=2,column=2)
                                                    def abcd3():
                                                            a=int(r.get())
                                                            aa=[int(r.get())]
                                                            c=0
                                                            while a>0:
                                                                    a=a/10
                                                                    c=c+1
                                                            if c!=10:
                                                                    showerror('ERROR','This field must have 10 digits\nPlease Enter Correct Mobile Number')
                                                            
                                                            
                                                            else:
                                                                cur.execute("select amount from paytm where mob_no=?",(aa))
                                                                x=cur.fetchall()
                                                                if (len(x)==0):
                                                                    showinfo('Information','Mobile Number Not Registered.')

                                                                else:
                                                                    ab=x[0][0]
                                                                    showinfo('Passbook',(('Total Amount is '),ab))
                                                    Button(root2,text='Enter',command=abcd3,width=6,bd=5,bg='Purple').grid(row=3,column=2)

                                                    #Quit
                                                    def abcd4():
                                                        ans=askyesnocancel('Quit','Are you sure you want to quit')
                                                        if ans==True:
                                                           root2.destroy()
                                                    Button(root2,text='Quit',command=abcd4,width=6,bd=5,fg='White',bg='Purple').grid(row=4,column=1)
                                                    
                                                    root2.mainloop()
                                            Button(root1,text='Passbook',command=abcd2,width=7,fg='White',bd=5,bg='Purple').grid(row=27,column=1)
                                            #Quit
                                            def abcd4():
                                                   ans=askyesnocancel('Quit','Are you sure you want to quit')                                              #      
                                                   if ans==True:
                                                       root1.destroy()
                                                       root4.destroy()
                                            Button(root1,text='Quit',command=abcd4,width=6,bd=5,fg='White',bg='Purple').grid(row=27,column=2)
                                            
                            Button(root1,text='Enter',command=funt,width=6,bd=5,fg='White',bg='Purple').grid(row=3,column=2)
                            root1.mainloop()
                    #abc2=PhotoImage(file='E:\\project\\gif\\p1.gif')
                    Button(root4,text='PayNow',command=funt3,font='Arial 20',width=9,height=3,bd=5,fg='White',bg='Purple').grid(row=1,column=1)

                    def funt4():
                            #Phonepe
                            #Add Money
                            root1=Tk()
                            root1.resizable(0,0)
                            Label(root1,text='WELCOME TO PHONEPE',fg='Black',font='calibri 20',background='white').grid(row=1,column=1,columnspan=4)
                            root1.geometry('500x650+1+1')

                            
                            Label(root1,text='Enter Mobile Number',font='Arial 12').grid(row=2,column=1)
                            E=Entry(root1,width=12,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                            E.grid(row=2,column=2)
                            #root.destroy()                        
                            
                            a1=IntVar()
                            a2=IntVar()
                            a3=IntVar()

                            
                            def funt():
                                    #Mobile Number
                                    #root4.destroy()
                                    a=int(E.get())
                                    c=0
                                    while a>0:
                                            a=a/10
                                            c=c+1
                                    if c!=10:
                                            showerror('ERROR','This field must have 10 digits\nPlease Enter Correct Mobile Number')
                                    
                                    else:
                                            #Card Details
                                            Label(root1,text='\n   Enter your Card details\n',fg='Black',font='calibri 20').grid(row=4,column=1)
                                            #Card Number
                                            Label(root1,text='Enter Card Number',font='Arial 12').grid(row=6,column=1)
                                            a1=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a1.grid(row=6,column=2)
                                            def cno():
                                                    b1=int(a1.get())
                                                    c11=0
                                                    while b1>0:
                                                            b1=b1/10
                                                            c11=c11+1
                                                    if c11!=16:
                                                            showerror('ERROR','Invalid Account Number\nPlease Enter a Valid Account Number')
                                            Button(root1,text='Enter',command=cno,width=6,bd=5,fg='White',bg='Purple').grid(row=7,column=2)

                                            #Card Holder's Name
                                            Label(root1,text='Enter card Holder Name',font='Arial 12',).grid(row=8,column=1)
                                            a2=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a2.grid(row=8,column=2)
                                            def chn():
                                                    b2=a2.get()
                                            Button(root1,text='Enter',command=chn,width=6,bd=5,fg='White',bg='Purple').grid(row=9,column=2)

                                            #CVV
                                            Label(root1,text='Enter CVV',font='Arial 12').grid(row=10,column=1)
                                            a3=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            a3.grid(row=10,column=2)
                                            def cv():
                                                    b3=int(a3.get())
                                                    c12=0
                                                    while b3>0:
                                                            b3=b3/10
                                                            c12=c12+1
                                                    if c12!=3:
                                                            showerror('ERROR','Invalid CVV\nPlease Enter Correct CVV')    
                                            Button(root1,text='Enter',command=cv,bd=5,width=6,fg='White',bg='Purple').grid(row=11,column=2)
                                            
                                            #Amount to Add
                                            Label(root1,text='Enter Amount to Add',font='Arial 12').grid(row=13,column=1)
                                            i=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            i.grid(row=13,column=2)
                                            def ata():
                                                    a12=int(i.get())
                                            Button(root1,text='ADD',command=ata,width=6,bd=5,fg='White',bg='Purple').grid(row=14,column=2)


                                            #DBMS

                                            #insert
                                            def insert():
                                                    
                                                    cur.execute("insert into paytm values(?,?,?,?,?)",(int(E.get()),int(a1.get()),a2.get(),int(a3.get()),int(i.get())))
                                                    con.commit()
                                                    showinfo('Information','Card Saved for further use\nYour Money has been added no need to press Add Money Button')
                                            Button(root1,text='Save Card for further use',command=insert,width=19,bd=5,fg='White',bg='Purple').grid(row=15,column=1)

                                            Label(root1,text='Enter mobile number to view saved cards').grid(row=17,column=1)
                                            d=Entry(root1,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                            d.grid(row=17,column=2)
                                            

                                            #show
                                            def show():
                                                    a=[(int(d.get()))]
                                                    cur.execute("select *from paytm where mob_no=?",a)
                                                    x=cur.fetchall()
                                                    showinfo('Result',x)
                                            Button(root1,text='Show Save Card',command=show,width=17,bd=5,fg='White',bg='Purple').grid(row=18,column=2)


                                            

                                            #showall                                        
                                            def showall():
                                                    cur.execute("select *from paytm")
                                                    x=cur.fetchall()
                                                    showinfo("Result",x)
                                            Button(root1,text='Show all saved Cards',command=showall,width=19,bd=5,fg='White',bg='Purple').grid(row=18,column=1)


                                            #delete all                                        
                                            def delete():
                                                    cur.execute("drop table paytm")
                                                    x=cur.fetchall()
                                                    Label(root1,text=x).grid(row=20,column=1)
                                                    showinfo('Information','All saved Cards are Deleted')
                                            Button(root1,text='Delete all saved cards',command=delete,width=19,bd=5,fg='White',bg='Purple').grid(row=22,column=1)

                                            

                                            #Add Money
                                            def abcd():
                                                    qq=int(E.get())
                                                    ff=int(i.get())
                                                    cur.execute("select amount from paytm where mob_no=?",(qq,))
                                                    x=cur.fetchall()
                                                    if (len(x)==0):
                                                        showinfo('Information','Mobile Number Not Registered\nPlease Enter all valid Details and Press Save for further use to get Registered.')

                                                    else:
                                                        aa=x[0][0]
                                                        print ff
                                                    
                                                        gg=(aa+ff)
                                                        print gg
                                                        #f=[gg,qq]
                                                        cur.execute("update paytm set amount=? where mob_no=?",(gg,qq))
                                                        x=cur.fetchall()
                                                        showinfo('Information','Your Amount has been successfully Added')
                                            Button(root1,text='Add Money',command=abcd,width=12,bd=5,fg='White',bg='Purple').grid(row=23,column=1,columnspan=5)


                                            #Passbook
                                            def abcd2():
                                                    root2=Tk()
                                                    root2.resizable(0,0)
                                                    Label(root2,text='PASSBOOK',fg='Black',font='calibri 40',background='white').grid(row=1,column=1,columnspan=12)
                                                    Label(root2,text='Enter Mobile No').grid(row=2,column=1)
                                                    r=Entry(root2,font="Arial 12 ",bd=5,bg="Light grey",justify='left')
                                                    r.grid(row=2,column=2)
                                                    def abcd3():
                                                            a=int(r.get())
                                                            aa=[int(r.get())]
                                                            c=0
                                                            while a>0:
                                                                    a=a/10
                                                                    c=c+1
                                                            if c!=10:
                                                                    showerror('ERROR','This field must have 10 digits\nPlease Enter Correct Mobile Number')
                                                            
                                                            
                                                            else:
                                                                cur.execute("select amount from paytm where mob_no=?",(aa))
                                                                x=cur.fetchall()
                                                                if (len(x)==0):
                                                                    showinfo('Information','Mobile Number Not Registered.')

                                                                else:
                                                                    ab=x[0][0]
                                                                    showinfo('Passbook',(('Total Amount is '),ab))
                                                    Button(root2,text='Enter',command=abcd3,width=6,fg='White',bd=5,bg='Purple').grid(row=3,column=2)
                                                    

                                                    #Quit
                                                    def abcd4():
                                                        ans=askyesnocancel('Quit','Are you sure you want to quit')
                                                        if ans==True:
                                                           root2.destroy()
                                                    Button(root2,text='Quit',command=abcd4,width=6,bd=5,fg='White',bg='Purple').grid(row=4,column=1)

                                                    root2.mainloop()
                                            Button(root1,text='Passbook',command=abcd2,width=7,fg='White',bd=5,bg='Purple').grid(row=24,column=1)
                                            #Quit
                                            def abcd4():
                                                   ans=askyesnocancel('Quit','Are you sure you want to quit')
                                                   if ans==True:
                                                       root1.destroy()
                                                       root4.destroy()
                                            Button(root1,text='Quit',command=abcd4,width=6,bd=5,fg='White',bg='Purple').grid(row=24,column=2)

                                            

                                            
                            Button(root1,text='Enter',command=funt,width=6,bd=5,fg='White',bg='Purple').grid(row=3,column=2)                
                            root1.mainloop()
                    Button(root4,text='Add Money',command=funt4,font='Arial 20',width=9,height=3,bd=5,fg='White',bg='Purple').grid(row=1,column=3)        
                    root4.mainloop()

                    
    Button(root,text='Enter',command=fun,width=8,height=2,bd=5,font='Arial 10 bold',bg='Light Grey').grid(row=6,column=2)
    root.mainloop()


lb=Label(root4,image=img)
lb.bind('<Motion>',fun)
lb.pack()
root4.mainloop()

               
