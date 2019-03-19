import string
import random
punctuationList = string.punctuation
filteredList = []


def filter_passwords(passwords):
    #filter passwords has a length less than 8 characters
    for password in passwords:
        if len(password) >= 8:
            lowercaseCount = 0
            uppercaseCount = 0
            digitCount = 0
            punctuationCount = 0
            for i in password:
                if i.islower() == True:
                    lowercaseCount += 1
                elif i.isupper() == True:
                    uppercaseCount += 1
                elif i.isdigit() == True:
                    digitCount += 1
                elif i in punctuationList:
                    punctuationCount +=1
            if lowercaseCount >= 1 and uppercaseCount >= 1 and digitCount >= 1 and punctuationCount >= 1:
                filteredList.append(password)
    return set(filteredList)


#there's a problem that the random program sometimes fails to generate a string w/ 1 uppercase, 1 lowercase, 1 digit and 1 symbol at the same time.
def generate_strong_password():
    strongPasswordElements = set(string.digits + string.ascii_letters + string.punctuation)
    passwordLength =int(random.randrange(8,20))
    generatedPassword = "".join(random.sample(strongPasswordElements, passwordLength))
    return generatedPassword


def test():
    generated_passwords = set(generate_strong_password() for _ in range(10))
    filteredPassword = set(filter_passwords(generated_passwords))
    print(generated_passwords)
    print(filteredPassword)    
    return generated_passwords == filteredPassword

print(test())
