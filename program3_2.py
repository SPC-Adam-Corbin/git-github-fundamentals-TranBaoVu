#Name: Tran Bao Vu          ID: 2489003
#Step1: prompt the user to enter an even multiple of 13 that is more than 150
#Step2: write a if-else statement to calculate an even multiple of 13 that is more than 150
#Step3: Display results with f-string


#Prompt the user to enter an even multiple of 13 that is more than 150
NUMBER = int(input('Enter even multiple of 13 and more than 150: '))

#write a if-else statement to calculate:
if NUMBER % 13 == 0 and NUMBER > 150:
    print(f' Good input')                           #Display as "Good input" for correct number

else:
    print(f'Bad input!')                            # #Display as "Bad input" for incorrect number

