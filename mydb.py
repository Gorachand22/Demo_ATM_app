import json

class Database:
    def __init__(self):
        self.current_pin = ''

    def add_data(self, pin):

        with open('db.json', 'r') as rf:
            database = json.load(rf)
        
        if pin in database:
            return 0
        else:
            if len(pin) == 4 and pin.isdigit() == True:
                database[pin] = [0]

                with open ('db.json', 'w') as wf:
                    json.dump(database, wf)
                return 1
            else:
                return 2
    
    def verify(self, Pin):
        with open ('db.json', 'r') as rf:
            database=json.load(rf)

            if Pin in database.keys():
                self.current_pin = Pin
                return 1
            else:
                return 0

    def doing_withdraw(self, amount):
        with open ('db.json', 'r') as rf:
            database=json.load(rf)
            amount = int(amount)
            if amount> database[self.current_pin][0]:
                return 0
            else:
                database[self.current_pin][0] = database[self.current_pin][0] - amount
                with open ('db.json', 'w') as wf:
                    json.dump(database, wf)
                
                with open ('db.json', 'r') as rf:
                        database=json.load(rf)
                        if database[self.current_pin][0] == 0:
                            return 'zero balance is available'
                        else:
                            return str(database[self.current_pin][0])
    
    def doing_deposite(self, amount):
        with open ('db.json', 'r') as rf:
            database=json.load(rf)
            try:
                amount = int(amount)
            except:
                return 0
            else:
                database[self.current_pin][0] = database[self.current_pin][0] + amount

                with open ('db.json', 'w') as wf:
                    json.dump(database, wf)
                return 1
    
    def doing_balance(self):
        with open ('db.json', 'r') as rf:
            database=json.load(rf)
            
            return str(database[self.current_pin][0])
    
    def doing_pin_change(self, new_pin):
        with open ('db.json', 'r') as rf:
            database=json.load(rf)
            
            database[new_pin] = database[self.current_pin][0]
            
            with open ('db.json', 'w') as rf:
                del database[self.current_pin]
                json.dump(database, rf)  
                return 1

             
        


