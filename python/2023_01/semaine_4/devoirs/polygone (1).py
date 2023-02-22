


class Polygone:

    def __init__(self,sommets,couleur):
        self.sommets = sommets
        self.couleur = couleur
    
    def __str__(self):
        chaine =""
        for i in self.sommets:
            chaine += " " + str(i)
        return f" Polygones {self.couleur} de sommets {chaine}"
    
    def __repr__(self):
        chaine =""
        for i in self.sommets:
            chaine += " " + repr(i)
        return f"{self.__class__.__name} de points {chaine} de couleur {self.couleur}"
   
    def __len__(self):
        ''' Renvoie le nombre de sommets du polygone'''
        return len(self.sommets)
    
    
    def perimetre(self):
        distance = 0
        for i in range(len(self.sommets)-1):
            distance += self.sommets[i].distance(self.sommets[i+1])
        return distance
    
  
    
    
def main():
    p1 = Point(0,0)
    p2 = Point(0,1)
    p3 = Point(1,0)
    p4 = Point(1,1)
    sommets = [p1,p2,p3,p4]
    couleur ="bleu"
    monpoly = Polygone((sommets), couleur)
    print(monpoly)
    print(len(monpoly))

if __name__ == '__main__':
    main()