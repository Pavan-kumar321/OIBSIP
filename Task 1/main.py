while True:
    try:
        Weight = float(input("Enter your weight in kg : "))
        Height = float(input("Enter your height in m : "))
        BMI = Weight / Height**2
        if Weight <= 0 or Height <= 0:
            print("Weight and Height must be positive numbers. Please try again.\n")
            continue  
        if BMI < 18.5:
            print(f" you are BMI is {BMI}, you are underweight.")
        elif 18.5 <= BMI < 24.9:
            print(f" you are BMI is {BMI}, you have normal weight.")
        else:
            print(f" you are BMI is {BMI}, you are overweight.")
        break
    except ValueError:
        print("Invalid input. Please enter numbers only.\n")