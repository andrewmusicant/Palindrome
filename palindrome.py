import re


def is_palindrome(sentence):
    sentence = sentence.lower()
    sentence = re.sub("[^A-Za-z]", "" , sentence)
    if len(sentence) < 2:
        return True
    if sentence[0] != sentence[ -1]:
        return False
    return is_palindrome(sentence[1: - 1])

def main():
    sentence = input("Please Enter a phrase: ")
    if is_palindrome(sentence):
        print("This is a palindrome")
    else:
        print("This is not a palindrome")



if __name__ == '__main__':
    main()
