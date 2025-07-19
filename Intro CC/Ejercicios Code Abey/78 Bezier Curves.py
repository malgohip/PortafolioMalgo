#Author: Sebastian Ochoa. Date: 08/19/2024
# -*- coding: utf-8 -*-

"""
Bezier curves are shapes very popular in computer design. They could be found among instruments in almost any image editor, including Microsoft Paint presented with any version of Windows.

Initially they were invented by engineers working on design of car bodies at automobile industry. Now we will try to learn how to create such curves programmatically.

Algorithm

The curve is defined by starting, ending and several intermediate points. The example above have 4 points - i.e. only 2 intermediate.

At first step we draw a polyline between these points, from starting via all intermediate in order to the ending one. It is shown with thin grey line at the picture.

Now suppose we choose some parameter alpha in range 0 ... 1 and divide each segment of the polyline according to it, i.e. in ratio:

alpha : (1 - alpha)
For example, in the drawing above alpha = 0.333.

For polyline drawn between N points and consisting of N - 1 segments we get N - 1 new points - they are shown as small purple dots at the leftmost picture.

Let us link these new points with new polyline, consisting of N - 2 segments. It is shown as thin blue line at the central and right-most pictures.

Then we can divide these new segments with the same ratio alpha once more. So we build a third polyline (shown in green at the rightmost picture).

We will continue building polylines until we get the last one consisting of only one segment. When we divide it with the ratio alpha, we get a single point.

This last point is the point of the Bezier Curve corresponding to parameter alpha.

The remaining is simple - just repeat these steps for different values of alpha - for example:

alpha = 0.00, 0.01, 0.02, 0.03, ... , 0.98, 0.99, 1.00
So that for example with 101 value (from 0 to 1 with the step of 0.01) we get the same amount of points, placed closely enough to each other. Connecting them we get the smooth curve (thick grey line at the rightmost picture).

Please refer to wikipedia article for more examples and animated demo.

Input data will contain the number of initial points M and the number N of values for parameter alpha.
Next M lines will contain coordinates of one initial point each (X and Y).
Answer should contain N pairs of coordinates (also X and Y) for all calculated points lying on the given curve. Pairs and points in them should be separated simply by space. Coordinates should be rounded to nearest integer (because when we do graphics coordinates of pixels are of course integer).

Note: the values for alpha should be calculated by dividing the range 0.0 ... 1.0 into N - 1 equal steps.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e78 Bezier Curves.txt','r')
P= a.readlines()

l=P[0].strip().split()
rangos=[]
for x in range(1,int(l[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=int(x)
        F.append(X)
    rangos.append(F)
rangos.append(int(l[1]))
print(rangos)
"""
rangos=[[438, 507], [286, 767], [515, 633], [821, 757], [689, 479], [709, 238], [491, 419], [267, 314], 38]

M=rangos.pop(-1)
def bezier_point(points, alpha):
    while len(points) > 1:
        new_points = []
        for i in range(len(points) - 1):
            x = (1 - alpha) * points[i][0] + alpha * points[i + 1][0]
            y = (1 - alpha) * points[i][1] + alpha * points[i + 1][1]
            new_points.append((x, y))
        points = new_points
    return points[0]

def bezier_curve(points, N):
    result = []
    for i in range(N):
        alpha = i / (N - 1)
        point = bezier_point(points, alpha)
        result.append((round(point[0]), round(point[1])))
    return result

respuesta=''
for x in bezier_curve(rangos,M):
    for y in x:
        respuesta+=str(y)+' '
print(respuesta)