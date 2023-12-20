# Singly Linked List implementation of contacts
from Contact import Contact


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
        
        def setVal(self, c : Contact):
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
            Returns none if list is empty.
        """
        # Complete this method
        if self.isEmpty():
            return None
        else:
            return self.sentinel.next().getVal()
    
    def getLast(self) -> Contact:
        """
            Get the last contact in this contact list.
            Returns none if list is empty.
        """
        # Complete this method
        if self.isEmpty():
            return None
        else:
            current = self.sentinel.next()
            while current.next() is not None:
                current = current.next()
            return current.getVal()

    def getContactAtIndex(self, index: int) -> Contact:
        """Gets the contact at given index in the contact linked list.
        Returns None if index is not found in the list.

        Args:
            index (int): Index to get in the contact linked list.

        Returns:
            Contact: Contact at index.
        """
        # Complete this method
        if index < 0 or index >= self.size:
            return None

        current = self.sentinel.next()
        for _ in range(index):
            current = current.next()

        return current.getVal()
    
    def getContact(self, identifier: str) -> Contact:
        """Gets the contact based on given student number. Will return None
        if contact is not found.

        Args:
            student_num (str): Student number to base search from.

        Returns:
            Contact: Contact information.
        """  
        # Complete this method      
        current = self.sentinel.next()
        while current is not None:
            if current.getVal().getStudentNumber() == identifier or current.getVal().getNumericCountryCode() == int(identifier):
                return current.getVal()
            current = current.next()

        return None
    
    def getContactBySurname(self, surname: str) -> Contact:
        """Gets the contact based on surname. Will return None if contact is not found.
        """
        # Complete this method
        current = self.sentinel.next()
        while current is not None:
            if current.getVal().getLName() == surname:
                return current.getVal()
            current = current.next()

        return None
    
    def isEmpty(self) -> bool:
        """
            Checks if contact list has no contacts.
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

    def insert(self, c : Contact):
        """Inserts new contact to the phonebook.

        Args:
            c (Contact): Contact to be inserted.
        """
        # Complete this method
        new_node = ContactList.ContactNode(c, None)

        if self.isEmpty():
            self.sentinel.setNext(new_node)
        else:
            current = self.sentinel.next()
            prev = self.sentinel

            while current is not None and c.compareNames(current.getVal(), c) < 0:
                prev = current
                current = current.next()

            prev.setNext(new_node)
            new_node.setNext(current)

        self.incrSize()

    def __findNodeInsertion(self, c: Contact) -> ContactNode:
        """Finds the node to insert from based on contact's
        last name, and first name if both have the same first names.

        Args:
            c (Contact): Contact to compare and to be inserted.

        Returns:
            ContactNode: Node insertion point for new contact.
        """
        # Complete this method
        current = self.sentinel.next()
        prev = self.sentinel

        while current is not None and c.compareNames(current.getVal(), c) < 0:
            prev = current
            current = current.next()

        return prev
    
    def deleteContact(self, stdn: str) -> Contact:
        """Finds a contact based on their student number.
        Returns the deleted contact. Otherwise, returns -1 if not found.

        Args:
            stdn (str): Student number of contact to be deleted.

        Returns:
            Contact: Deleted contact, if found.
        """
        # Complete this method
        current = self.sentinel.next()
        prev = self.sentinel

        while current is not None and current.getVal().getStudentNumber() != stdn:
            prev = current
            current = current.next()

        if current is not None:
            prev.setNext(current.next())
            deleted_contact = current.getVal()
            self.decrSize()
            return deleted_contact

        return -1
        
    def __str__(self, f = None) -> str:
        """Prints every contact in this contact list.

        Args:
            f (list, optional): A list that filters which contact should
                be outputted. Defaults to None.

        Returns:
            str: Every contact in this contact list.
        """
        # Complete this method
        s = "<----Phonebook---->"
        current = self.sentinel.next()

        if f is not None:
            # Print contacts based on selected country code(s)
            while current is not None:
                if current.getVal().getNumericCountryCode() in f:
                    s += "\n" + str(current.getVal())
                current = current.next()
        else:
        # Print all contacts
            while current is not None:
                s += "\n" + str(current.getVal())
                current = current.next()

            if self.isEmpty():
            # Complete this method.
                s += "\nThis phonebook is currently empty..."

        s += "\n<----End---->"
        return s
    
