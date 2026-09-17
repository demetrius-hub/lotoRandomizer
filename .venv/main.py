"""
╔════════════════════════════════════════════╗
║     Программа генерации случайных чисел    ║
╚════════════════════════════════════════════╝

Версия:     0.2.5
Автор:      Дмитрий Подольский
Дата:       2026-09-15
Лицензия:   MIT

Описание:
    Программа разрабатывалась в целях практики при самостоятельном обучении основам Python.

Использование:
    python main.py

Требования:
    - Python 3.14+
"""

import random
import time
from pathlib import Path
import secrets
import os
from datetime import datetime
from playsound3 import playsound
from colorama import Fore, Back, Style, init

Повтор_программы = 'y'
while (Повтор_программы == 'y'):
    try:
        init(autoreset=True)
        while True:
            try:
                количество_чисел = int(input("Сколько чисел сгенерировать: "))
                if (количество_чисел < 1):
                    print(Fore.RED + "Ошибка! Число должно быть положительным.")
                    continue
                break
            except ValueError:
                print(Fore.RED + "Ошибка! Введите целое число")
        while True:
            try:
                от = int(input("От: "))
                if (от < 1):
                    print(Fore.RED + "Ошибка! Число должно быть положительным.")
                    continue
                break
            except ValueError:
                print(Fore.RED + "Ошибка! Введите целое число")
        while True:
            try:
                до = int(input("До: "))
                if (до < 2):
                    print(Fore.RED + "Ошибка! Число должно быть положительным и не меньше 2")
                    continue
                break
            except ValueError:
                print(Fore.RED + "Ошибка! Введите целое число")
        while True:
            try:
                промежуток_в_секундах = int(input("Максимальный промежуток времени между генерациями (в минутах): ")) * 60
                if (промежуток_в_секундах < 0):
                    print(Fore.RED + "Ошибка! Число должно быть не меньше 0")
                    continue
                break
            except ValueError:
                print(Fore.RED + "Ошибка! Введите целое число")

        print(Fore.GREEN + "\nРезультат: ")
        счётчик = 0
        накопитель_чисел = []
        while счётчик < количество_чисел:
            if промежуток_в_секундах > 0:
                случайный_промежуток = random.randint(1, промежуток_в_секундах)
                time.sleep(случайный_промежуток)

            # Генерация с помощью комбинирования системного RNG, os.urandom, secrets и смешивания через XOR
            def генерация_числа():
                значение1 = secrets.randbelow(до)
                значение2 = int.from_bytes(os.urandom(от), 'big') % до
                значение3 = random.SystemRandom().randint(от-1, до-1)
                комбинированный = (значение1 ^ значение2 ^ значение3) % до + от
                return комбинированный

            накопитель_чисел.append(генерация_числа())

            # Проверка сгенерированных чисел на совпадения
            if счётчик > 0:
                второстипенный_счётчик = 0
                while второстипенный_счётчик < счётчик:
                    if накопитель_чисел[счётчик] == накопитель_чисел[второстипенный_счётчик]:
                        накопитель_чисел[счётчик] = генерация_числа()
                        второстипенный_счётчик = -1
                    второстипенный_счётчик += 1

            playsound('resources/sounds/key.mp3')
            print(накопитель_чисел[счётчик], end=" ")
            счётчик += 1
        print()

        playsound("resources/sounds/finish.mp3")

        накопитель_чисел.sort()
        documents = Path.home() / "Documents"
        file_path = documents / "Сгенерированные числа.txt"
        текущая_дата = datetime.now()
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write('Дата: ' + текущая_дата.strftime("%d.%m.%Y | %H:%M:%S"))
            f.write("\n---------------------------")
            f.write('\nРезультат: ')
            for элемент in накопитель_чисел:
                f.write(str(элемент) + " ")
            f.write("\n===========================\n\n")

        Повтор_программы = input(Fore.BLUE + "\nСгенерировать ещё раз? (y/n): ")
        print()

    except:
        print(Fore.GREEN + "\nПрограмма завершила свою работу...")