import random
import time
from pathlib import Path
import secrets
import os
import random
from datetime import datetime

количество_чисел = int(input("Сколько чисел сгенерировать: "))
от = int(input("От: "))
до = int(input("До: "))
промежуток_в_секундах = int(input("Промежуток времени между генерациями (в минутах): ")) * 60

print("\nРезультат: ")
счётчик = 0
накопитель_чисел = []
while счётчик < количество_чисел:
    случайный_промежуток = random.randint(1, промежуток_в_секундах)
    time.sleep(случайный_промежуток)

    # Комбинируем: системный RNG, os.urandom и secrets
    значение1 = secrets.randbelow(до)
    значение2 = int.from_bytes(os.urandom(от), 'big') % до
    значение3 = random.SystemRandom().randint(от-1, до-1)
    # Смешиваем значения через XOR
    комбинированный = (значение1 ^ значение2 ^ значение3) % до + от
    накопитель_чисел.append(комбинированный)

    # Проверка сгенерированных чисел на совпадения
    if счётчик > 0:
        второстипенный_счётчик = 0
        while второстипенный_счётчик < счётчик:
            if накопитель_чисел[счётчик] == накопитель_чисел[второстипенный_счётчик]:

                значение1 = secrets.randbelow(до)
                значение2 = int.from_bytes(os.urandom(от), 'big') % до
                значение3 = random.SystemRandom().randint(от - 1, до - 1)
                комбинированный = (значение1 ^ значение2 ^ значение3) % до + от
                накопитель_чисел[счётчик] = комбинированный

                второстипенный_счётчик = -1
            второстипенный_счётчик += 1

    print(накопитель_чисел[счётчик], end=" ")
    счётчик += 1
print()

накопитель_чисел.sort()
documents = Path.home() / "Documents"
file_path = documents / "Лотерейные номера.txt"
текущая_дата = datetime.now()
with open(file_path, 'a', encoding='utf-8') as f:
    f.write('Дата: ' + текущая_дата.strftime("%d.%m.%Y | %H:%M:%S"))
    f.write("\n--------------------------")
    f.write('\nРезультат: ')
    for элемент in накопитель_чисел:
        f.write(str(элемент) + " ")
    f.write("\n==========================\n\n")