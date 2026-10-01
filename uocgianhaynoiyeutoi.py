import sys
import threading
import tkinter as tk
from time import sleep
import pygame

pygame.mixer.init()
try:
    pygame.mixer.music.load("uocgianhaynoiyeutoi.mp3")
except Exception as e:
    print(
        f"Lỗi tải nhạc: {e}. Vui lòng kiểm tra lại tên file 'uocgianhaynoiyeutoi.mp3'"
    )

root = tk.Tk()
root.title("Lyrics Player")
root.geometry("600x400")
root.configure(bg="#1e1e1e")  

label = tk.Label(
    root,
    text="",
    font=("Segoe UI", 16, "bold"),
    fg="#ffffff",
    bg="#1e1e1e",
    wraplength=550,
    justify="center",
)
label.pack(expand=True)

def animate_lyrics():
    if pygame.mixer.music.get_busy() or True:
        pygame.mixer.music.play()

    lines = [
        ("Nhớ nhớ thương nhau chỉ làm trái tim đau", 0.05, 0.3),
        ("Em đã bước đi mau chẳng còn nhớ tên anh", 0.05, 0.3),
        ("Hứa chi ba lời nhảm nhí xa xăm rồi em cũng quay lưng vì em hết thương anh", 0.05, 0.1),
        ("Khóc-khóc đi em nhoè hết mascara", 0.05, 0.1),
        ("Anh đã ngước lên cao tại sao chẳng yêu anh ", 0.06, 0.1),
        ("Em nói rằng anh rất tốt babe à", 0.05, 0.1),
        ("Nhưng anh không thể ép buộc một người chẳng yêu anh", 0.04, 0.5),
    ]

    sleep(1.5)

    for line, char_delay, line_delay in lines:
        current_text = ""
        for char in line:
            current_text += char
            label.config(text=current_text)
            sleep(char_delay)
        sleep(line_delay)

def start_app():
    threading.Thread(target=animate_lyrics, daemon=True).start()

def on_closing():
    pygame.mixer.music.stop()
    root.destroy()
    sys.exit()


root.protocol("WM_DELETE_WINDOW", on_closing)

root.after(500, start_app)
root.mainloop()