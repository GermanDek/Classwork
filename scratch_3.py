from datetime import datetime
from time import sleep

def time_now(msg, dt=datetime.now()):
    print(msg, dt)

time_now("Сейчас такое время:")
sleep(1)
time_now("Прошла секунда:")
time_now("Ничего не понимаю...")