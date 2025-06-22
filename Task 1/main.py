while True:   # loops until user enters valid input
    try:      # loop to handle invalid input
        Weight = float(input("Enter your weight in kg : ")) # asks user for weight
        Height = float(input("Enter your height in m : "))  # asks user for height
        BMI = Weight / Height ** 2    # calculates BMI using this formula.
        if Weight <= 0 or Height <= 0:                      # checks if weight and height are positive numbers.
            print("Weight and Height must be positive numbers. Please try again.\n")
            continue      # continue to next iteration if input is invalid.if its valid input then it skips this print statement and calculate BMI.
        if BMI < 18.5:    # checks if BMI is less than 18.5
            print(f" you are BMI is {BMI}, you are underweight.")
        elif 18.5 <= BMI < 24.9:
            print(f" you are BMI is {BMI}, you have normal weight.")
        else:
            print(f" you are BMI is {BMI}, you are overweight.")
        break
    except ValueError: # handles the case if user enters invalid input
        print("Invalid input. Please enter numbers only.\n")