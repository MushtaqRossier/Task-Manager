from datetime import date
#------------------------------------------------------------------------------
"""
Creating a function that registers new users whose details are not yet in the
text file.
"""
def reg_user():
    
    user_list = []
    
    with open("user.txt") as f:
        
        incorrect_info = True
        while incorrect_info:
            
            #Requests user to input new username
            new_user = input("Create your new user name here: ")
            
            #Opens user text file to read
            f = open("user.txt", "r")
            
            for line in f:
                info = line.split(", ")  #Converts data in f to lists
                user_list.append(info[0])
                
            if new_user not in user_list:    
                #Requests user to enter and confirm new password
                new_password = input("Create your new password here: ")
                confirm = input("Confirm your new password here: ")
                
                if new_password == confirm:
                    #Opens user text file to append new details
                    file = open("user.txt", "a")
                    file.write("\n" + new_user + ", ")
                    file.write(new_password)
                   
                    #Closing user text file with updated details
                    file.close()
                    incorrect_info = False
                    break
       
                else:
                    print("Your passwords do not match")     
                    
            else:
                print("User already exist, please try again")
                
        
            #Closes user text file
            f.close()
        
    return "Registration of new user was successful"
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
"""
Creating a function that assigns a new task to the user and writes the details
to a text file.
"""    
def add_task():
    
    with open("tasks.txt") as f:
        
        #Opens tasks text file to append 
        f = open("tasks.txt", "a")
        
        #Requests user to input the following details
        username = input("Enter username of the person that the task is assigned to: ")
        title = input("Enter the title of the task: ")
        description = input("Enter the description of the task here: ")
        assign = input("Enter the date the task was assigned to you (format: year-month-day): ")
        due = input("Enter the due date of the task (format: year-month-day): ")
        complete = ""
        
        #Writes details to tasks text file
        f.write(username + ", " +  title + ", " + description + ", " + assign + ", " + due + ", " + complete + '\n')
           
        #Closes tasks text file with new appended details
        f.close()
        
    return "Assigning task to new user was successful"
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
"""
Function that reads and convert data from tasks text file to a nested list.
"""
def to_list():
    
    with open("tasks.txt") as f:
        
        #Initialising a variable that will be used in the loop
        new_list = []
        
        f = open("tasks.txt", "r")
        
        #Loops through tasks text file, reads the data, edit the the data and store in new variables
        for line in f:
            x = line.replace("\n", "")
            y = x.split(", ")
            new_list.append(y)
        f.close()
        
    return new_list
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
"""
Creating a function that reads all the task assignments in the text file and 
displays it in a user-friendly manner.
"""
def view_all():
    
    count = 0
    new_list = to_list()
           
    #Outputs the task assignments in a user-friendly manner                      
    for inner_list in new_list :
        count += 1
        print("Task number = " + str(count))
        print("Task assigned to : " + inner_list[0])
        print("Job title : " + inner_list[1])
        print("Job description : " + inner_list[2])
        print("Date assigned : " + inner_list[3])
        print("Due date : " + inner_list[4])
        print("Completed? : " + inner_list[5])
        print()
        
    return "All task assignments are presented above"
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
"""
Function that allows the user that is logged in to view their task assignments. 
"""
def view_mine():
    
    count = 0
    new_list = to_list()
    
    #Outputs the user's task assignments in a user-friendly manner 
    for inner_list in new_list :
        count += 1
        if user == inner_list[0] :
            print("Task number = " + str(count))
            print("Task assigned to : " + inner_list[0])
            print("Job title : " + inner_list[1])
            print("Job description : " + inner_list[2])
            print("Date assigned : " + inner_list[3])
            print("Due date : " + inner_list[4])
            print("Completed? : " + inner_list[5])
            print()

    return "Choose task number to view details"  
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
"""
Function that enables the user to mark their task assignments as complete.
"""
def mark_as_complete(x):
    
    new_list = to_list()
  
    for inner_list in new_list:
        if user == inner_list[0]:
            new_list[x - 1][5] = "Yes" 
    
    return new_list[x - 1], "Your task completion was successful"
 
def edit_the_task(x):
     
    #Initialising a variable that will be used in the loop
    new_list = to_list()
     
    for inner_list in new_list:
        if user == inner_list[0]:
           username = input("Who is taking over the responsibility of this task: ")
           due = input("What is the new due date (format year-month-day): ")
           new_list[x - 1][0] = username
           new_list[x - 1][4] = due
                    
    return new_list[x - 1], "The editing of your details was successful"
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
"""
Function that writes the task statistics to the task overview text file.
"""
def task_overview_write():
    
    with open("task_overview.txt") as f:
        count = 0
        count_complete = 0
        count_incomplete = 0
        complete_overdue = 0
        incomplete_perc = 0
        overdue_perc = 0
        today = str(date.today())
        new_list = to_list()
        
        current = today.replace("-", "")
        
        for inner_list in new_list:
            count += 1
            due = inner_list[3].replace("-", "")
            
            #Condtions that check whether tasks are complete or incomplete and overdue
            if inner_list[-1] == "No":
                count_incomplete += 1
            elif inner_list[-1] == "Yes":
                count_complete += 1
            elif inner_list[-1] == "No" and int(current) > int(due):
                complete_overdue += 1
        
        #Calculating percenatges        
        incomplete_perc = (count_incomplete/count)*100
        overdue_perc = (complete_overdue/count)*100
        
        f = open("task_overview.txt", "w")
        
        f.write(str(count) + ", " +  str(count_complete) + ", " + str(count_incomplete)
                + ", " + str(incomplete_perc) + ", " + str(overdue_perc))
        
        f.close()
     
    return "All statistics have been successfully written to task_overview.txt"
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------
"""
Function that displays the data in the task overview text file in a friendly manner.
"""
def task_overview_display():
    
    with open("task_overview.txt") as f:
        
        f = open("task_overview.txt", "r")
        
        new_list = []
        
        for line in f:
           y = line.split(", ")
           new_list.append(y)
        f.close()
        
        for inner_list in new_list:
            print("Total number of tasks = " + inner_list[0])
            print("Total number of completed tasks = " + inner_list[1])
            print("Total number of uncompleted tasks = " + inner_list[2])
            print("The percentage of incomplete tasks = " + inner_list[3] + "%")
            print("The percentage of overdue tasks = " + inner_list[4] + "%")
            print()
            
    return ""
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
"""
Function that writes the user statistics to the user overview text file.
"""
def user_overview_write():
    
    with open("user.txt") as f:
        
        f = open("user.txt", "r")
        
        user_list = []
        new_list = to_list()
        today = str(date.today())
        current = today.replace("-", "")
        count_user = 0
        count_task = 0
        count_user1 = 0
        count_user2 = 0
        count_user3 = 0
        user1_complete = 0
        user2_complete = 0
        user3_complete = 0
        user1_incomplete = 0
        user2_incomplete = 0
        user3_incomplete = 0
        incomplete_overdue1 = 0
        incomplete_overdue2= 0
        incomplete_overdue3 = 0
        
        for line in f:
            info = line.split(", ")  #Converts data in f to lists
            user_list.append(info[0])
            
        for i in user_list:
            count_user += 1
            
        for inner_list in new_list:
           count_task += 1
           due = inner_list[3].replace("-", "")
        
        #Checking conditions for each registered user
        
           if user_list[1] in inner_list:
               count_user1 += 1
               if inner_list[-1] == "No":
                   user1_incomplete += 1
               elif inner_list[-1] == "Yes":
                   user1_complete += 1
               elif inner_list[-1] == "No" and int(current) > int(due):
                   incomplete_overdue1 += 1 
           
           if user_list[2] in inner_list:
               count_user2 += 1
               if inner_list[-1] == "No":
                   user2_incomplete += 1
               elif inner_list[-1] == "Yes":
                   user2_complete += 1
               elif inner_list[-1] == "No" and int(current) > int(due):
                   incomplete_overdue2 += 1 
               
           if user_list[3] in inner_list:
               count_user3 += 1
               if inner_list[-1] == "No":
                   user3_incomplete += 1
               elif inner_list[-1] == "Yes":
                   user3_complete += 1
               elif inner_list[-1] == "No" and int(current) > int(due):
                   incomplete_overdue3 += 1 
        
        #Calculating percentages           
        count_user1 = (count_user1/count_task)*100
        count_user2 = (count_user2/count_task)*100
        count_user3 = (count_user3/count_task)*100
        user1_complete = (user1_complete/count_task)*100
        user2_complete = (user2_complete/count_task)*100
        user3_complete = (user3_complete/count_task)*100
        user1_incomplete = (user1_incomplete/count_task)*100
        user2_incomplete = (user2_incomplete/count_task)*100
        user3_incomplete = (user3_incomplete/count_task)*100
        incomplete_overdue1 = (incomplete_overdue1/count_task)*100
        incomplete_overdue2 = (incomplete_overdue2/count_task)*100
        incomplete_overdue3 = (incomplete_overdue3/count_task)*100
        
        f.close()
        
        f = open("user_overview.txt", "w")
        
        f.write("Total number of registered users = " + str(count_user) + "\nTotal number of tasks = " + str(count_task) + "\n")
        f.write("\n")
        f.write(user_list[1] + ": Percentage of tasks assigned = " + str(count_user1) + "%, Percentage of completed tasks = " + 
                str(user1_complete) + "%, Percentage of incompleted tasks = " + str(user1_incomplete) + "%, Percentage of tasks that are incomplete and overdue = " + str(incomplete_overdue1) + "\n")
        f.write("\n")
        f.write(user_list[2] + ": Percentage of tasks assigned = " + str(count_user2) + "%, Percentage of completed tasks = " + 
                str(user2_complete) + "%, Percentage of incompleted tasks = " + str(user2_incomplete) + "%, Percentage of tasks that are incomplete and overdue = " + str(incomplete_overdue2) + "\n")
        f.write("\n")
        f.write(user_list[3] + ": Percentage of tasks assigned = " + str(count_user3) + "%, Percentage of completed tasks = " + 
                str(user3_complete) + "%, Percentage of incompleted tasks = " + str(user3_incomplete) + "%, Percentage of tasks that are incomplete and overdue = " + str(incomplete_overdue3) + "\n")
        f.write("\n")
        f.close()
        
        return "All statistics have been successfully written to user_overview.txt"
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
"""
Function that displays the data in the user overview text file in a friendly manner.
"""
def user_overview_display():

    with open("user_overview.txt", "r") as f:
        
        f = open("user_overview.txt", "r")
        
        read_file = f.read()
        
        f.close()
        
    return read_file        
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------

#BEGINNING OF THE PROGRAM!!
#Open user text file for reading
#Checking if the person trying to login is a registered user 
with open("user.txt", "r") as file:
    
    #Loop to check for the correct username and password
    incorrect_info = True
    while incorrect_info:
        
        user = input("Username: ")
        
        file = open("user.txt", "r")
        
        #Loop through all lines of user text file to see if the username is registered
        for line in file:
            info = line.split(", ")
            
            if user == info[0]:
                break
            
        if user == info[0]:
            while True:
                
                #If the username is valid, check for the correct password
                password = input("Password: ")
                
                if password == info[1].strip():
                    incorrect_info = False
                    break
                
                else:
                    print("Incorrect password, please try again")
                    
        else:
            print("Username does not exist")
            
        #Closes the user text file
        file.close()
 
#Outputs the menu options for admin and other registered users after succesful login
print("Please select one of the following options:")
if user == "admin":
    print("r - register user \n" + 
          "a - add task \n" + 
          "va - view all tasks \n" + 
          "vm - view my tasks \n" +
          "gr - generate reports \n" +
          "ds - display statistics \n" +
          "e - exit")      
else:
    print("r - register user \n" + 
          "a - add task \n" + 
          "va - view all tasks \n" + 
          "vm - view my tasks \n" + 
          "e - exit")  

#Initialising variable that will be used in task option loop
task = ""
new_list = to_list()

while task != "e":
    
    #Requests user to input which option on the menu they'd like to choose
    task = input("Enter your task option here: ")
    print()
    
    if task == "r":  #Registers new user in order for them to be able to login to the task manager
        if user != "admin":
            print("Only admin is allowed to register new users")
        else:
            print(reg_user())
   
    if task == "a":  #Assigns task details to user 
        print(add_task())
        
    if task == "va":  #Displays all the task assignments
        print(view_all())
        
    if task == "vm":  #Displays task assignments assigned to the user that logged in
        
        print(view_mine())
        
        user_choice1 = int(input("Enter which task you'd like to mark as complete or edit: "))
        user_choice2 = input("Would you like to mark as complete or edit: ")
        
        if user_choice2 == "mark as complete":
            print(mark_as_complete(user_choice1))
            
        elif user_choice2 == "edit":
            print(edit_the_task(user_choice1))
            
    if task == "gr":  #Generates user and task reports
       print(task_overview_write())
       print(user_overview_write())
       
    if task == "ds":  #Displays task and user statistics
        if user == "admin":
            print("Task statistics: \n")
            print(task_overview_display())
            print()
            print("User statistics: \n")
            print(user_overview_display())
        else:
            ("Only admin can generate reports")
            
#------------------------------------------------------------------------------       
            
        
        
            
            
        
        
    