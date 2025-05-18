
# # factorial
# def fact(a):
#     if(a==1):
#         return 1
#     return a*fact(a-1)
# print(fact(5))

# # panagram
# str="abcdefghijklmnopqrstuvwxyz"
# def panagram(a):
#     for i in a:
#         if (not(i in str)):
#             return False
#     return True
# print(panagram("abcdefghijklmnopqrstuvyz"))

 

# def welcome():
#     college="abes college"
#     def welcome_again():
#         nonlocal college
#         college="abes engineering college"
#         university="aktu"
#     welcome_again("college name:",college)
# welcome()


spam_keywords = ["lottery", "win", "prize","money"]
def filterSpam(message,keyword):
    for word in keyword:
        if word in message:
            return True
    return False
# message="hello my name is sawej"
message="Congratulations! You have won a lottery worth $10,000."
check=filterSpam(message,spam_keywords)
if(check):
    print("spam message!")
else :
    print("not spam message")