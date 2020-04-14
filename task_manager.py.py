#This is a pythonn program for a small business
import datetime
import os

#Import necessary modules
#Create a menu with choices to select from and define each selection

def choices():
    print("You are logged in. Welcome to the program!")
    print("Please select one option from below")
    choice = input("r - register user\n a - add tasks\n va - view all task\n vm - view my tasks\n s - Statistics\n e - Exit\n")
    if choice == "r" and userName == "admin":
        return register()
    elif choice == "a":
        return addTask()
    elif choice == "va":
        return viewAll_tasks()
    elif choice == "vm":
        return viewMy_tasks()
    elif choice == "s" and userName == "admin":
        return Statistics()
    else:
        return Exit()
     
 
#if user chooses "r", the admin gets to register a new user to the data base
def register():
    print("Register a new user")
    print("-------------------")
    name = str(input("Enter Username: "))
    password = str(input("Enter Password: "))
    f = open('user.txt','r')
    info = f.read()
    info = info.split(",")
    if name in info:
        return "Username already in use, please enter a different Username"
#write new registered user to the user text file
    else:
        f = open('user.txt','a')
        f.write("\n")
        f.write(name)
        f.write(",")
        f.write(password)
        f.write("\n")
        f.close()
        return "Registering user to data base" 

#If user choose "a" they add a task for an exixting user on the database
def addTask():
    print("Add a new task: ")
    print("----------------")
    name = input("Enter Username assigned to the task: ").lower()
    f = open('user.txt','r')
    info = f.read()
    info = info.split(",")
    
#Getting the user to assign the task to the user in the data base an setting due dates
    if name in info:
        taskTitle = input("Enter title for the task: ")
        taskDescription = input("Enter task description: ")
        taskDueDate = input("Enter due date for the task: (yyy-mm-dd)")
        taskSignOnDate = datetime.datetime.now()
        print(taskSignOnDate.strftime('%Y-%m-%d'))
        taskCompleted = "no"
        taskFile = open('tasks.txt','a+')
        tasks = ("\nUser assigned to task: " + count + "\n " + name + "\nTask Title: " +"\n" + taskTitle + "\n" + "Task Description:\n"+ taskDescription + "\n" + "Task Due Date:\n" + str(taskDueDate) + "\n" + "Date Signed:\n" + str(taskSignOnDate) + "\n" + "Task Completed:\n" + taskCompleted + "\n")
        taskFile.write(tasks)
        taskFile.close()
        return "Writing to file"
    else:
         return "Username entered is not on data base"

#If user chooses "va",they view all tasks in the database
def viewAll_tasks():
    print("Here is a list of all the tasks in the database: ")
    print("--------------------------------------------------")
    print("Username" +5*"" + "Title" + 15*"" + "Description" +50*"" + "Due Date" + 50*"" + "Assigned Date" + 5*"" + "Completed")
    taskList = open('tasks.txt','r')
    tasks = taskList.read()
    tasks = tasks.split()
    print(tasks[0] + (12-len(tasks[0]))*" "+
          tasks[1] + (20-len(tasks[1]))*" "+
          tasks[2] + (61-len(tasks[2]))*" "+
          tasks[3] + (13-len(tasks[1]))*" "+
          tasks[4] + (18-len(tasks[1]))*" "+
          tasks[5])

#If user chooses "vm" they view all tasks assigned to them
def viewMy_tasks():
    print("Here are the tasks assigned to your Username: ")
    print("----------------------------------------------")
    print("Task" + 5*"" + "Title" + 15*"" + "Description" + 50* "" + "Due Date" + 5* "" + "Assigned Date" + 5* "" + "Completed")
    print("-"*134)
    count = 0
    name = open('user.txt','r')
    user = name.read()
    user = name.split()
    tasks = open('tasks.txt','r')
    userTask = tasks.read()
    userTask = userTask.split()
    if user == userTask[0]:
        print(str(count+1)+ (8-len(str(count+1)))*" "+
            taskItems[0] + (12-len(taskItems[0]))*" "+
            taskItems[1] + (20-len(taskItems[1]))*" "+
            taskItems[2] + (61-len(taskItems[2]))*" "+
            taskItems[3] + (13-len(taskItems[1]))*" "+
            taskItems[4] + (18-len(taskItems[1]))*" "+
            taskItems[5])
        count += 1

    else:
        #count == 0:
            return "There are no tasks assigned to your username"

#If admin chooses "s" they view all statistics in the database
def Statistics():
    print("Statistics")
    print("----------")
    f = open('user.txt','r')
    user = f.read()
    file = open('tasks.txt','r')
    tasks = file.read()
    userCount = 0
    tasksCount = 0
    for task in tasks:
        tasksCount +=1
    for users in user:
        userCount +=1
        print("The total number of tasks listed is :" + str(tasksCount)+ " tasks")
        print("The total number of users registered is :" + str(userCount)+ " users.")
        
def Exit():
    print("Goodbye")
    exit()

    
#Logging in and getting the program to start     
users = {}
with open('user.txt','rt')as username:
    for line in username:
        username,password = line.split(",")
        users[username.strip()] = password.strip()

userName = input("Enter your username:\n")
if username not in users:
    print("Username incorrect")
    userName = input("Enter correct username: \n")

if userName in users:
    print("Username correct")

    with open('user.txt','rt') as password:
        for line in password:
            username,password = line.split(",")
            users[password.strip()]= username.strip()
            
passWord = input("Enter your password: \n")
if passWord not in users:
    print("Incorrect password")
    passWord = input("Enter correct password: \n")

if passWord in users:
    print("Correct password")

print(choices())                    



    
        














          
    
    






                 
    
                     
