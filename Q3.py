def checkPalindrome(word):
    if word[::-1]==word:
        return True
    else:
        return False
def append(d):
    if (checkPalindrome(d)):
        return 0
    del d[0]
    return 1 + append(d)

str = "hello"
d = [i for i in str]
a = (append(d))
# print(a)
b = (str[0:a])
c = b[::-1]
d = str + "\033[1m" + c + "\033[1m"
# print(d)



#
# def checkPalindrome(word):
#     if word[::-1]==word:
#         return True
#     else:
#         return False
# def append(d):
#     if (checkPalindrome(d)):
#         return 0
#     del d[0]
#     return 1 + append(d)
# str= input("please write a word to check ")
# if len(str) >1 and len(str)< 103:
#     str = str.lower()
#     d = [i for i in str]
#     a=(append(d))
#     print(a)
#     b=(str[0:a])
#     c=b[::-1]
#     d= str+"\033[1m"+c+"\033[1m"
#     print(d)
# else:
#     print("word length should be larger than 1 and smaller than 103 ")
