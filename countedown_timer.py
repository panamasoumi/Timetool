import tkinter as tk
import time
import threading

# Function for Countdown Timer
def countdown_timer(seconds):
    while seconds >= 0 and not stop_flag[0]:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        timer_label.config(text=timer)
        root.update()
        time.sleep(1)
        seconds -= 1

    if not stop_flag[0]:
        timer_label.config(text="Time's up!")  

# Function to Start Countdown Timer
def start_countdown():
    try:
        seconds = int(entry_time.get())  
        stop_flag[0] = False
        countdown_thread = threading.Thread(target=countdown_timer, args=(seconds,))
        countdown_thread.start()
    except ValueError:
        timer_label.config(text="Invalid Input")  
# Function to Stop Timer
def stop_timer():
    stop_flag[0] = True
    timer_label.config(text="Stopped")

# Function to Reset Timer
def reset_timer():
    stop_flag[0] = True  # Stop the timer
    timer_label.config(text="00:00") 
    entry_time.delete(0, tk.END)  


# Initialize Tkinter Window
root = tk.Tk()
root.title("Countdown Timer ")
root.geometry("300x300")


stop_flag = [False] 


# Countdown Timer Section
frame_timer = tk.Frame(root)
frame_timer.pack(pady=20)

tk.Label(frame_timer, text="Countdown Timer", font=("Helvetica", 16)).pack()
entry_time = tk.Entry(frame_timer, width=10, font=("Helvetica", 14))
entry_time.pack(pady=10)
tk.Button(frame_timer, text="Start Timer", command=start_countdown, font=("Helvetica", 12)).pack(pady=5)
tk.Button(frame_timer, text="Stop Timer", command=stop_timer, font=("Helvetica", 12)).pack(pady=5)
tk.Button(frame_timer, text="Reset Timer", command=reset_timer, font=("Helvetica", 12)).pack(pady=5)
timer_label = tk.Label(frame_timer, text="00:00", font=("Helvetica", 24), fg="blue")
timer_label.pack(pady=10)


# Run the Tkinter Event Loop
root.mainloop()
