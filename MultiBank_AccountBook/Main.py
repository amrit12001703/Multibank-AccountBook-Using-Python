# ================================= Basic Python Module =================================
import os    
import random
from datetime import datetime

# ================================= For GUI Modules =====================================
from tkinter import*    
from tkinter import ttk  
from tkinter import messagebox 
from tkcalendar import Calendar,DateEntry

# ================================= Image handling Module ================================
from PIL import ImageTk  

# ================================== Attributes of GUI Used ==========================================
'''
1. Label
2. Frame
3. LabelFrame
4. Button
5. Images
6. Listbox
7. Comboboxes
8. Calender
9. Scrollbar

'''
# ================== First Page Class ==============
# ================== First Page Class ==============

class win1(Tk):
    new=None
    def __init__(self,*arg):       # Constructors
        Tk.__init__(self,*arg)
        F1 = Frame(self,bg="black",relief=GROOVE,bd=10)
        F1.pack()
        lab1=Label(F1,text='Welcome to',font=('Comic Sans MS',35),fg='red',bg="black",width=13)
        lab1.pack()
        lab2=Label(F1,text='Personal Account Management',bg="black",font=('Comic Sans MS',40,'bold'),fg='#994483',width=25)
        lab2.pack()
        lab1=Label(F1,text='Creator---                    ',bg="black",font=('Times',35,'bold'),fg='green',width=17,justify='right')
        lab1.pack()
        lab1=Label(F1,text='  Amrit Anand',font=('Verdana',30),bg="black",fg='lightgreen',width=23)
        lab1.pack()
        
        
        bottom=Frame()
        bottom.pack()
        but=Button(bottom,text='NEW USER',font=('Courier',15,'bold'),fg='#436632',bg='#abcdef',width=33,cursor='hand2',
                   activebackground='#86cc64',command=self.open1)
        but.pack(side='left')
        but=Button(bottom,text='EXISTING USER',font=('Courier',15,'bold'),fg='#436632',bg='#abcdef',width=34
                   ,cursor='hand2',
                   activebackground='#86cc64',command=self.open2)
        but.pack(side='right')

    def open1(self,*arg):  # Function calls window 2 that is Signup window
        self.destroy()
        win2().mainloop()

    def open2(self,*arg):  # Function calls Login window
        self.destroy()     # Used to destroy window
        root=Tk()
        clas=login(root)
        win1.new=clas
        
# ================================ SignUp Class(SignUp Window) ==============================
# ================================ SignUp Class(SignUp Window) ==============================
# ================================ SignUp Class(SignUp Window) ==============================
# ================================ SignUp Class(SignUp Window) ==============================

class win2(Tk):
    def __init__(self,*arg):
        Tk.__init__(self,*arg)
        self.title("Signup".center(420))  # title for Window 
        self.configure(background = "black")  # background color for window 
        self.geometry("1350x700+0+0")

        bg_color ="#074463"
        font_=("times new roman")

        title= Label(self, bd=10, relief=GROOVE, text="SignUp Page", font=(font_,40,"bold"),bg=bg_color,fg="gold").pack(side=TOP, fill=X)


        #===========variables===================

        self.uname=StringVar()
        self.pasw=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.contact=StringVar()
        self.dob=StringVar()
        

        now = datetime.now()
        self.today= now.strftime("%d/%m/%Y")
        self.label,self.calender="",""


        Manage_Frame=Frame(self,bd=10, relief=RIDGE,bg=bg_color)
        Manage_Frame.place(x=450, y=100, width=500, height=550)
        m_title=Label(Manage_Frame,text="SIGN UP", compound=LEFT, bg=bg_color,fg="white",font=(font_,30,"bold"))
        m_title.grid(row=0, columnspan=2,pady=20)

#=======================Entries==============================
        lbl1=Label(Manage_Frame,text="Username",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        lbl1.grid(row=1, column=0,padx=20,pady=10,sticky="w")

        txt1=Entry(Manage_Frame,textvariable=self.uname,  bd=5,relief=GROOVE,font=(font_,15,"bold"))
        txt1.grid(row=1, column=1,padx=20,pady=10,sticky="w")
#*****************************************************************************************************

        lbl2=Label(Manage_Frame,text="Password",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        lbl2.grid(row=2, column=0,padx=20,pady=10,sticky="w")

        txt2=Entry(Manage_Frame,textvariable=self.pasw,  bd=5,relief=GROOVE,font=(font_,15,"bold"))
        txt2.grid(row=2, column=1,padx=20,pady=10,sticky="w")
#*****************************************************************************************************

        lbl3=Label(Manage_Frame,text="Email",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        lbl3.grid(row=3, column=0,padx=20,pady=10,sticky="w")

        txt3=Entry(Manage_Frame,textvariable=self.email,  bd=5,relief=GROOVE,font=(font_,15,"bold"))
        txt3.grid(row=3, column=1,padx=20,pady=10,sticky="w")
#*****************************************************************************************************

        self.label=(Label(Manage_Frame,text="D.O.B", bg=bg_color,fg="white",font=(font_,20,"bold")))
        self.label.grid(row=4, column=0,padx=20,pady=10,sticky="w")
        
        self.calendar=(DateEntry(Manage_Frame, textvariable=self.dob,font=("times new roman",18,"bold"), locale='en_GB', width=16,state="readonly"))
        self.calendar.place(x=180, y=290, anchor="w")

#*****************************************************************************************************

        gender_lbl=Label(Manage_Frame,text="Gender",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        gender_lbl.grid(row=5, column=0,padx=20,pady=10,sticky="w")
        
        # ================== Combobox (used to create Drop down Menu) ====================================       
        
        gender=ttk.Combobox(Manage_Frame,textvariable=self.gender, font=(font_,13,"bold"),width=21,state="readonly")
        gender['values']=("Male","Female","Others")
        gender.grid(row=5, column=1,padx=20,pady=10,sticky="w")



#*****************************************************************************************************
        lbl6=Label(Manage_Frame,text="Contact",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        lbl6.grid(row=6, column=0,padx=20,pady=10,sticky="w")

        txt6=Entry(Manage_Frame,textvariable=self.contact,  bd=5,relief=GROOVE,font=(font_,15,"bold"))
        txt6.grid(row=6, column=1,padx=20,pady=10,sticky="w")

# ==================================== Buttons ================================================
# ==================================== Buttons ================================================
# ==================================== Buttons ================================================
# ==================================== Buttons ================================================
        
        Button_Frame=Frame(Manage_Frame,bd=4, relief=RIDGE,bg=bg_color)
        Button_Frame.place(x=10, y=450,width=460,height=70)

        btn_sgnup = Button(Button_Frame, text="SignUp",width =8, command = self.signup, font="bold").grid(row = 0,column=0,padx=15,pady=15 )
        btn_back = Button(Button_Frame, text="Back",width =8, command = self.back, font="bold").grid(row = 0,column=1,padx=15,pady=15 )
        btn_Clear = Button(Button_Frame, text="Clear",width =8, command = self.clear, font="bold").grid(row = 0,column=2,padx=15,pady=15 )
        btn_Exit = Button(Button_Frame, text="Exit",width =8, command = self.exit, font="bold").grid(row = 0,column=3,padx=15,pady=15 )

    def exit(self):
        self.destroy()  
    
    def clear(self):
        self.uname.set("")
        self.pasw.set("")
        self.email.set("")
        self.gender.set("")
        self.contact.set("")
        self.dob.set(self.today)
    
    
    def signup(self): # The Function Used to create new User ID by new Ids
        # => Checking Feilds Empty or not , valid email or not , contact and DOB. If All Pass true then will check that user name already exists or not
        # if we find that user name is unique then only new file will create with ts data

        if self.uname.get()=="" and self.contact.get()=="" and self.pasw.get=="" and self.email.get()=="" and self.gender.get()=="" and self.dob.get()==self.today :
            return messagebox.showerror("Error","All Fields Required")
        
        if self.uname.get()==""  :
            return messagebox.showerror("Error","Username Required")
        if self.pasw.get=="" :
            return messagebox.showerror("Error","Password Required")
        if len(str(self.pasw.get()))<8:
            return messagebox.showerror("Error","Password should of minimum 8 character")
        
        if self.email.get()=="" :
            return messagebox.showerror("Error","Email Required")
        if "@" not in self.email.get():
            return messagebox.showerror("Error","Email Should have '@' character")
            
        if self.gender.get()==""  :
            return messagebox.showerror("Error","Gender Required")

        if self.dob.get()>=self.today  :
            return messagebox.showerror("Error","DOB Not Possible")
        
        if self.contact.get()==""  :
            return messagebox.showerror("Error","Contact Required")
        
        try:
            temp=self.contact.get()
            int(temp)
        except ValueError:
            return messagebox.showerror("Error","Contact should be Integer")
 
        if len(str(self.contact.get()))<10 or len(str(self.contact.get()))>10 :
            return messagebox.showerror("Error","Contact should consist of 10 numbers")     
        
        else:
            present ="no"
            f = os.listdir("User_F/")
            try:
                if len(f)>0:
                    for i in f:
                        if i.split(".")[0]==self.uname.get():
                            present="yes"
                    if present == "yes":
                        messagebox.showerror("Error","Username Already Exist")
                        
                    else:
                        self.get_data() # Goto Function to know what it says
                else:
                    self.get_data()
            
            except EOFError:
                f.close()   

    def get_data(self):
        # Getting data from feilds to store data in file

        f=open("User_F/"+str(self.uname.get())+".txt","w")  # open File in writing mode from directary 
        # Writing the data into file that is opend in writing mode
        f.write(
                    str(self.uname.get())+","+
                    str(self.pasw.get())+","+
                    str(self.email.get())+","+
                    str(self.dob.get())+","+
                    str(self.contact.get())+","+
                    str(self.gender.get())
                )
        f.close()
        self.clear()
        messagebox.showinfo("Info","Succesfully Signed Up")

    def back(self):
        self.destroy()
        win1()

# ===================================== Login Window =======================================
# ===================================== Login Window =======================================
# ===================================== Login Window =======================================
# ===================================== Login Window =======================================

class login():
    def __init__(self,root):
        self.root=root
        self.root.title("Login Form".center(420))  
        self.root.configure(background="black")  
        self.root.geometry("1360x768+0+0")
        bg_color = "#2B547E"

        # =========================== Image Storing ========================================
        # =========================== Image Storing ========================================
        # =========================== Image Storing ========================================
        # =========================== Image Storing ========================================

        self.eye_icon = PhotoImage(file="Pics\\2.png")
        self.bg_icon = ImageTk.PhotoImage(file="Pics\\1.jpg")
        self.bank_icon = ImageTk.PhotoImage(file="Pics\\6.jpg")    
        self.user_icon = ImageTk.PhotoImage(file="Pics\\4.png")
        self.pasw_icon = ImageTk.PhotoImage(file="Pics\\3.png")
        self.user_ = ImageTk.PhotoImage(file="Pics\\5.png")


        # =========================== Variables ========================================
        # =========================== Variables ========================================
        # =========================== Variables ========================================
        # =========================== Variables ========================================

        self.uname = StringVar()
        self.pasw = StringVar()
        self.uname.set("User Id")
        self.pass_1 = StringVar()
        self.pass_1.set("Password Mode: Hidden")
        
        # ============================ GUI Window and Functional Buttons Creation ============================
        # ============================ GUI Window and Functional Buttons Creation ============================
        # ============================ GUI Window and Functional Buttons Creation ============================
        # ============================ GUI Window and Functional Buttons Creation ============================

        bg_lbl = Label(root, image=self.bg_icon).pack(fill=Y) 

        
        # ============================ Frame 1 (F1) ===============================
        # ============================ Frame 1 (F1) ===============================
        # ============================ Frame 1 (F1) ===============================
        # ============================ Frame 1 (F1) ===============================

        self.F1 = LabelFrame(root, bd=10, relief=GROOVE, bg=bg_color)
        self.F1.place(x=195, y=95, width=600, height=480)
        
        F1=self.F1
        
        lbl = Label(F1, text="User Login ", bg=bg_color, fg="gold", font=("times new roman", 30, "bold")).grid(row=0, column=0, padx=80, pady=30)

        logolbl = Label(F1, image=self.user_icon).place(x=80, y=200, anchor="w")
        
        lbl6 = Label(F1, text="User ID", fg="white", bg=bg_color, font=("times new roman", 18, "bold")).place(x=115, y=200, anchor="w")
        
        self.txtu = Entry(F1, bd=5, textvariable=self.uname, relief=GROOVE,font=("", 15)).place(x=250, y=200, anchor="w")

        logolbl2 = Label(F1, image=self.pasw_icon).place(x=80, y=260, anchor="w")
        
        lbl7 = Label(F1, text="Password", fg="white", bg=bg_color, font=("times new roman", 20, "bold"))
        
        lbl7.place(x=115, y=260, anchor="w")
        
        self.txtp = Entry(F1, bd=5, textvariable=self.pasw, show="*",relief=GROOVE, font=("", 15))
        
        self.txtp.place(x=250, y=260, anchor="w")

        
        self.txtp_1 = Entry(F1, bd=0, bg=bg_color, fg="white", textvariable=self.pass_1,relief=GROOVE, width="45", font=("times new roman", 10))
        
        self.txtp_1.place(x=250, y=10, anchor="w")

        self.txtp_1.config(state="readonly",width=23,fg="black")
        # ============================ Frame 2 (F2) ===============================
        # ============================ Frame 2 (F2) ===============================
        # ============================ Frame 2 (F2) ===============================
        # ============================ Frame 2 (F2) ===============================

        self.F2 = LabelFrame(root, bd=10, relief=GROOVE, bg="#3b444b")
        self.F2.place(x=790, y=95, width=310, height=480)
        F2 = self.F2 
        
        lbl2 = Label(F2, bg=bg_color, image=self.user_).grid(row=0, column=0, padx=100, pady=20)
        
        lbl3 = Label(F2, text="Get you all account details at ", bg="#3b444b", fg="#00FFFF", font=("times new roman", 15, "italic")).grid(row=1, column=0, padx=5)
        
        lbl4 = Label(F2, text="one place @PersonalAcc", fg="#00FFFF", bg="#3b444b", font=("times new roman", 10, "italic")).grid(row=2, column=0, padx=10)

        lbl6 = Label(F2, text="Developed by Aditya",fg="#4863A0", bg="#3b444b", font=("times new roman", 20)).place(x=20, y=420)

        img_lbl7 = Label(F2, image=self.bank_icon, bg="#3b444b").place(x=20, y=300, width=250, height=100) 
        # ========================== Buttons ======================================
        # ========================== Buttons ======================================
        # ========================== Buttons ======================================
        # ========================== Buttons ======================================

        btn_login1 = Button(F1, text="SignIn", relief=RAISED, width=12, height=1, font=("times new roman", 12, "bold"), bg="green", foreground="#FEFCFF", command=self.logfun).place(x=530, y=330, width=150, anchor="e")

        btn_Signup = Button(F1, text="Sign Up", relief=GROOVE, width=8, height=1, activebackground="Red", activeforeground="white", command=self.Signup, font=("times new roman", 14, "bold"), bg="Red", fg="white").place(x=330, y=330, width=150, anchor="e")

        btn_Eye = Button(F1, image=self.eye_icon, relief=GROOVE, font=("times new roman", 14, "bold"), bg="light green", command=self.show_pasw).place(x=528, y=260, height=35, anchor="e")    

        btn_Exit = Button(F2, text="Exit", relief=GROOVE, width=8, height=1, activebackground="Red", activeforeground="white", command=self.Exit, font=("times new roman", 14, "bold"), bg="Red", fg="white").grid(row=5, column=0, padx=15, pady=60, sticky="w")

        btn_Back = Button(F2, text="Back", relief=GROOVE, width=8, height=1, activebackground="Red", activeforeground="white", command=self.Back_T, font=("times new roman", 14, "bold"), bg="lightgreen", fg="black").place(x=170, y=215)

    def Back_T(self,*arg):
        self.root.destroy()
        win1()
        
    def Signup(self,*arg):
        self.root.destroy()
        win2().mainloop()
        
    def logfun(self):
        
        ''' This is a login function first it checks that fields are not empty.
            If uname and password given to the field then it checks by opening user file of same name that is with user name
            and check password into it if it matches with the typed one then it calls existing class that is our main window
        '''

        if self.uname.get()=="" or self.pasw.get()=="":
            messagebox.showerror("Error","All fields should be entered")
        else:
            present ="no"
            f = os.listdir("User_F/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0]==self.uname.get():
                        present="yes"
                if present == "yes":
                    L=[]
                    file = open("User_F/"+self.uname.get()+".txt","r")
                    data = file.read()
                    words = data.split(",")
                    if str(words[1]) == self.pasw.get():
                        messagebox.showinfo("Successful","Successfully Logined")
                        self.root.destroy()
                        existing(win1.new).mainloop()                        
                    else: 
                        messagebox.showerror("Error","Username or Password May be wrong")
            else:
                messagebox.showerror("Error","No Data Exist to this Username")

    def Exit(self):
        self.root.destroy()

    def show_pasw(self):
        ''' Basically this functions is used to shift wheather we want to type password by seeing its characters or by hidding it'''

        a = self.pasw.get()  # Storing Password Field Value to a Variable
        self.txtp_1.config(state="normal") # change the field state to normal so that we can read our mode of password type (Hidden or Shown)
        self.pasw.set(a) # Not set the vale into field again

        if self.txtp_1.get() == "Password Mode: Hidden": # If we get Mode hidden then when Button Clicks it should turn into show and visa-versa for elif condition
            self.txtp_1.config(state="normal") # Similar work as Above
            self.txtp_1.insert(0, "Password Mode: Shown")
            self.txtp_1.config(state="readonly",width=23,fg="black")
            
            self.txtp = Entry(self.F1, bd=5, textvariable=self.pasw, relief=GROOVE, font=("", 15))
            self.txtp.place(x=250, y=260, anchor="w")
            self.pass_1.set("Password Mode: Shown")
            self.pasw.set(a)
            self.txtp_1.config(state="readonly",width=23,fg="black")
        
        elif self.txtp_1.get() == "Password Mode: Shown":
            self.txtp_1.config(state="normal")
            self.txtp_1.delete(0, END)
            self.txtp_1.insert(0, "Password Mode: Hidden")
            self.txtp = Entry(self.F1, bd=5, textvariable=self.pasw,
                                relief=GROOVE, show="*", font=("", 15))
            self.txtp.place(x=250, y=260, anchor="w")
            self.pasw.set(a)
            self.txtp_1.config(state="readonly",width=23,fg="black")

        self.root.mainloop()


# ========================================= Main Window =======================================    
# ========================================= Main Window =======================================    
# ========================================= Main Window =======================================    
# ========================================= Main Window =======================================    

class existing(Tk):
    def __init__(self,name,*arg):
        Tk.__init__(self,*arg)
   
        self.title("Personal Bank Account Record System".center(420))
        self.configure(background = "black")
        bg_color="#4169E1" 
        self.geometry("1350x700+0+0")
        
        title=Label(self,text="Personal Bank Account Record System",font=("times new roman",35,"bold"),bd=5,relief=GROOVE ,bg="#9370DB",pady=2).pack(fill=X)

        UserF1=LabelFrame(self, bd=10, text="Account Details",relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        UserF1.place(x=0,y=70,height=460)


        #--------------Variables-----------------

        self.u_id =StringVar()
        self.name =StringVar()
        self.state =StringVar()
        self.city =StringVar()
        self.pin =StringVar()
        self.house_no =StringVar()
        self.contact =StringVar()
        self.date =StringVar()
        self.bank =StringVar()
        self.id_proof =StringVar()
        self.total =StringVar()
        self.withdraw =StringVar()
        self.deposite =StringVar()
        self.acc_no =StringVar()
        self.all_acc_total = StringVar()
        self.u_id.set(str(random.randint(100000,999999)))
        self.total.set("0.0")
        self.withdraw.set("0.0")
        self.deposite.set("0.0")
        
        
        lbluid=Label(UserF1,text="User Id",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=0,column=2,padx=20,pady=10,sticky="w")
        txtuid=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.u_id,width=21,state="readonly",font="arial 15 bold").grid(row=0,column=3,padx=20,pady=10)
        
        lblacc=Label(UserF1,text="Account No.",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=0,column=0,padx=20,pady=10,sticky="w")
        txtacc=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.acc_no,width=21,font="arial 15 bold").grid(row=0,column=1,padx=20,pady=10)
    
        lblname=Label(UserF1,text="Name",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(sticky="w",row=1,column=0,padx=20,pady=10)
        txtname=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.name, width=21,font="arial 15 bold").grid(row=1,column=1,padx=20,pady=10,sticky="w")

        lblcontact=Label(UserF1,text="Contact",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=1,sticky="w",column=2,padx=20,pady=10)
        txtcontact=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.contact,width=21,font="arial 15 bold").grid(row=1,column=3,padx=20,pady=10)

        
        lbldate=Label(UserF1,text="Date(dd/mm/yyyy)",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(sticky="w",row=2,column=2,padx=20,pady=10)
        txtdate=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.date,width=21,font="arial 15 bold").grid(row=2,column=3,padx=20,pady=10)

        
        lblstate=Label(UserF1,text="State",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=2,sticky="w",column=0,padx=20,pady=10)
        txtstate=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.state,width=21,font="arial 15 bold").grid(row=2,column=1,padx=20,pady=10)

        
        lblSD=Label(UserF1,text="Select Bank",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=3,sticky="w",column=2,padx=20,pady=10)

        
        lblcity=Label(UserF1,text="City",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=3,sticky="w",column=0,padx=20,pady=10)
        txtcity=Entry(UserF1,bd=7,textvariable=self.city,relief=GROOVE,width=21,font="arial 15 bold").grid(row=3,column=1,padx=20,pady=10)

        
        lblIP=Label(UserF1,text="ID Proof",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=4,sticky="w",column=2,padx=20,pady=10)

        lblhouse=Label(UserF1,text="House No.",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=4,column=0,sticky="w",padx=20,pady=10)
        txthouse=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.house_no,width=21,font="arial 15 bold").grid(row=4,column=1,padx=20,pady=10)

        lblpin=Label(UserF1,text="Pin and Locality",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=5,column=0,sticky="w",padx=20,pady=10)
        txtpin=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.pin,width=21,font="arial 15 bold").grid(row=5,column=1,padx=20,pady=10)

    
        lblwithdraw=Label(UserF1,text="Withdraw (INR)",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=5,column=2,sticky="w",padx=20,pady=10)
        txtwithdraw=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.withdraw,width=21,font="arial 15 bold").grid(row=5,column=3,padx=20,pady=10)

        lbldeposite=Label(UserF1,text="Deposite (INR)",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=6,column=0,sticky="w",padx=20,pady=10)
        txtdeposite=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.deposite,width=21,font="arial 15 bold").grid(row=6,column=1,padx=20,pady=10)
        
        lblT=Label(UserF1,text="Total Amount (INR)",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(sticky="w",row=6,column=2,padx=20,pady=10)
        Ttxt=Entry(UserF1,bd=7,textvariable=self.total,relief=GROOVE,width=21,font="arial 15 bold")
        Ttxt.grid(row=6,column=3,pady=10, padx=20)
        
        
        bankcombobox=ttk.Combobox(UserF1,width=20, textvariable=self.bank,font="arial 15 bold")
        bankcombobox['values']=("SBI","HDFC","ICICI","PNB","COB","BOI","Yes","Axis","PostOffice")
        bankcombobox.grid(row=3,column=3,pady=10, padx=20)   
        
        IPcombobox=ttk.Combobox(UserF1,width=20, textvariable=self.id_proof,state="readonly",font="arial 15 bold")
        IPcombobox['values']=("Addhar Card","Pan Card","Driving Licence","PassPort","VoterId Card")
        IPcombobox.grid(row=4,column=3,pady=10, padx=20)

# ================================== Buttons ========================================
# ================================== Buttons ========================================
# ================================== Buttons ========================================
# ================================== Buttons ========================================

        btnalter = Button(self,text="Alter User ID",bd=5, relief=GROOVE,command=self.alter, font="arial 15 bold",activebackground="red",activeforeground="white",fg="white",bg="red").place(x=1200,y=10)

        btnframe=Frame(self,bd=10,relief=GROOVE, bg="light blue")
        btnframe.place(x=0,y=535,width=1350, height=290)

        btnsave=Button(btnframe,text="Save", command=self.save_data, font="arial 15 bold", bd=7, width=18,height=3,bg="yellow").grid(row=0,column=0,padx=15,pady=30)
        btndelete=Button(btnframe,text="Delete",command=self.delete, font="arial 15 bold", bd=7, width=18,height=3,bg="yellow").grid(row=0,column=1,padx=15,pady=30)
        btnclear=Button(btnframe,text="Clear", command=self.clear,font="arial 15 bold", bd=7, width=18,height=3,bg="yellow").grid(row=0,column=2,padx=15,pady=30)
        btnlog=Button(btnframe,text="Logout", command=self.logout,font="arial 15 bold", bd=7, width=18,height=3,bg="yellow").grid(row=0,column=3,padx=15,pady=30)
        btnexit=Button(btnframe,text="Exit", command=self.exit,font="arial 15 bold", bd=7, width=18,height=3, bg="yellow").grid(row=0,column=4,padx=15,pady=30)


# =========================== Acc File Showing Window ================================
# =========================== Acc File Showing Window ================================
# =========================== Acc File Showing Window ================================
# =========================== Acc File Showing Window ================================

        fileframe=Frame(self,bd=10,relief=GROOVE)
        fileframe.place(x=995, y=70,width=365,height=420)

        ftitle=Label(fileframe,text="Your all Account Files", font="arial 20 bold",bd=5,relief=GROOVE,bg="light blue").pack(side=TOP,fill=X)

        scroll_y=Scrollbar(fileframe,orient=VERTICAL)  
        self.f_list=Listbox(fileframe,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.f_list.yview)
        self.f_list.pack(fill=BOTH,expand=1)

        self.f_list.bind("<ButtonRelease-1>",self.get_data)
        self.show_files()

        self.frame=Frame(self,bd=10,bg=bg_color,relief=GROOVE)
        self.frame.place(x=995, y=470,width=365,height=60)
    
        self.totalamt_allfiles()

    def save_data(self):
        present="no"
        self.final = float(self.total.get())-float(self.withdraw.get())+float(self.deposite.get())
        
        
        if len(self.acc_no.get())<11 or len(self.contact.get())>16:
            return messagebox.showerror("Error","Invalid Account Number")

        if self.total.get()=="":
            return messagebox.showerror("Error", "Total amount should be filled")
                       
        if self.final < 0.0:
            return messagebox.showerror("Error","Not Sufficient Balance to Withdraw")

        if len(self.contact.get())<10 or len(self.contact.get())>10:
            return messagebox.showerror("Error","Contact invalid")

        try:
            tmp=self.acc_no.get()
            int(tmp)
        except ValueError:
            return messagebox.showinfo('Error','Account No. Should Be Integer')

        try:
            tmp=self.contact.get()
            int(tmp)
        except ValueError:
            return messagebox.showinfo('Error','Contact No. Should Be Integer')
        try:
            b=self.total.get()
            float(b)
        except ValueError:
            return messagebox.showerror("Error","Total Amount should be float Value")   
                
        try:
            c=self.withdraw.get()
            float(c)
        except ValueError:
            return messagebox.showerror("Error","Withdrawal Amount should be float Value")   
        
        try:
            d=self.deposite.get()
            float(d)
        except ValueError:
            return messagebox.showerror("Error","Deposite Amount should be float Value")   
        
        else:
        
            f=os.listdir("Files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.u_id.get():
                        present="yes"
                if present=="yes":
                    ask=messagebox.askyesnocancel("Update","File already presennt \nDo you really want to Update?!!")
                    if ask>0:
                        self.save_file()
                        messagebox.showinfo("Update","Record has Been saved!!")
                        self.show_files()
                else:
                    self.save_file()
                    messagebox.showinfo("Saved","Record has Been saved!!")
                    self.show_files()      
    
            else:
                self.save_file()
                messagebox.showinfo("Saved","Record has Been saved!!")
                self.show_files()      
    
    def save_file(self):
        a="Withdraw: "
        b="Deposite: "
        f=open("Files/"+str(self.u_id.get())+str(self.bank.get())+".txt","w")
        f.write(
                    str(self.u_id.get())+","+
                    str(self.acc_no.get())+","+
                    str(self.name.get())+","+
                    str(self.state.get())+","+
                    str(self.city.get())+","+
                    str(self.house_no.get())+","+
                    str(self.pin.get())+","+
                    str(self.contact.get())+","+
                    str(self.date.get())+","+
                    str(self.bank.get())+","+
                    str(self.id_proof.get())+","+
                    str(a)+","+
                    str(self.withdraw.get())+","+
                    str(b)+","+
                    str(self.deposite.get())+","+
                    str(self.final)
                )
        f.close()
        self.clear()
        self.totalamt_allfiles()
        self.show_files()    
            
    def show_files(self):
        Files=os.listdir("Files/")
        self.f_list.delete(0,END)
        if len(Files)>0:        
            for i in Files:
                self.f_list.insert(END,i)

    def get_data(self,ev):
        try:
            getcursor=self.f_list.curselection()
            #print(self.f_list.get(getcursor))
            f1=open("Files/"+self.f_list.get(getcursor))
            value=[]
            for f in f1:
                value=f.split(",")
                #print(value)
            self.u_id.set(value[0])
            self.acc_no.set(value[1])
            self.name.set(value[2])
            self.state.set(value[3])
            self.city.set(value[4])
            self.house_no.set(value[5])
            self.pin.set(value[6])
            self.contact.set(value[7])
            self.date.set(value[8])
            self.bank.set(value[9])
            self.id_proof.set(value[10])
            self.withdraw.set(value[12])
            self.deposite.set(value[14])
            self.total.set(value[15])
        except Exception:
            pass

    def clear(self):
        self.u_id.set(str(random.randint(100000,999999)))
        self.acc_no.set("")
        self.name.set("")
        self.state.set("")
        self.city.set("")
        self.pin.set("")
        self.house_no.set("")
        self.contact.set("")
        self.date.set("")
        self.bank.set("")
        self.id_proof.set("")
        self.total.set("0.0")
        self.withdraw.set("0.0")
        self.deposite.set("0.0")

    def delete(self):
        present="no"
        if self.u_id.get()=="":
            messagebox.showerror("Error","UserF1 Id must be Required!!!")
        else:
            f=os.listdir("Files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == (str(self.u_id.get())+str(self.bank.get())):  
                        present="yes"
                if present=="yes":
                    ask=messagebox.askyesnocancel("Delete","Do you really want to delete?!!")
                    if ask>0:
                        os.remove("Files/"+self.u_id.get()+self.bank.get()+".txt")
                        messagebox.showinfo("Success","Deleted Successfully")
                        self.show_files()
                        self.clear()
                else:
                    messagebox.showerror("Error","File not found!!!!")
    
    def alter(self):
        self.u_id.set(str(random.randint(100000,999999)))

    def totalamt_allfiles(self):    
        file_list=os.listdir(r"Files\\")
        #print (file_list)
        self.s=0.0
        for i in file_list:
            #print(i)
            f1=open("Files/"+str(i))
            value=[]
            for f in f1:
               value=f.split(",")
            self.s+=float(value[-1])
        
        lbltxt=Label(self.frame,text="Amount (INR) in All",bg="#4169E1", fg="white",font=("times new roman",15, "bold")).place(x=5, y=5)
        newtxt=Entry(self.frame,bd=7,textvariable=self.all_acc_total,relief=GROOVE,width=21,font="arial 15 bold")
        newtxt.place(x=190,width=150)
        self.all_acc_total.set(str(self.s))
    
 
    def exit(self):
        ask=messagebox.askyesnocancel("Exit","Do you really want to Exit?!!")
        if ask>0:
            self.destroy()
        else:
            return

    def logout(self):
        ask=messagebox.askyesno("Logout","Do you really want to Logout?!!")
        if ask>0:
            messagebox.showinfo("Logout","Loged Out Successfully")
            self.destroy()
            win1().win1()
        else:
            return
app=win1()
app.mainloop()
