import string

password=input("Enter your password for strength check: ")

lower_case=any([1 if c in string.ascii_lowercase else 0 for c in password ])
upper_case=any([1 if c in string.ascii_uppercase else 0 for c in password ])
special=any([1 if c in string.punctuation else 0 for c in password ])
digits=any([1 if c in string.digits else 0 for c in password ])

character=[lower_case, upper_case, special, digits]

length=len(password)

score=0

with open('common.txt','r') as f:
    common = f.read().splitlines()

if password in common:
    print("Password was found in common password list. Score: 0 / 7 \n")
    exit()

if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 17:
    score += 1
if length > 20:
    score += 1

print(f"\nPassword Length is {str(length)}, adding {str(score)} points! \n")
# Google: common password list filetype:txt

if sum(character) > 1:
    score += 1
if sum(character) > 2:
    score += 1
if sum(character) > 3:
    score += 1

print(f"password has {str(sum(character))} different character types, adding {str(sum(character) - 1)} points! \n")

if score < 4:
    print(f"the password is quite week, score: {str(score)} / 7")
elif score == 4:
    print(f"the password is ok, score: {str(score)} / 7")
elif 4 < score < 6:
    print(f"the password is pretty good, score: {str(score)} / 7")
elif score > 6:
    print(f"the password is strong, score: {str(score)} / 7")