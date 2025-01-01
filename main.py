import random 
NOMBRE_MIN= 1 
NOMBRE_MAX= 10 
NB_VIE = 4

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
# nombre = 0 
# while not nombre==NOMBRE_MAGIQUE and NB_VIE>0  :
#     nombre = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)
#     print(f"Il vous reste {NB_VIE} vie ")
#     if nombre==NOMBRE_MAGIQUE :
#         print("Bravo, vous avez gagné !")

#     elif nombre<NOMBRE_MAGIQUE : 
#         print("Le nombre magique est plus grand")
#         NB_VIE-=1

#     else :
#         print("Le nombre magique est plus petiT")
#         NB_VIE-=1
    
# if NB_VIE == 0 :
#     print(f"Vous avez perdue ! le nombre magique était : {NOMBRE_MAGIQUE} ") 

gagne=False
for i in range(0,NB_VIE):
    vies= NB_VIE-i
    nombre = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)
    print(f"Il vous reste {vies} vie ")
    if nombre==NOMBRE_MAGIQUE :
        print("Bravo, vous avez gagné !")
        gagne=True
        break

    elif nombre<NOMBRE_MAGIQUE : 
        print("Le nombre magique est plus grand")
        

    else :
        print("Le nombre magique est plus petiT")
        
    
# if vies == 0 :
if not gagne : 
    print(f"Vous avez perdue ! le nombre magique était : {NOMBRE_MAGIQUE} ")   
            





