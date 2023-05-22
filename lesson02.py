#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

def flipCoins():
    import numpy as np
    coins = np.random.randint(5, 10)
    generator = lambda n:np.random.randint(2, size=n)
    
    coinsList = list(generator(coins))
    print(coinsList)
    
    for i in range(len(coinsList)):
        if coinsList[i] == 0:
            coinsList[i] = 1
    print("fixed coins list --> ", coinsList)
    

# Задача 12: Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
def guessNumber():
    import random
    x = random.randint(1, 1001)
    y = random.randint(1, 1001)
    print("cheat: " , x , y)
    
    sumOfDigits = x + y
    multiplDigits = x*y
    
    print(f"Guess two numbers. Prompt:\nSum = {sumOfDigits}, Multiplication = {multiplDigits}")
    while True:
        userAnswerX = input("X: ")
        userAnswerY = input("Y: ")
        
        if userAnswerX == str(x) and userAnswerY == str(y):
            print("You are right")
            break
        else:
            print('Try again')
  
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
def gradeNumber(n):
    counter = 2
    while (counter <=  n):
        print(counter)
        counter = counter * 2

# доп задания
# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
def findOddPosition():
    listOfNumbers = [1, 3, 5, 6 ,7 ,8 ,9]
    oddSum = 0
    
    for i in range(len(listOfNumbers)):
        if i % 2 == 0:
            oddSum = oddSum + listOfNumbers[i]
    print(oddSum)
    
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д


  
    
# ----------------------------------------
# flipCoins()
# guessNumber()  
# gradeNumber(513)
# findOddPosition()
