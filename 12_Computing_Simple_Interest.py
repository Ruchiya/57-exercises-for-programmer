#Challenges Included

def supinterest(P,r,t):
    for i in range(1,int(t)+1):
        A = round(P*(1+r*i),2)
        print(f"Amount for year {i}:${A}")
    A = round(P*(1+r*t),2)
    print(f'After {t} years at {r*100}%, the investment will be worth ${A}')

while True:
    try:
        P = float(input("Enter the principal:"))
        r = float(input("Enter the rate of interest:"))/100
        t = float(input("Enter the number of years:"))
        supinterest(P,r,t)
        break
    except ValueError:
        print("All value must be numeric, try again")
