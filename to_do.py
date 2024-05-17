#creating command line based applications
tasks=[]
def add_task(task):
  tasks.append(task)
  print(f" Yahhh!! Task '{task}' successfully added")
def update_task(index,new_task):
  if 0<=index<len(tasks):
    tasks[index]=new_task
    print(f" task at index {index}  updated to '{new_task}'")
  else:
    print("index is invalid")
def display_tasks():
  print("Tasks:")
  for index,task in enumerate(tasks,start=1):
    print(f"{index}.{task}") 
def remove_task(task):
  tasks.remove(task)
  print(f"Task '{task}' is removed successfully")
#usage
add_task("complete the assingment before the deadline")
add_task("go to temple")
add_task("complete the course")
add_task("buy veggies")
display_tasks()
update_task(1,"finish assignment")
display_tasks()
remove_task("complete the course")
display_tasks()






  
