name = input('Enter your name')
age = input('Enter age:')

# outer if condition
if int(age) > 18:
   # inner if condition
   if name.lower() =='john':
       print("Welcome John,we've been expecting you")
   else:
       print(f"Welcome {name}")   
else:
    print('You are too young to be accepted')        
