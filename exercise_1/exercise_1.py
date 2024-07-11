def option_menu():
    option = ""
    names = []
    
    while option != "0":
        print("==Select one of the following options==")
        print(">Press [1] for: import list_name file")
        print(">Press [2] for: show names")
        print(">Press [0] for: exit")
        
        option = input("Enter option: ")
        
        if option == "1":
            names = load_listname()
            if names:
                print("\n====>> Name list uploaded successfully\n")
            else:
                print("\n====>> Failed to upload name list\n")
        
        elif option == "2":
            if not names:
                print("\n====>> X First upload the file. Press [1]\n")
            else:
                show_listname(names)
        
        elif option == "0":
            print("\nBye!!\n")
        else:
            print("\nInvalid option. Please try again.\n")

def load_listname():
    try:
        with open('exercise_1/names.txt', 'r') as file:
            list_names = [name.strip() for name in file.readlines()]
        return list_names
    except FileNotFoundError:
        print("File not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def show_listname(list_names):
    count = 0
    for name in list_names:
        print(name)
        count += 1
        if count == 20:
            input("Press [Enter] to continue...")
            count = 0

if __name__ == "__main__":
    option_menu()
