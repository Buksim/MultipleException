try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"Result is : {result}")
    
except ZeroDivisionError:
    print("Division by Zero is not allowed")
except ValueError:
    print("Please Enter Numeric Values Only")
except NameError as ex
    print("The Exception is: ", ex)
except:
    print("Some Error Occurred")
finally:
    print("I will execute no matter what happens")