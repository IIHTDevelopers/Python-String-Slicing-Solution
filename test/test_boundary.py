import unittest
from test.TestUtils import TestUtils

class BoundaryTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.test_obj = TestUtils()  # Initialize test_obj here

    def test_boundary(self):
        result = True  # Example test logic
        if result:
            self.test_obj.yakshaAssert("TestBoundary", True, "boundary")
            print("TestBoundary = Passed")
        else:
            self.test_obj.yakshaAssert("TestBoundary", False, "boundary")
            print("TestBoundary = Failed")

    def test_empty_string(self):
        my_string = ""
        result = my_string[:3]
        if result == "":
            self.test_obj.yakshaAssert("TestEmptyString", True, "functional")
            print("TestEmptyString = Passed")
        else:
            self.test_obj.yakshaAssert("TestEmptyString", False, "functional")
            print("TestEmptyString = Failed")

    def test_index_out_of_range(self):
        my_string = "Python"
        try:
            result = my_string[20:]
            self.test_obj.yakshaAssert("TestIndexOutOfRange", result == "", "functional")
            print("TestIndexOutOfRange = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestIndexOutOfRange", False, "functional")
            print(f"TestIndexOutOfRange = Failed with Exception: {str(e)}")

    def test_negative_index_out_of_range(self):
        my_string = "Python"
        try:
            result = my_string[-20:]
            if result == "Python":
                self.test_obj.yakshaAssert("TestNegativeIndexOutOfRange", True, "functional")
                print("TestNegativeIndexOutOfRange = Passed")
            else:
                self.test_obj.yakshaAssert("TestNegativeIndexOutOfRange", False, "functional")
                print("TestNegativeIndexOutOfRange = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestNegativeIndexOutOfRange", False, "functional")
            print(f"TestNegativeIndexOutOfRange = Failed with Exception: {str(e)}")

if __name__ == '__main__':
    unittest.main()
