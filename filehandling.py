results = open('filehandling2.txt', 'r')
print(results.read())
print(results.readlines())


results = open('filehandling2.txt', 'w')
results.writelines(['Phython dealings \n', 'God never fails'])


with open('filehandling2.txt') as file:
    result = file.read()
    print(result)