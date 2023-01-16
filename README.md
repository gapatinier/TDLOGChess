# Projet TDLOG : Jeu d'échecs

L'objectif du projet est d'implémenter le jeu d'échecs.
La première étape sera de programmer le modèle du jeu
(board, pièces, coups possibles, etc.). La seconde étape
consistera à programmer une interface graphique. Ensuite,
on pourra envisager de créer une IA ou de permettre le
jeu multijoueurs en réseau.

Les objectifs pour la fin du projet seront de nettoyer et factoriser le code, créer un diagramme d’architecture, ajouter certaines fonctionnalités au jeu (ajouter la promotion du pion) et d’ajouter des boutons afin que l’interface graphique soit plus agréable pour le ou les joueurs.

## Création des différentes classes

On pourra créer les classes : 'Game', 'Player', 'Board',
et 'Piece'.

La classe 'Piece' aura comme attribut COLOR qui prendra
la valeur BLACK ou WHITE pour désigner la couleur de la
pièce ainsi qu'un attribut pour désigner sa position sur
le board. Elle aura également plusieurs sous-classes pour
les pièces différentes. La sous-classe 'Rook' aura un
attribut en plus pour prendre en compte les roques.

La classe 'Board' aura comme attribut une liste de
'Piece' ainsi qu'un Int prenant la valeur 0 ou 1 pour
désigner quel joueur jouera le prochain coup.

La classe 'Player' aura un attribut COLOR qui prendra
la valeur BLACK ou WHITE pour désigner la couleur des
pièces du joueur, un attribut Pieces qui sera la liste
des pièces de ce joueur. Il aura deux sous-classes
HumanPlayer et ComputerPlayer.

La classe 'Game' se chargera de commencer une partie.

## Création des méthodes

Après avoir créé les différentes classes, on peut
introduire les méthodes qui permettront de modéliser
le jeu.

La classe 'Piece' aura une méthode 'Moves' prenant
en argument 'Board' et renvoyant la liste des positions
sur le board où cette pièce peut atterrir. 

## Diagramme de classes
![Alt text](images/uml_chess.drawio.png?raw=true "Diagramme de classes")

## Schéma d'architecture
![Alt_text](images/architecture.png?raw=true "Schéma d'architecture")
