# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
def listCase01():
    n = int(input("Insert the lenght of the list >   "))
    x = int(input("number: "))
    count = 0
    listOfElements = []
    
    for i in range(0, n):
        listOfElements.append(i+1)

    print("list of elements: ")
    print(listOfElements)
    
    for i in listOfElements:
        if i == x:
            count += 1
    print(f"--> {count}")

    
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
def listCase02():
    n = int(input("Insert the lenght of the list >   "))
    x = int(input("number: "))
    number = 0
    listOfElements = []
    for i in range(0, n):
        listOfElements.append(i+1)
    
    for i in listOfElements:
        if i == x or x > i:
            number = i
    print(number)


# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 

# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

def scrableCase():
    import re
    name = input("Insert your name // Введи имя>   ").upper()
    count = 0
  
    engDict = {
        1:["A","E","I","O","U","L","N","S","T","R"], 
        2:["G","D"], 
        3:["B","C","M","P"], 
        4:["F","H","V","W","Y"], 
        5:["K"], 
        6:["J","X"], 
        7:["Q","Z"], 
    }
    
    rusDict = {
        1:["А","В","Е","И","Н","О","Р","С","Т"], 
        2:["Д", "К", "Л", "М", "П", "У"], 
        3:["Б", "Г", "Ё", "Ь", "Я"], 
        4:["Й", "Ы"], 
        5:["Ж", "З", "Х", "Ц", "Ч"], 
        6:["Ш", "Э", "Ю"], 
        7:["Ф", "Щ", "Ъ"], 
    }
    
    mainDict = engDict
    
    if bool(re.search('[а-яА-Я]', name)) != 0:
        mainDict = rusDict
    
    for char in name:
        
        for i in mainDict:
            if char in mainDict[i]:
                count = count + i
    print(count)
    
scrableCase()