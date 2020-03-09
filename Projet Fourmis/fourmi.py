"""
Alexandre & Thomas, le 09/03/20
"""

class Fourmi():

    def __init__(self, alpha, beta, gamma, position, food):
        """
        @param : alpha, beta, gamma -> réels qui donnent les caractéristiques de la fourmi
                 food -> booléen si la fourmi porte ou non de la nourriture
        """

        self.__alpha = alpha
        self.__beta = beta
        self.__gamma = gamma
        self.__food_fourmi = food   #Boolean
        self.__position = Nid
        self.__destination = Nid
        self.__routes_rempruntees = []
        self.__distance_a_parcourir = 0

    def get_position(self):
        return(self.__position)

    def set_position(self,position):
        self.__position = position

    def avancer(self):
        d = self.__distance_a_parcourir
        d -= 1
        if d<0:
            ville = self.__routes_rempruntees[-1].get_arrival()
            self.__position = ville
            self.action_en_ville(ville)

    def action_en_ville(self, ville):
        # Vérifier qu'il y a de la nourriture
        if not self.__food_fourmi:
            if ville.get_food() > 0:
                self.__villearrivee.moins_food()
                self.__food_fourmi = True
                self.revenir_nid()
            else:
                self.decider_route()


    def laisser_au_nid(self, ville):
        if est_nid(ville):
            ville.plus_food()

    def revenir_nid(self,ville):
        "test"

    def deposer_pheromone(self, Route):
        Route.incremente_pheromone()


    def decider_route(self, Routes):
        #Routes est la liste des objet Route adjacent à la ville ou on se trouve
        pheromones = []
        #pheromones est la liste des phéromones de ces routes
        for i in range(len(Routes)):
            pheromones.append(Routes[i].get_pheromone())
        return(Routes[argmax(pheromones)])
