#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
Brethren of CodeAbbey are running several small businesses to support the Monastery. One of them is the Winemaking.

One of the interesting issues here is that the price of the wine is not constant. At some years customers are ready to buy more barrels and pay higher, while at other years they are reluctant and brotherhood needs to lower prices to get rid of wine stores.

It was found that the reason for such behavior is simple - after rainy years grapes yield wine of better quality and people are more eager to purchase it.

This gives monks the idea - they need to find the formula for calculating more just price depending on weather records from the preceeding year, so that trade will run more smoothly. (the wine which is sold this year was prepared from the grapes picked the year before)

You are to help them in finding this formula. To keep things simple let us try approximating the dependency with the linear function in the form

Y = K * X + B
Where X is the amount of rainy days and Y is the price.

Problem statement
You will be given a list of records, each containing the number of rainy days during previous year along with the average price for which the wine was sold during current year.

Use the Simple Linear Regression and criteria of the Ordinary Least Squares to find parameters of the linear function which can approximate the dependence between price and amound of rainy days.

Input agnos contains starting A and ending B year in the first line.
Then lines follow for each year in form YYYY: D P where YYYY is the mark of year, D is the number of rainy days (in previous season) and P is the wine price (in crowns per barrel).
Answer should contain values for K and B with accuracy of 1e-7 or better.
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e95 Simple Linear Regression.txt','r')
P= a.readlines()

l=P[0].strip().split()
agnos={}
for x in range(int(l[0]),int(l[1])):
    pos=x-int(l[0])+1
    f=P[pos].strip().split()
    F=[]
    for y in range(len(f)):
        if y != 0:
            Y=int(f[y])
            F.append(Y)
    agnos[x]=F

print(agnos)
"""
agnos={1926: [62, 226], 1927: [146, 411], 1928: [78, 260], 1929: [78, 322], 1930: [112, 341], 1931: [138, 389], 1932: [77, 241], 1933: [70, 252], 1934: [54, 207], 1935: [127, 368], 1936: [150, 399], 1937: [59, 219], 1938: [78, 258], 1939: [63, 199], 1940: [111, 315], 1941: [85, 240], 1942: [112, 355], 1943: [75, 256], 1944: [91, 271], 1945: [114, 353], 1946: [65, 230], 1947: [123, 314], 1948: [117, 345], 1949: [147, 408], 1950: [55, 219], 1951: [103, 309], 1952: [76, 242], 1953: [89, 282], 1954: [80, 241], 1955: [75, 271], 1956: [125, 359], 1957: [74, 242], 1958: [120, 354], 1959: [62, 215], 1960: [144, 400], 1961: [87, 264], 1962: [60, 250], 1963: [64, 235], 1964: [66, 199], 1965: [111, 331], 1966: [72, 247], 1967: [122, 358], 1968: [82, 269], 1969: [116, 377], 1970: [148, 416], 1971: [105, 350], 1972: [66, 238], 1973: [106, 323], 1974: [90, 291], 1975: [145, 393], 1976: [110, 353], 1977: [140, 402], 1978: [92, 297], 1979: [103, 306], 1980: [150, 416], 1981: [75, 253], 1982: [101, 320], 1983: [74, 298], 1984: [104, 317], 1985: [83, 322], 1986: [102, 277], 1987: [69, 237], 1988: [119, 353], 1989: [74, 283], 1990: [94, 326], 1991: [55, 213], 1992: [135, 418], 1993: [51, 204], 1994: [137, 385], 1995: [98, 268], 1996: [139, 404], 1997: [139, 401], 1998: [146, 390], 1999: [97, 357], 2000: [85, 203], 2001: [148, 415], 2002: [97, 302], 2003: [108, 400], 2004: [110, 327], 2005: [88, 279], 2006: [55, 266], 2007: [142, 390]}

def linear_regression(data):
    N = len(data)
    sum_x = sum(value[0] for value in data.values())
    sum_y = sum(value[1] for value in data.values())
    sum_xx = sum(value[0]**2 for value in data.values())
    sum_xy = sum(value[0] * value[1] for value in data.values())
    K = (N * sum_xy - sum_x * sum_y) / (N * sum_xx - sum_x**2)
    B = (sum_y - K * sum_x) / N
    
    return K, B

respuesta=''
for x in linear_regression(agnos):
    respuesta+=str(x)+' '
print(respuesta)