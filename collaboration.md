# Workflow de Collaboration Git

## Vue d'ensemble
Dans ce workflow, chaque développeur travaille sur une branche de fonctionnalité distincte et fusionne son travail dans la branche principale (main) via des pull requests.

## Étapes clés

1. Cloner le dépôt
   ```
   git clone [url-du-repo]
   ```

2. Créer une nouvelle branche de fonctionnalité (les branches ne doivent pas avoir le même nom)
   ```
   git checkout -b votre-feature-branche
   ```

3. Travailler sur votre fonctionnalité et faire des commits
   ```
   git add .
   git commit -m "Description de vos changements"
   ```

4. **Mettre à jour votre branche avec les derniers changements de main**

   Il faut prévoir qu'un autre étudiant a peut-être modifié la branche main, donc vous devez vous assurez que vous êtes à jour avant de merger vos propres changements.


   ```
   git checkout main
   git pull origin main
   git checkout votre-feature-branche
   git merge main
   ```

5. Pousser votre branche vers le dépôt distant
   ```
   git push -u origin votre-feature-branche
   ```

6. Créer une Pull Request sur GitHub
   - Allez sur la page du dépôt GitHub
   - Cliquez sur "New Pull Request"
   - Sélectionnez votre branche pour fusionner dans main

7. Après révision et approbation, votre code sera fusionné dans main

## Points importants à retenir
- Toujours travailler sur une branche de fonctionnalité, jamais directement sur main
- Mettre à jour régulièrement votre branche avec les derniers changements de main
- Nommer vos branches de manière descriptive (ex: feature/alice-menu-navigation)
- Faire des commits fréquents avec des messages clairs
- Créer une Pull Request pour chaque fonctionnalité terminée

En suivant ce workflow, vous assurez une collaboration efficace et maintenez un historique de projet clair et organisé.