
user_input = ''
expences = []
prices = []
total = 0 
while user_input != 'q': 
    print ("-------------Choose a nummer to Continiue ------------")
    user_input = input("type 1  - to Add expences.\ntype 2 -to view all. Expencces\ntype 3 -View total Expences\ntype 'q' -to Quit\n")
    
    
    if user_input == '1':
        user_input_item = input("Enter name of the item - ")
        expences.append(user_input_item) 
        user_input_price = float(input("How Much that cost? - "))
        prices.append(user_input_price) 
        total = total + user_input_price
        
    elif user_input == '2': 
         for expence,price in zip(expences,prices):
             print (expence,price)          
            
    elif user_input == '3': 
        print ("your total spended ${total: .2f}" ) 
        
    elif user_input == 'q': 
        print ("bye")
        break 
  
  
