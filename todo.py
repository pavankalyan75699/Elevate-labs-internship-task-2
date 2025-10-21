from datetime import datetime1


def load_tasks(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def todo_list():
    filename = "tasks.txt"
    tasks = load_tasks(filename)
    while True:
        print("1.add tasks")
        print("2.remove the tasks")
        print("3.view tasks")
        print("4.exit the tasks")
        choice=int(input("enter your choice:"))
        if choice==1:
              task=input("enter the task:")
              tasks.append(task)
              print("task added successfully")
        elif choice==2:
            if not tasks:
              print("no tasks to remove")
            else:
              task=input("enter the task to remove:")
              if task in tasks:
                tasks.remove(task)
                print("task removed successfully")
              else:
                print("task not found") 
        elif choice==3:
            if not tasks:
              print("no tasks to view")
            else:
              print("tasks:")
              for task in tasks:
                print("-"+task)     
        elif choice==4:
            print("exiting the program....BYEE")
            break
    else:
        print("invalid choice")
if __name__=="__main__":
    todo_list()     