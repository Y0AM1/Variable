
def circle_area(radius):
    pi = 3.14159
    area = pi * radius **2
    return area

def tax_total(money, tax):
    return money + (money * tax)

def convert_fahrenheit(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

#2nd function
def main():
    #this is just for the circle
    radius = int(input("Input the Radius: "))
    area = circle_area(radius)
    print(f"{area:.2f}")
    print()

    # for the tax total
    money = float(input("Input the Money Amount: "))
    tax = float(input("Input tax rate (whole number): "))/100
    total = tax_total(money,tax)
    print(f"{total:.2f}")
    print()

    # for the temperature
    fahrenheit = float(input("Enter the Temp in Fahrenheit:"))
    celsius = convert_fahrenheit(fahrenheit)
    print(celsius)

main()









