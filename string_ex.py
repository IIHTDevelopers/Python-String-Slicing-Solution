

def slicing(text):
    return text[1:3]
actual_result = slicing("this is my world")
print(actual_result)

def slice_deletion(text, start, end):
    # Combine the slices before and after the deleted portion
    return text[:start] + text[end:]

# Example usage
original_text = "Delete the word"
new_text = slice_deletion(original_text, 6, 12)
print(new_text)  # Output: "Deleteord"

def tokenize_sentence(sentence):
    # Split the sentence into words based on whitespace
    tokens = sentence.split()
    return tokens

# Example usage
sentence = "I like working in my company"
tokens = tokenize_sentence(sentence)
print("Tokens:", tokens)

def extract_long_words(sentence, min_length):
    # Split the sentence into words
    words = sentence.split()
    # Extract words longer than the specified length
    long_words = [word for word in words if len(word) > min_length]
    return long_words

# Example usage
sentence = "I like to work with python code"
min_length = 4
long_words = extract_long_words(sentence, min_length)
print("Words longer than {} characters:".format(min_length), long_words)

def transform_extensions_to_lowercase(extensions):
    transformed_extensions = []
    for extension in extensions:
        # Convert the extension to lowercase using string slicing
        transformed_extension = extension.lower()
        transformed_extensions.append(transformed_extension)
    return transformed_extensions

# Example usage
extensions = [".TXT", ".jpg", ".PNG", ".html"]
transformed_extensions = transform_extensions_to_lowercase(extensions)
print("Transformed Extensions:", transformed_extensions)

def slice_with_skip(string, skip):
    return string[::skip]

# Example usage
text = "abcdefghij"
skip = 2
result = slice_with_skip(text, skip)
print(result)  # Output: "acegi"

def extract_domain(email):
    # Find the position of '@' symbol
    at_index = email.find('@')

    # Slice the string to get the domain name
    domain = email[at_index + 1:]

    return domain

# Example usage
email = "user@yaksha.com"
domain = extract_domain(email)
print(domain)  # Output: example.com

def search_and_manipulate_filenames(filenames, substring, replacement):
    manipulated_filenames = []
    for filename in filenames:
        if substring in filename:
            # Replace the substring with the replacement using string slicing
            manipulated_filename = filename.replace(substring, replacement)
            manipulated_filenames.append(manipulated_filename)
        else:
            manipulated_filenames.append(filename)
    return manipulated_filenames

# Example usage
filenames = ["document1.docx", "document2.docx", "report.docx", "presentation.pptx"]
substring = ".docx"
replacement = ".pdf"
manipulated_filenames = search_and_manipulate_filenames(filenames, substring, replacement)
print("Manipulated Filenames:", manipulated_filenames)

def reverse_string(input_string):
    return input_string[::-1]

# Example usage
String = 'THEWORLDISMINE'
reversed_string = reverse_string(String)
print(reversed_string)
