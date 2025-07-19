#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
not necessarily bounded to subset of conventional notes...
The music could be represented as a stream of different sounds. We can distinguish these sounds as they have different tones. For example if we listen to "Moonlight Sonata" of Beethoven, its 1st movement (find it on youtube if you forget what it is) - our ear easily catch in the beginning the same pattern of 3 tones played several times.

These tones are called notes in music. From physical point of view they are just stable oscillations (of a string or some other part of instrument) in the air.

Such oscillations are characterized firstly by the frequency - i.e. simply the amount of "forth-and-back" movements performed during a second. If the string make 440 such oscillations per second, we say it has a pitch (or frequency) of 440 Hz (the measurement unit is called Hertz after famous German scientist who discovered electromagnetic waves while trying to prove they could not exist).

What is important, notes have not some randomly assigned pitch, but rather one defined by simple mathematical law. This task is dedicated to calculation of note frequencies.

NOTE NAMES

In music the whole range of possible pitches is divided in octaves. Each octave have frequency range twice larger compared to preceding one, i.e. if one octave covers the range 110 ... 220 Hz, the next will cover the range 220 ... 440 Hz, while third - 440 ... 880 Hz.

Each octave has 12 notes in it, of them 7 have proper names, C D E F G A B in English musical notation. Other 5 notes are added between some of these and have derived names, so the whole octave looks like:

C  C#  D  D#  E  F  F#  G  G#  A  A#  B
Notes with # sign are read as C-sharp for example. You see, there are no "sharps" for E and B - strictly speaking E# has the same pitch as F and B# has the same pitch as C of the next octave.

So the full title of the note consists of its own name and the number of octave, e.g.:

A2 G#5 G#2 A1 F3 D4 D2 E5 C#3 D#1 E3 C2 F4 B2 A#3 D3 D1 B5 A#4
(do not try to play this on piano - it would not yield nice music, ha-ha)

FREQUENCY LAW

You see, the frequency range of octave is not constant. Rathe the ratio between ranges of octaves is a constant factor of 2. The same with notes - the ratio of frequencies of two neighbor notes is a constant - and has such a value that if we multiply it by itself for 12 times (i.e. raising note for 12 steps) whe get the value of 2, i.e. the whole octave.

You may guess that since the ratios of octave steps is represented by a sequence of powers of 2, i.e.:

2 ^ 1 = 2   2 ^ 2 = 4   2 ^ 3 = 8 ...
then the ratios of single note steps are created similarly:

2 ^ (1/12)   2 ^ (2/12)   2 ^ (3/12)   ...   2 ^ (12/12) = 2 ^ 1
Calculator will help us to see that the ratio for a single pitch step is 1.059463094, though it is not important.

Now we can find the frequency for any note, though we need some basis point. Internationaly it is chosen as the pitch for A4 note which is exactly 440 Hz, so that A3 is 220 Hz and C4 is about 261.63 Hz etc.

PROBLEM STATEMENT

You are given a sequence of notes - calculate frequencies for them using the explanations above.

Input data will have the number of notes in the first line.
Next line contains note names separated by spaces.
Answer should contain frequencies for these notes, rounded to nearest integer.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e88 Pitch and Notes.txt','r')
P= a.readlines()

notas=P[1].strip().split()

print(notas)
"""
notas=['G#5', 'G#3', 'D3', 'G2', 'A#4', 'D#4', 'A#1', 'C1', 'G1', 'D#2', 'A3', 'F#5', 'G5', 'F#2', 'F5', 'E3', 'C#4', 'E2', 'E5', 'F#1']

respuesta=''
posiciones_notas = {'C': -9, 'C#': -8, 'D': -7, 'D#': -6,'E': -5, 'F': -4, 'F#': -3, 'G': -2, 'G#': -1,'A': 0, 'A#': 1, 'B': 2}
for x in notas:
    frecuencia_A4 = 440.0
    letra_nota = x[:-1]
    octava = int(x[-1])
    semitono = posiciones_notas[letra_nota] + (octava - 4) * 12
    frecuencia = frecuencia_A4 * (2 ** (semitono / 12.0))
    respuesta+=str(round(frecuencia))+' '
print(respuesta)