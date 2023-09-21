# EMI = p * r * (1+r)n / ((1+r)n-1)

amount = int(input("Enter the principle amount: "))
interest = float(input("Enter loan interest: "))
tenure = int(input("Enter tenure(in number of months): "))


def emi_calculation(p, n, r):
    emi = p * r * (1 + r) ** n / ((1 + r) ** n - 1)
    emi = round(emi, 2)
    return emi


result = emi_calculation(amount, interest, tenure)
print(result)
