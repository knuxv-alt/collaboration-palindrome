import sys
from typing import List, Dict
import re
from unidecode import unidecode
#Commentaire
#Test Fiona
def read_file(file_path: str) -> str:

    # TODO: Read the file and return its content as a string
    with open(file_path, 'r', encoding='utf-8') as file:
        txt = file.read()
    if txt == "":
        raise ValueError('file is empty')
    return txt

def split_into_paragraphs(text: str) -> List[str]:
    paragraphs = text.split("\n\n")

    return [p.strip() for p in paragraphs if p]

def is_palindrome(word: str) -> bool:
    word = unidecode(word.lower())
    if len(word) <2:
        return False
    return word == word[::-1]

def count_palindromes(paragraph: str) -> List[str]:
    lst_palindrome =[]
    words = re.findall(r"\w+", paragraph.lower())
    for word in words: 
        if is_palindrome(word=word):
                lst_palindrome.append(word)
    return lst_palindrome

def process_file(file_path: str) -> Dict[int, List[str]]:
    content = read_file(file_path)
    paragraphs = split_into_paragraphs(content)
    palindromes_by_paragraph = {}
    for i, paragraph in enumerate(paragraphs, 1):
        palindromes = count_palindromes(paragraph=paragraph)
        if palindromes:
            palindromes_by_paragraph[i] = palindromes
        else:
            palindromes_by_paragraph[i] = "No Palindrome"

    return palindromes_by_paragraph

def main(file_path: str) -> None:
    results = process_file(file_path)
    
    # Print results in a readable format
    for paragraph_num, palindromes in results.items():
        print(f"Paragraph {paragraph_num}:")
        if palindromes != "No Palindrome":
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
