import sys
from typing import List, Dict
import re
from unidecode import unidecode

def read_file(file_path: str) -> str:
    """
    Lit le contenu d'un fichier et le renvoie sous forme de chaîne de caractères.

    Args:
        file_path: Le chemin vers le fichier à lire.

    Returns:
        Le contenu du fichier sous forme de chaîne de caractères.

    Raises:
        ValueError: Si le fichier est vide.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        txt = file.read()
    if txt == "":
        raise ValueError('file is empty')
    return txt

def split_into_paragraphs(text: str) -> List[str]:
    """
    Sépare le texte fourni en paragraphes en fonction des doubles sauts de ligne.

    Args:
        text: Le texte à diviser en paragraphes.

    Returns:
        Une liste de paragraphes sans espaces supplémentaires.
    """
    paragraphs = text.split("\n\n")
    return [p.strip() for p in paragraphs if p]

def is_palindrome(word: str) -> bool:
    """
    Vérifie si un mot est un palindrome.

    Args:
        word: Le mot à vérifier.

    Returns:
        True si le mot est un palindrome, False sinon.
    """
    word = unidecode(word.lower())
    if len(word) < 2:
        return False
    return word == word[::-1]

def count_palindromes(paragraph: str) -> List[str]:
    """
    Trouve et compte tous les palindromes dans un paragraphe.

    Args:
        paragraph: Le paragraphe dans lequel rechercher des palindromes.

    Returns:
        Une liste de palindromes trouvés dans le paragraphe.
    """
    lst_palindrome = []
    words = re.findall(r"\w+", paragraph.lower())
    for word in words:
        if is_palindrome(word=word):
            lst_palindrome.append(word)
    return lst_palindrome

def process_file(file_path: str) -> Dict[int, List[str]]:
    """
    Traite le fichier, le divise en paragraphes, et trouve les palindromes dans chaque paragraphe.

    Args:
        file_path: Le chemin vers le fichier à traiter.

    Returns:
        Un dictionnaire où les clés sont les numéros de paragraphe et les valeurs sont des listes de palindromes.
    """
    content = read_file(file_path)
    paragraphs = split_into_paragraphs(content)
    palindromes_by_paragraph = {}
    for i, paragraph in enumerate(paragraphs, 1):
        palindromes = count_palindromes(paragraph=paragraph)
        if palindromes:
            palindromes_by_paragraph[i] = palindromes
        else:
            palindromes_by_paragraph[i] = "Aucun palindrome"
    return palindromes_by_paragraph

def main(file_path: str) -> None:
    """
    Fonction principale qui traite le fichier et affiche les résultats dans un format lisible.

    Args:
        file_path: Le chemin vers le fichier à traiter.
    """
    results = process_file(file_path)

    # Affiche les résultats dans un format lisible
    for paragraph_num, palindromes in results.items():
        print(f"Paragraphe {paragraph_num}:")
        if palindromes != "Aucun palindrome":
            print(f"  Trouvé {len(palindromes)} palindrome(s):")
            for palindrome in palindromes:
                print(f"    - {palindrome}")
        else:
            print("  Aucun palindrome trouvé.")
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python palindrome_counter.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    main(file_path)
