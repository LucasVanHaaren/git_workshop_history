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

On squash tous les commits dans le premier :

```
pick 527a4ae initial commit
s 2bdea61 add name option
s e0e2764 add help menu
s a56da87 cleanup codebase
s 01097d4 add docs
```

On peux éditer le message de notre commit fusionné :

```
# This is a combination of 5 commits.
# This is the 1st commit message:

squash all commits inot this one

# This is the commit message #2:
```

- Récupérez la liste des commits une seconde fois :
```bash
git log
```

```
commit 731aec7ebf33a5d7f87e5a590d2fb12855111fbf (HEAD -> main)
Author: LucasVanHaaren <29121316+LucasVanHaaren@users.noreply.github.com>
Date:   Fri Oct 20 09:40:08 2023 +0200

    squash all commits into this one
```

- Récupérez la liste des refs (`reflog`) :
```bash
git reflog
```

- On sélectionne le commit juste avant le rebase

- Retrouvez l'état précédent avant le squash :
```bash
git reset --hard <COMMIT_HASH>
```

- WELL DONE ! Vous venez de récupérer un commit "perdu" !

> NB: Cela n'est possible que sur un dépot local, dans le cas où le reflog n'a pas été "nettoyé"
