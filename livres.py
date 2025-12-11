# Structure initiale
bibliotheque = []

def ajouter_livre(titre : str, auteur : str):
    '''
    Docstring for ajouter_livre
    
    :param titre: Le titre du livre que vous désirez ajouter
    :type titre: str
    :param auteur: L'auteur de ce livre
    :type auteur: str
    '''
    # Vérifie qu'il n'y ait pas deux fois le même livre
    for livre in bibliotheque:
        if livre ["titre"] == titre:
            print("Ce livre est déjà dans votre bibliothèque")
            return
        
    livre = {"titre" : titre, "auteur" : auteur}
    bibliotheque.append(livre)
    print(f"Le livre {titre} a été ajouté avec succès !")


def afficher_livres():
    if not bibliotheque:
        print("La bibliothèque est vide.")
    else:
        print("Liste des livres:")
        for i, livre in enumerate(bibliotheque, 1):
            print(f"{i}. {livre['titre']} par {livre['auteur']}")


def rechercher_livre(titre):
    pass