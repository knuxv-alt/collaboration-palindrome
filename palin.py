import sys
import json
import os

def is_palindrome(word):
    # TODO: Implement palindrome check
    pass

def count_palindromes_paragraph(paragraph):
    # TODO: Count palindromes in a paragraph
    pass

def read_file(file_path):
    # TODO: Read the file and split it into paragraphs
    pass

def process_file(file_path):
    # TODO: Process a file and return the results
    pass

def save_results(results):
    # TODO: Save the results to a JSON file
    pass

def main(folder):
    results = {}
    # TODO: Loop through all files in the folder and process them
    
    # Display results in the terminal
    print(json.dumps(results, indent=2, ensure_ascii=False))
    
    # Save results to a JSON file
    save_results(results)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python palindrome_counter.py <folder_path>")
        sys.exit(1)
    
    folder = sys.argv[1]
    main(folder)
