# GitHub 


## Prérequis
Rien. Vous n'avez pas besoin de savoir coder pour valider ce module. 

## Qu'est ce que GitHub 

GitHub est avant tout une plateforme d'hébergement de code. On peut le voir comme le "google drive" (outils de stockage en ligne de google) pour le code. Il permet aussi la gestion de version et la collaboration. 

### La gestion de version 

La gestion de versions (en anglais : version control ou revision control) consiste à gérer l'ensemble des versions d'un ou plusieurs fichiers (généralement en texte). Essentiellement utilisée dans le domaine de la création de logiciels, elle concerne surtout la gestion des codes source.

Cette activité étant fastidieuse et relativement complexe, un appui logiciel est presque indispensable. À cet effet, il existe différents logiciels de gestion de versions qui, bien qu'ayant des concepts communs, apportent chacun leur propre vocabulaire et leurs propres usages. À titre d'exemple, on trouve un mécanisme rudimentaire de gestion de versions dans Wikipédia : pour chaque article, l'historique est disponible en cliquant sur le lien Afficher l'historique ; chaque ligne est une version de l'article. 
*(définition de wikipedia : https://fr.wikipedia.org/wiki/Gestion_de_versions)* 

Par ailleurs vous pouvez retrouver cette fonctionnalité dans google drive si vous chargez un document qui porte le même nom google va automatiquement remplacer l’ancien document par votre nouveau document en ajoutant version 2 à la fin. 

Aujourd’hui utiliser des logiciels de gestion de versions est quasiment obligatoire dans la plus part des entreprises car ils facilitent grandement la gestion des projets et permettent de faciliter la collaboration entre developpeurs. 

Il existe plusieurs logiciels de ce type qui fonctionnent plus ou moins de façon similaire. Pour en savoir plus 

GitHub est le leader incontesté et il est donc indispensable pour tout développeur de savoir utiliser Git.



### La collaboration 

Il vous permet, à vous et à d'autres, de travailler ensemble sur des projets de n'importe où.



## Créer un nouveau dépot (repository)

Un repository ou un dépot (dossier qui contient du code) est généralement utilisé pour organiser un seul projet. Les repository peuvent contenir des dossiers et des fichiers, des images, des vidéos, des feuilles de calcul et des ensembles de données, globalement tout ce dont votre projet a besoin pour fonctionner. 

Nous vous recommandons d'inclure un README ou un fichier contenant des informations sur votre projet. GitHub facilite son ajout en même temps que vous créez votre nouveau référentiel. Il offre également d'autres options courantes telles qu'un fichier de licence.

Votre référentiel hello-world peut être un endroit où vous stockez des idées, des ressources ou même partagez et discutez de choses avec d'autres.


Créez un nouveau dossier, ouvrez le et exécutez la commande
```
git init
```

## Cloner un dépôt


Créez une copie de votre dépôt local en exécutant la commande
```
git clone /path/to/repository
```

## Ajouter & valider du code dans un dépot
Pour un fichier utilisez 
```
git add <filename>
```
Pour ajouter tous les fichiers modifiés
```
git add *
```

### Pour valider vos changements, utilisez
```
git commit -m "Message de validation"
```

## Envoyer des changements sur une branche 
Pour envoyer vos changement à votre dépôt distant, exécutez la commande
```
git push origin master
```

## Les branches 
Les branches sont utilisées pour développer des fonctionnalités isolées des autres. La branche master est la branche par défaut quand vous créez un dépôt. Utilisez les autres branches pour le développement et fusionnez ensuite à la branche principale quand vous avez fini.

### Créer une branche sur votre dépot 
Pour créer une nouvelle branche nommée "feature_x" et passer dessus pour l'utiliser
```
git checkout -b feature_x
```

### Retourner sur votre branche principale
```
git checkout master
```

### supprimer la branche
```
git branch -d feature_x
```
**Attention une branche n'est pas disponible pour les autres tant que vous ne l'aurez pas envoyée vers votre dépôt distant**

### Git Tips

Pour ceux qui n'arrivent pas à pull parce qu'ils ont fait des modif dans le repo, lancer la commande : 
```
git stash
git pull
git stash pop
```
 
 
 
# Biblio 

- https://www.pierre-giraud.com/git-github-apprendre-cours/presentation-git-github/ 
- mini git no deep shit 