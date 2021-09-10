print(
    '\n \n   © 2021 by blkcpk | https://github.com/blkcpk | All Rights Reserved\n\n                  PYTHON MINI IDENTIFICATION QUIZ BY ELIGIO R. BAUTISTA III')
tanong = [
    'Question #1 |    What is the missing part of the code below to output "Hello World"?\n                 _____("Hello World")',
    'Question #2 |    Comments in Python are written with a special character. Identify the missing special character.\n                 _This is a comment.',
    'Question #3 |    It is used to create a multiline string to make a multi line comment.\n               ___This is a comment\n                witten in\n                more that just one line___.',
    'Question #4 |    Identify what type container/collection is being used in the given example.\n               tables = ["table 1", "table 2", "table 3"]',
    'Question #5 |    The statement below would print a Boolean value. Identify what is the Boolean value.\n               print(10 > 9)']
enter = input('\nPress "Enter" to start the quiz . . .')
global score
score = 0


def simula():
    global score, sagot1, sagot2, sagot3, sagot4, sagot5
    print('----------------------------------------------------------------------------------------------------------------')    
    print('----------------------------------------------------------------------------------------------------------------\n')        
    print(tanong[0])
    sagot1 = str(input('\nEnter your answer: '))
    print('\n----------------------------------------------------------------------------------------------------------------')    
    if sagot1 == 'print' or sagot1 == 'Print' or sagot1 == 'PRINT':
        score = score + 1
        print('                        ON TO THE NEXT QUESTION!')

    # ==============================================================
    print('----------------------------------------------------------------------------------------------------------------')    
    print('----------------------------------------------------------------------------------------------------------------\n')       
    print(tanong[1])
    sagot2 = str(input('Enter your answer: '))
    print('\n----------------------------------------------------------------------------------------------------------------')    
    if sagot2 == '#':
        print('On to the next question!')
        score = score + 1
        print('                        ON TO THE NEXT QUESTION!')

        # ==============================================================
    print('----------------------------------------------------------------------------------------------------------------')    
    print('----------------------------------------------------------------------------------------------------------------\n')       
    print(tanong[2])
    sagot3 = str(input('Enter your answer: '))
    print('\n----------------------------------------------------------------------------------------------------------------')     
    if sagot3 == "'''":
        print('On to the next question!')
        score = score + 1
        print('                        ON TO THE NEXT QUESTION!')

        # ==============================================================
    print('----------------------------------------------------------------------------------------------------------------')    
    print('----------------------------------------------------------------------------------------------------------------\n')       
    print(tanong[3])
    sagot4 = str(input('Enter your answer: '))
    print('\n----------------------------------------------------------------------------------------------------------------')        
    if sagot4 == 'list' or sagot4 == 'List' or sagot4 == 'LIST':
        print('On to the next question!')
        score = score + 1
        print('                        ON TO THE NEXT QUESTION!')

        # ==============================================================
    print('----------------------------------------------------------------------------------------------------------------')    
    print('----------------------------------------------------------------------------------------------------------------\n')          
    print(tanong[4])
    sagot5 = str(input('Enter your answer: '))
    print('\n----------------------------------------------------------------------------------------------------------------')
    if sagot5 == 'true' or sagot5 == 'True' or sagot5 == 'TRUE':
        score = score + 1


simula()

def resulta1():
    print("\n                                     ITO NA ANG KATAPUSAN NG PAGSUSULIT                                       \n")
    result = input('Enter "v" to view the result: ')
    if result == 'v' or result == 'V':
     print(
        '\n----------------------------------------------------------------------------------------------------------------')
     print(
        '                                     --------------------------------------                                     ')
     print('                                        HERE IS THE RESULT OF YOUR QUIZ:')
     print(
        '                                     --------------------------------------                                     ')
     if score == 0 or score == 1 or score == 2:
        print("\nComputer: IT'S OKAY TO MAKE MISTAKE SOMETIMES BUT MAKE SURE YOU TAKE IT AS A LESSON AND DO BETTER NEXT TIME")
     elif score == 3 or score == 4:
        print("\n          Computer: GOOD JOB YOU PASSED THE PAGSUSULIT")
     elif score == 5:
        print("\n          Computer: WOW YOU DID GREAT! YOU'RE GOING TO BE A GREAT PROGRAMMER IN THE FUTURE!")


resulta1()


def resulta2():
    print('\n           THIS IS YOUR SCORE:', score, '/', len(tanong))
    print('\n                                       THIS IS THE QUESTIONS AND YOUR ANSWERS:\n',
          "What is the missing part of the code below to output 'Hello World'? _____('Hello World') ",
          '\nTHIS IS YOUR ANSWER: ', sagot1, '\nThe Correct Answer is : "print" or "Print" or "LIST"',
          "\n\nComments in Python are written with a special character. Identify the missing special character. _This is a comment.",
          '\nTHIS IS YOUR ANSWER: ', sagot2, 'The Correct Answer is : "#"',
          "\n\nIt is used to create a multiline string to make a multi line comment.",
          '\nTHIS IS YOUR ANSWER: ', sagot3, "The Correct Answer is : '''  ",
          '\n\nIdentify what type container/collection is being used in the given example. tables = ["table 1", "table 2", "table 3"]',
          '\nTHIS IS YOUR ANSWER: ', sagot4, 'The Correct Answer is : "list" or "List" or "LIST"',
          "\n\nThis statement would print a Boolean value. Identify what is the Boolean value. print(10 > 9)",
          '\nTHIS IS YOUR ANSWER: ', sagot5, 'The Correct Answer is : "true" or "True" or "TRUE"')
    exit = input()
    if exit == "":
     exit()
resulta2()


