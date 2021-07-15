# Check if given string is an anagram of another given string.
def Anagram(str1, str2):
    
    j1 = len(str1)
    j2 = len(str2)


    if j1 != j2:
        return 0

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(0, j1):
        if str1[i] != str2[i]:
            return 0

    return 1

str1 = "listen"
str2 = "silent"

if Anagram(str1, str2):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other") 