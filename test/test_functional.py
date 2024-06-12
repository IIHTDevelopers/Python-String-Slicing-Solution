import unittest
from string_ex import *
from string_ex import slicing, slice_deletion, reverse_string, tokenize_sentence, \
    extract_long_words, transform_extensions_to_lowercase, slice_with_skip, extract_domain, \
    search_and_manipulate_filenames  # Import slicing directly
from test.TestUtils import TestUtils

class TestStringFunctions(unittest.TestCase):
    def test_slicing(self):
        test_utils_instance = TestUtils()
        # Test input and expected output
        text = "thisismyworld"
        expected_result = "hi"

        # Call the slicing function from string_ex
        actual_result = slicing(text)

        # Remove trailing whitespaces from actual result
        actual_result = actual_result.rstrip()

        # Assertion using yakshaAssert
        try:
            test_utils_instance.yakshaAssert("TestSlicing", actual_result == expected_result, "functional")
            print("TestSlicing: Passed")
        except AssertionError as e:
            print("TestSlicing: Failed", e)
     def test_reverse_string(self):
        test_utils_instance = TestUtils()

        # Test input and expected output
        input_string = 'THEWORLDISMINE'
        reversed_string = reverse_string(input_string)
        expected_result = 'ENIMSIIDLOWEHT'

        # Assertion using yakshaAssert
        try:
            test_utils_instance.yakshaAssert("TestReverseString", reversed_string == expected_result, "functional")
            print("TestReverseString: Passed")
        except AssertionError as e:
            print("TestReverseString: Failed", e)
    def test_slice_deletion(self):
        test_utils_instance = TestUtils()

        # Test input and expected output
        original_text = "Delete the word"
        new_text = slice_deletion(original_text, 6, 12)
        expected_result = "Deleteord"

        # Assertion using yakshaAssert
        try:
            test_utils_instance.yakshaAssert("TestSliceDeletion", new_text == expected_result, "functional")
            print("TestSliceDeletion: Passed")
        except AssertionError as e:
            print("TestSliceDeletion: Failed", e)
    
    def test_tokenize_sentence(self):
        test_utils_instance = TestUtils()

        # Test input and expected output
        sentence = "I like working in my company"
        tokens = tokenize_sentence(sentence)
        expected_result = ['I', 'like', 'working', 'in', 'my', 'company']

        # Assertion using yakshaAssert
        try:
            test_utils_instance.yakshaAssert("TestTokenizeSentence", tokens == expected_result, "functional")
            print("TestTokenizeSentence: Passed")
        except AssertionError as e:
            print("TestTokenizeSentence: Failed", e)

    def test_extract_long_words(self):
        test_utils_instance = TestUtils()

        # Test input and expected output
        sentence = "I like to work with python code"
        min_length = 4
        long_words = extract_long_words(sentence, min_length)
        expected_result = ['python']

        # Assertion using yakshaAssert
        try:
            test_utils_instance.yakshaAssert("TestExtractLongWords", long_words == expected_result, "functional")
            print("TestExtractLongWords: Passed")
        except AssertionError as e:
            print("TestExtractLongWords: Failed", e)

    def test_transform_extensions_to_lowercase(self):
        test_utils_instance = TestUtils()

        # Test input and expected output
        extensions = [".TXT", ".jpg", ".PNG", ".html"]
        transformed_extensions = transform_extensions_to_lowercase(extensions)
        expected_result = [".txt", ".jpg", ".png", ".html"]

        # Assertion using yakshaAssert
        try:
            test_utils_instance.yakshaAssert("TestTransformExtensionsToLowercase",
                                             transformed_extensions == expected_result, "functional")
            print("TestTransformExtensionsToLowercase: Passed")
        except AssertionError as e:
            print("TestTransformExtensionsToLowercase: Failed", e)

    def test_slice_with_skip(self):
        test_utils_instance = TestUtils()

        # Test input and expected output
        text = "abcdefghij"
        skip = 2
        result = slice_with_skip(text, skip)
        expected_result = "acegi"

        # Assertion using yakshaAssert
        try:
            test_utils_instance.yakshaAssert("TestSliceWithSkip", result == expected_result, "functional")
            print("TestSliceWithSkip: Passed")
        except AssertionError as e:
            print("TestSliceWithSkip: Failed", e)

    def test_extract_domain(self):
        test_utils_instance = TestUtils()

        # Test input and expected output
        email = "user@yaksha.com"
        domain = extract_domain(email)
        expected_result = "yaksha.com"

        # Assertion using yakshaAssert
        try:
            test_utils_instance.yakshaAssert("TestExtractDomain", domain == expected_result, "functional")
            print("TestExtractDomain: Passed")
        except AssertionError as e:
            print("TestExtractDomain: Failed", e)

    def test_search_and_manipulate_filenames(self):
        test_utils_instance = TestUtils()

        # Test input and expected output
        filenames = ["document1.docx", "document2.docx", "report.docx", "presentation.pptx"]
        substring = ".docx"
        replacement = ".pdf"
        manipulated_filenames = search_and_manipulate_filenames(filenames, substring, replacement)
        expected_result = ["document1.pdf", "document2.pdf", "report.pdf", "presentation.pptx"]

        # Assertion using yakshaAssert
        try:
            test_utils_instance.yakshaAssert("TestSearchAndManipulateFilenames",
                                             manipulated_filenames == expected_result, "functional")
            print("TestSearchAndManipulateFilenames: Passed")
        except AssertionError as e:
            print("TestSearchAndManipulateFilenames: Failed", e)
if __name__ == '__main__':
    unittest.main()
