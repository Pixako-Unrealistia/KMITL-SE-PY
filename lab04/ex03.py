
k = []

k.append(input("Enter your name: "))
k.append(int(input("Enter your age: ")))
k.append(float(input("Enter your weight in KG: ")))
k.append(float(input("Enter your height in CM: ")))

neo  = k[2]/((k[3]/100)**2)
print(f"Your BMI is {neo:.9F}")
if k[1] < 17:
    if neo < 15:
        print(f"{k[0]} you are underweight")
    elif neo <= 20:
        print(f"{k[0]} you are normal")
    else:
        print(f"{k[0]}, you are overweight")
elif k[1] < 35:
    if neo < 18:
        print(f"{k[0]} you are underweight")
    elif neo <= 24:
        print(f"{k[0]} you are normal")
    else:
        print(f"{k[0]}, you are overweight")
        
else:
    if neo < 19:
        print(f"{k[0]} you are underweight")
    elif neo <= 26:
        print(f"{k[0]} you are normal")
    else:
        print(f"{k[0]}, you are overweight")
                
