
                        self.cartes[self.cartes.index(carte_actuelle)] = carte_pioche
                    else:
                        erreur = True
                        print(carte_pioche)
                        print('C\'est faux !')
                        self.deck.ajout_carte(carte_actuelle)
                        self.deck.battre()
                        self.cartes[self.cartes.index(carte_actuelle)] = carte_pioche
                        break
                elif réponse == 'moins' or réponse == "-" or réponse == 'Moins':
                    carte_pioche = self.deck.pop_carte()
                    if carte_actuelle.valeur > carte_pioche.valeur:
                        print(carte_pioche)