#Author: Sebastian Ochoa. Date: 08/21/2024
# -*- coding: utf-8 -*-

"""
Gradient is the same thing as derivative, but applied to function with more than one parameter. Physical meaning is just the characteristic of the slope at the given point (though it is hard to imagine for functions with 3 or more arguments) - its direction and steepness.

For example suppose we have a 2D function like the following:

f = f(x, y) = x * x + y * y
And we want to find the gradient value at point (1, 2). Let us calculate the value of the function at this point and then at two neighboring points with offset of dt = 0.1:

f(x0, y0)      = f(1.0, 2.0) = 1.0 * 1.0 + 2.0 * 2.0 = 5

f(x0 + dt, y0) = f(1.1, 2.0) = 1.1 * 1.1 + 2.0 * 2.0 = 5.21

f(x0, y0 + dt) = f(1.0, 2.1) = 1.0 * 1.0 + 2.1 * 2.1 = 5.41
The gradient is a vector of values, representing the tangent of the slope in each direction (by x and by y in our case):

g(x0, y0) = [(f(x0 + dt, y0) - f(x0, y0)) / dt, (f(x0, y0 + dt) - f(x0, y0) / dt] =
          = [(5.21 - 5.00) / 0.1, (5.41 - 5.00) / 0.1] =
          = [2.1, 4.1]
Of course this way of calculations will give precise value for gradient only when dt is infinitesimal (i.e. "non-measurably small" or "infinitely small") - though for practical reasons we can use some finitely small values, like 1e-9 and calculate gradient with given precision.

Slope direction

The direction of the resulting vector, i.e. in our case:

atan2(4.1, 2.1) = 63 degrees from axis X, counterclockwise
is the direction in which the slope at this point raises most steeply. At the same time the reverse direction is the one of the fastest descent from this point. This still works for functions with more than two arguments, i.e. for spaces with more dimensions - though it is hard to imagine visually.

We now are going to practice calculation of gradient with a small program - this is important for some further tasks (i.e. ones about searching for minimums with fastest descent path etc).

Problem statement
You are given a function in the form (with A, B and C being some constants):

f = f(x, y) = (x - A)^2 + (y - B)^2 + C * exp(- (x + A)^2 - (y + B)^2)
It looks like a wide bowl having small peak somewhere inside, see the pictures above.

You will be given some points, as pairs of coordinates (x, y) and asked about the direction of the descent from this point.

Input data will contain four values in the first line: N - the number of points, then constants A, B and C.
Next lines will contain one point each, as a pair of cooridnates X and Y.
Answer should give integers in range from 0 to 360 - the direction of the descent of the slope in each of the points, expressed in degrees and rounded to whole integers.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e101 Gradient Calculation.txt','r')
P= a.readlines()

l=P[0].strip().split()
A=float(l[1])
B=float(l[2])
C=float(l[3])
puntos=[]
for x in range(1,int(l[0])+1):
    f=P[x].strip().split()
    F=[]
    for x in f:
        X=float(x)
        F.append(X)
    puntos.append(F)
puntos.append(list((A,B,C)))

print(puntos)
"""
puntos=[[0.7, 0.6], [0.9, -0.3], [-0.7, -0.1], [-0.3, -0.5], [0.5, -0.4], [-0.9, 0.3], [-0.5, 0.5], [0.6, 0.6], [0.2, 0.9], [-0.7, 0.6], [-1.0, -0.5], [0.7, 0.9], [-0.2, 0.8], [-0.8, 0.3], [1.0, -0.4], [-0.9, -0.1], [-0.4, -0.2, 5.0]]

k=puntos.pop(-1)
A=k[0]
B=k[1]
C=k[2]

import math

def calculate_gradient(x, y, A, B, C, dt=1e-9):
    def f(x, y):
        return (x - A)**2 + (y - B)**2 + C * math.exp(- (x + A)**2 - (y + B)**2)

    df_dx = (f(x + dt, y) - f(x, y)) / dt
    df_dy = (f(x, y + dt) - f(x, y)) / dt
    
    return df_dx, df_dy

def direction_of_descent(df_dx, df_dy):
    angle = math.atan2(-df_dy, -df_dx)
    angle_degrees = math.degrees(angle)
    angle_degrees = (angle_degrees + 360) % 360 
    return round(angle_degrees)

respuesta=''
for x in puntos:
    df_dx, df_dy = calculate_gradient(x[0], x[1], A, B, C)
    direction = direction_of_descent(df_dx, df_dy)
    respuesta+=str(direction)+' '
print(respuesta)