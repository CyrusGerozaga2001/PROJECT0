from Contact import Contact
from ContactList import ContactList
import unittest    

class TestPhonebookSearch(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestPhonebookSearch, self).__init__(*args, **kwargs)
        self.pb = ContactList()

    def test_1(self):
        """Three contact test.
        """
        c1 = Contact("2018-1799","Juan","Dela Cruz","Makata",
                    "M",63,12,677865)
        c2 = Contact("1950-1900","Maria","Clara","Binibini",
                    "F",63,10,189006)
        c3 = Contact("1968-1940","Joseph","Joestar","Stand User",
                    "M",84,20,174265)
        self.pb.insert(c1)
        self.pb.insert(c2)
        self.pb.insert(c3)
        self.pb.deleteContact("2018-1799")
        self.assertEqual(2, self.pb.getSize())
        self.assertEqual("Joseph Joestar", self.pb.getContactAtIndex(1).getFullName())

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
        self.pb.deleteContact("1950-1900")
        self.pb.deleteContact("1950-6525")
        self.assertEqual(3, self.pb.getSize())
        self.assertEqual("Jose Rizal", self.pb.getLast().getFullName())
        self.assertEqual("Joaquin Jacinto", self.pb.first().getFullName())

if __name__ == "__main__":
    unittest.main()