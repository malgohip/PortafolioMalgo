import math as mt

def sacadatos(s):
    a=b=d=1
    if s[0].isdigit():
        i=0
        while i<len(s) and s[i].isdigit():
            i+=1
        a=int(s[:i])
        s=s[i:]
    else:
        a=1
    i=s.find("/")
    j=i+1
    while j<len(s) and s[j].isdigit():
        j+=1
    b=int(s[i+1:j])
    pos_mas = s.find("+")
    costo = s[pos_mas+1:] if pos_mas!=-1 else ""
    if "^(" in s:
        i=costo.find("^(")+2
        j=costo.find(")", i)
        d=int(costo[i:j])
    elif "^" in costo:
        i=costo.find("^")+1
        j=i
        while j<len(costo) and costo[j].isdigit():
            j+=1
        d=int(costo[i:j])
    elif "n" in costo:
        d=1
    else:
        d=0
    return a,b,d

def fornE(expo, b=None):
    if expo==0:
        return "1"
    elif expo==1:
        return "n"
    if isinstance(expo,(int,float)):
        if isinstance(expo,float) and expo.is_integer():
            expo=int(expo)
            if expo==1: return "n"
            return f"n^({expo})"
        elif isinstance(expo,int):
            return f"n^({expo})"
    return f"n^({expo})"

def sol(a,b,d):
    log_b_a=mt.log(a, b)
    if log_b_a.is_integer():
        str_log_b_a=int(log_b_a)
    else:
        if b==2:
            str_log_b_a=f"lg({a})"
        else:
            str_log_b_a=f"log_({b})({a})"
    log_b_a_val=round(log_b_a, 9)
    if log_b_a_val>d:
        return f"O({fornE(str_log_b_a)})"
    elif abs(log_b_a_val - d) < 1e-9:
        parte_n=fornE(d)
        if parte_n == "1":
            return "O(lg(n))"
        else:
            return f"O({parte_n}lg(n))"
    else:
        return f"O({fornE(d)})"

data=input().strip()
data=data.replace(" ","")
pos_igual=data.find("=")
a,b,d=sacadatos(data[pos_igual+1:])
print(sol(a,b,d))