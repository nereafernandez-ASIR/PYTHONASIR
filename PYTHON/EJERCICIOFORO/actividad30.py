'''ejercicio cuadrado altura 9'''

rows = 9  
cols = 9  

for i in range(rows):
    for j in range(cols):
        if i % 2 == 0: 
            print("*", end=" ")
        else:
           
            if j % 2 == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()
