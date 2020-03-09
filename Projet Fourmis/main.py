import fourmi
import pays

Paris = Ville(0, 0, 10, "Paris")
Nid = Paris
Bordeaux = Ville(-10, -33, 2, "Bordeaux")
Toulouse = Ville(-2, -10, 463, "Toulouse")
Lyon = Ville(21, -5, 134, "Lyon")
Marseille = Ville(20, -35, 1, "Marseille")
Lille = Ville(5, 13, 298, "Lille")


France = Pays(Nid)
France.ajouter_villes(Bordeaux)
France.ajouter_villes(Toulouse)
France.ajouter_villes(Lyon)
France.ajouter_villes(Marseille)
France.ajouter_villes(Lille)

A10 = Route(Paris,Bordeaux)
A6 = Route(Paris,Lyon)
A89 = Route(Bordeaux,Lyon)
A7 = Route(Lyon,Marseille)
A3 = Route(Paris,Lille)
A87 = Route(Marseille,Toulouse)

France.afficher_pays()
