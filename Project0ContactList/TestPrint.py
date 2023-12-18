from Contact import Contact
from ContactList import ContactList
import unittest    

class TestPhonebookSearch(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestPhonebookSearch, self).__init__(*args, **kwargs)
        self.pb = ContactList()

    def test_1(self):
        """One contact test.
        """
        c = Contact("2018-1799","Juan","Dela Cruz","Makata",
                    "M",63,12,677865)
        self.pb.insert(c)
        s = "<----Phonebook---->"
        s += "\n{}".format(self.pb.getContactAtIndex(0).__str__())
        s += "\n<----End---->"
        self.assertEqual(s, self.pb.__str__())

    def test_2(self):
        """Five contact test
        """
        c1 = Contact("2018-1799","Jose","Rizal","Hero","M",63,
                     63,22922)
        c2 = Contact("1999-6742","Joaquin","Jacinto","Person","M",60,
                     98,67251)
        c3 = Contact("1950-6525","Yin","Xie","Gamer","M",84,
                     45,66771)
        c4 = Contact("1950-1900","Maria","Clara","Binibini","F", 84,
                     63,12991)
        c5 = Contact("1770-6259","Ahmed","Rizal","Poser","M",63,
                     67,17651)
        self.pb.insert(c1)
        self.pb.insert(c2)
        self.pb.insert(c4)
        self.pb.insert(c3)
        self.pb.insert(c5)
        s = "<----Phonebook---->"
        s += "\n{}".format(self.pb.getContactAtIndex(0).__str__())
        s += "\n{}".format(self.pb.getContactAtIndex(1).__str__())
        s += "\n{}".format(self.pb.getContactAtIndex(2).__str__())
        s += "\n{}".format(self.pb.getContactAtIndex(3).__str__())
        s += "\n{}".format(self.pb.getContactAtIndex(4).__str__())
        s += "\n<----End---->"
        self.assertEqual(s, self.pb.__str__())

    def test_3(self):
        """Zero Contact Test
        """
        s = "<----Phonebook---->"
        s += "\nThis phonebook is currently empty..."
        s += "\n<----End---->"
        self.assertEqual(s, self.pb.__str__())

if __name__ == "__main__":
    unittest.main()