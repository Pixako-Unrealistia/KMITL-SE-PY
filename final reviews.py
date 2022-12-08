#The subject would be the final exam of 2021's computer engineering course at KMITL.


#question 1 
print("Q1:")
def find_word_positions(word, list_of_words):
    indexes = []
    counter = 0
    for k in list_of_words:
        if k.lower() == word.lower():
            indexes.append(counter)
        counter += 1

    if indexes:
        print(indexes)
    else:
        print(0)
    
find_word_positions("Python",["python","java", "c","PYTHON","Prolog"])
find_word_positions("iOS",["Windows","macOS","Linux"])

print("\n\nQ2:")

#in case sorted is not allowed for whatever reason
#with less loop iteration is of course possible as this example is probably one of the worst way to approach sorting this.
#but pretty sure you'd still get same mark inspite of apparent ineffiency
def dictionary_sorter(somedict):
    new_dictionary = {}
    maxval = 0
    max_name = ""
    #loop to find current max
    while somedict:
        for c in somedict:
            if somedict[c] > maxval:
                maxval = somedict[c]
                max_name = c
        new_dictionary[max_name] = maxval
        maxval = 0
        del somedict[max_name]
    
    return(new_dictionary)



def rank_translator(popularity_scores):
    data_len = len(popularity_scores)
    rank = 0
    val_buffer = 0
    new_dictionary = {}
    
    #popularity_scores = dict(sorted(popularity_scores.items(), key = lambda x : x[1], reverse = True ))
    popularity_scores = dictionary_sorter(popularity_scores)
    print(popularity_scores)
    
    for k in popularity_scores:
        acc_value = popularity_scores[k]
        
        if acc_value != val_buffer:
            rank += 1
            
        new_dictionary[k] = rank
        val_buffer = acc_value
    return (new_dictionary)

print(rank_translator({"c++": 99.7, "c" : 99.7 , "Java" : 97.5, "Python": 100, "C#" : 89.4}))




print("\n\nQ3:")
#question 3
def count_operands_in_expr(tuple_in):
	
	if type(tuple_in) != tuple:
		return 1
	else:
		return count_operands_in_expr(tuple_in[0]) + count_operands_in_expr(tuple_in[2])
		
print(count_operands_in_expr((3,'**',4)))
print(count_operands_in_expr(((((2, '+', 4), '/', 3), '*', 2), '+', (3, '**', 4))))

print("\n\nQ4:")
class SavingAccount():
    def __init__(self, bank_name, acc_name, acc_id ,  balance , transaction_history):
        self.bank_name = bank_name
        self.acc_name = acc_name
        self.acc_id = acc_id
        self.balance = balance
        self.transaction_history = transaction_history
    
    def deposit(self, money, person , date):
        if money < 0:
            print("Invalid deposit")
        else:
            self.balance += money
            self.transaction_history.append((f"{person} deposited {money} at {date}"))

    def withdraw(self, money, person , date):
        
        if (money > self.balance) or money < 0:
            print("insufficient funds or invalid amount")
        else:
            self.balance -= money
            self.transaction_history.append((f"{person} withdrew {money} at {date}"))
            
    def get_balance(self):
        return(self.balance)
    
    def print_statement(self):
        for c in self.transaction_history:
            print(self.transaction_history)
        
class OverDrawnAccount(SavingAccount):
    def __init__(self, bank_name, acc_name, acc_id ,  balance , transaction_history, limit):
        super().__init__(bank_name, acc_name, acc_id ,  balance , transaction_history)
        self.limit = limit

    def withdraw(self,money,person,date):
        if (self.balance - money < self.limit) or money < 0:
            print("exceeded the overdrawn limitations or invalid amount")
        else:
            self.balance -= money
            self.transaction_history.append((f"{person} withdrew {money} at {date}"))
      
            
Saving = SavingAccount("PIX", "Figurine's funds" , "11037" , 99999 , [])
Over = OverDrawnAccount("PIX", "Figurine's funds" , "11037" , 500 , [], -5000)
Saving.withdraw(55551, "Generico", "21/12/22")
print(Saving.get_balance())
Saving.print_statement()

Over.withdraw(5000, "Generico", "21/12/22")
print(Over.get_balance())
Over.withdraw(1000, "Generico", "21/12/22")



print("\n\nQ5:")

#CR @Kasitphoom
from abc import ABC, abstractmethod

class Sale_item:
	def __init__(self, name, cost, sale):
		self.name = name
		self.cost = cost
		self.sale = sale
		pass
	
	@abstractmethod
	def calculate_cost(self):
		pass

class Food(Sale_item):
	def __init__(self, name, cost, sale = 0):
		super().__init__(name, cost, sale)
		pass
	
	@abstractmethod
	def calculate_cost(self):
		pass

class Itemized_food(Food):
	def __init__(self, name, cost, amount):
		super().__init__(name, cost)
		self.amount = amount

	def calculate_cost(self):
		return self.cost * self.amount

class Measured_food(Food):
	def __init__(self, name, cost, weight):
		super().__init__(name, cost)
		self.weight = weight

	def calculate_cost(self):
		return self.cost * self.weight

class Book(Sale_item):
	def __init__(self, name, cost, sale, amount):
		super().__init__(name, cost, sale)
		self.amount = amount
	
	def calculate_cost(self):
		return self.cost * self.amount * (100 - self.sale) / 100

class Appliance(Sale_item):
	def __init__(self, name, cost, sale, amount):
		super().__init__(name, cost, sale)
		self.amount = amount
	
	def calculate_cost(self):
		return self.cost * self.amount * (100 + self.sale) / 100

vegtable = Itemized_food("Vegetable", 40, 2)
mango = Measured_food("Mango", 70, 1.8)
pythonbook = Book("Python", 200, 15, 1)
ricecooker = Appliance("Rice cooker", 1200, 7, 1)

poly = [vegtable, mango, pythonbook, ricecooker]

for i in poly:
    print(i.name, i.calculate_cost())
