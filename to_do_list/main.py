import sys

tasks = []

def input_task(option):
    print("Please enter the task you want to " + option + ":")
    return input()

#test
def add_task(item):
	tasks.append({"name": item, "done": False})

def add_item():
    item = input_task("add")
    add_task(item)
    
#test
def update_status(index):
	tasks[index]["done"] = True
    
def mark_as_done():
    item = input_task("mark as done")
    index = search_item(item)
    if index is not None:
        update_status(index)
    
#test
def search_item(item):
    for i, task in enumerate(tasks):
        if task["name"] == item:
            return i
    print("Item not found.")
    return None
        
#test
def remove_task(index):
    del tasks[index]        
        
def remove_item():
    item = input_task("remove")
    index = search_item(item)
    if index is not None:
        remove_task(index)
    
#test    
def show_list():
    if len(tasks) > 0:
        for i, task in enumerate(tasks, start=1):
            if task["done"]:
                status = " [X] "
            else:
                status = " [ ] "
            print(str(i) + ") " + status + task["name"])
    else:
        print("The list is empty.")
        
def show_options():
    print("Please select an option: ")
    print("1) Show list")
    print("2) Add item")
    print("3) Mark item as done")
    print("4) Remove item")
    print("5) Exit")
    
def execute_option(op):
	match op:
		case 1: show_list()
		case 2: add_item()
		case 3: mark_as_done()
		case 4: remove_item()
		case 5: sys.exit()

def menu():
    continue_op = 'y'
    while continue_op.lower() == 'y':
        show_options()
        op = int(input())
        execute_option(op)
        print("Do you want to continue? (Y/N)")
        continue_op = input()
    
def main():
    menu()

if __name__ == "__main__":
    main()