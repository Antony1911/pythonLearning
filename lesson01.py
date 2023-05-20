# Задача 2: Найдите сумму цифр трехзначного числа.
def sumOfTripple(digit):
    sum = 0
    for number in str(digit):
        sum = sum + int(number)
    print("sum jf digits: " + sum)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
def sumOfCranes(num):
    pete = serge = num/6
    kate = (pete + serge)*2
    print(f"Kate: {kate}\nPete: {pete}\nSerge: {serge}")


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
def checkLuckyTicket(ticketNumber):
    leftSide = 0
    rightSide = 0
    tempList = []

    for number in str(ticketNumber):
        tempList.append(int(number))
    
    for i in tempList[:3]:
        leftSide = leftSide + i
    for j in tempList[3:]:
        rightSide = rightSide + j
    
    if leftSide == rightSide:
        print("This is a lucky ticket")
    else:
        print("nope")


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
def checkPossibilityToSplit(m, n, k):
    if k // n or k // m:
        print('Yess')
    else:
        print("no")

# -------------------------------
# sumOfTripple(321)
# sumOfCranes(24)
# checkLuckyTicket(385916)
# checkPossibilityToSplit(3, 2, 6)