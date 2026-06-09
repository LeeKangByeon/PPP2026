import tkinter as tk
from tkinter import simpledialog

Root = tk.Tk()
Root.withdraw()

def gui_input(text):
    return simpledialog.askstring(title="Test", prompt=text)


def main():
    count = gui_input("카운트 다운를 시작하시겠습니까?")
    if count == "네":
     for i in range(10, 0 , -1):
             print(f"{i:3d}")
             time.sleep(1)

if __name__ == "__main__":
    main()
