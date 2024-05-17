#creating command line based applications
task=[]
def add_task(task):
  tasks.append(task)
  print(f" Yahhh!! Task '{task}' successfully added")
def update_task(task,index,new_task):
  if 0<=index<len(task):
    task[index]=new_task
    print(f" task at index {index}  updated to '{new_index}'")
  else:
    print("index is invalid")
def display_tasks():
  print("Tasks:")
  for index task in enumarate(tasks,start=1):
  print(f"{index}.{task}") 
#usage
add_task("complete the assingment before the deadline")
add_task("go to temple")
add_task("complete the course")
add_task("buy veggies")
display_tasks()
update_task(1,"finish assignment")
display_tasks()






  
