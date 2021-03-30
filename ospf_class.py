class Reseau:
    def __init__(self,zones):
        self.liste_zones = zones             #liste de toutes les zones

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
        Le routeur envoie un message hello comprennant sa lsbd (table de relation) vers tous ses sous liens (self.links). La méthode 'destination_hello' de la class Link enverra le message
        à l'autre extrémité du lien (avec en paramètre self.name)
        '''
        pass

    def envoi_paquet(self):
        '''
        Le routeur envoie simplement vers une destination de son choix. Via les relations déterminées dans la méthode 'plus_courts_chemins', et possiblement la méthode 'view_zone',
        le paquet pourra partir de son origine jusqu'à sa destination.
        '''
        pass

    def recevoir_paquet(self,type):
        '''
        Si le paquet reçu est un paquet hello, le routeur met à jour sa table de routage. Par ailleurs, s'il voit dans le message reçu apparaître son propre nom, il ajoutera le nom du routeur ou
        sous-réseau ayant envoyé le message comme l'un de ses voisins (self.voisins)
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

    #De manière globale, si self.status == 'Down', les fonctions renverront à celui qui les a input un message d'erreur (via une fonction pas encore définie : recevoir_erreur()) 

    def destination_hello(self,R):
        '''
        Méthode déclenchée par la méthode 'hello' de la class Routeur. R est le routeur ayant envoyé le message Hello. Lance soit la méthode 'recevoir_paquet()' de la class Routeur, soit la méthode
        'transmission_hello' de la class Sous-Reseau
        '''
        pass


class Sous_Reseau():
    def __init__(self):
        self.links = links
        self.voisins = voisins
        #un peu obscure...

    def transmission_hello(self):
        '''
        Lorsqu'un sous-reseau reçoit un paquet hello, il l'envoie à travers tous ses liens vers d'autres destinations pour le propager. Il déclenchera alors la méthode 'destination_hello' de la class Link
        (la même méthode qui l'a lancé)
        '''
        pass
