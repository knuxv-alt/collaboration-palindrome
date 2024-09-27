import sys
from typing import List, Dict

def read_file(file_path: str) -> str:
    # TODO: Read the file and return its content as a string
    with open(file_path, 'r', encoding='utf-8') as file:
    return file
    pass

def split_into_paragraphs(text: str) -> List[str]:
    # TODO: Split the text into paragraphs, a delimiter between two paragraphs is \n\n
    # Return a list of paragraphs
    pass

def is_palindrome(word: str) -> bool:
    # TODO: Check if a word is a palindrome
    pass

def count_palindromes(paragraph: str) -> List[str]:
    # TODO: Find all palindromes in a paragraph
    # Split paragraph into words (SpaCy, NLTK or regex) and check for each word
    # Return a list of palindromes
    pass

def process_file(file_path: str) -> Dict[int, List[str]]:
    # TODO: Process a file and return the results
    # Read the file, split into paragraphs, count palindromes in each paragraph
    # Return a dictionary with paragraph numbers as keys and lists of palindromes as values
    pass

def main(file_path: str) -> None:
    results = process_file(file_path)
    
    # Print results in a readable format
    for paragraph_num, palindromes in results.items():
        print(f"Paragraph {paragraph_num}:")
        if palindromes:
            print(f"  Found {len(palindromes)} palindrome(s):")
            for palindrome in palindromes:
                print(f"    - {palindrome}")
        else:
            print("  No palindromes found.")
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python palindrome_counter.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    main(file_path)