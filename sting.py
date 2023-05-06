# 1. Write a Python program to get a single string from two given 
# strings, separated by a space, and swap the first two characters
#  of each string


def swap_the_characters(string1,string2):
    new_string1=string2[:2]+string1[2:]
    new_string2=string1[:2]+string2[2:]
    return new_string1+" "+new_string2
# swap_the_characters(["My","mum","is","Anabo"])

# print(swap_characters(string1,string2))


# 2.  Write a Python function that takes a list of words and 
# returns the longest word and the length of the longest one

def longest_string(words):
   longest=""
   for i in words:
       if len(i)>len(longest):
           longest=i
   return longest,len(longest)

     

# 3. Write a Python program that accepts a comma-separated sequence 
# of words as input and prints the distinct words in sorted form 
# (alphanumerically).
def comma_seperated_sequence(wordy):
     for i in wordy:
         wordy.sort()
         
     return wordy



# 4.. Write a Python function that takes two lists and returns True 
# if they have at least one common member.

def two_list(list1,list2):
    return boolean(set(list1) & set(list2))
if has_common_members(list1,list2):
    print(f"The two lists have a common member")

   
# 5. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", 
# "#FF0000", "#800000", "#FFFF00"]

# 6. Write a Python program to check whether all dictionaries 
# in a list are empty or not

# def check_empty(numbers):
#    for z in numbers:
#       return i.isNAN()
#    numbers=[00,22,33,44,55]
#    print(check_empty(numbers))

# 7. Given a list of numbers, use list comprehension to remove
#  all odd numbers from the list:
# numbers = [3,5,45,97,32,22,10,19,39,43]
def removed_all_odd_numbers(numbers):
   empty=[]
   odd_numbers=[num  for numbers in num %2!=0]
   empty.append(odd_numbers[num])
   return empty
numbers= [3,5,45,97,32,22,10,19,39,43]
print(removed_all_odd_numbers(numbers))
   
      
# 8. Find the common numbers in two lists (without using a tuple or set) 
# list_a = 1, 2, 3, 4, 
# list_b = 2, 3, 4, 5

# 9. Use a nested list comprehension to find all of the numbers from 
# 1-1000 that are divisible by any single digit besides 1 (2-9)
def nested_lists():
    
    numbered=[n for n in range if n%d==0]
    return n
# 10. Write a Python function to remove all vowels in a string.

