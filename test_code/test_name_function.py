from formatted_name import get_formatted_name
import unittest

class Name_Test_Case(unittest.TestCase):
    def test_first_lase_name(self):
        formatted_name=get_formatted_name("zeng","shuai")
        self.assertEqual(formatted_name,"Zeng Shuai")
    def test_first_middle_lase_name(self):
        formatted_name=get_formatted_name("zeng","shuai","wei")
        self.assertEqual(formatted_name,"Zeng Wei Shuai")

unittest.main()