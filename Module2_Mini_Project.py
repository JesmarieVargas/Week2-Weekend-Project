# To do List Application

to_do_list = {
    "High" : "School Project", # Added keys and values to to_do_list
    "Low" : "Chores" 
}

def main():
    while True:
        try:
            ans = input('''
  Welcome to the To-Do List App!
Menu:

    1- Add a task
    2- View tasks
    3- Mark a task as complete
    4- Delete a task
    5- Quit
                        

''')
         
            if ans == '1': # Adding a task to the To-do list
                add()
            elif ans == '2': # Viewing a task in the To-do list
               view()
            elif ans == '3': # Mark a task as complete
                mark()
            elif ans == '4': # Delete a task
               remove()
            elif ans == '5': # Quit
                print("Have a good day!")
                break
            elif ans > 5: # if answer is greater than 5 print invalid
                print("Invalid input")
                continue
        except Exception as e: # if a letter is entered other than a number print invalid option
            print("Invalid option")
    

def add():
    while True:
        priority = input('''
What is the priority of your task?
Choose below:
         High Priority
        Low Priority                                         
''')
        task = input("What is your task?:\n")
        print(f"\nPriority: {priority} \ntask: {task}")
        varification = input("Does everything look correct? y/n ")
        if varification == "y": # if input is yes add task to list
            to_do_list.update({priority : task})
            print(to_do_list) 
            break
        elif varification == "n": # if input is no return to add option 
             print("Let's verify information again!")
             return add()
    
def view():
    while True:
        print("To-do List") # Print the To-Do List
        for keys,values in to_do_list.items():
                    print(keys, ':', values)
        menu = input("Would you like to return to the main menu?: \n yes?").upper() # Ask if you want to return to menu
        if menu =="YES" or "Y":
            break
        else: # Return to menu if no to question
            return main()
       
def mark():
    while True:
        finished = input("Which task would you like to mark as completed?")
        if finished in to_do_list.values(): # if task is completed print completed
            to_do_list[finished] = "Completed X" # Add completed and X to task if finished
            print("Perfect!", finished, "will be marked as completed")
            break
        else:
            return main() # If task is not completed return to main menu

def remove():
    while True:
        completed = input(''' # Ask if task has been completed
Did you complete the task? y/n
''')
        if completed == "y": # If task has been completed remove task from list
            print("Task has been completed")
            to_do = list(to_do_list.keys())
            print(to_do)
            remove = input('Which task would you like to remove?:\n')
            to_do_list.pop(remove, "Please check spelling and reenter task you would like to remove")
            print(remove, "has been removed from To-Do list")
            break
        elif completed == "n": # If task has not been completed return to the main menu
            print("Task has not been completed")
            return main()
        elif completed != "y" or "n": # If rssponse is neither yes o no print Invalid response
            print("Invalid response")
            continue       

main()