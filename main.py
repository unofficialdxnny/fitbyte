import os, workout
from win10toast import ToastNotifier
import time

while True:
    workout.squats()
    time.sleep(10)
    workout.pushups()