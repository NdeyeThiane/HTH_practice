checklist = list()

def create(color):
    checklist.append(color)
    return f"Added {color} to checklist"

def read(index):
    return(checklist[index])
     
def update(color, index):

    old = checklist[index]
    checklist[index] = color
    return f"Changed {old} to {color}"

def destroy(index):
    removed = checklist[index]
    checklist.pop(index)
    return f"Removed {removed} from checklist"

def all_item():
    colors = list()
    
    for c in checklist:
        print(c)
        colors.append(c)
        return colors

def checked(index):
    unchecked = checklist[index]
    checklist[index] = '√ ' + unchecked
    return checklist[index]

def user_input(prompt):
    entry = input(prompt)

    return entry

def user_choice():
    editing = True
    while editing:

        choice = user_input("Choose one of this functions? C for create, R for read, U for update, D for destroy, A to view all items: ")

        if choice == "C" or choice == "c":

            color = user_input("Type the name of the item. ")

            create(color)

            continue

        elif choice == "R" or choice == "r":

            index = user_input("Enter the index number you want to read: ")

            read(int(index))

            continue

        elif choice == "U" or choice == "u":

            update_index = user_input("Enter the index numbber of the item you want to update: ")

            new_item = user_input("Enter new item: ")

            update(int(update_index), new_item)

            continue

        elif choice == "D" or choice == "d":

            delete_index = user_input("Enter the index number of the item you want to delete: ")

            destroy(int(delete_index))

            continue

        elif choice == "A" or choice == "a":


            all_item()

            continue

        elif choice == "S" or choice == "s":

            checked_index = user_input("Enter the index number of thhe item you want to check: ")

            checked(int(checked_index))

            continue

        else:

            end = user_input("Enter Y to quit N to contenue: ")

            if end == "Y" or end == "y":
                print(checklist)
                editing = False

            else:

                continue


def test():

    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(all_item())
    print(checked(0))
    user_choice()

user_choice()



test()