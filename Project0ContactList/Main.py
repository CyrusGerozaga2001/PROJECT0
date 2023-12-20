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
    print("\n<-----Menu----->")
    i = 1 if inline != None else None
    for menu in MENUS[target]:
        out = "[{}]".format(menu)
        if inline != None and i == inline:
            out = "\n[{}]".format(menu)
        print("{} {}".format(out, MENUS[target][menu]), end= "\t" if inline != None else "\n")
        if i != None:
            i = 1 if i == inline else i + 1
        
def receiveContactInfo() -> Contact:
    """Cast several prompts for user to input about the
    contact's data.

    Returns:
       Contact: Contact object created based from data.
    """
    stdn = prompt("Enter student number: ")    
    lname = prompt("Enter surname: ")
    fname = prompt("Enter first name: ")
    occupation = prompt("Enter occupation: ")
    gender = prompt("Enter gender (M for male, F for female): ")
    cc = int(prompt("Enter country code: "))
    area = int(prompt("Enter area code: "))
    number = int(prompt("Enter number: "))
    return Contact(stdn,fname,lname,occupation,gender,cc,area,number)

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

        # Complete your code here
        if opt == 1:
            # Store to ASEAN Phonebook
            while True:
                contact = receiveContactInfo()
                pb.insert(contact)
                print("Contact added to the phonebook.")
                add_another = input("Do you want to another entry? [Y/N]: ").lower()
                if add_another != "y":
                    break  # Exit the loop if the user doesn't want to add another entry

        elif opt == 2:
            # Edit entry in ASEAN Phonebook
            student_num = prompt("Enter student number to edit: ")
            contact = pb.getContact(student_num)

            if contact is not None:
                showMenu("edit")
                edit_opt = int(input("Select what to edit: "))
                    
                if edit_opt == 1:
                    new_stdn = prompt("Enter new student number: ")
                    contact.setStudentNumber(new_stdn)

                elif edit_opt == 2:
                    new_surname = prompt("Enter new surname: ")
                    contact.setLName(new_surname)

                elif edit_opt == 3:
                    new_gender = prompt("Enter new gender (M for male, F for female): ")
                    contact.setGender(new_gender)

                elif edit_opt == 4:
                    new_occupation = prompt("Enter new occupation: ")
                    contact.setOccupation(new_occupation)

                elif edit_opt == 5:
                    new_cc = int(input("Enter new country code: "))
                    contact.setCountryCode(new_cc)

                elif edit_opt == 6:
                    new_area = int(input("Enter new area code: "))
                    contact.setAreaCode(new_area)

                elif edit_opt == 7:
                    new_number = int(input("Enter new phone number: "))
                    contact.setContactNumber(new_number)

                elif edit_opt == 8:
                    # None - Go back to the main menu
                    pass

                else:
                    print("Invalid option. Please try again.")
                    
            else:
                print("Contact not found.")

        elif opt == 3:
            # Delete entry from ASEAN Phonebook
            student_num = prompt("Enter student number to delete: ")
            deleted_contact = pb.deleteContact(student_num)

            if deleted_contact != -1:
                print("Contact deleted:")
                print(deleted_contact)
            else:
                print("Contact not found.")

        elif opt == 4:
            # View/Search ASEAN Phonebook
            showMenu("views")
            view_opt = int(input("Select view/search option: "))

            if view_opt == 1:
                # Search by country
                showMenu("cc", inline=3)
                choices = convertChoices(list(map(int, input("\nSelect country code(s): ").split())))

                # Get contacts based on selected country code(s)
                contacts_found = [pb.getContactAtIndex(index) for index in range(pb.getSize())
                                  if pb.getContactAtIndex(index).getNumericCountryCode() in choices]

                # Bubble sort contacts alphabetically by last name
                n = len(contacts_found)
                for i in range(n):
                    for j in range(0, n-i-1):
                        current_contact = contacts_found[j]
                        next_contact = contacts_found[j+1]

                        if current_contact.getLName() > next_contact.getLName() or \
                            (current_contact.getLName() == next_contact.getLName() and current_contact.getFName() > next_contact.getFName()):
                            # Swap if the last name is greater or if the last names are equal, compare first names
                            contacts_found[j], contacts_found[j+1] = contacts_found[j+1], contacts_found[j]

                # Print sorted contacts
                for contact in contacts_found:
                    print(contact)

                if not contacts_found:
                    print(f"No contacts found for the selected country code(s).")


            elif view_opt == 2:
                # Search by surname
                surname_to_search = prompt("Enter surname to search: ")

                # Get contacts with the matching surname
                matching_contacts = []
                for i in range(pb.getSize()):
                    contact = pb.getContactAtIndex(i)
                    if contact.getLName().lower() == surname_to_search.lower():
                        matching_contacts.append(contact)

                if matching_contacts:
                    # Bubble sort matching contacts alphabetically by last name and first name
                    n = len(matching_contacts)
                    for i in range(n):
                        for j in range(0, n-i-1):
                            current_contact = matching_contacts[j]
                            next_contact = matching_contacts[j+1]

                            if current_contact.getLName() > next_contact.getLName() or \
                               (current_contact.getLName() == next_contact.getLName() and current_contact.getFName() > next_contact.getFName()):
                                # Swap if the last name is greater or if the last names are equal, compare first names
                                matching_contacts[j], matching_contacts[j+1] = matching_contacts[j+1], matching_contacts[j]

                    # Print sorted contacts with the matching surname
                    for contact in matching_contacts:
                        print(contact)
                else:
                    print(f"No contacts found with the surname '{surname_to_search}'.")

            elif view_opt == 3:
                # View all contacts and sort alphabetically by last name and first name
                all_contacts = [pb.getContactAtIndex(index) for index in range(pb.getSize())]

                # Bubble sort contacts alphabetically by last name and first name
                n = len(all_contacts)
                for i in range(n):
                    for j in range(0, n-i-1):
                        current_contact = all_contacts[j]
                        next_contact = all_contacts[j+1]

                        if current_contact.getLName() > next_contact.getLName() or \
                            (current_contact.getLName() == next_contact.getLName() and current_contact.getFName() > next_contact.getFName()):
                            # Swap if the last name is greater or if the last names are equal, compare first names
                            all_contacts[j], all_contacts[j+1] = all_contacts[j+1], all_contacts[j]

                # Print sorted contacts
                for contact in all_contacts:
                    print(contact)

            elif view_opt == 4:
                # Go back to main menu
                pass

            else:
                print("Invalid option. Please try again.")

        elif opt == 5:
            # Exit
            print("Exiting ASEAN Phonebook. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")