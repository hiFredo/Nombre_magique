import random 
NOMBRE_MIN= 1 
NOMBRE_MAX= 10 

NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN,NOMBRE_MAX) 
def demander_nombre(nb_min,nb_max):
    nombre_int= 0 
    while nombre_int ==0 :
        print() 
        nombre_str= input(f"Quelle est le nombre magique entre ( {nb_min} et {nb_max} ) ? ")
        try :
            nombre_int = int(nombre_str)
            
        except: 
            print("ERREUR : vous devez rentre un nombre. Réessayer  ") 
        else :
            if nombre_int > nb_max  or nombre_int < nb_min:
                print(f"ERREUR : Le  nombre doit etre  entre ({nb_min} et {nb_max})  ") 
                nombre_int = 0 
    return nombre_int   

while True:
    nombre = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)
    
    if nombre>NOMBRE_MAGIQUE :
        print("Le nombre magique est plus petit")

    elif nombre<NOMBRE_MAGIQUE : 
        print("Le nombre magique est plus grand")
    else :
        break
                
print("Bravo, vous avez gagné !") 

