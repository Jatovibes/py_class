try:
    result = 10/0

except ZeroDivisionError:
    print('You should have done that') 
    

try:
    with open('main.txt', 'r') as file:  
        print(file.read())
except IOError:
    with open('main.txt', 'w') as file:  
        file.write('Hello World')

try:
    a = 10/0
except (ZeroDivisionError, SyntaxError, NameError):
    print('You are doing something wrong')    
finally:
    print('Done')

def main(age):
    if age < 18:
        raise ZeroDivisionError
    print(age)


class NetworkError(ZeroDivisionError):
    def __init__(self, *args):
        super().__init__(*args)    


try:
    result = 10/0
except NetworkError:
    print('It did not work')    



class NetworkError(Exception):
    def __init__(self, *args):
        super().__init__(*args)    


try:
    raise NetworkError
except NetworkError:
    print('It did not work')        
