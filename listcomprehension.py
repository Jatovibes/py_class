nums = [n for n in range(100) if sum([int(j) for j in str(n)]) % 7==0]


print(nums)