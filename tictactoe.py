import sqlite3
from tkinter import messagebox
from tkinter import *
def first():
    turn1='gu est1';turn2="gu est2"
    from tkinter import messagebox
    import chime
    a=Tk()
    a.geometry("650x650");a.resizable(False,False)
    a.configure(bg="black")
    count=0
    def turny(cbtn):
        nonlocal turn1,turn2
        if cbtn:
            turn2='gu est2';b16['state']='disable';b18['text']='WITH PROFILE'
        else:
            turn1='gu est1';b15['state']='disable';b17['text']='WITH PROFILE'
    def disble():
        b1['state']=b2['state']=b3['state']=b4['state']=b5['state']=b6['state']=b7['state']=b8['state']=b9['state']='disable'
    def anable():
        b10['state']=b11['state']=b13['state']=b15['state']=b16['state']=b17['state']=b18['state']=b23['state']='disable'
        chime.theme('zelda');chime.success()
        nonlocal count
        l1['text']='RESULT';count=0
        b1.configure(state='normal',text="  1  ");b2.configure(state='normal',text="  2  ");b3.configure(state='normal',text="  3  ")
        b4.configure(state='normal',text="  4  ");b5.configure(state='normal',text="  5  ");b6.configure(state='normal',text="  6  ")
        b7.configure(state='normal',text="  7  ");b8.configure(state='normal',text="  8  ");b9.configure(state='normal',text="  9  ")
    def work():
        z=0;nonlocal count
        if b1['text']==b2['text']==b3['text']:
            l1['text']=f"{b1['text']} WON";disble();z=1
        elif b1['text']==b5['text']==b9['text']:
            l1['text']=f"{b1['text']} WON";disble();z=1
        elif b1['text']==b4['text']==b7['text']:
            l1['text']=f"{b1['text']} WON";disble();z=1
        elif b2['text']==b5['text']==b8['text']:
            l1['text']=f"{b2['text']} WON";disble();z=1
        elif b3['text']==b6['text']==b9['text']:
            l1['text']=f"{b3['text']} WON";disble();z=1
        elif b4['text']==b5['text']==b6['text']:
            l1['text']=f"{b4['text']} WON";disble();z=1
        elif b7['text']==b8['text']==b9['text']:
            l1['text']=f"{b7['text']} WON";disble();z=1
        elif b3['text']==b5['text']==b7['text']:
            l1['text']=f"{b7['text']} WON";disble();z=1
        elif count==9:
            l1['text']="DRAW";z=1
        if(z==1):
            chime.theme('mario')
            chime.success()
            b10['text']='PLAY AGAIN'
            b10['state']=b11['state']=b13['state']=b17['state']=b18['state']=b23['state']='normal'
            if turn1!='gu est1':
                b15['state']='normal'
            if turn2!='gu est2':
                b16['state']='normal'
            if l1['text']==" X  WON": 
                mark('win')
            elif l1['text']==" O  WON":
                mark('loss')
            else:
                mark('draw')
    def mark(condition):
        nonlocal turn1,turn2
        if turn1!='gu est1':
            try:
                conn=sqlite3.connect('gfg.db')
                cursor = conn.execute(f"SELECT {condition} from {turn1} where serial=1;");point=cursor.fetchone()[0]
                conn.execute(f'''update {turn1} set {condition}={point+1} where serial=1;''')
                conn.commit()
                conn.close()
            except:
                turn1='gu est1';b15['state']='disable';b17['text']='WITH PROFILE'
        if condition=='loss':
            condition='win';print(condition)
        else:
            condition='loss'
        if turn2!='gu est2':
            try:
                conn=sqlite3.connect('gfg.db')
                cursor = conn.execute(f"SELECT {condition} from {turn2} where serial=1;");point=cursor.fetchone()[0]
                conn.execute(f'''update {turn2} set {condition}={point+1} where serial=1;''')
                conn.commit()
                conn.close()
            except:
                turn2='gu est2';b16['state']='disable';b18['text']='WITH PROFILE'
    def chng(b):
        nonlocal count
        if count%2==0:
            b['text']=" X ";count+=1
        else:
            b['text']=" O ";count+=1
        b['state']='disabled'
        chime.theme('chime')
        chime.info()
        if count>4:
            work()
    def credel(zero):
        if zero==True:
            adder=0
        else:
            adder=4
        def setnm():
            if ' ' in playername.get():
                messagebox.showinfo('information',"no space allowed in profile name!")
            elif playername.get()!="":
                try:
                    conn=sqlite3.connect('gfg.db')
                    if zero==True:
                        conn.execute(f'''CREATE TABLE {playername.get()}
                        (serial number(1),
                        WIN NUMBER(3),
                        LOSS NUMBER(3),
                        DRAW NUMBER(3));''')
                        conn.execute(f'''insert into {playername.get()} values(1,0,0,0);''')
                    else:
                        conn=sqlite3.connect('gfg.db')
                        conn.execute(f'''drop table {playername.get()};''')
                    conn.commit()
                    conn.close()
                except:
                    if zero==True:
                        messagebox.showwarning('warning',"profile already exists!choose another name.")
                    else:
                        messagebox.showwarning('warning',"profile doesn't exist!!!")
                else:
                    cncl()
                    if zero==True:
                        messagebox.showinfo('information','profile created!')
                    else:
                        messagebox.showinfo('information','profile deleted!')
            else:
                messagebox.showwarning('warning',"Enter name first")
        def cncl():
            stnm.destroy()
            b12.destroy()
            b14.destroy()
            b23['state']='normal'
            b11['state']='normal'
            b13['state']='normal'
            b17['state']='normal'
            b18['state']='normal'
            b10['state']='normal'
        playername=StringVar();stnm=Entry(f2,textvariable=playername,font="12",relief='sunken',bd=5,bg='red');stnm.grid(row=2+adder,column=0)
        b12=Button(f2,text="SET NAME",activebackground='red',font="Constantia 18 bold",fg="yellow",bg="black",bd=5,relief="raised",command=setnm);b12.grid(row=3+adder,column=0)
        b14=Button(f2,text="CANCEL",activebackground='red',font="Constantia 18 bold",fg="yellow",bg="black",bd=5,relief="raised",command=cncl);b14.grid(row=4+adder,column=0)
        b23['state']='disable'
        b10['state']='disable'
        b11['state']='disable'
        b13['state']='disable'
        b17['state']='disable'
        b18['state']='disable'
    def see(gtro):
        def setnm():
            nonlocal turn1,turn2
            if turn1==player_name.get() or turn2==player_name.get():
                messagebox.showwarning('warning',"can't set same name!!!")
            elif ' ' in player_name.get():
                messagebox.showinfo('information',"no space allowed in profile name!")
            elif player_name.get()!="":
                try:
                    conn=sqlite3.connect('gfg.db')
                    conn.execute(f'''select * from {player_name.get()};''')
                    conn.commit()
                    conn.close()
                except:
                    if gtro==0:
                        turn1='gu est1'
                    else:
                        turn2="gu est2"
                    messagebox.showwarning('warning',"profile doesn't exist!!!")
                else:
                    if gtro==0:
                        turn1=player_name.get()
                    else:
                        turn2=player_name.get()
                    cncl()
                    if gtro==0:
                        b17['text']=player_name.get()[0:12]
                    else:
                        b18['text']=player_name.get()[0:12]
                    messagebox.showinfo('information','got profile!')
                    if gtro==0:
                        b15['state']='normal'
                    else:
                        b16['state']='normal'
            else:
                messagebox.showwarning('warning',"set name first")
        def cncl():
            stnm_.destroy()
            b19.destroy()
            b20.destroy()
            b23['state']='normal'
            b11['state']='normal'
            b13['state']='normal'
            b17['state']='normal'
            b18['state']='normal'
            b10['state']='normal'
        player_name=StringVar();stnm_=Entry(f4,textvariable=player_name,font="12",relief='sunken',bd=5,bg='red');stnm_.grid(row=3,column=gtro)
        b19=Button(f4,text="ENTER",activebackground='red',font="Constantia 18 bold",fg="yellow",bg="black",bd=5,relief="raised",command=setnm);b19.grid(row=4,column=gtro)
        b20=Button(f4,text="CANCEL",activebackground='red',font="Constantia 18 bold",fg="yellow",bg="black",bd=5,relief="raised",command=cncl);b20.grid(row=5,column=gtro)
        b23['state']='disable'
        b10['state']='disable'
        b11['state']='disable'
        b13['state']='disable'
        b17['state']='disable'
        b18['state']='disable'
    def stats():
        def tknm():
            if ' ' in player_nam.get():
                messagebox.showinfo('information',"no space allowed in profile name!")
            elif player_nam.get()!="":
                try:
                    conn=sqlite3.connect('gfg.db')
                    cursor=conn.execute(f'''select * from {player_nam.get()};''');p=cursor.fetchone()
                    pstat=f"WIN:{p[1]} LOSS:{p[2]} DRAW:{p[3]}"
                    conn.commit()
                    conn.close()
                except:
                    messagebox.showwarning('warning',"profile doesn't exist!!!")
                else:
                    cncl()
                    messagebox.showinfo('information',f'{pstat}')
            else:
                messagebox.showwarning('warning',"set name first")
        def cncl():
            stnm_.destroy()
            b21.destroy()
            b22.destroy()
            b23['state']='normal'
            b11['state']='normal'
            b13['state']='normal'
            b17['state']='normal'
            b18['state']='normal'
            b10['state']='normal'
        player_nam=StringVar();stnm_=Entry(f4,textvariable=player_nam,font="12",relief='sunken',bd=5,bg='red');stnm_.grid(row=1,column=2)
        b21=Button(f4,text="ENTER",activebackground='red',font="Constantia 18 bold",fg="yellow",bg="black",bd=5,relief="raised",command=tknm);b21.grid(row=2,column=2)
        b22=Button(f4,text="CANCEL",activebackground='red',font="Constantia 18 bold",fg="yellow",bg="black",bd=5,relief="raised",command=cncl);b22.grid(row=3,column=2)
        b23['state']='disable'
        b10['state']='disable'
        b11['state']='disable'
        b13['state']='disable'
        b17['state']='disable'
        b18['state']='disable'
    fl=Frame(a,bg="black");fl.grid(row=0,column=0)
    fa=Frame(fl,relief="sunken",bd=5,bg="blue");fa.grid(row=0,column=0,padx=5,pady=5)
    f1=Frame(fa,relief="sunken",bd=5,bg="blue");f1.grid(row=0,column=0,padx=5,pady=5)
    b1=Button(f1,text="  1  ",font="Constantia 24 bold",fg="green",bg="black",bd=5,state='disable',relief="raised",command=lambda :chng(b1));b1.grid(row=0,column=0)
    b2=Button(f1,text="  2  ",font="Constantia 24 bold",fg="green",bg="black",bd=5,state='disable',relief="raised",command=lambda :chng(b2));b2.grid(row=0,column=1)
    b3=Button(f1,text="  3  ",font="Constantia 24 bold",fg="green",bg="black",bd=5,state='disable',relief="raised",command=lambda :chng(b3));b3.grid(row=0,column=2)
    b4=Button(f1,text="  4  ",font="Constantia 24 bold",fg="green",bg="black",bd=5,state='disable',relief="raised",command=lambda :chng(b4));b4.grid(row=1,column=0)
    b5=Button(f1,text="  5  ",font="Constantia 24 bold",fg="green",bg="black",bd=5,state='disable',relief="raised",command=lambda :chng(b5));b5.grid(row=1,column=1)
    b6=Button(f1,text="  6  ",font="Constantia 24 bold",fg="green",bg="black",bd=5,state='disable',relief="raised",command=lambda :chng(b6));b6.grid(row=1,column=2)
    b7=Button(f1,text="  7  ",font="Constantia 24 bold",fg="green",bg="black",bd=5,state='disable',relief="raised",command=lambda :chng(b7));b7.grid(row=2,column=0)
    b8=Button(f1,text="  8  ",font="Constantia 24 bold",fg="green",bg="black",bd=5,state='disable',relief="raised",command=lambda :chng(b8));b8.grid(row=2,column=1)
    b9=Button(f1,text="  9  ",font="Constantia 24 bold",fg="green",bg="black",bd=5,state='disable',relief="raised",command=lambda :chng(b9));b9.grid(row=2,column=2)
    l1=Label(fa,text="RESULT",fg="red",font="Constantia 24 bold",bg="black",bd=5,relief="flat");l1.grid(row=1,column=0)
    f2=Frame(fl,relief="sunken",bd=5,bg="black");f2.grid(row=0,column=1,padx=5,pady=5)
    b10=Button(f2,text="PLAY",activebackground='red',font="Constantia 24 bold",fg="yellow",bg="black",bd=5,relief="raised",command=anable);b10.grid(row=0,column=0)
    b11=Button(f2,text="CREATE PROFILE",activebackground='red',font="Constantia 18 bold",fg="yellow",bg="black",bd=5,relief="raised",command=lambda :credel(True));b11.grid(row=1,column=0)
    b13=Button(f2,text="DELETE PROFILE",activebackground='red',font="Constantia 18 bold",fg="yellow",bg="black",bd=5,relief="raised",command=lambda :credel(False));b13.grid(row=5,column=0)
    f4=Frame(a,bg="black");f4.grid(row=1,column=0)
    l2=Label(f4,text="PLAYER X",fg="red",font="Constantia 24 bold",bg="black",bd=5,relief="flat");l2.grid(row=0,column=0)
    l3=Label(f4,text="PLAYER O",fg="red",font="Constantia 24 bold",bg="black",bd=5,relief="flat");l3.grid(row=0,column=1)
    b15=Button(f4,text="AS GUEST",activebackground='red',font="Constantia 18 bold",fg="yellow",bg="black",bd=5,relief="raised",command=lambda :turny(False));b15.grid(row=1,column=0)
    b16=Button(f4,text="AS GUEST",activebackground='red',font="Constantia 18 bold",fg="yellow",bg="black",bd=5,relief="raised",command=lambda :turny(True));b16.grid(row=1,column=1)
    b17=Button(f4,text="WITH PROFILE",activebackground='red',font="Constantia 18 bold",fg="yellow",bg="black",bd=5,relief="raised",command=lambda :see(0));b17.grid(row=2,column=0)
    b18=Button(f4,text="WITH PROFILE",activebackground='red',font="Constantia 18 bold",fg="yellow",bg="black",bd=5,relief="raised",command=lambda :see(1));b18.grid(row=2,column=1)
    b23=Button(f4,text="PLAYER STATS",activebackground='red',font="Constantia 18 bold",fg="yellow",bg="black",bd=5,relief="raised",command=stats);b23.grid(row=0,column=2)
    a.mainloop()
first()