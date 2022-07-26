import os, workout
from win10toast import ToastNotifier
import time


def squats():
    toaster = ToastNotifier()
    toaster.show_toast("20 Bodyweight squats.",
                       "Stop! Do 20 Squats right now",
                       icon_path="./assets/logos/squats.ico",
                       duration=5)

def pushups():
    toaster = ToastNotifier()
    toaster.show_toast("20 Push-ups.",
                       "Stop! Do 20 pusups right now",
                       icon_path="./assets/logos/pushups.ico",
                       duration=5)