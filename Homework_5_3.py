def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a valid user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
        except Exception as e:
            return f"An unexpected error occurred: {e}."
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added successfully."


@input_error
def change_contact(args, contacts):
    
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone 
        return "Contact updated"
    else:
        return "Contact not found"

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]
    
@input_error
def show_all(contacts):
    if contacts:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip() 
    else:
        return "No contacts found" 
    

def parse_input(user_input):
    if not user_input.strip():
        return None, []  
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():

    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        
        if not user_input:  
            print("Please enter a command.")
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))  
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()  