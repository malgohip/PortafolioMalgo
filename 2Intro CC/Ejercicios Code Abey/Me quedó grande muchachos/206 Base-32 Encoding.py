#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
This problem was "invented" while creating suitable encoding algorithm for using with certain functionality of CodeAbbey site. Probably you can even find this functionality, though algorithm was slightly changed.

How attachments are transferred inside e-mails? Binary files contain many special byte values which could not be represented easily in a text... Well, you probably heard that they are encoded using Base64. This system converts every 3 bytes of 8 bits each into 4 visible symbols, taken from the alphabet of 64 characters (upper and lower Latin letters, digits and also '+' and '/'). Each such symbol represents 6-bit value in the range 0..63. So we represent 24 bits of the source message with 4*6 chunks instead of 3*8.

You may play with such conversion with the help of some online tool like this.

In some cases this system still is not convenient. For example, suppose we need to pass bytes in the URL, e.g. paste it into browser address line. Here '+' and '/' have special meaning - and also uppercase letters could be sometimes transformed into lowercase. Let us use Base32 conversion instead! It will utilize the following alphabet, consisting of 26 letters and 6 digits:

ABCDEFGHIJKLMNOPQRSTUVWXYZ234567
We avoid digits O and 1 since they look similar to some letters. So it would be possible to encode every 5 bytes (of 8 bits each) of the source message using 8 symbols (each representing 5-byte value).

Problem Statement
You need to write encoder and decoder for Base32. Please follow the specifications below.

Source message should be at first "padded" with one or more symbols so that its total length is a multiple of 5. These symbols should be just integer values showing how many symbols were added. I.e.:

Hi          ->  Hi333
Bye         ->  Bye22
John        ->  John1
Abbey       ->  Abbey55555
Jeopardy    ->  Jeopardy22
CodeMasters ->  CodeMasters4444
With such padding we later will need only to peek at the last symbol to understand by which amount the string should be reduced.

Then take every 5-bytes chunk of the source message and write it down as bits (converting symbols to their ASCII values and then to binary octets). So that John1 becomes:

John1 => 74 111 104 110 49 =>

01001010  01101111  01101000  01101110  00110001
Now this binary line is just glued together and split into chunks of 5:

01001  01001  10111  10110  10000  11011  10001  10001 =>

  9      9     23     22     16     27     17     17
And with alphabet shown above it will be encoded as JJXWQ3RR.

We hope that you will be able to work out how to proceed with decoding on your own.

Input data will give total amount of test-cases in the first line.
Next lines will contain one test-case each, of them odd lines (1-st, 3-rd, 5-th) will contain normal text to be encoded while remaining will contain Base32 data to decode.
Answer should contain encoded and decoded phrases, all glued with spaces (it is not a problem that some phrases contain spaces themselves).
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e206 Base-32 Encoding.txt','r')
P= a.readlines()

frases=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip()
    frases.append(f)

print(frases)
"""
frases=['livelier', 'MVWWCY3JMF2GS33OGU2TKNJV', 'sulkiest destines', 'MRUXGY3PNVTG64TUNFXGOIDTORSXA3LPORUGK4RAMZWG6Z3TEBWWC5DUOJSXG43FOMQG2ZLOOVZTGMZT', 'maltreatment wardened', 'NFXGG2LUMUQHA33TON2W2IDTMFWGCYLNOMQGG2DMN5ZGS3TBORUW4ZZAOVWHI2LNMF2GKZBR', 'promoted receptors nearsighted', 'OJUW42ZAORSW443FON2CA43ZNRWGCYTJEBRGKZLQMVSCAZLYORZGC5DFOJZGK43UOJUWC3DTGU2TKNJV', 'coordinating', 'OJSWYYLYMF2GS33OGU2TKNJV', 'depute reapportions torpedoes nutritional', 'MNWG65DIMVZWY2LOMVZSA4DFOBYGK4TDN5ZG4IDNMFZHMZLMNFXGOIDDN5XHG4DJMN2W65LTEB2GC5DUNRUW4ZZR', 'classing rowdy', 'OJXXKZ3INBXXK43JNZTSAYTFNZ2W2YRAMNXW4ZDVNF2DGMZT', 'potboiler', 'OJXWOZLSMVSDGMZT', 'declivities', 'OBXWYYLSNF5GK4ZAOZUWO2LMMFXHIIDSMVQWY3DZNFXGOMRS', 'earthen cultivation currycombed', 'NB2XEZDMMVZCA3DBOZQXI33SNFSXGIDVNZRXK3DUOVZGKZBAOZUW63DPNZRWK3DMN42DINBU', 'gipsy waning', 'OBQXS3LBON2GK4TTEBUW23LJM5ZGC3TUEBTGSZTUNFSXI2BANJSWY3DZEBZHK3LNPE2DINBU', 'phoneme bespoke flamingoes adulterer counterfeited', 'M5ZGS43UNRSSA4DBMNSWIIDGOJUWO2LENR4SAZLZMVZXI4TBNFXCAZDJM5XGS5DBOJ4TGMZT', 'chaparrals fitters crewing reptile gringos', 'MFXHI2LWNFZGC3BAOJSXGYLMMVZSAY3INRXXE33GN5ZG22LOM4QG4ZLVORZGC3DJPJSXEMRS', 'yuletide']

BASE32_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

def encode_base32(text):
    padding_length = (5 - len(text) % 5) % 5
    padded_text = text + str(padding_length) * padding_length
    binary_string = ""
    for char in padded_text:
        binary_string += f"{ord(char):08b}"
    encoded_text = ""
    for i in range(0, len(binary_string), 5):
        segment = binary_string[i:i+5]
        if len(segment) < 5:
            segment = segment.ljust(5, '0')
        index = int(segment, 2)
        encoded_text += BASE32_ALPHABET[index]
    
    return encoded_text

def decode_base32(encoded_text):
    binary_string = ""
    for char in encoded_text:
        index = BASE32_ALPHABET.index(char)
        binary_string += f"{index:05b}"
    decoded_text = ""
    for i in range(0, len(binary_string), 8):
        segment = binary_string[i:i+8]
        if len(segment) == 8:
            decoded_text += chr(int(segment, 2))
    padding_length = int(decoded_text[-1])
    if padding_length > 0:
        decoded_text = decoded_text[:-padding_length]
    
    return decoded_text

respuesta=''
for x in range(0,len(frases),2):
    
    if x+1 < len(frases):
        code=encode_base32(frases[x])
        decode=decode_base32(frases[x+1])
        respuesta+=code+' '+decode+' '
    else:
        code=encode_base32(frases[x])
        respuesta+=code+' '

print(respuesta)