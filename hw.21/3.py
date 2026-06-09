import tkinter as tk
from tkinter import simpledialog
import random
import PySimpleGUI

Root = tk.Tk()
Root.withdraw()

def gui_input(text):
    return simpledialog.askstring(title="Test", prompt=text)


def lotto():
    numbers = random.sample(range(1, 46), 6)
    return numbers


def main():
    A = gui_input("로또 번호를 뽑을까요? ")
    if A == "네":
        result = lotto()
        print(f"회차 1227  당첨번호  {result}입니다")


if __name__ == "__main__":
    main()