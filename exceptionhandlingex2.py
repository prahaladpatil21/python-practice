try:
    a=int(input("Enter a number: "))
    b=int(input("Enter second number: "))
    if b==0:
        print("cannont divide by zero")
    else:
        print("number is divided successfully")

    print(a/b)
except ZeroDivisionError:
    print("zero divisor error")
except ValueError:
    print("it's value error")

except Exception as e:
    print(f"Error is -{e}")

#safe divider ask two numbers from the user and divie them handle zero divisor error and value error