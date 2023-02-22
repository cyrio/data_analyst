carre_test = [[4,14,15,1],
              [9,7,6,12],
              [5,11,10,8],
              [16,2,3,13]]

def is_magic(unCarre):
    dimension = len(unCarre)
    # somme de chaque ligne
    somme_test = sum(unCarre[0])
    for row in unCarre:
        if sum(row)!= somme_test:
            return False
    print('test lignes validé')

    # somme de chaque colonne
    for x in range(dimension):
        somme_colonne = 0
        for y in range(dimension):
            somme_colonne = somme_colonne + unCarre[x][y]
        if somme_colonne != somme_test:
            return False
    print('test colonnes validé')

    # somme des diagonales
    somme_diag1 = 0
    somme_diag2 = 0
    for i in range(dimension):
        somme_diag1 = somme_diag1 + unCarre[i][i]
        somme_diag2 = somme_diag2 + unCarre[dimension-1-x][i]
    if somme_diag1 != somme_test or somme_diag2 != somme_test:
        return False
    print('test diagonales validé')

    # Bonus : vérification de l'unicité des nombres
    liste_nombres =[]
    for uneligne in unCarre :
        for unelement in uneligne:
            if unelement not in liste_nombres:
                liste_nombres.append(unelement)
            else :
                return False
    print('test unicité validé')
    
    return True

print(is_magic(carre_test))
