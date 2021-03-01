from random import randint
from tkinter import *
import os
t_pseudo_player = []
t_dés = []
t_jetons = []
t_ordi = ["ordi1", "ordi2", "ordi3", "ordi4"]
Vn_maximum = 0
Vn_x = 0
clear = lambda: os.system('clear')
Vn_pot = 21

#---------------------------------
# nombres de joueurs et pseudo
#---------------------------------
Vn_player = int(input("Combien y a t-il de joueurs ? (de 1 à 4) : "))
while Vn_player > 4:
    Vn_player = int(input("Combien y a t-il de joueurs ? (DE 1 À 4 JOUEURS) : "))

if Vn_player == 4:
    while Vn_x < Vn_player:
        Van_pseudo = input("Nouveau joueur : quel est ton pseudo ? : ")
        Vn_x += 1
        print("Joueur", Vn_x, "-> pseudo :", Van_pseudo)
        t_pseudo_player.append(Van_pseudo)
else:
    while Vn_x < Vn_player:
        Van_pseudo = input("Nouveau joueur : quel est ton pseudo ? : ")
        Vn_x += 1
        print("Joueur", Vn_x, "-> pseudo :", Van_pseudo)
        t_pseudo_player.append(Van_pseudo)

#---------------------------------
# nombres d'ordi dans le partie
#---------------------------------
if Vn_player == 4:
    None
elif Vn_player != 4:
    print("Nombre d'ia max :", 4 - Vn_player)
    Vn_player_ordi = int(input("Combien d'IA rejoint la partie ? : "))
    while Vn_player + Vn_player_ordi > 4:
        print("Nombre d'ia max :", 4 - Vn_player)
        Vn_player_ordi = int(input("Combien d'IA rejoint la partie ? : "))
    Vn_x = 0
    while Vn_player_ordi != Vn_x:
        print("ordi", Vn_x + 1, "-> pseudo :", t_ordi[Vn_x])
        t_pseudo_player.append(t_ordi[Vn_x])
        Vn_x += 1

print("Il y a donc", len(t_pseudo_player), "joueurs, il y a :", t_pseudo_player)

#---------------------------------
# début de la partie
#---------------------------------

while Vn_pot != 0:
    Vn_x = 0
    t_scores = []
    while Vn_x != len(t_pseudo_player):
        Vn_relance = 0
        Vn_résultat = 0
        Vn_score = 0
        dé_1 = randint(1, 6)
        dé_2 = randint(1, 6)
        dé_3 = randint(1, 6)
        print(t_pseudo_player[Vn_x], "à toi de jouer :")
        print("dé 1 :", dé_1)
        print("dé 2 :", dé_2)
        print("dé 3 :", dé_3)
        Vn_tour = 1
# ---------------------------------
# lancement des dés
# ---------------------------------
        while Vn_tour != 3:
            # clear() // À revoir avec un terminal
            Vn_relance = input("Quel(s) dé(s) voulez vous relancer ? :")
            if Vn_relance == "123":
                dé_1 = randint(1, 6)
                dé_2 = randint(1, 6)
                dé_3 = randint(1, 6)
            elif Vn_relance == "12":
                dé_1 = randint(1, 6)
                dé_2 = randint(1, 6)
            elif Vn_relance == "13":
                dé_1 = randint(1, 6)
                dé_3 = randint(1, 6)
            elif Vn_relance == "23":
                dé_2 = randint(1, 6)
                dé_3 = randint(1, 6)
            elif Vn_relance == "1":
                dé_1 = randint(1, 6)
            elif Vn_relance == "2":
                dé_2 = randint(1, 6)
            elif Vn_relance == "3":
                dé_3 = randint(1, 6)
            else:
                print("LE BON")
                break
            print("dé 1 :", dé_1)
            print("dé 2 :", dé_2)
            print("dé 3 :", dé_3)
            Vn_tour += 1

# ---------------------------------
# comptage des scores selon les dés
# ---------------------------------
        t_dés = [dé_1, dé_2, dé_3]
        t_résultat = sorted(t_dés, reverse=True)
        if t_résultat == [4, 2, 1]:
            Vn_score += 10
            t_scores.append(Vn_score)
        elif t_résultat == [1, 1, 1]:
            Vn_score += 7
            t_scores.append(Vn_score)
        elif t_résultat == [6, 6, 6] or t_résultat == [6, 1, 1]:
            Vn_score += 6
            t_scores.append(Vn_score)
        elif t_résultat == [5, 5, 5] or t_résultat == [5, 1, 1]:
            Vn_score += 5
            t_scores.append(Vn_score)
        elif t_résultat == [4, 4, 4] or t_résultat == [4, 1, 1]:
            Vn_score += 4
            t_scores.append(Vn_score)
        elif t_résultat == [3, 3, 3] or t_résultat == [3, 1, 1]:
            Vn_score += 3
            t_scores.append(Vn_score)
        elif t_résultat == [2, 2, 2] or t_résultat == [2, 1, 1]:
            Vn_score += 2
            t_scores.append(Vn_score)
        elif t_résultat == [3, 2, 1] or t_résultat == [4, 3, 2] or t_résultat == [5, 4, 3] or t_résultat == [6, 5, 4] or t_résultat == [7, 6, 5] or t_résultat == [8, 7, 6] or t_résultat == [9, 8, 7]:
            Vn_score += 2
            t_scores.append(Vn_score)
        else:
            Vn_score += 1
            t_scores.append(Vn_score)
        print(t_pseudo_player[Vn_x], "suite a ton score :", t_dés, ": ton score est de", t_scores[Vn_x], "point(s).")
        Vn_x += 1

    print("RÉCAPITULATIF DES POINTS")
    Vn_x = 0
    while Vn_x != len(t_pseudo_player):
        print(t_pseudo_player[Vn_x], ": ton score est de", t_scores[Vn_x])
        Vn_x += 1

# ---------------------------------
# distribution des jetons aux joueurs
#---------------------------------

    Vn_x = 0
    t_ordre_scores = sorted(t_scores, reverse=True)

    Vn_mini = t_ordre_scores[len(t_ordre_scores)-1]
    if t_ordre_scores[len(t_ordre_scores) - 1] == t_ordre_scores[len(t_ordre_scores) - 2]:
        print("égalité")
    else:
        while len(t_jetons) != len(t_pseudo_player):
            t_jetons.append(0)
        Vn_jetons = 0
        while Vn_mini != Vn_jetons:
            for Vn_jetons in t_scores:
                if Vn_jetons == Vn_mini:
                    if Vn_pot < t_ordre_scores[0]:
                        t_ordre_scores[0] = Vn_pot
                        t_jetons[Vn_x] += t_ordre_scores[0]
                        Vn_pot = 0
                        break
                    else:
                        Vn_pot -= t_ordre_scores[0]
                        t_jetons[Vn_x] += t_ordre_scores[0]
                        print("Il reste", Vn_pot, "jetons dans le pot")
                    print(t_pseudo_player[Vn_x], ": tu as cummulé", t_jetons[Vn_x], "jetons")
                    break
                else:
                    Vn_x += 1

Vn_x = 0
while Vn_x != len(t_pseudo_player):
    print(t_pseudo_player[Vn_x], ": tu as", t_jetons[Vn_x], "jetons")
    Vn_x += 1
print("LE POT EST VIDE, PLACE À LA DÉCHARGE !")

t_ordre_jetons = sorted(t_jetons, reverse=True)

# ---------------------------------
# Fin de la charge
#DÉBUT DE LA DÉCHARGE
#---------------------------------
Vn_x = 0
while Vn_x < 4:
    if t_ordre_scores[len(t_ordre_scores) - 1] == 0:
        Vn_jetons = 0
        Vn_maxi = t_ordre_scores[0]
        while Vn_maxi != Vn_jetons:
            for Vn_jetons in t_scores:
                if Vn_jetons == Vn_maxi:
                    print("Espagnol ! il n'y a pas besoin de décharge,", t_pseudo_player[Vn_x], "n'as plus de jetons :", t_pseudo_player[Vn_x], "est notre vainqueur !!")
                else:
                    Vn_x += 1
    else:
        Vn_x += 1
while t_ordre_jetons[len(t_ordre_jetons)-1] != 0:
    Vn_x = 0
    t_scores = []
    while Vn_x != Vn_player + Vn_player_ordi:
        Vn_relance = 0
        Vn_résultat = 0
        Vn_score = 0
        dé_1 = randint(1, 6)
        dé_2 = randint(1, 6)
        dé_3 = randint(1, 6)
        print(t_pseudo_player[Vn_x], "à toi de jouer :")
        print("dé 1 :", dé_1)
        print("dé 2 :", dé_2)
        print("dé 3 :", dé_3)
        Vn_tour = 1
        # ---------------------------------
        # lancement des dés
        # ---------------------------------
        while Vn_tour != 3:
            Vn_relance = input("Quel(s) dé(s) voulez vous relancer ? :")
            if Vn_relance == "123":
                dé_1 = randint(1, 6)
                dé_2 = randint(1, 6)
                dé_3 = randint(1, 6)
            elif Vn_relance == "12":
                dé_1 = randint(1, 6)
                dé_2 = randint(1, 6)
            elif Vn_relance == "13":
                dé_1 = randint(1, 6)
                dé_3 = randint(1, 6)
            elif Vn_relance == "23":
                dé_2 = randint(1, 6)
                dé_3 = randint(1, 6)
            elif Vn_relance == "1":
                dé_1 = randint(1, 6)
            elif Vn_relance == "2":
                dé_2 = randint(1, 6)
            elif Vn_relance == "3":
                dé_3 = randint(1, 6)
            else:
                print("LE BON")
                break
            print("dé 1 :", dé_1)
            print("dé 2 :", dé_2)
            print("dé 3 :", dé_3)
            Vn_tour += 1

        # ---------------------------------
        # comptage des scores selon les dés
        # ---------------------------------
        t_dés = [dé_1, dé_2, dé_3]
        t_résultat = sorted(t_dés, reverse=True)
        if t_résultat == [4, 2, 1]:
            Vn_score += 10
            t_scores.append(Vn_score)
        elif t_résultat == [1, 1, 1]:
            Vn_score += 7
            t_scores.append(Vn_score)
        elif t_résultat == [6, 6, 6] or t_résultat == [6, 1, 1]:
            Vn_score += 6
            t_scores.append(Vn_score)
        elif t_résultat == [5, 5, 5] or t_résultat == [5, 1, 1]:
            Vn_score += 5
            t_scores.append(Vn_score)
        elif t_résultat == [4, 4, 4] or t_résultat == [4, 1, 1]:
            Vn_score += 4
            t_scores.append(Vn_score)
        elif t_résultat == [3, 3, 3] or t_résultat == [3, 1, 1]:
            Vn_score += 3
            t_scores.append(Vn_score)
        elif t_résultat == [2, 2, 2] or t_résultat == [2, 1, 1]:
            Vn_score += 2
            t_scores.append(Vn_score)
        elif t_résultat == [3, 2, 1] or t_résultat == [4, 3, 2] or t_résultat == [5, 4, 3] or t_résultat == [6, 5, 4] or t_résultat == [7, 6, 5] or t_résultat == [8, 7, 6] or t_résultat == [9, 8, 7]:
            Vn_score += 2
            t_scores.append(Vn_score)
        else:
            Vn_score += 1
            t_scores.append(Vn_score)
        print(t_pseudo_player[Vn_x], "suite a ton score :", t_dés, ": ton score est de", t_scores[Vn_x], "point(s).")
        if t_résultat == [2, 2, 1]:
            print("NÉNETTE !"
                  "Tu récupéres 2 jetons")
            Vn_pot -= 2
            print("il reste", Vn_pot, "jetons dans le pot")
            t_jetons[Vn_x] += 2
        Vn_x += 1

    print("RÉCAPITULATIF DES POINTS")
    Vn_x = 0
    while Vn_x != Vn_player:
        print(t_pseudo_player[Vn_x], ": ton score est de", t_scores[Vn_x])
        Vn_x += 1

    Vn_x = 0
    t_ordre_scores = sorted(t_scores, reverse=True)
    Vn_maxi = t_ordre_scores[0]
    Vn_mini = t_ordre_scores[len(t_ordre_scores) - 1]
    print("la valeur la plus grande est", Vn_maxi)

# ---------------------------------
# Détermine la valeur et le joueur avec le meilleur score qui va donner ses jetons au moins bon score
# Détermine la valeur et le joueur avec le pire score qui va récupérer ler jetons du joueur avec le meilleur score
# ---------------------------------

    if t_ordre_scores[0] == t_ordre_scores[1]:
        print("Égalité")
    else:
        Vn_jetons = 0
        while Vn_maxi != Vn_jetons:
            for Vn_jetons in t_scores:
                if Vn_jetons == Vn_maxi:
                    if Vn_maxi >= t_jetons[Vn_x]:
                        Vn_maxi = t_scores[Vn_x]
                        t_jetons[Vn_x] = 0
                        print(t_pseudo_player[Vn_x], "tu n'as plus de jetons : tu es notre vainqueur !!")
                        t_ordre_jetons = sorted(t_jetons, reverse=True)
                        break
                    else:
                        t_jetons[Vn_x] -= Vn_maxi
                        print(t_pseudo_player[Vn_x], "tu as", t_jetons[Vn_x], "jetons")
                        t_ordre_jetons = sorted(t_jetons, reverse=True)
                        break
                else:
                    Vn_x += 1
        Vn_jetons = 0
        Vn_x = 0
        while Vn_mini != Vn_jetons:
            if t_ordre_scores[len(t_ordre_scores) - 1] == 0:
                t_ordre_jetons = sorted(t_jetons, reverse=True)
                break
            for Vn_jetons in t_scores:
                if Vn_jetons == Vn_mini:
                    t_jetons[Vn_x] += t_ordre_scores[0]
                    print(t_pseudo_player[Vn_x], "tu as", t_jetons[Vn_x], "jetons")
                    t_ordre_jetons = sorted(t_jetons, reverse=True)
                    break
                else:
                    Vn_x += 1

