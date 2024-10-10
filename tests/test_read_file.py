import pytest
from palin import read_file

def test_read_file_ok():
    # On essaye avec un fichier
    assert read_file(file_path="../data/palin_single_para.txt") == "Le pilote utilise le radar pour naviguer par mauvais temps."

def test_read_file_dont_exist():
    # On veut que le programme génère une erreur si le chemin est mauvais
    with pytest.raises(FileNotFoundError):
        read_file("ThisFileDontExist")

def test_read_empty_option1():
    # Fichier vide ==> retourne une chaine de caractère vide
    assert read_file("../data/palin_empty.txt") == ""

def test_read_empty_option2():
    # OU AU CHOIX
    # Fichier vide ==>retourne une erreur
    with pytest.raises(ValueError): # Si on choisit cette option il faut changer le code
        read_file("../data/palin_empty.txt")



