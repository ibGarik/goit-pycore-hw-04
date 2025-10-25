def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact '{name}' not found."

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact '{name}' not found."

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ").strip()

        if not user_input:
            print("Invalid command. Please enter a command.")
            continue
            
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
            
        elif command == "add":
            try:
                print(add_contact(args, contacts))
            except ValueError:
                print("Invalid command. Usage: add [name] [phone]")
                
        elif command == "change":
            try:
                print(change_contact(args, contacts))
            except ValueError:
                print("Invalid command. Usage: change [name] [new_phone]")
                
        elif command == "phone":
            try:
                print(show_phone(args, contacts))
            except IndexError:
                print("Invalid command. Usage: phone [name]")
                
        elif command == "all":
            print(show_all(contacts))
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()