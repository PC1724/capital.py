import re

def abbreviate_text(text):
    # Function to abbreviate each word
    def abbreviate_match(match):
        word = match.group()
        if word.isalpha():
            if word.isupper():  # Leave already abbreviated words unchanged
                return word
            return word[0].upper()  # Return only the first letter, capitalized
        else:
            return word  # Keep punctuation or other non-alphabetic characters as is
    
    # Replace words using the abbreviate_match function
    result = re.sub(r'\w+', abbreviate_match, text)
    
    return result

# Example usage:
input_text = input("Enter your text: ")
output_text = abbreviate_text(input_text)
print("Abbreviated Output:", output_text)