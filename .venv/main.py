import random
import time
from pathlib import Path
import secrets
import os
import random

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
    value1 = secrets.randbelow(до)
    value2 = int.from_bytes(os.urandom(от), 'big') % до
    value3 = random.SystemRandom().randint(от-1, до-1)
    # Смешиваем значения через XOR
    combined = (value1 ^ value2 ^ value3) % до + от
    накопитель_чисел.append(combined)

    # Проверка сгенерированных чисел на совпадения
    if счётчик > 0:
        второстипенный_счётчик = 0
        while второстипенный_счётчик < счётчик:
            if накопитель_чисел[счётчик] == накопитель_чисел[второстипенный_счётчик]:
                накопитель_чисел[счётчик] = random.randint(от, до)
                второстипенный_счётчик = -1
            второстипенный_счётчик += 1

    print(накопитель_чисел[счётчик], end=" ")
    счётчик += 1
print()

накопитель_чисел.sort()
documents = Path.home() / "Documents"
file_path = documents / "Лотерейные номера.txt"
with open(file_path, 'a', encoding='utf-8') as f:
    f.write('\nРезультат: ')
    for элемент in накопитель_чисел:
        f.write(str(элемент) + " ")