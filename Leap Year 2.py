year = int(input("Please Enter A Year :"))

if year % 400 == 0 and year > 0 :
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")