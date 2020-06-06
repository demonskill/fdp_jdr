# fdp_jdr
generateur de feuille de personnage pour un jeu de role

## Lancer le programme

Pour lancer le programme, il suffit de lancer dans un terminal :

```shell
python3.8 /cheminvers/jdr.py
```

## Différents modes

Après avoir spécifier les caractéristiques, la manière de les déterminer et le nombre de personnage à créer, il va vous être demandé de choisir entre 3 modes :

- manuel

- aléatoire

- procédural

  ### Manuel

  Dans le mode manuel vous écrivez vous-même le nom, la race et le sexe des personnages

  ### Aléatoire

  Dans le mode aléatoire la race et le sexe des personnages sont déterminés aléatoirement puis le nom  des personnages est déterminés aléatoirement, si vous souhaitez ajouter ou supprimer des noms, race ,sexe qui seront tirés aléatoirement il suffit  de :

  - modifier un fichier listenom déja existant comme listenomhumain1.txt
  - rajouter un fichier listenom qui devra impérativement être de la forme "listenom" + race + sexe(un caractère) + ".txt" comme par exemple **listenomorc1.txt**
   ### Procédural
  
  Dans le mode procédural, l'utilisateur choisit la race et le sexe de chaque personnage et leur nom est déterminé aléatoirement


