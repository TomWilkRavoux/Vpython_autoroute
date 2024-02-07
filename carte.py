import random


class Carte:
    noms_valeurs = [None, 'as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi']
    noms_couleurs = ['trèfle', 'carreau', 'cœur', 'pique']

    def __init__(self, valeur=0, couleur=2):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return '%s de %s' % (self.noms_valeurs[self.valeur], self.noms_couleurs[self.couleur])

    def __lt__(self, other):
        return self.valeur < other.valeur


class Deck:
    def __init__(self):
        self.cartes = []
        for couleur in range(4):
            for valeur in range(1, 14):
                carte = Carte(valeur, couleur)
                self.cartes.append(carte)

    def __str__(self):
        res = []
        for carte in self.cartes:
            res.append(str(carte))
        return '\n'.join(res)

    def pop_carte(self):
        a = self.cartes.pop()
        return a

    def retirer_carte(self):
        return self.cartes.pop(0)

    def ajout_carte(self, carte):
        self.cartes.append(carte)

    def battre(self):
        random.shuffle(self.cartes)

        
    def carte_supérieure(self):
        if self.cartes:
            return self.cartes[-1]
        else:
            return None

    def carte_inférieure(self):
        if self.cartes:
            return self.cartes[0]
        else:
            return None

class Plateau:
    def __init__(self, deck):
        self.deck = deck
        self.cartes = []

    def tirer_6_cartes(self):
        self.cartes = []
        for _ in range(6):
            carte = self.deck.retirer_carte()
            self.cartes.append(carte)

    def afficher_prise(self):
        print('Voici votre prise :')
        for carte in self.cartes:
            print(carte)

    def reset(self):
        self.cartes = []

    def jouer(self):

        carte_pioche = None
        while True:
            for carte in self.cartes:
                carte_actuelle = carte
                for carte in self.cartes:
                 print(carte, end='      ')
                print()
                print("****************")
                print('La carte actuelle est : ',carte_actuelle)
                print("****************")
                

                réponse = input('Plus, moins ou egal ? ')
                print("****************")
                print("\n")

                if réponse == 'plus' or réponse == "+":
                    carte_pioche = self.deck.pop_carte()
                    if carte_actuelle.valeur < carte_pioche.valeur:
                        print('Carte piochée = ',carte_pioche, '\nLa réponse est bonne bien jouée chacal tu bois pas tous mes respects')
                        print("****************")
                        print("\n")
                        self.deck.ajout_carte(carte_actuelle)
                        self.deck.battre()
                        self.cartes[self.cartes.index(carte_actuelle)] = carte_pioche
                    else:
                        erreur = True
                        print('Carte piochée = ',carte_pioche, '\nLa réponse est fausse dommage tu es nul bois pour oublier')
                        print("****************")
                        print("\n")
                        self.deck.ajout_carte(carte_actuelle)
                        self.deck.battre()
                        self.cartes[self.cartes.index(carte_actuelle)] = carte_pioche
                        break
                elif réponse == 'moins' or réponse == "-":
                    carte_pioche = self.deck.pop_carte()
                    if carte_actuelle.valeur > carte_pioche.valeur:
                        print('Carte piochée = ',carte_pioche, '\nLa réponse est bonne bien jouée chacal tu bois pas tous mes respects')
                        print("****************")
                        print("\n")
                        self.deck.ajout_carte(carte_actuelle)
                        self.deck.battre()
                        self.cartes[self.cartes.index(carte_actuelle)] = carte_pioche
                    else:
                        erreur = True
                        print('Carte piochée = ',carte_pioche, '\nLa réponse est fausse dommage tu es nul bois pour oublier')
                        print("****************")
                        print("\n")
                        self.deck.ajout_carte(carte_actuelle)
                        self.deck.battre()
                        self.cartes[self.cartes.index(carte_actuelle)] = carte_pioche
                        break
                elif réponse == 'egale' or réponse == '=':
                        carte_pioche = self.deck.pop_carte()
                        if carte_actuelle.valeur == carte_pioche.valeur:
                            print('Carte piochée = ',carte_pioche, '\nLa réponse est bonne bien jouée chacal tu bois pas tous mes respects')   
                            print("****************")
                            print("\n")
                            self.deck.ajout_carte(carte_actuelle)
                            self.deck.battre()
                            self.cartes[self.cartes.index(carte_actuelle)] = carte_pioche
                        else:
                            erreur = True
                            print('Carte piochée = ',carte_pioche, '\nLa réponse est fausse dommage tu es nul bois pour oublier')
                            print("****************")
                            print("\n")
                            self.deck.ajout_carte(carte_actuelle)
                            self.deck.battre()
                            self.cartes[self.cartes.index(carte_actuelle)] = carte_pioche
                        break                            
                else:
                    print('Réponse incorrecte.')
                    break
            if erreur:
                self.cartes = self.cartes[:]
                erreur = False
                continue
            else:
                break


paquet = Deck ()

paquet.battre()

game = Plateau(paquet)
game.tirer_6_cartes()
game.jouer()






