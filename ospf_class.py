class Reseau:
    def __init__(self,zones):
        self.liste_zone = zones             #liste de toutes les zones

    def initialisation(self):
        '''
        Lance la phase d'initialisation du reseau. Lance la méthode 'init_zone' de chaque zone contenues dans self.liste_zone, et attend que chacune d'entre elles return True avant de lancer
        les envois de paquets.
        '''
        pass


class Zone:
    def __init__(self,routeurs):
        self.liste_routeurs = routeurs      #liste de tous les routeurs de la zone

    def init_zone(self):
        '''
        Viens lancer l'initialisation de chaque routeur. Lorsque tous les routeurs possèdent une vue complète sur la topologie de la zone, renvoie True à la fonction 'initialisation' de la
        class Reseau
        '''
        pass


class Routeur:
    def __init__(self,name,lsbd,links,status):
        self.name = name
        self.lsbd = lsbd
        self.links = links              #liste des liens auquel le routeur est lié. Chaque élément de la liste est un objet représentant de la class Link
        self._status = status           #les routeurs peuvent être en panne ou fonctionnels
        self.voisins = []               #liste vide qui se remplira des voisins du routeur
        self.plus_courts_chemins = []   #liste vide qui se remplira des plus courts chemins en fin d'initialisation de la zone
    
    def get_status(self):
        return self._status
    def set_status(self,val):
        if val in ["Up","Down"]:
            self._status = val
    status = property(get_status,set_status)

    def hello(self):
        '''
        Le routeur parcours chacun de ses liens (self.links) et envoie un message dans chacun d'entre eux. Il déclenche la méthode 'destination_hello' du link
        visé, [... pas encore certains de la suite]
        '''

        pass


class ABR(Routeur):
    def __init__(self, name, lsbd, links, status):
        super().__init__(name, lsbd, links, status)

    def view_zones(self):
        '''
        Méthode déclenchée lorsque l'ABR recevra un paquet à envoyer vers une autre zone. Elle viendra consulter les ABR de toutes les autres zones, de sorte à 
        pouvoir localiser la cible du paquet. Alors, elle demandera à l'ABR de la bonne zone sa liste des plus courts chemins.
        '''
        pass


class Link:
    def __init__(self,vitesse,status,p1,p2):
        self.vitesse = vitesse
        self._status = status
        self.parents = (p1,p2)

    def get_status(self):
        return self._status
    def set_status(self,val):
        if val in ["Up","Down"]:
            self._status = val
    status = property(get_status,set_status) 


    def destination_hello(self,R):
        '''
        Méthode déclenchée par la méthode 'hello' de la class Routeur. R est le routeur ayant envoyé le message Hello. La fonction retourne None si le Routeur destination est en panne. Sinon, elle en retourne
        le nom
        '''
        pass