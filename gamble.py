while True:
    try:
        num = float(input("Please enter a number:"))
        if num < 0:
            print("Please enter a positive number.")
        else:
            print("The square of",num,"is",num**2)    
            break
    except ValueError:
        print("Please enter a valid number.")    
