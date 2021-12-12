                                                             # build an calculator using python


first = input("enter your first number:")
operator = input("enter your operator(+,_,*,/,%,):")
second = input("enter your second number:")

first =int(first)
second =int(second)

if operator == "+":
    print(first + second)
elif operator =="_":
    print(first - second)
elif operator =="*":
    print(first * second)
elif operator =="/":
    print(first / second)
elif operator == "%":
    print(first % second)    
else:
    print("invalid operation")
