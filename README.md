# ESGI Git Workshop - History Manipulation

- Clonez le projet :
```bash
git clone https://github.com/LucasVanHaaren/git_workshop_history.git
```

- Récupérez la liste des commits :
```bash
git log
```

- Effectuez un squash de tout les commits afin de les fusionner en un seul :
```bash
git rebase --root -i
```

- Récupérez la liste des commits une seconde fois :
```bash
git log
```

- Récupérez la liste des refs (`reflog`) :
```bash
git reflog
```

- Retrouvez l'état précédent avant le squash :
```bash
git reset --hard <COMMIT_HASH>
```

- WELL DONE ! Vous venez de récupérer un commit "perdu" !

> NB: Cela n'est possible que sur un dépot local, dans le cas où le reflog n'a pas été "nettoyé"

