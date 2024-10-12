from threading import Thread
from time import sleep

# Создаём класс, который будет работать в потоке
class Knight(Thread):
    def __init__(self, name: str, power: int):
        Thread.__init__(self)
        self.name = name  # Имя рыцаря
        self.power = power # Сила рыцаря
        self.enemies = 100 # количество врагов у каждого потока

    # Метод, который запускается при старте потока
    def run(self):
        days = 0
        print(f"{self.name}, на нас напали") # Сообщение о начале сражения
        # Пока у рыцаря остаются враги
        for i in range(self.power):
            if self.enemies > 0:
                days += 1
                self.enemies -= self.power # выбираем минимальное значение между силой и количеством врагов и отнимаем их от
                print(f"{self.name}, сражается {days} день(дня)..., осталось {self.enemies} войнов")
                sleep(0.5)
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")




# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

# Ждем завершения всех рыцарей
first_knight.join()
second_knight.join()

print("Все рыцари победили своих врагов!")


