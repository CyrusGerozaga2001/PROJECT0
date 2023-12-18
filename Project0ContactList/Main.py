# Main Python File to run from
from ContactList import ContactList
from Contact import Contact

MENUS = {
    "main": {
        1: "Store to ASEAN Phonebook",
        2: "Edit entry in ASEAN Phonebook",
        3: "Delete entry from ASEAN Phonebook",
        4: "View/Search ASEAN Phonebook",
        5: "Exit"
    },
    "views": {
        1: "Search by country",
        2: "Search by surname",
        3: "View all",
        4: "Go back to main menu"
    },
    "edit": {
        1: "Student Number",
        2: "Surname",
        3: "Gender",
        4: "Occupation",
        5: "Country Code",
        6: "Area Code",
        7: "Phone Number",
        8: "None - Go back to main menu"
    },
    "cc": {
        1: "Burma", # 856
        2: "Cambodia", # 855
        3: "Thailand", # 66
        4: "Vietnam", # 84
        5: "Malaysia", # 60
        6: "Philippines", # 63
        7: "Indonesia", # 62
        8: "Timor Leste", # 670
        9: "Laos", # 95
        10: "Brunei", # 673
        11: "Singapore", #65
        12: "All",
        0: "No More"
    }
}

def showMenu(target: str, inline :int = None):
    """Shows the target menu in the ASEAN Phonebook program.
    
    Args:
        target (str): Target menu to show. Refer to MENUS dictionary.
        inline (int): If not none, then will create an inline menu with n items each.
    """
    menu = MENUS[target]
    print("\n<-----Menu----->")
    i = 1 if inline is not None else None

    for option in menu:
        out = "[{}]".format(option)
        if inline is not None and i == inline:
            out = "\n[{}]".format(option)
        print("{} {}".format(out, menu[option]), end="\t" if inline is not None else "\n")
        if i is not None:
            i = 1 if i == inline else i + 1

    if target != "cc":
        print(f"Enter choice{'s' if inline is not None else ''}: ", end="")
        
def receiveContactInfo() -> Contact:
    """Cast several prompts for the user to input about the
    contact's data.

    Returns:
       Contact: Contact object created based on data.
    """
    contacts = []
    
    while True:
        stdn = prompt("Enter student number: ")    
        lname = prompt("Enter surname: ")
        fname = prompt("Enter first name: ")
        occupation = prompt("Enter occupation: ")
        gender = prompt("Enter gender (M for male, F for female): ")
        cc = int(prompt("Enter country code: "))
        area = int(prompt("Enter area code: "))
        number = int(prompt("Enter number: "))
        
        contacts.append(Contact(stdn, fname, lname, occupation, gender, cc, area, number))
        
        another_entry = prompt("Do you want to enter another entry [Y/N]? ")
        if another_entry.upper() != 'Y':
            break
    
    # If only one contact is entered, return that contact; otherwise, return a list of contacts
    return contacts[0] if len(contacts) == 1 else contacts
def searchByCountry(phonebook: ContactList):
    """Searches and displays students from selected countries.

    Args:
        phonebook (ContactList): The contact list to search in.
    """
    selected_countries = []

    while True:
        showMenu("cc", inline=3)
        choice = int(input("\nEnter choice {}: ".format(len(selected_countries) + 1)))

        if choice == 0:
            break
        elif choice == 12:
            selected_countries = list(Contact.COUNTRY_CODES.keys())  # ALL selected
            break
        elif choice in range(1, 12):
            selected_countries.append(choice)

    if not selected_countries:
        print("No countries selected.")
        return

    # Convert choices to country codes
    selected_countries = convertChoices(selected_countries)

    # Get contacts from selected countries
    filtered_contacts = []
    for country_code in selected_countries:
        filtered_contacts.extend(phonebook.getContactByCountryCode(country_code))

    # Sort contacts by surname alphabetically
    filtered_contacts.sort(key=lambda contact: contact.getLName())

    # Print the filtered contacts
    if filtered_contacts:
        print("Here are the students from the selected countries:")
        for contact in filtered_contacts:
            print(contact)
    else:
        print("No contacts found from the selected countries.")
    input("Press Enter to continue...")

@staticmethod
def prompt(phrase: str) -> str:
    """Prompts an input to the user

    Args:
        phrase (str): Input phrase.

    Returns:
        str : Returns a string type of inputted value.
    """
    return input(phrase)

def convertChoices(choices: list) -> list:
    """Converts choices from the phonebook menu
    into proper country code value for accuracy purposes.

    Args:
        choices (list): Choices selected by user during prompt.

    Returns:
        list: Converted values of choices.
    """
    for i in range(0, len(choices)):
        match choices[i]:
            case 1:
                choices[i] = 856
            case 2:
                choices[i] = 855
            case 3:
                choices[i] = 66
            case 4: 
                choices[i] = 84
            case 5:
                choices[i] = 60
            case 6:
                choices[i] = 63
            case 7:
                choices[i] = 62
            case 8:
                choices[i] = 670
            case 9:
                choices[i] = 95
            case 10:
                choices[i] = 673
            case 11:
                choices[i] = 65
    return choices
                

if __name__ == "__main__":
    pb = ContactList()
    while True:
        showMenu("main")
        opt = int(input("Select Operation: "))
        
        if opt == 1:  # Store to ASEAN Phonebook
            contacts = receiveContactInfo()
            if isinstance(contacts, Contact):  # Single contact
                pb.insert(contacts)
            elif isinstance(contacts, list):  # List of contacts
                for contact in contacts:
                    pb.insert(contact)
        
        elif opt == 2:  # Edit entry in ASEAN Phonebook
            showMenu("edit")
            edit_opt = int(input("Select field to edit: "))
            if edit_opt == 8:
                continue  # Go back to main menu
            student_num = prompt("Enter student number of the contact you want to edit: ")
            contact = pb.getContact(student_num)
            
            if contact is None:
                print("Contact not found.")
                continue
            
            new_value = prompt("Enter new value: ")
            
            if edit_opt == 1:
                contact.setStudentNumber(new_value)
            elif edit_opt == 2:
                contact.setLName(new_value)
            elif edit_opt == 3:
                contact.setGender(new_value)
            elif edit_opt == 4:
                contact.setOccupation(new_value)
            elif edit_opt == 5:
                contact.setCountryCode(int(new_value))
            elif edit_opt == 6:
                contact.setAreaCode(int(new_value))
            elif edit_opt == 7:
                contact.setContactNumber(int(new_value))
            
            print("Contact information updated successfully.")
        
        if opt == 3:  # Delete entry from ASEAN Phonebook
            stdn_to_delete = prompt("Enter the student number to delete: ")
            deleted_contact = pb.deleteContact(stdn_to_delete)
            if deleted_contact != -1:
                print("Contact successfully deleted from the ASEAN Phonebook!")
            else:
                print("")
        
        if opt == 4:  # View/Search ASEAN Phonebook
            showMenu("views")
            view_opt = int(input("Select view option: "))

            if view_opt == 1:  # Search by country
                searchByCountry(pb)
            elif view_opt == 2:  # Search by surname
                surname = input("Enter surname: ")
                contact = pb.getContactBySurname(surname)

                if contact is not None:
                    print(contact)
                else:
                    print("No contacts found with the specified surname.")
            elif view_opt == 3:  # View all
                print(pb)
            elif view_opt == 4:  # Go back to the main menu
                continue