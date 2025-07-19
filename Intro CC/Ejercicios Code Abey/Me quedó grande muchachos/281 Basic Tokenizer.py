#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
Problem Statement
Basic sources are parsed and even executed line-per-line. So you'll get a number of source lines as input and the goal is for every line to tell of which token types it consists.

Only 5 token types need to be recognized:

"word" (w) - anything which starts with letter and then continues with letters or digits; also it may end with dollar sign (examples LET, X13, A5);
"number" (n) - for simplicity, regard only integers - i.e. sequence of digits (e.g. 0, 12357);
"quotes" (q) - string literal, starting and ending with double quotes, no provision is made for escaping double quote itself as a part of string (for example "Hi Peoplezzz!!!");
"operators" (o) - any of >=, <=, <>, >, <, =, +, -, *, /, ^
"punctuation" (p) - any of ,, ;, :, (, ) (comma, semicolon, colon, parentheses)
Token types are identified by single letters (w, n, q, o, p). So the line like this:

PRINT "Meaning of the life is", 40+2
Should give as an answer wqpnon.

Spaces between tokens are skipped. If you detect some state of error while trying to parse the next token, add letter e to the answer and don't parse this line further.

Note 1: in real interpreter we keep token content of course, not only their type - but for our exercise it is not important.

Note 2: some language errors are on higher level than tokenization. For example PRINT +-* 40 40 has illogical chain of tokens - but tokens themselves parse correctly, there is no error on tokenization step, that's all right.

Input data give the total number (N) of lines first. Then N source lines follow.
Answer should give chains of token types for every of these lines, separated with spaces.
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e281 Basic Tokenizer.txt','r')
P= a.readlines()

codigos=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip()
    codigos.append(f)

print(codigos)
"""
codigos=['1230 PRINT CHR$(30)"FROM"R(1);R(2)"TO"R(3);R(4);:R(0)=-99', '1040 IF U-C<0 OR U-C>7 OR V-G>7 THEN 1080', '790 U=U+A:V=V+B:IF U<0 OR V<0 OR U>7 OR V>7 THEN 870', '80 DIM R(4),S(7,7):G=-1:R(0)=-99', '960 IF Y=7 THEN Q=Q-2', '1800 S((E+A)/2,(H+B)/2)=0', '1564 IF Z<>1 THEN 1885', 'NEXT C:IF Q>R(0)THEN R(0)=Q:R(1)=X:R(2)=Y:R(3)=U:R(4)=V', '740 IF S(U,V)=0 THEN GOSUB 910:GOTO 870', 'PRINT "THIS IS THE GAME OF CHECKERS.  THE COMPUTER IS X,"', '1120 A$ = "Magic Word Xyzzy', 'IF S(X,Y)=0 THEN PRINT".";', '15 PRINT:PRINT:PRINT', 'IF S(U,V)=0 THEN GOSUB 910', 'IF S(X,Y)=-1 THEN FOR A=-1 TO 1 STEP 2:B=G:GOSUB 650:NEXT A', 'FOR X=0 TO 7:FOR Y=0 TO 7:IF S(X,Y)>-1 THEN 350', '5 PRINT TAB(32);"CHECKERS"', 'IF S(U,V)<0 THEN 870', '1030 FOR C=-1 TO 1 STEP 2:IF U+C<0 OR U+C>7 OR V+G<0 THEN 1080', '650 U=X+A:V=Y+B:IF U<0 OR U>7 OR V<0 OR V>7 THEN 870', '1330 S((R(1)+R(3))/2,(R(2)+R(4))/2)=0', 'IF S(U+C,V+G)<0 THEN Q=Q+1:GOTO 1080', 'IF B=7 THEN S(A,B)=2', '35 PRINT "(0,0) IS THE LOWER LEFT CORNER"', '1563 REM Just a fine comment!', '1310 S(R(1),R(2))=0:IF ABS(R(1)-R(3))<>2 THEN 1420', '1400 RETURN', 'FOR M=0 TO 7', 'RESTORE:READ S(X,Y)', '25 PRINT "AND YOU ARE O.  THE COMPUTER WILL MOVE FIRST."', '860 PRINT S + &16', '1530 IF S(X,Y)=2 THEN PRINT"O*";', 'IF S(X,Y)=0 AND ABS(A-E)<=2 AND ABS(A-E)=ABS(B-H)THEN 1700', '1360 NEXT A:IF R(0)<>-99 THEN PRINT"TO"R(3);R(4);:R(0)=-99:GOTO 1240', 'IF S(U,V)=0 AND S(X+A/2,Y+B/2)>0 THEN GOSUB 910', '1570 Z=0: T=0', 'FOR L=0 TO 7', 'PRINT: PRINT "I WIN.": END', '1558 IF S(L,M)=-1 OR S(L,M)=-2 THEN T=1', 'PRINT: PRINT "YOU WIN.": END', 'INPUT "TO";A,B:X=A:Y=B', '1045 IF S(U+C,V+G)>0 AND(S(U-C,V-G)=0 OR(U-C=X AND V-G=Y))THEN Q=Q-2', '1470 IF S(X,Y)=1 THEN PRINT"O";', '1700 I=46', 'PRINT "(7,7) IS THE UPPER RIGHT CORNER"', '980 IF U=0 OR U=7 THEN Q=Q+1', 'Q=0:RETURN', '120 FOR X=0 TO 7:FOR Y=0 TO 7:READ J:IF J=15 THEN 180', 'IF T<>1 THEN 1880', 'IF R(4)=0 THEN S(R(3),R(4))=-2:GOTO 1420', '1806 E=A:H=B:A=A1:B=B1:I=I+15:GOTO 1750', 'NEXT X:PRINT" ":PRINT:NEXT Y:PRINT', 'IF R(0)=-99 THEN 1880', '1830 GOTO 230', 'S(R(3),R(4))=S(R(1),R(2))', 'IF S(X,Y)=-2 THEN PRINT"X*";', 'INPUT "FROM";E,H:X=E:Y=H:IF S(X,Y)<=0 THEN 1590', '160 S(X,Y)=J:GOTO 200', '910 IF V=0 AND S(X,Y)=-1 THEN Q=Q+2', '1804 IF S(A1,B1)<>0 OR ABS(A1-A)<>2 OR ABS(B1-B)<>2 THEN 1802', "1540 REM here's a break", '870 RETURN', '330 IF S(X,Y)=-2 THEN FOR A=-1 TO 1 STEP 2:FOR B=-1 TO 1 STEP 2:GOSUB 650:NEXT B,A', '1562 NEXT L', 'INPUT "+TO";A1,B1:IF A1<0 THEN 1810', '350 NEXT Y,X:GOTO 1140', '1750 S(A,B)=S(E,H):S(E,H)=0:IF ABS(E-A)<>2 THEN 1810', 'DATA 1,0,1,0,0,0,-1,0,0,1,0,0,0,-1,0,-1,15', '40 PRINT "(0,7) IS THE UPPER LEFT CORNER"', '1370 U=X+A:V=Y+B:IF U<0 OR U>7 OR V<0 OR V>7 THEN 1400', '220 GOSUB 650: INPUT "X=", X, "Y="", Y', '1340 X=R(3):Y=R(4):IF S(X,Y)=-1 THEN B=-2:FOR A=-2 TO 2 STEP 4:GOSUB 1370', '65 PRINT:PRINT:PRINT', '30 PRINT "SQUARES ARE REFERRED TO BY A COORDINATE SYSTEM."', 'PRINT TAB(15);"CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY"', '60 PRINT "JUMP.  TYPE TWO NEGATIVE NUMBERS IF YOU CANNOT JUMP."', 'IF S(L,M)=1 OR S(L,M)=2 THEN Z=1', '1560 NEXT M', '1420 PRINT:PRINT:PRINT:FOR Y=7 TO 0 STEP-1:FOR X=0 TO 7:I=5*X:PRINT TAB(I);', '200 NEXT Y,X']

import re

def identify_token_type(token):
    """Identify the type of token."""
    # Check if token is a word (including variable names ending with $)
    if re.match(r'^[A-Za-z][A-Za-z0-9]*\$$', token) or re.match(r'^[A-Za-z][A-Za-z0-9]*$', token):
        return 'w'  # word
    # Check if token is a number
    elif re.match(r'^\d+$', token):
        return 'n'  # number
    # Check if token is a quoted string
    elif re.match(r'^".*"$', token):
        return 'q'  # quotes
    # Check if token is an operator
    elif token in ['>=', '<=', '<>', '>', '<', '=', '+', '-', '*', '/', '^']:
        return 'o'  # operators
    # Check if token is a punctuation mark
    elif token in [',', ';', ':', '(', ')']:
        return 'p'  # punctuation
    # If none of the above, it is an error
    else:
        return 'e'  # error

def tokenize_line(line):
    """Tokenize the line and return a string of token types."""
    # Removing leading and trailing spaces
    line = line.strip()
    
    # Regular expression to split tokens
    token_pattern = re.compile(r'[A-Za-z][A-Za-z0-9]*\$?|[0-9]+|"(?:[^"]|\\")*"|>=|<=|<>|>|<|=|\+|-|\*|/|\^|,|;|:|\(|\)')
    
    tokens = token_pattern.findall(line)
    
    if not tokens:
        return 'e'
    
    result = []
    
    for token in tokens:
        token_type = identify_token_type(token)
        if token_type == 'e':
            return 'e'
        result.append(token_type)
    
    return ''.join(result)

def process_lines(num_lines, lines):
    """Process each line and output the token types."""
    results = []
    for line in lines:
        results.append(tokenize_line(line))
    return ' '.join(results)

print(process_lines(len(codigos), codigos))