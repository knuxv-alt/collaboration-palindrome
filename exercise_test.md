# Instructions pour écrire et exécuter les tests

## Étape 1: Organisation des tests

Pour tester les fonctions du projet, suivez les étapes ci-dessous :

1. **Créez un nouveau fichier de tests pour chaque fonction** :
   - Chaque fonction devra avoir son propre fichier de test qui commencera par `test_` dans le dossier `tests`.
   - Exemples : 
     - Pour la fonction `split_into_paragraphs`, créez un fichier nommé `test_split_into_paragraphs.py`.
     - Pour la fonction `is_palindrome`, créez un fichier nommé `test_is_palindrome.py`.

2. **Tests pour `read_file`** :
   - La fonction `read_file` a déjà été testée. Cependant, il y a un problème, car il faut choisir entre deux options :
     - Option 1 : Si le fichier est vide, retourner une chaîne vide.
     - Option 2 : Si le fichier est vide, générer une erreur personnalisée.

   Selon votre choix, adaptez le test correspondant et assurez-vous que la fonction `read_file` est modifiée pour respecter ce choix.

## Étape 2: Tests pour `split_into_paragraphs`

### Cas réguliers et cas limites à tester :

- **Cas régulier** : Le texte contient plusieurs paragraphes séparés par `\n\n`, et ils sont correctement divisés.
- **Cas limites** :
  - Le texte ne contient pas de sauts de paragraphe (pas de `\n\n`) ==> Doit retourner un seul paragraphe.
  - Le texte est totalement vide ==> Doit retourner une liste vide.
  - Sauts de paragraphe consécutifs (par exemple, `\n\n\n\n`) ==> Aucun paragraphe vide entre les sauts multiples.
    - Vous pouvez tester le script sur l'exemple `palin_many_newlines.txt` pour vérifier

Écrivez d'abord les tests reflétant ces choix dans le fichier `test_split_into_paragraphs.py`.

## Étape 3: Tests pour `is_palindrome`

### Cas réguliers et cas limites à tester :

- **Cas réguliers** :
  - Testez des mots palindromes.
  - Testez des mots non palindromes.
  
- **Cas limites** :
  - Palindromes avec des majuscules et minuscules mélangées (par exemple, "MadAm"). 
    - Décidez si la casse doit être ignorée. Écrivez les tests en conséquence.
  - Mots d'un seul caractère ==> Choisissez si cela est considéré comme un palindrome.
  - Chaîne vide ==> Décidez si cela doit retourner `True` ou `False`.
  - Caractères spéciaux ou ponctuation (par exemple, "Un élan en a nul").
    - Décidez si les accents et ponctuations doivent être ignorés. 
    - Écrivez par exemple un test pour "réifier" en indiquant s'il est considéré comme un palindrome ou non.

Créez les tests dans le fichier `test_is_palindrome.py` reflétant ces choix.

## Étape 4: Lancer les tests

```bash
pytest
```

## Étape 5: Modifier le code

Si certains tests échouent, modifiez le code de vos fonctions pour qu'ils passent. Par exemple :
- Si vous décidez que les accents doivent être ignorés pour les palindromes, modifiez la fonction `is_palindrome` pour utiliser une normalisation Unicode.
- Si vous voulez que les paragraphes consécutifs ne génèrent pas de paragraphes vides, ajustez la fonction `split_into_paragraphs` pour ignorer les sauts multiples.

Continuez à lancer les tests après chaque modification pour vous assurer que tout fonctionne correctement.
portement attendu pour chaque fonction, en prenant en compte les différents cas limites que vous pourriez rencontrer.