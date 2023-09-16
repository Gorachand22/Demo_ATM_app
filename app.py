from tkinter import *
from tkinter import messagebox
from mydb import Database

class ATM:
    def __init__(self):
        # Create db object
        self.dob=Database()

        self.root = Tk() 
        self.root.title('ATM') 
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg = '#DE3163')

        self.starting()
        self.root.mainloop()
    
    def starting(self):
        self.clear()
        label1 = Label(self.root, text = "already have your pin!!", bg = '#CCCCFF',fg = 'black')
        label1.pack(pady=(30,10))
        label1.configure(font=('verdana',10, 'bold'))

#-------------------------------------------------------------------------------------------------------------------------------- 
        login_btn = Button(self.root, text = "verify your pin!!!", width = 20, height= 1, bg= 'white',command= self.pin_verify) # Button class for login click
        login_btn.pack(pady=(3,20))
        login_btn.configure(font = ('verdana', 15, 'bold'))
#-------------------------------------------------------------------------------------------------------------------------------- 
        label3 = Label(self.root, text = "Don't Have Pin?", bg = '#CCCCFF',fg = 'black')
        label3.pack(pady=(3,10))
        label3.configure(font=('verdana',10, 'bold'))
        register_btn = Button(self.root, text = 'create your pin', width = 20, height= 1, bg = 'white', command=self.add_pin)
        register_btn.pack(pady=(3,20))
        register_btn.configure(font=('verdana',15, 'bold'))
#-------------------------------------------------------------------------------------------------------------------------------- 
    def add_pin(self):
        self.clear()
        heading = Label(self.root, text = 'ATM', bg = '#1C2833', fg = 'white') 
        heading.pack(pady=(30,30)) 
        heading.configure(font = ('verdana', 24, 'bold')) 
#--------------------------------------------------------------------------------------------------------------------------------        
        label0 = Label(self.root, text = 'Set The Pin')
        label0.pack(pady=(10,10))
        label0.configure(font = ('verdana', 10)) 

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5,10), ipady = 4) #ipady use for set height
        
#--------------------------------------------------------------------------------------------------------------------------------        
        Register_btn = Button(self.root, text = "Register", width = 30, height= 2, bg= 'white', command=self.perform_registration) # Button class for Register click
        Register_btn.pack(pady=(5,10))
        Register_btn.configure(font = ('verdana', 10))
#--------------------------------------------------------------------------------------------------------------------------------        
        label3 = Label(self.root, text = "already have your pin!!", bg = '#CCCCFF',fg = 'black')
        label3.pack(pady=(3,10))
        label3.configure(font=('verdana',10, 'bold'))

        login_btn = Button(self.root, text = "verify your pin!!!", width = 15, height= 1, bg= 'white',command= self.pin_verify)
        login_btn.pack(pady=(3,10))
        login_btn.configure(font=('verdana',10))
#--------------------------------------------------------------------------------------------------------------------------------        
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
 #--------------------------------------------------------------------------------------------------------------------------------    
    def perform_registration(self):
        pin = self.name_input.get()   
        response = self.dob.add_data(pin)

        if response == 1:
            messagebox.showinfo('Pin added', 'successfully')
        else:
            if response == 0:
                messagebox.showerror('error', 'Pin Already Exists')
            else:
                messagebox.showerror('error', 'Insert Valid Pin')
#--------------------------------------------------------------------------------------------------------------------------------     
    def pin_verify(self):
        self.clear()
        label1 = Label(self.root, text = "Enter Your Current pin!!", bg = '#CCCCFF',fg = 'black')
        label1.pack(pady=(30,10))
        label1.configure(font=('verdana',10, 'bold'))

        self.pin_input = Entry(self.root, width=50)

        self.current = self.pin_input
        self.pin_input.pack(pady=(5,10), ipady = 4) 
#-------------------------------------------------------------------------------------------------------------------------------- 
        login_btn = Button(self.root, text = "verify your pin!!!", width = 20, height= 1, bg= 'white',command= self.pin_check) # Button class for login click
        login_btn.pack(pady=(5,10))
        login_btn.configure(font = ('verdana', 10))
    
    def pin_check(self):
        current_pin = self.pin_input.get() 
        response = self.dob.verify(current_pin)

        if response == 1:
            messagebox.showinfo('Valid Pin', 'You Can Proceed')
            self.home_gui()

        else:
            messagebox.showerror('Error', 'Login failed')
            self.starting()
#--------------------------------------------------------------------------------------------------------------------------------     
    def home_gui(self):
        self.clear()
        heading = Label(self.root, text = 'ATM',bg = '#1C2833' , fg = 'white' )
        heading.pack(pady=(10,10))
        heading.configure(font = ('Verdana',24, 'bold'))
#-------------------------------------------------------------------------------------------------------------------------------- 
        debit_btn = Button(self.root, text = "Withdraw", width = 30, height = 4, command = self.withdraw)
        debit_btn.pack(pady= (10,10))
        debit_btn.configure(font = ('verdana', 10))
#-------------------------------------------------------------------------------------------------------------------------------- 
        deposite_btn = Button(self.root, text = "Deposite", width = 30, height = 4, command = self.deposite)
        deposite_btn.pack(pady= (10,10))
        deposite_btn.configure(font = ('verdana', 10))
#-------------------------------------------------------------------------------------------------------------------------------- 
        balance_btn = Button(self.root, text = "Check Balance", width = 30, height = 4, command = self.balance)
        balance_btn.pack(pady= (10,10))
        balance_btn.configure(font = ('verdana', 10))

#-------------------------------------------------------------------------------------------------------------------------------- 
        Change_pin_btn = Button(self.root, text = "Change Pin", width = 30, height = 4, command = self.change_pin)
        Change_pin_btn.pack(pady= (10,10))
        Change_pin_btn.configure(font = ('verdana', 10))
#-------------------------------------------------------------------------------------------------------------------------------- 
        logout_btn = Button(self.root, text = "logout", width = 30, height = 4, command = self.starting)
        logout_btn.pack(pady= (3,10))
        logout_btn.configure(font = ('verdana', 10))

#-------------------------------------------------------------------------------------------------------------------------------- 
    def withdraw(self):
        self.clear()
        heading2 = Label(self.root, text = 'Withdraw',bg = '#1C2833' , fg = 'white' )
        heading2.pack(pady=(8,8))
        heading2.configure(font = ('Verdana',20))
#--------------------------------------------------------------------------------------------------------------------------------
        label1 = Label(self.root, text = 'Enter the withdraw amount',bg = '#1C2833' , fg = 'red')
        label1.pack(pady=(10,10))
        label1.configure(font=('verdana',15))

        self.withdraw_input = Entry(self.root, width=50)
        self.withdraw_input.pack(pady=(5,10), ipady = 5)
        
        btn = Button(self.root, text = "Analyze Withdraw", command = self.withdraw_analysis)
        btn.pack(pady = (10,10))

        self.withdraw_result = Button(self.root, text = '', bg = '#1C2833', fg = 'green')
        self.withdraw_result.pack(pady= (10,10))
        self.withdraw_result.configure(font = ('verdana', 16))
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------        
        goback_btn = Button(self.root, text = "Back", command = self.home_gui)
        goback_btn.pack(pady= (10,10))
        goback_btn.configure(font = ('verdana', 10))
#--------------------------------------------------------------------------------------------------------------------------------
    def withdraw_analysis(self):

        amount = self.withdraw_input.get()
        result= self.dob.doing_withdraw(amount )

        if result == 0:
            messagebox.showinfo('insufficient balance','You cannot withdraw')
            self.home_gui()
        else:
            messagebox.showinfo('congrats','Withdraw successful')
            self.withdraw_result['text']= result
            self.home_gui()
    
    def deposite(self):
        self.clear()
        heading2 = Label(self.root, text = 'Deposite',bg = '#1C2833' , fg = 'white' )
        heading2.pack(pady=(8,8))
        heading2.configure(font = ('Verdana',20))
#--------------------------------------------------------------------------------------------------------------------------------
        label1 = Label(self.root, text = 'Enter the deposite amount',bg = '#1C2833' , fg = 'red')
        label1.pack(pady=(10,10))
        label1.configure(font=('verdana',15))

        self.deposite_input = Entry(self.root, width=50)
        self.deposite_input.pack(pady=(5,10), ipady = 5)
        
        btn = Button(self.root, text = "Analyze Deposite", command = self.deposite_analysis)
        btn.pack(pady = (10,10))
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------        
        goback_btn = Button(self.root, text = "Back", command = self.home_gui)
        goback_btn.pack(pady= (10,10))
        goback_btn.configure(font = ('verdana', 10))
#--------------------------------------------------------------------------------------------------------------------------------
    def deposite_analysis(self):
        amount = self.deposite_input.get()
        result= self.dob.doing_deposite(amount)

        if result == 0:
            messagebox.showinfo('incorrect','pass correct data type!!')
            self.home_gui()
        else:
            messagebox.showinfo('congrats','deposite successful')
            
#--------------------------------------------------------------------------------------------------------------------------------  
    def balance(self):
        self.clear()

        self.deposite_result = Button(self.root, text = '', bg = '#1C2833', fg = 'green')
        self.deposite_result.pack(pady= (30,30))
        self.deposite_result.configure(font = ('verdana', 16))
        
#--------------------------------------------------------------------------------------------------------------------------------
        result= self.dob.doing_balance()

        self.deposite_result['text']= result
#--------------------------------------------------------------------------------------------------------------------------------        
        goback_btn = Button(self.root, text = "Back", command = self.home_gui)
        goback_btn.pack(pady= (10,10))
        goback_btn.configure(font = ('verdana', 10))
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------
    
    def change_pin(self):
        self.clear()
        heading2 = Label(self.root, text = 'Pin Change',bg = '#1C2833' , fg = 'white' )
        heading2.pack(pady=(8,8))
        heading2.configure(font = ('Verdana',20))
        label1 = Label(self.root, text = 'Enter the new pin',bg = '#1C2833' , fg = 'red')
        label1.pack(pady=(10,10))
        label1.configure(font=('verdana',15))

        self.new_pin_input = Entry(self.root, width=50)
        self.new_pin_input.pack(pady=(5,10), ipady = 5)
        
        btn = Button(self.root, text = "Pin Changing", command = self.new_pin_analysis)
        btn.pack(pady = (10,10))
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------        
        goback_btn = Button(self.root, text = "Back", command = self.home_gui)
        goback_btn.pack(pady= (10,10))
        goback_btn.configure(font = ('verdana', 10))
#--------------------------------------------------------------------------------------------------------------------------------
    def new_pin_analysis(self):
        new_pin = self.new_pin_input.get()
        result= self.dob.doing_pin_change(new_pin)

        if result == 1:
            messagebox.showinfo('pin changed','success')

nlp = ATM()