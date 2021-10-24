#Name: Tran Bao Vu          ID: 2489003
#Step1: Ask user the first question with int data type, and assign it to QUESTION_1
#Step2: Using if-else statements to determine True-False,
#       and immediately using f-string to show the answer.
#Step3: Ask user the second question with float data type, and assign it to QUESTION_2
#Step4: Using if-else statements to determine True-False,
#       and immediately using f-string to show the answer.
#Step3: #Step3: Ask user the third question with string data type, and assign it to QUESTION_3
#Step4: Using if-else statements to determine True-False,
#       and immediately using f-string to show the answer.


 # Ask user the first question and write two if-else statements
QUESTION_1 = int(input('How many days in 2021? '))
if QUESTION_1 == 365:
    QUESTION_1 = True
else:
    QUESTION_1 = False
if QUESTION_1 == True:
    print(f'You are correct!!')
else:
    print('This answer is not correct :( The right answer is: 365 ')

# Ask user the second question and write two if-else statements:
QUESTION_2 = float(input("What is the Pi number's value? (round upto 2 numbers) "))
if QUESTION_2 == 3.14:
    QUESTION_2 = True
else:
    QUESTION_2 = False
if QUESTION_2 == True:
    print(f'You are correct!!')
else:
    print('This answer is not correct :( The right answer is: 3.14 ')

# Ask user the second question and write two if-else statements:
QUESTION_3 = str(input("Can you guess my first name? "))
if QUESTION_3 == "Tran":
    QUESTION_3 = True
else:
    QUESTION_3 = False
if QUESTION_3 == True:
    print(f'You are correct!!')
else:
    print('This answer is not correct :( The right answer is: Tran ')





