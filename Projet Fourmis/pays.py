"""
Alexandre & Thomas, le 09/03/20
"""

import numpy as np

class Pays:
    def __init__(self, Nid):

        self.__nid = Nid
        self.__villes = []

    def ajouter_villes(self, ville):
        self.__villes.append(ville)

    def afficher_pays(self):
        for ville in self.__villes:
            ville.afficher_ville()


class Ville:
    def __init__(self, x, y, food, nom):
        """
        @params : x,y : position
                  food : quantité de nourriture
        """

        self.__nom = nom
        self.__x = x
        self.__y = y
        self.__quantite_food = food #int
        self.__routes = []

    def get_position(self):
        return([self.__x, self.__y])

    def get_food(self):
        return(self.__quantite_food)

    def plus_food(self):
        self.__quantite_food += 1

    def get_nom(self):
        return(self.__nom)

    def moins_food(self):
        self.__quantite_food -= 1

    def est_nid(self):
        if self.__x == 0 and self.__y == 0:
            return True
        else:
            return False

    def ajouter_route(self, route):
        self.__routes.append(route)

    def afficher_destinations_possibles(self):
        destinations_possibles = []
        for route in self.__routes:
            destinations_possibles.append(route.get_arrival(self).get_nom())
        return(destinations_possibles)

    def afficher_ville(self):
        print("Nom : ", self.__nom)
        print("Position : ", [self.__x,self.__y])
        print("Food : ", self.__quantite_food)
        print("Routes : ", self.afficher_destinations_possibles())
        print("\n")


class Route:
    def __init__(self, ville1, ville2):

        self.__villes = [ville1, ville2]
        ville1.ajouter_route(self)
        ville2.ajouter_route(self)
        self.__trace = 0

    def get_arrival(self, ville_depart):
        if ville_depart == self.__villes[0]:
            return(self.__villes[1])
        else:
            return(self.__villes[0])

    def longueur(self):
        [x1, y1] = self.get_departure().get_position()
        [x2, y2] = self.get_arrival().get_position()
        return np.sqrt((x2-x1)**2+(y2-y1)**2)

    def incremente_pheromone(self):
        self.__trace += 1

    def get_pheromone(self):
        return(self.__trace)

    def dissipation_pheromone(self, rho):
        """
        @params : rho -> facteur d'évaporation
        """
        self.__trace = (1-rho) * self.__trace
