from Contact import Contact
from ContactList import ContactList
import unittest    

class TestPhonebookInsert(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestPhonebookInsert, self).__init__(*args, **kwargs)
        self.pb = ContactList()
    
    def test_1(self):
        c = Contact("2018-1799","Juan","Dela Cruz","Makata",
                    "M",63,12,677865)
        self.pb.insert(c)    
        self.assertEqual("Dela Cruz",self.pb.first().getLName())

    def test_2(self):
        c1 = Contact("2018-1799","Juan","Dela Cruz","Makata",
                    "M",63,12,677865)
        c2 = Contact("1950-1900","Maria","Clara","Binibini",
                    "F",63,10,189006)
        self.pb.insert(c1)
        self.pb.insert(c2)
        self.assertEqual(2, self.pb.getSize())
        self.assertEqual("Clara", self.pb.getContactAtIndex(0).getLName())
        self.assertEqual("Dela Cruz", self.pb.getContactAtIndex(1).getLName())
        self.assertEqual(None, self.pb.getContactAtIndex(2))

    def test_3(self):
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
        self.assertEqual(5, self.pb.getSize())
        self.assertEqual("Jose",self.pb.getContactAtIndex(3).getFName())
        self.assertEqual("Ahmed",self.pb.getContactAtIndex(2).getFName())
        self.assertEqual("Maria",self.pb.getContactAtIndex(0).getFName())
        self.assertEqual("Yin Xie",self.pb.getContactAtIndex(4).getFullName())

if __name__ == "__main__":
    unittest.main()
    
    