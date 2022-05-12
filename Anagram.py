

def anagram_check(str1, str2):
    if sorted(str1)==sorted(str2):
        print('Its anagram')
    else:
        print('Its not an anagram')




a = 'bhavik'
b = 'kavibh'

v = anagram_check(a,b)
print(v)
