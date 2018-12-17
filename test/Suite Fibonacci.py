# == Fonction Suite de Fibonacci ==
 
"""
==== Programme de base en FOR ====
N = input("Entrer le maximum de la suite : ")

U=range(1,N*N)
U[0]=1
U[1]=1

for i in range(2,N+1) :
    U[i] = U[i-1] + U[i-2]

for i in range (0,N):
    print U[i]

"""

#Demande la valeur max
n = input("Entrer le maximum de la suite : ")


#Debug si entrée = 0 ou 1 ou 2
if n <=2:
    n = input ("Veuillez saisir une nombre superieur à 2 ")

#Debug si entrée = STRING / FLOAT
"""try:
    n = int(n)

except:
    print("Erreur de saisie")
"""    
#Fonction de traitement de la suite
def fiba(para):
    #Calcul de la suite
    r = range(1,n*n)
    #Set de la valeur 0 et valeur 1
    r[0]=1
    r[1]=1

    for i in range(2,n+1):
        r[i] = r[i-1] + r[i-2]

    for i in range (0,n):
        print r[i]

fiba(n)
# == FIN ===
