Objectifs d'apprentissage
Implémentez une application Python qui inclut une interface de ligne de commande .
Implémentez un ensemble de fonctions de mappage objet-relationnel pour deux classes de modèles ou plus.
Définissez un modèle d’objet Python qui inclut une relation un-à-plusieurs entre deux classes.
Exercez les meilleures pratiques en matière de conception CLI.
Exercez les meilleures pratiques en POO.
Vocabulaire clé
Ligne de commande : interface textuelle intégrée au système d'exploitation de votre ordinateur. Elle vous permet d'accéder aux fichiers et aux applications de votre ordinateur manuellement ou via des scripts.
Terminal : l'application sous Mac OS qui permet d'accéder à la ligne de commande.
Command Shell/Powershell : les applications sous Windows qui permettent d'accéder à la ligne de commande.
Interface de ligne de commande (CLI) : interface textuelle permettant d'exécuter des programmes, de gérer des fichiers et d'interagir avec des objets en mémoire. Comme son nom l'indique, elle s'exécute en ligne de commande.
Mappage objet-relationnel (ORM) : technique de programmation qui fournit un mappage entre un modèle de données orienté objet et un modèle de base de données relationnelle.
Attribut : variables qui appartiennent à un objet.
Propriété : attributs contrôlés par des méthodes.
Décorateur : fonction qui prend une autre fonction comme argument et renvoie une nouvelle fonction avec des fonctionnalités supplémentaires.
Introduction
Bienvenue à la fin de la phase 3 ! Vous avez beaucoup appris dans cette unité :

Principes fondamentaux de Python.
Structures de données (et plus récemment, algorithmes).
Programmation orientée objet.
Héritage d'objets.
Attributs et méthodes d'instance et de classe.
Configuration des applications.
Principes fondamentaux de SQL.
Relations de table dans SQL.
Mappage objet-relationnel avec Python.
Création d'interfaces de ligne de commande.
Le projet de phase 3 est ouvert quant au contenu. Vous êtes libre de créer ce que vous souhaitez, à condition que cela respecte les exigences listées ci-dessous.

Exigences
Lors du précédent atelier et du code-along, nous avons créé une interface de ligne de commande destinée à un développeur pour tester ses méthodes ORM. Pour ce projet, nous vous demandons de sélectionner un autre type d'utilisateur et de créer votre propre interface de ligne de commande (CLI) et ses méthodes d'assistance qui lui affichent des informations client. Pensez à l'expérience utilisateur. Comment la simplifier ? Les options de la CLI ne se résument pas à une longue liste de choix. S'il s'agit d'une application de boîte à recettes, si l'utilisateur consulte la catégorie Desserts et souhaite ajouter une recette, il doit pouvoir le faire sans avoir à préciser à quelle catégorie appartient la recette : il consulte la catégorie Desserts ! N'affichez pas les informations backend de l'utilisateur, telles que les identifiants de base de données et les objets renvoyés formatés par la  méthode repr du modèle  , qui sont des informations destinées au développeur. La CLI et ses méthodes d'assistance représentent le frontend de votre projet. De la même manière que vous n'avez pas affiché le JSON de l'utilisateur dans votre projet de phase 2, vous ne lui montrerez pas les objets Python envoyés depuis le backend. C'est dans l'interface utilisateur (CLI et assistants) que le formatage est effectué. Vous devez créer la CLI et les assistants, et non une copie de nos CLI et assistants simplement adaptés à vos modèles. Ils étaient adaptés aux tests de nos développeurs sur leurs méthodes ORM, mais vous devez créer vos propres CLI et assistants, adaptés à votre scénario utilisateur et à vos modèles. Soyez créatif !

Exigences ORM
L'application doit inclure une base de données créée et modifiée avec les méthodes Python ORM que vous écrivez.

Le modèle de données doit inclure au moins 2 classes de modèles.
Le modèle de données doit inclure au moins une relation un-à-plusieurs.
Des méthodes de propriété doivent être définies pour ajouter des contraintes appropriées à chaque classe de modèle.
Chaque classe de modèle doit inclure des méthodes ORM (créer, supprimer, obtenir tout et rechercher par identifiant au minimum).
Exigences CLI
La CLI doit afficher des menus avec lesquels un utilisateur peut interagir.
L'interface de ligne de commande doit utiliser des boucles selon les besoins pour maintenir l'utilisateur dans l'application jusqu'à ce qu'il décide de quitter.
Pour CHAQUE classe du modèle de données, la CLI doit inclure des options : créer un objet, supprimer un objet, afficher tous les objets, afficher les objets associés et rechercher un objet par attribut.
L'interface de ligne de commande doit valider les entrées de l'utilisateur et les créations/suppressions d'objets, en fournissant des erreurs informatives à l'utilisateur.
Le code du projet doit suivre les meilleures pratiques de la POO.
Pipfile contient toutes les dépendances nécessaires et aucune dépendance inutile.
Les importations sont utilisées dans les fichiers uniquement lorsque cela est nécessaire.
Les dossiers, fichiers et modules du projet doivent être organisés et suivre les conventions de dénomination appropriées.
Le projet doit inclure un README.mddocument décrivant l’application.
Vous n'avez pas besoin d'implémenter de tests pour pytest, mais vous devriez tester votre code minutieusement à l'aide de votre interface de ligne de commande. Essayez de saisir des données erronées lorsque vous y êtes invité et vérifiez que votre application affiche un message d'erreur pertinent.

Comment commencer ?
Commencez avec le modèle de projet (fourni dans la leçon suivante). Vous êtes libre d'adapter la structure du modèle, à condition de respecter les exigences du projet.
Pensez à l'interaction utilisateur. Comment allez-vous l'inviter ? Quelles informations saisira-t-il ? Comment allez-vous lui fournir un retour ?
Réfléchissez à votre modèle de données. Comment allez-vous organiser et stocker les informations reçues de l'utilisateur ?
Si vous êtes bloqué en essayant d'accomplir une tâche spécifique, vérifiez en ligne s'il existe une bibliothèque Python qui vous facilitera la tâche.
Pensez à utiliser ClickLiens vers un site externe.ou le feuLiens vers un site externe.pour prendre en charge les tâches CLI de base pour vous.

# Laptop Store CLI + ORM

This is a command-line interface (CLI) application to manage a laptop store using Python and SQLite.

## Features
- Manage categories (create, list, delete)
- Manage laptops (create, list, delete, view by category)
- ORM-style methods with SQLite database

<!-- ## How to run
```bash
python main.py
``` -->

The database file (`laptops.db`) will be created automatically.


