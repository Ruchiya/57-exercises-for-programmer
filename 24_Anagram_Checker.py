def isAnagram(s1,s2):
    if sorted(s1) == sorted(s2):
        print(f'"{s1}" and "{s2}" are anagrams.')
        return True
    return False

print('Enter two strings and I\'ll tell you if they are anagrams:')
s1 = input("Enter the first string:")
s2 = input("Enter the second string:")
isAnagram(s1,s2)
