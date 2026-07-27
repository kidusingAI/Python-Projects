p = float(input("what was the principle amount"))
n = float(input("how many times does the interest compound per year"))
t = float(input("how many years does the interest last"))
r = input("what was the interest rate per year")
r = float(r.replace("%",""))/100
compoundint = (1+r/n)**n*t
compoundint = p*compoundint

print(compoundint)
