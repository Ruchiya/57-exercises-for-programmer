#Challenges Included

def comint(P,r,t,n):
    A = round(P* ((1 +(r/n))**(n*t)),2)
    r = r*100
    print(f"${P} invested at {r}% for {t} years compounded {n} times per year is ${A}")

def calPrincipal(A,r,t,n):
    P = round(A / ((1+r/n)**(n*t)),2)
    r = r*100
    print(f"To reach ${A} at {r}% for {t} years compounded {n} times, you will need ${P}")

while True:
    try:
        func = input("Would you like to calculate interest or set a goal, enter 'interest' or 'goal':")
        if func == 'interest':
            P = float(input("What is the principal:"))
            r = float(input("What is the rate:"))/100
            t = float(input("What is the number of years:"))
            n = float(input("What is the number of times the interest is compounded per year:"))
            comint(P,r,t,n)
        elif func == 'goal':
            A = float(input("What is your goal:"))
            r = float(input("What is the rate:"))/100
            t = float(input("What is the number of years:"))
            n = float(input("What is the number of times the interest is compounded per year:"))
            calPrincipal(A,r,t,n)
        break
    except ValueError:
        print("All value must be numeric, try again")
