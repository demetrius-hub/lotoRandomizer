import random
import time
from pathlib import Path
import secrets
import os
import random
from datetime import datetime
from playsound3 import playsound

количество_чисел = int(input("Сколько чисел сгенерировать: "))
от = int(input("От: "))
до = int(input("До: "))
промежуток_в_секундах = int(input("Максимальный промежуток времени между генерациями (в минутах): ")) * 60

print("\nРезультат: ")
счётчик = 0
накопитель_чисел = []
while счётчик < количество_чисел:
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