# define a function that accepts a string as input and uses 
# the for loop to iterate through the string and counts the vowels.
def accepts(names):
 count=0
 vowels=('a','e','i','o','u')
 for i in names:
  for v in vowels:
   if i==v:
    count+=1
    return count
   print(accepts('Beautiful'))


# Write a Python function that takes two arguments (a and b) 
# and returns their sum.
def takes(a,b):
 sum=0
feed=takes(a,b)
for i in feed:
    i+=sum
#    return sum
#  print(takes(12,10))
       
   

# Write a Python function that takes a string as input and 
# returns the string reversed.
def written(name):
 for i in name:
  return name[::-1]
  reap=written('Omara')
  return reap
print(written)

# Write a Python function that takes a list of integers as 
# input and returns the sum of all the integers in the list.
def legal(numbers):
    sum=0
    for num in numbers:
         sum +=num
    return sum
output = legal ([2,8,4,5,7,6])
print(legal(output))

# Write a Python function that takes a list of integers as 
# input and returns a new list with all the even numbers removed.

def put_in(numbers):
 sum=0
 for i in numbers:
  if i%2!=0:
   sum+=i
   return sum
  print(put_in([2,24,17,1874]))
  
# Write a Python function that takes a list of integers as input
#  and returns the highest value in the list.

def highest_value(numbers):
 highest= numbers[0]
 for num in numbers:
   if num > highest:
     highest=num
 return highest
output = highest_value(100,64,20,1,3)
print (output)


# Write a Python function that takes a list of strings as input
#  and returns a new list with all the strings capitalized.

def typed(strings):
   return strings.titleCase()
output = typed(['wind','sand','soil'])
print (output)
