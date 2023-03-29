import random

#print("Número aleatorio del 1 al 1000: ",random.randrange(1000))
#print("Lista aleatoria de números entre el 1 y el 1000: ",random.sample#(range(1000),3))
#print("Número aleatorio con coma flotante: ",random.random())
#print("Elección aleatoria [Python,Java,C#,Ruby,Go]: ",random.choice(["Python","Java","C#","Ruby","Go"]))

import statistics

print("The mean of 5,3,7,9,4,2,2 is: ",statistics.mean([5,3,7,9,4,2,2]))
print("\nThe median of 5,3,7,4,2,2 is: ",statistics.median([5,3,7,4,2,2]))
print("\nThe inferior median of 2,2,3,4,5,7 is: ",statistics.median_low([2,2,3,4,5,7]))
print("\nThe high median of 2,2,3,4,5,7 is: ",statistics.median_high([2,2,3,4,5,7]))
print("\nThe mode of 2,2,3,4,5,7 is: ",statistics.mode([2,2,3,4,5,7]))
print("\n\tThe variance of 2,2,3,4,5,7 is: ",statistics.variance([2,2,3,4,5,7]))






