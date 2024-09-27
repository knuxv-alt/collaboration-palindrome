import sys
from typing import List, Dict
#Commentaire

def read_file(file_path: str) -> str:
    # TODO: Read the file and return its content as a string
    with open(file_path, 'r', encoding='utf-8') as f:
        file = f.read()
    return file

def split_into_paragraphs(text: str) -> List[str]:
    # TODO: Split the text into paragraphs, a delimiter between two paragraphs is \n\n
    # Return a list of paragraphs
    pass

def is_palindrome(word: str) -> bool:
    word = word.lower()
    return word == word[::-1]

def count_palindromes(paragraph: str) -> List[str]:
    # TODO: Find all palindromes in a paragraph
    # Split paragraph into words (SpaCy, NLTK or regex) and check for each word
    # Return a list of palindromes
    pass

def process_file(file_path: str) -> Dict[int, List[str]]:
    content = read_file(file_path)
    paragraphs = split_into_paragraphs(content)
    palindromes_by_paragraph = {}
    for i, paragraph in enumerate(paragraphs, 1):
        words = paragraph.split()

        palindromes = count_palindromes(words)

        if palindromes:
            palindromes_by_paragraph[i] = palindromes

    return palindromes_by_paragraph

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
