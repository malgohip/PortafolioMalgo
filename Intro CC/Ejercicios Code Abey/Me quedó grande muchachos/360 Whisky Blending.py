#Author: Sebastian Ochoa. Date: 08/21/2024
# -*- coding: utf-8 -*-

"""
Whisky is matured in casks but every cask, even for the same whisky, gives rise to a distinctly different final result. When whisky is put into bottles for sale it is necessary for the contents of all bottles carrying the same label to contain identical contents. In order to achieve this the contents of different casks are mixed in order to create a large volume of whisky with the same overall characteristics. There is much more to the blending process than this but, for the purpose of this problem, we will concentrate on the process of mixing two different samples of whisky, from different casks.

To keep things simple we will consider only the alcohol content of the whisky. This is one of the items on the bottle label so this must be the same for all bottles having the same label. The alcohol strength of the whisky is given by its ABV value which denotes the percentage by volume of the whisky which is alcohol. Normal bottles have values around 40 but specialist whiskies can have values up to 70 or more.

Suppose that we want to create 500 litres of whisky with a strength of 46 and that we have available 250 litres of whisky of strength 40 and 400 litres of whisky of strength 50. We can create the necessary 500 litres with strength 46 by mixing 200 litres of strength 40 with 300 litres of strength 50. This is easily demonstrated by the following calculation:

(200*40 + 300*50)/500 = 46
Note that the division by 500 results from the fact that the total volume of whisky in the mixture is now 500 litres. Clearly we did not use all of the whisky from the two available samples but these can always be used in another mixing later.

Next suppose that we want to create 520 litres of whisky with a strength of 65. We have available 250 litres of whisky with strength 70 and 400 litres of whisky with strength 40. Although the total volume of whisky is greater than the required 520 litres there is no combination of the two whiskies which will provide the required strength.

You will be given a number of sets of data. Each of these will have a target strength and quantity for the mixture. You will be provided with two different whiskies (along with their strength and volume). You need to determine whether or not it is possible to create the required target (both strength and volume).

Input and Answer
The first line of the problem will be a single integer N denoting the number of test cases. Each of the following N lines will hold 7 separate integer values. The first of these is the number of the test case. The next 6 are (in order) target strength, target volume, sample 1 strength, sample 1 volume, sample 2 strength, sample 2 volume. For each test case you must determine whether or not the target can be created. Give the numbers of the test cases where the target can be created, separated by spaces, as a single string.
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e360 Whisky Blending.txt','r')
P= a.readlines()

datos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    datos.append(F)

print(datos)
"""
data=[[1, 52, 1197, 40, 465, 60, 752], [2, 58, 700, 63, 721, 48, 712], [3, 54, 786, 52, 692, 70, 115], [4, 60, 750, 65, 772, 51, 599], [5, 70, 537, 73, 501, 40, 516], [6, 48, 610, 41, 626, 68, 606], [7, 68, 737, 68, 71, 68, 656], [8, 61, 545, 62, 525, 53, 253], [9, 46, 1167, 39, 251, 44, 945], [10, 64, 567, 64, 581, 48, 480], [11, 44, 598, 44, 586, 42, 322], [12, 40, 727, 43, 389, 36, 323], [13, 70, 991, 70, 717, 70, 289], [14, 64, 1063, 46, 142, 67, 1037], [15, 53, 840, 45, 724, 69, 277], [16, 50, 615, 45, 618, 55, 636], [17, 46, 749, 42, 371, 50, 679], [18, 43, 1034, 63, 223, 38, 815], [19, 43, 932, 60, 881, 46, 76], [20, 59, 558, 62, 580, 58, 425], [21, 46, 1070, 42, 973, 58, 797]]

def can_create_target(target_strength, target_volume, strength1, volume1, strength2, volume2):
    # Check if target strength is within the range
    if not (min(strength1, strength2) <= target_strength <= max(strength1, strength2)):
        return False

    # Calculate required total strength
    required_total_strength = target_volume * target_strength

    # Iterate through possible volumes of the first whisky
    for v1 in range(max(0, target_volume - volume2), min(volume1, target_volume) + 1):
        v2 = target_volume - v1
        if 0 <= v2 <= volume2:
            # Calculate total strength of the mixture
            total_strength = v1 * strength1 + v2 * strength2

            # Check if the mixture meets the target strength (with tolerance)
            if abs(total_strength - required_total_strength) < 0.001:
                return True

    return False

def process_data(data):
    results = []
    for i, line in enumerate(data[1:], start=1):  # Empezamos desde el segundo elemento (índice 1)
        target_strength, target_volume, strength1, volume1, strength2, volume2 = map(int, line.split()[1:])
        if can_create_target(target_strength, target_volume, strength1, volume1, strength2, volume2):
            results.append(i)
    return results

# Procesar los datos
data = [
    [46, 500, 40, 250, 50, 400],
    [65, 520, 70, 250, 40, 400],
    [71, 721, 57, 464, 71, 637],
    [49, 452, 60, 373, 42, 518]
]

# Procesar los datos
results = []
for i, line in enumerate(data, start=1):
    target_strength, target_volume, strength1, volume1, strength2, volume2 = line
    if can_create_target(target_strength, target_volume, strength1, volume1, strength2, volume2):
        results.append(i)

respuesta=''
for x in results:
    respuesta+=str(x)+' '
print(respuesta)