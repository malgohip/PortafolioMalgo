#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
This task is the reverse of Pitch and Notes (so perhaps you may want to read or solve it first) - suppose you are building the electronic tuner for guitar, violin or piano - and you already connected microphone to microcontroller and succeeded in registering the sound wave, smoothering it and measuring its frequency.

Now the only thing remained is to write a part of program responsible for determining the note played by its frequency.
I.e. if the device have detected sound of 440 Hz it should be able to tell that note A4 is played.

Since in reality instruments could be slightly out of tune, you need not expect that pitch will be mathematically exact. Nevertheless you'll be able to determine the nearest note. I.e. frequencies of 433 Hz or 449 Hz should anyway be classified as A4.

Input data contains number of notes to identify.
The next line will provide the frequencies, separated by spaces.
Answer should contain identified note names.
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e89 Instrument Tuner.txt','r')
P= a.readlines()

frecuencias=[]
f=P[1].strip().split()
for x in f:
    X=float(x)
    frecuencias.append(X)

print(frecuencias)
"""
import math
frecuencias=[998.6, 417.0, 92.6, 335.9, 51.7, 42.0, 61.0, 102.7, 817.3, 49.8, 211.0, 398.7, 659.3, 229.4, 188.5, 596.1, 220.4, 32.7, 251.4, 66.1]

posiciones_notas = {0: 'A',  1: 'A#',  2: 'B',3: 'C',  4: 'C#',  5: 'D',6: 'D#', 7: 'E',  8: 'F',9: 'F#', 10: 'G', 11: 'G#'}
frecuencia_A4 = 440.0
respuesta=''

for x in frecuencias:
    semitono = round(12 * math.log2(x / frecuencia_A4))
    posicion_nota = semitono % 12
    octava = 4 + (semitono // 12)

    # Ajustar la octava si el semitono está por debajo de A4
    if semitono < 0:
        octava += 1
        posicion_nota = (semitono % 12 + 12) % 12

    nota = posiciones_notas[posicion_nota]
    respuesta += f"{nota}{octava} "

print(respuesta)