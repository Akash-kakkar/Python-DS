#Create a list of the first 15 even numbers that are not divisible by 6

numList, counter, appender = [], 0, lambda num: numList.append(num)
while len(numList) < 15: appender(counter) if not counter % 2 and counter % 6 else None; counter += 1
numList

#Write a function to Check whether given two string is anagram or not.

def anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        print("Anagrams")
    else:
        print("!Anagrams")

anagram('okzzz', 'zzzko')
anagram('PyDS', 'pyds')



