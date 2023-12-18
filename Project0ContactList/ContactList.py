# Singly Linked List implementation of contacts
from Contact import Contact
from typing import List


class ContactList:
    """Contact List class that creates a singly linked list phonebook.
    """

    class ContactNode:

        def __init__(self, item: Contact, ptr):
            self.item = item
            self.ptr = ptr

        def getVal(self) -> Contact:
            """Get the contact value of this node.

            Returns:
                Contact: Contact of the student.
            """
            return self.item

        def next(self) -> 'ContactList.ContactNode':
            """Gets the node pointer of this node.

            Returns:
                ContactList.ContactNode: The node connected to this node.
            """
            return self.ptr

        def setNext(self, node: 'ContactList.ContactNode'):
            """Sets a new pointer for this node

            Args:
                node (ContactList.ContactNode): New node pointer.
            """
            self.ptr = node

        def setVal(self, c: Contact):
            """Sets the contact value of this node.

            Args:
                c (Contact): New contact value.
            """
            self.item = c

    def __init__(self):
        self.sentinel = ContactList.ContactNode(None, None)
        self.size = 0

    def getSize(self):
        """
            Get the size of this contact list.
        """
        return self.size

    def first(self) -> Contact:
        """
            Get the first contact in this contact list.
            Returns none if the list is empty.
        """
        if self.sentinel.next() is not None:
            return self.sentinel.next().getVal()
        else:
            return None

    def getLast(self) -> Contact:
        """
            Get the last contact in this contact list.
            Returns none if the list is empty.
        """
        current = self.sentinel
        while current.next() is not None:
            current = current.next()
        if current != self.sentinel:
            return current.getVal()
        else:
            return None

    def getContactAtIndex(self, index: int) -> Contact:
        """Gets the contact at the given index in the contact linked list.
        Returns None if the index is not found in the list.

        Args:
            index (int): Index to get in the contact linked list.

        Returns:
            Contact: Contact at index.
        """
        current = self.sentinel.next()
        count = 0
        while current is not None:
            if count == index:
                return current.getVal()
            current = current.next()
            count += 1
        return None

    def getContact(self, student_num: str) -> Contact:
        """Gets the contact based on the given student number. Will return None
        if the contact is not found.

        Args:
            student_num (str): Student number to base the search from.

        Returns:
            Contact: Contact information.
        """
        current = self.sentinel.next()
        while current is not None:
            if current.getVal().getStudentNumber() == student_num:
                return current.getVal()
            current = current.next()
        return None

    def getContactBySurname(self, surname: str, f=None) -> Contact:
        """Gets the contact based on surname. Will return None if contact is not found.

        Args:
            surname (str): Surname to search for.
            f (list, optional): A list that filters which contact should
                be outputted based on country codes. Defaults to None.

        Returns:
            Contact: Contact information.
        """
        current = self.sentinel.next()
        while current is not None:
            contact = current.getVal()
            if contact.getLName() == surname and (f is None or contact.getNumericCountryCode() in f):
                return contact
            current = current.next()
        return None

    def isEmpty(self) -> bool:
        """
            Checks if the contact list has no contacts.
        """
        return self.getSize() == 0

    def incrSize(self) -> None:
        """
            Increase the size of this contact list.
        """
        self.size += 1

    def decrSize(self) -> None:
        """
            Decrease the size of this contact list.
        """
        self.size -= 1

    def insert(self, c: Contact) -> None:
        """Inserts new contact to the phonebook.

        Args:
            c (Contact): Contact to be inserted.
        """
        insertion_point = self.__findNodeInsertion(c)

        new_node = ContactList.ContactNode(c, insertion_point.next())
        insertion_point.setNext(new_node)

        self.incrSize()

        print("Contact successfully added to the ASEAN Phonebook!")

    def __findNodeInsertion(self, c: Contact) -> 'ContactList.ContactNode':
        """Finds the node to insert from based on contact's
        last name, and first name if both have the same first names.

        Args:
            c (Contact): Contact to compare and to be inserted.

        Returns:
            ContactList.ContactNode: Node insertion point for a new contact.
        """
        current = self.sentinel

        while current.next() is not None and Contact.compareNames(c, current.next().getVal()) == 1:
            current = current.next()

        while current.next() is not None and Contact.compareNames(c, current.next().getVal()) == 0:
            if Contact.compareNames(c, current.next().getVal(), comparison_type=1) == -1:
                break
            current = current.next()

        return current
    def getContactByCountryCode(self, country_code: int) -> List[Contact]:
        """Gets contacts from the specified country code.

        Args:
            country_code (int): Numeric country code.

        Returns:
            List[Contact]: List of contacts from the specified country code.
        """
        contacts_from_country = []
        current = self.sentinel.next()

        while current is not None:
            if current.getVal().getNumericCountryCode() == country_code:
                contacts_from_country.append(current.getVal())
            current = current.next()

        return contacts_from_country
    
    @staticmethod
    def prompt(phrase: str) -> str:
        """Prompts an input to the user

        Args:
            phrase (str): Input phrase.

        Returns:
            str: Returns a string type of inputted value.
        """
        return input(phrase)


    def deleteContact(self, stdn: str) -> Contact:
        """Finds a contact based on their student number.
        Returns the deleted contact. Otherwise, returns None if not found.

        Args:
            stdn (str): Student number of contact to be deleted.

        Returns:
            Contact: Deleted contact, if found.
        """
        current = self.sentinel

        while current.next() is not None:
            if current.next().getVal().getStudentNumber() == stdn:
                to_delete = current.next()
                
                # Confirmation prompt
                confirm_delete = self.prompt("Are you sure you want to delete this contact [Y/N]? ")
                
                if confirm_delete.upper() == 'Y':
                    current.setNext(to_delete.next())
                    to_delete.setNext(None)
                    self.decrSize()
                    return to_delete.getVal()
                else:
                    print("Contact deletion canceled.")
                    return -1
            
            current = current.next()

        print("Contact with student number {} not found.".format(stdn))
        return -1


    def __str__(self, f=None) -> str:
        """Prints every contact in this contact list.

        Args:
            f (list, optional): A list that filters which contact should
                be outputted based on country codes. Defaults to None.

        Returns:
            str: Every contact in this contact list.
        """
        s = "<----Phonebook---->"
        current = self.sentinel.next()

        while current is not None:
            contact = current.getVal()
            if f is None or contact.getNumericCountryCode() in f:
                s += "\n" + str(contact)
            current = current.next()

        if not self.isEmpty():
            print("")
        else:
            s += "\nThis phonebook is currently empty..."

        s += "\n<----End---->"
        return s
    
    def editContactSurname(self, student_num: str, new_surname: str) -> bool:
        """Edits the surname of a contact in the phonebook.

        Args:
            student_num (str): Student number of the contact to be edited.
            new_surname (str): New surname to be set.

        Returns:
            bool: True if the edit is successful, False otherwise.
        """
        contact = self.getContact(student_num)
        if contact is not None:
            old_surname = contact.setLName(new_surname)

            # Now, rearrange the phonebook based on the updated surname
            current = self.sentinel.next()
            prev = self.sentinel

            while current is not None and Contact.compareNames(contact, current.getVal()) == -1:
                prev = current
                current = current.next()

            # Update the links in the linked list to rearrange the phonebook
            prev.setNext(ContactList.ContactNode(contact, current))

            # If we're not at the end of the list, link the updated contact to the next node
            if current is not None:
                contact_node = ContactList.ContactNode(contact, current.next())
                current.setNext(contact_node)

            return True
        else:
            return False
        
    def __iter__(self):
        current = self.sentinel.next()
        while current is not None:
            yield current.getVal()
            current = current.next()