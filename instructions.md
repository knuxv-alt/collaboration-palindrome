# Exercice : Compteur de Palindromes

## Objectif
Créer un script Python qui lit des fichiers texte, compte le nombre de palindromes par paragraphe, et affiche les résultats dans le terminal et dans un fichier JSON.

## Instructions

1. Clonez le dépôt contenant le squelette du script.

2. Créez votre branche de fonctionnalité :
   ```git
   git checkout -b votre-feature-branche
   ```

3. Apportez les modifications au dossier

   1. Complétez les fonctions qui vous ont été attribuées dans `palindrome_counter.py`.
   2. (ou) Générez des fichiers textes contenant des paragraphes avec zéro, un ou plusieurs palindromes

4. Assurez vous que vous êtes à jour par rapport à la branche main du `remote`. Si non, vous devez merger les changements dans votre branche de développement pour qu'elle soit à jour..

   ```git
   git checkout main
   git pull origin main
   git checkout votre-feature-branche
   git merge main
   ```

   

5. Commitez vos changements et poussez votre branche :
   ```git
   git add palindrome_counter.py
   git commit -m "Implémentation du compteur de palindromes"
   git push -u origin feature/votre-nom-palindrome-counter
   ```

6. Créez une Pull Request sur GitHub pour fusionner votre travail dans la branche principale.

## Spécifications
- Le script doit accepter le chemin d'un ficher comme argument.
- Pour chaque fichier, comptez les palindromes dans chaque paragraphe.
- Affichez les résultats dans le terminal.
- Un palindrome est un mot ou une phrase qui se lit de la même façon dans les deux sens, en ignorant les espaces, la ponctuation et la casse.
- 
