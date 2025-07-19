#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
Nowadays many applications perform spell-checking as you type in text. Among first programs to implement this feature was Microsoft Word - you know, you type the misspelled word and it is marked with red wavy line below.

You also know that usually such spell-checking not only checks the word in question by some internal vocabulary, but also suggests some substitutions. For example if you enter crain you are proposed to change it to brain, train or chain.

How these substitutions are chosen? One of the basic and popular solution is to run through vocabulary and calculate the Levenshtein Distance between the misspelled word and each of dictionary words. Words which give minimal distance are, probably, the best substitutions.

What is the Levenshtein Distance?

Shortly speaking it is the diference between two strings. Levenshtein distance counts 1 point of penalty for each of three mismatch kind:

the letter is present in the first string but absent in the second (like plain and plan);
the letter is absent in the first string but present in the second (like tree and three);
the letter is different in the same position of two words (like woman and women).
As an example, let us see what is the distance between hate and shot:

hate -> hat      (one letter removed)
hat  -> hot      (one letter substituted)
hot  -> shot     (one letter inserted)
So the distance is 3.

Your task now is simply to calculate the Levenshtein Distance between two strings. There are different algorithms, of which most popular uses dynamic programming with a table M by N (however it could be reduced to only two lines, previous and current, reassigned after each current line is completed). You can read more in the wikipedia article on Levenshtein Distance or get info from many other sources.

Input data will contain the number of test-cases in the first line.
Next lines will contain 2 "words" each - words will contain of capital latin letters only.
Answer should contain the distances for each pair of words, separated by spaces.
"""
"""
a = open('Ejercicios Code Abey\TXTs\e82 Levenshtein Distance.txt','r')
P= a.readlines()

palabras=[]
for x in range(1,int(P[0])+1):
    f=P[x].strip().split()
    palabras.append(f)

print(palabras)
"""
palabras=[['DBRDDBDYXSSCEZTMUBUUUM', 'DFBRIEDDBDYSSCEZTIMFUUMM'], ['EGOZSKHATUPEFNWKGBYAHOMO', 'EGIZSKAXTUUEFWKGBFMOAHMO'], ['KEKUREIZBGFUHZXSFLH', 'MKEKAREIHGFUHZXJSFLI'], ['YOFXNSVONSPTZFEUJQPNZVOMBZXZJBWWQ', 'SYOFXNZUVOONSPKTZFEUJQPNZVOMBAZXZJBWWO'], ['JURENCXUCLJKTUPPMSGRLKCXAGONFL', 'RURENCXUCLJEQTUPPMSRGRLKCXAONF'], ['OETWTIEWWSGQDRNOMOXOFZGO', 'OBAWTKXKEWHDRSNYIMOXOUZBO'], ['CPENMZCUCFCVXGHC', 'CPFENZYUCHHC'], ['DJPORQFKUXWVJGHWPMVENPETNMOFIIIFMBTYKA', 'DUPKRQFKUXTVVGHWEMVEETNOFIIMFMSZYKSA'], ['UQBOYWYHDYIWRNVWYQFS', 'UQBOYYHMXIWQRVWYQOFS'], ['EKCEBJMXHVJSZSS', 'EKCQBJMXSVJSZSSGO'], ['TCGEPZQXUDAC', 'TWDGEPQXUDTAZWC'], ['QQIPQGFFOEDSUUDGQUKNUCKFQHAHVJODGW', 'QIWQGWSFOEGSUUNDGQUKNMCKFHAVJOIDGH'], ['SSYMMZYKWIFAKKYA', 'USMMZYKMIFAKKA'], ['YRAJTYFTBNVJPZUTWFSPMGOVIGISGO', 'YRAJTYFVTIBVJZDTFSQQGOIGIRGO'], ['UEUQKCABMXWEHLRLJKJAALADLCU', 'UEUQCABMOXWEHLSRDLDJKJAWLADLCUH'], ['MECOADHGIKSBHMAQHEFDAVUXWNIDCFIRXQF', 'MEOADGIKSBHBAQHEFSATUXWNIDCFAFRTQQY'], ['DSGFFLJNYDTYGJEGLCYKYHECJ', 'DLJNYDTYJEGLCYKYHECJ'], ['CVXZPFNUIILFPVCGXOUVOYGKMIHOHR', 'CVZPFNUIILFPCGXQULOYGKMIHHR'], ['DMCWSORYCQVNSZ', 'DMCWSORYCSVNNSK'], ['MPPLONWRMIGBPOQXKFMOVJ', 'MPPLONWRMIGBPOQGGKFMHVJ'], ['TOXPALGIEGEPYNIAARKZPVEPOWRFBVYYH', 'TOXEPALGIEGEPYNOAAERKZPVJWRFKBVYYHG'], ['XLLRTQHZFZRZBTNHLNDYGGMJ', 'BLLRRTQKRZFZRBTTNHHLNDMYGDAJ'], ['XZRREVLBDDYHMLQDOQVQSONLZIIV', 'XXRRTVGBDYHMLCQDOOQDQSONLZRIV'], ['WEPQHTQNFGRHETKYEEPMKMKQZ', 'WEVMPHTQNFGRETKYEECMKVKQZY'], ['AAPBURJUWFXWRTZKMDIRTULUHSG', 'PAPJUJUWFXWRTGAJLTUXMHSGF'], ['ZJBNYSUBWYKKTLDRMBB', 'ZJBNYSGUBWCLKKTLDDRBAB'], ['ZPGUANMVDTRNKIILHCOCHURRQKVGBIIGS', 'MZLPGUSNVDSARKILPHCKOHURRSUVSSTUS'], ['QFGTQJBLDJIPQVC', 'QFGTQJBLDJIMPQVC'], ['SNLGZZHJYOITOOASRKBPSMF', 'SNLLZZHJYOTOOBSBRTAPSMFT'], ['YYKGJJZTFTOSGMT', 'YWKGGJJATFTOUSGG'], ['TETXSZRTJMLYOUCGJMUXIZRSPUPNK', 'TEXSZPJVMLYOUCGJUXFZSUPNK'], ['VGNVDZDRUGGLZOV', 'VGNVMZDRBAUGGLZOV'], ['UVQPVWVYOPBSMZJIFDVPDFWNCDLIY', 'UVQCPVWFYOPBUMZJOIFDVPHFWNCDLIY'], ['PYFRYQHVPEOUMGU', 'PYFXRYUQHOPOUMGU'], ['GMUODPVHTPNWVYEONNJRIWPNVQRCXRUUIXID', 'GUODPVWTTNWVYEONZJRVIWPNVQRCXRUUIXID'], ['RHGNQSTBKZFDXJUBZYRKSDAWSMEZTWPBIRB', 'IRHGQASFBKFDXUHZYRKKDASMEZTWBRIRB'], ['ZPNFHMOIJBZPQKTCXPKGKVFNBIRUNLUA', 'ZRRDNGFHMOJBZPQKTCXPKGKFVNBIRUNQUAPL'], ['OWPCPMLATIBQTTQEWEIO', 'OBWPCPMLATIBQTTQYWEI'], ['RRSFUXQCARZRHYXHBYLK', 'RSFUFCARKZRHYXHBBLKF']]

def levenshtein_distance(s1, s2):
    n_1 = len(s1)
    n_2 = len(s2)
    dp = [[0 for _ in range(n_2 + 1)] for _ in range(n_1 + 1)]
    for i in range(n_1 + 1):
        dp[i][0] = i
    for j in range(n_2 + 1):
        dp[0][j] = j
    for i in range(1, n_1 + 1):
        for j in range(1, n_2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,
                               dp[i][j - 1] + 1, 
                               dp[i - 1][j - 1] + 1) 
    return dp[n_1][n_2]

respuesta=''
for x in palabras:
    dis=levenshtein_distance(x[0],x[1])
    respuesta+=str(dis)+' '
print(respuesta)