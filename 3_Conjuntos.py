#Dados dos conjuntos, A y B, escribe un programa en Python que imprima el
#conjunto de los elementos que se encuentran en A o en B, pero no en ambos.

conjuntoA = {"Juan", "Pedro", "Maria", "Jose"}   
conjuntoB = {"Esteban","Carlos", "Maria"} 
print(conjuntoA.symmetric_difference(conjuntoB))
  
