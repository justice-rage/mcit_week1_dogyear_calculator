def calculator():
    
    # Get dog age
    age = input("Input dog years: ")

    try:
        # Cast to float
        age = float(age)
        d_age = float(age) # Dog age

        # If user enters negative number, print message
        # Otherwise, calculate dog's age in human years
    
        # your code here
        if age < 0:
                print("Please do not enter negative numbers.")
        if age == 1:
            d_age = 15
        if age == 2:
            d_age = 24
        if age == 3:
            d_age = 27.9
        if age == 4:
            d_age = 32
        if age == 5:
            d_age = 36
        if age > 5:
            d_age = (36 + (age - 5) * 7)
        if age > 0:
            print(f"The given dog age {age} is {float(d_age)} in human years.")
    
    except:
        print(age, "is an invalid age.")
    
calculator() # This line calls the calculator function