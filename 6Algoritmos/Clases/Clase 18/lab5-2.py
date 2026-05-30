import math as mt

def sacadatos(s):
    a=b=d=1
    if s[0].isdigit():
        i=0
        while s[i].isdigit():
            i+=1
        a=int(s[:i])
        s=s[i:]
    i=s.find("/")
    j=i+1
    while s[j].isdigit():
        j+=1
    b=int(s[i+1:j])
    if "^(" in s:
        i=s.find("^(") + 2
        j=s.find(")", i)
        d=int(s[i:j])
    elif "cn" in s:
        d=1
    else:
        d=0
    return a,b,d

def sol(a,b,d,i):
    if i=="Size subproblem i":
        if b==1:
            return "n"
        return f"n/{b}^i"
    elif i=="Cost node i":
        if d==0:
            return "c"
        if d==1:
            if b==1:
                return "cn"
            return f"c(n/{b}^i)"
        if b==1:
            return f"c(n^({d}))"
        return f"c(n/{b}^i)^({d})"
    elif i=="Number nodes i":
        if a==1:
            return "1"
        return f"{a}^i"
    elif i=="Number leaves":
        x=mt.log(a, b)
        if x.is_integer():
            x = int(x)
            if x==0:
                return "1"
            elif x==1:
                return "n"
            else:
                return f"n^({x})"
        else:
            if b==2:
                return f"n^(lg({a}))"
            return f"n^(log_({b})({a}))"

data=input().strip()
a, b, d = sacadatos(data[5:])
i=input().strip()
print(sol(a,b,d,i))