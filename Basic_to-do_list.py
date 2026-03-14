task = []



while True:
    
    print("Your to-do list app")
    print("Please choose the action")
    print("1. Add")
    print("2. View")
    print("3. Remove")
    print("4. Exit")
    
    choose = input("Choose the numbers: ")
    
    if choose == "1":
        user_input = input("Type what will you gonna add: ")
        task.append(user_input)
        print("Your pending task: ",task)
        
    elif choose == "2":
        for i in task:
            print("Your pending task: ",i)  
            
    elif choose == "3":
        user_input = int(input("Type number which task you want to remove: "))
        task.pop()
        print("Your remaining task is: ",task) 
        
    elif choose == "4":
        user_input = input("Are you sure? Yes or No: ").capitalize()
        
        if user_input == "Yes":
            print("As you wish")
            exit()
            
        elif user_input == "No":
            print("Let's begin")
            
        else:
            while user_input != "Yes" and user_input != "No":
                print("Please answer carefully")
                user_input = input("Yes or No: ").capitalize()
                
                if user_input == "Yes":
                    print("As you wish")
                    exit()
                    
                elif user_input == "No":
                    print("Let's begin!")    
                     
        
        



