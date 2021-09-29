from  tkinter  import *
import random 
win=Tk()
win.title("sang-kaghz-gh")
win.geometry('400x300+50+50')
win.resizable(False,False)

def s():
    st=["سنگ","کاغذ","قیچی"]
    c= random.choice(st)
    lbl_com["text"] = "انتخاب حریف : " + c
    if c == "قیچی":
        label_scuser["text"]=int(label_scuser["text"]) + 1
    elif c == "کاغذ":
        lbl_sccomputer["text"]=int(lbl_sccomputer["text"]) + 1
    else:
        pass

def k():
    st=["سنگ","کاغذ","قیچی"]
    c= random.choice(st)
    lbl_com["text"] = "انتخاب حریف : " + c
    if c =="قیچی":
        lbl_sccomputer["text"]=int(lbl_sccomputer["text"]) + 1
    elif c=="سنگ":
        label_scuser["text"]=int(label_scuser["text"]) + 1  
    else:
        pass

def gh():
    st=["سنگ","کاغذ","قیچی"]
    c= random.choice(st)
    lbl_com["text"] = "انتخاب حریف : " + c
    if c == "کاغذ":
        label_scuser["text"]=int(label_scuser["text"]) + 1
    elif c=="سنگ":
        lbl_sccomputer["text"]=int(lbl_sccomputer["text"]) + 1
    else:
        pass
#########################################################################33
lbl_com=Label(win,text="انتخاب کنید",bg="black",font=('zar',14,'bold'),fg="#fff",height=2,relief=GROOVE)
lbl_com.grid(row=2,column=0,columnspan=3,sticky="nwe")


btn_sang=Button(win,text="سنگ",bg="#669900",font=('zar',14),height=2,width=10,padx=3,command=s).grid(row=1,column=0,ipadx=5)
btn_kaghz=Button(win,text="کاغذ",bg="#669900",font=('zar',14),height=2,width=10,padx=3,command=k).grid(row=1,column=1,ipadx=5)
btn_ghechi=Button(win,text="قیچی",bg="#669900",font=('zar',14),height=2,width=10,padx=3,command=gh).grid(row=1,column=2,ipadx=4)

label_scu=Label(win,text="امتیاز کاربر",bg="#669900",font=('zar',16,'bold'),height=2,width=8,relief=RAISED ).grid(row=3,column=0)
label_scuser=Label(win,text="0",bg="#fff",font=('zar',16,'bold'),height=2,relief=RAISED )
label_scuser.grid(row=3,column=1,columnspan=2,sticky="nwe")

lbl_scucom=Label(win,text="امتیاز کامپیوتر",bg="#669900",font=('zar',16,'bold'),height=2,width=8,relief=RAISED ).grid(row=4,column=0)
lbl_sccomputer=Label(win,text="0",bg="#fff",font=('zar',16,'bold'),height=2,relief=RAISED )
lbl_sccomputer.grid(row=4,column=1,columnspan=2,sticky="nwe")

#######################################
 



mainloop()