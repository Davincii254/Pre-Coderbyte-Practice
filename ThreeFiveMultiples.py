def ThreeFiveMultiples(num):
    num = (sum(i for i in range(num) if i % 3==0 or i % 5 ==0))
  # code goes here
    return num

# keep this function call here 
print(ThreeFiveMultiples(input()))