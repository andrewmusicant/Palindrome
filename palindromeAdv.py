import re


def is_palindrome(sentence):
   a = list(sentence)
   b = a[::-1]
   return a == b


def main():
    sentence = input("Please Enter a phrase: ").lower()
    sentence = re.sub("[^A-Za-z]", "" , sentence)
    if is_palindrome(sentence):
        print("This is a palindrome")
    else:
        print("This is not a palindrome")



if __name__ == '__main__':
    main()
