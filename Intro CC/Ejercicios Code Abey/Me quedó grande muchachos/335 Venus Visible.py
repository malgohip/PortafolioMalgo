#Author: Sebastian Ochoa. Date: 08/21/2024
# -*- coding: utf-8 -*-

"""
Problem Statement
Our goal is to figure out at which position Venus sends maximum light to the Earth! Of course when it is too close to the Sun its light is obscured by daylight, but for the sake of calculations let's ignore this fact (suppose we are observing it from the top of Everest mountain where athmosphere is less dense).

This amount of light depends on two factors - the phase of the Venus, and its distance to us. Consider the diagram below to clarify this.

Venus, Sun and Earth positions in space

Let's assume the orbits of the Earth and Venus are perfect circles (they are slightly elliptical in fact) so that the distances from them to the Sun are constant. Distance to Earth Re is 1 ("astronomical unit") and distance to Venus Rv is given in relation to it, say 0.7. So we see the distance between Earth and Venus, marked D depends on relative position of the Venus.

Let's describe this position by the angle alpha - between direction from Sun to Venus (purple, non-horizontal) - and direction from the Earth to Sun (horizontal, purple). When Venus is behind the Sun, alpha is zero. When Venus is between Sun and Earth, this angle becomes maximal, 180 degrees.

The light reaching us from any celestial body (and any light source) decreases in proportion to distance squared (to this source).

Now about the phases. Obviously Venus is "full" when it is behind the Sun, in opposition to Earth. When it is nearest to Earth, on contrary, we see only its back side (similar to "new moon" condition) - or rather don't see anything at all. This obviously is the factor of the angle between our line of sight to Venus (green line) and direction of falling light (purple line between Venus and Sun). Let's call this angle gamma.

Really the amount of light reflected from the body depends on the quality of the surface. It is big relief to us that Venus (as almost all celestial bodies) reflects light in almost completely "diffuse" way - every beam scatters uniformly in all directions. That's why moon looks so evenly lighted despite it is not flat.

The light reduction due to phase in this condition is found by using the angle between line of sight and direction of light, particularly, multiply by (1 + cos(gamma)) / 2.

You are to tell, for several different distances Rv the angles alpha at which Venus reaches maximum apparent brightness.

Input: the first line provides N - total number of test-cases.
The next line contains N values of Rv.

Answer should have angle of maximum visible brightness for each testcase, rounded to the nearest integer (in degrees).
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e335 Venus Visible.txt','r')
P= a.readlines()

rvs=[]
f=P[1].strip().split()
for x in f:
    X=float(x)
    rvs.append(X)

print(rvs)
"""
rvs=[0.472, 0.541, 0.736, 0.827]

import math

def brightness_function(alpha, Rv):
    alpha_rad = math.radians(alpha)
    D_alpha = math.sqrt(1 + Rv**2 - 2 * Rv * math.cos(alpha_rad))
    cos_gamma = (Rv - math.cos(alpha_rad)) / D_alpha
    I_alpha = (1 + cos_gamma) / (2 * D_alpha**2)
    return I_alpha

def find_max_brightness_angle(Rv):
    max_brightness = -1
    best_alpha = 0
    for alpha in range(0, 181): 
        current_brightness = brightness_function(alpha, Rv)
        if current_brightness > max_brightness:
            max_brightness = current_brightness
            best_alpha = alpha
    return best_alpha


    
results = []
for Rv in rvs:
    angle = find_max_brightness_angle(Rv)
    results.append(angle)
    
print(" ".join(map(str, results)))