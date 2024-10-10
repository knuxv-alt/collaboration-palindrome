### Cas réguliers et cas limites à tester


### 1. **Lecture du fichier**
   - **Cas régulier** : Le fichier existe, peut être ouvert et lu correctement.
   - **Cas limites** :
     - Le fichier n'existe pas ==> génère une erreur `FileNotFoundError`).
     - Le fichier est vide, ==> retourne une chaine de caractères vide.

### 2. **Division en paragraphes (`split_into_paragraphs`)**
   - **Cas régulier** : Le texte contient plusieurs paragraphes séparés par `\n\n`, et ils sont correctement divisés.
   - **Cas limites** :
     - Le texte ne contient pas de sauts de paragraphe (c.-à-d., pas de `\n\n`) ==> génère un seul paragraphe
     - Le texte est totalement vide ==> génère une liste vide
     - Sauts de paragraphe consécutifs (par exemple, `\n\n\n\n`) ==> Pas paragraphes vides équivalent à \n\n

### 3. **Détection de palindrome (`is_palindrome`)**
   - **Cas réguliers** : 
     - Des mots palindromes
     - Des mots non palindromes
   - **Cas limites** :
     - Palindromes avec des majuscules et minuscules mélangées (par exemple, "MadAm"). ==> Choix à faire (est-ce qu'on compte la casse)
     - Mots d'un seul caractère ==> Choix à faire
     - Chaîne vide ==> Choix à faire
     - Caractères spéciaux ou ponctuation (par exemple, "Un élan en a nul") ==> Choix à faire, est-ce qu'on décode les accents?


### 7. **Journalisation (logging)**
   Lors de l'incorporation de la journalisation dans ce script, vous devez enregistrer :
   - **Erreurs** :
     - Fichier non trouvé (`FileNotFoundError`).
     - Problèmes lors de la lecture du fichier.
     - Entrée invalide (par exemple, nombre incorrect d'arguments en ligne de commande).
   - **Informations de débogage** :
     - Nombre de paragraphes détectés.
     - Nombre de palindromes trouvés par paragraphe.
     - Quand un paragraphe ne contient aucun palindrome.
     - Problèmes avec la division en paragraphes ou la gestion des caractères spéciaux.

### Exemples de tests de cas limites :

1. **Fichier vide** :
   - Entrée : Un fichier vide.
   - Sortie attendue : Aucun paragraphe ou palindrome ne devrait être trouvé.

2. **Fichier sans saut de paragraphe** :
   - Entrée : Un long bloc de texte sans aucun `\n\n`.
   - Sortie attendue : Tout le texte doit être traité comme un seul paragraphe.

3. **Fichier avec plusieurs paragraphes vides** :
   - Entrée : Un fichier avec des `\n\n\n\n` consécutifs entre certains paragraphes.
   - Sortie attendue : Les paragraphes vides doivent être ignorés ou traités de manière appropriée.

4. **Palindromes avec des caractères spéciaux** :
   - Entrée : Un paragraphe contenant des palindromes avec des caractères spéciaux (par exemple, "Un élan en a nul").
   - Sortie attendue : Seuls les palindromes valides doivent être détectés après avoir supprimé la ponctuation ou les caractères spéciaux.

5. **Paragraphe avec un seul mot** :
   - Entrée : Un paragraphe avec un seul mot qui est un palindrome.
   - Sortie attendue : Le palindrome doit être détecté.

En testant ces cas, vos étudiants pourront s'assurer que le script fonctionne correctement dans une variété de conditions.