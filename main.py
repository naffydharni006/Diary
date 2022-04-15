import tkinter as tk
import datetime
import ctypes.wintypes
from tkinter import messagebox, PhotoImage

window = tk.Tk()
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry(str(width)+"x"+str(height-70)+"+0+0")
window.title("Diary Entry")
window.configure(bg='#444444')

CSIDL_PERSONAL = 5       # My Documents
SHGFP_TYPE_CURRENT = 0   # Get current, not default value

buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)

def msg(title, message):
    messagebox.showinfo(title,  message)

def doneForNow():
    note = entry.get("1.0", tk.END)
    x = datetime.datetime.now()
    dayStr = x.strftime("%A")
    month = x.strftime("%B")
    yearStr = str(x.year)
    dateStr = str(x.strftime("%d"))
    yearInt = x.year
    dateInt = x.strftime("%d")
    monthStr = x.strftime("%m")

    Filename = dateStr + "-" + monthStr + "-" + yearStr + ".txt"
    header = "Date: " + dateStr + " " + month + " " + yearStr + "\nDay: " + dayStr + "\n\n"
    destination = buf.value + "\\Naffy's Diary\\" + Filename
    # destination = Filename

    try:
        file = open(destination, "rt")
        file.read()
        file.close()
    except:
        file = open(destination, "at")
        file.write(header + note)
        file.close()
        print("Created a new file: " + Filename)
        entry.delete("1.0", tk.END)
        msg("Success!", "New file created and saved.")
    else:
        file = open(destination, "at")
        file.write("\n" + note)
        file.close()
        entry.delete("1.0", tk.END)
        print("Edited the file: " + Filename)
        msg("Success!", "Edited the previous file")

def doneForYest():
    note = entry.get("1.0", tk.END)
    x = datetime.date.today() - datetime.timedelta(days=1)
    dayStr = x.strftime("%A")
    month = x.strftime("%B")
    yearStr = str(x.year)
    dateStr = str(x.strftime("%d"))
    yearInt = x.year
    dateInt = x.strftime("%d")
    monthStr = x.strftime("%m")

    Filename = dateStr + "-" + monthStr + "-" + yearStr + ".txt"
    header = "Date: " + dateStr + " " + month + " " + yearStr + "\nDay: " + dayStr + "\n\n"
    destination = buf.value + "\\Naffy's Diary\\" + Filename
    # destination = Filename

    try:
        file = open(destination, "rt")
        file.read()
        file.close()
    except:
        file = open(destination, "at")
        file.write(header + note)
        file.close()
        print("Created a new file: " + Filename)
        entry.delete("1.0", tk.END)
        msg("Success!", "New file created and saved.")
    else:
        file = open(destination, "at")
        file.write("\n" + note)
        file.close()
        entry.delete("1.0", tk.END)
        print("Edited the file: " + Filename)
        msg("Success!", "Edited the previous file")

def no():
    msg("Sorry", "But I know that you can't predict the future. HEHEHE")

frame = tk.Frame(window, bg='#444444')

greeting = tk.Label(text="Hello Naffy, What is new today?", height=3, font=("Comic Sans MS", 20, "bold"), bg='#444444', fg='#cccccc')
greeting.pack()

entry = tk.Text(height=20, font=("Comic Sans MS", 13), bg='#cccccc')
entry.pack()

nowImg = PhotoImage(file='./assets/done_for_now.png')
yestImg = PhotoImage(file='./assets/done_for_yest.png')
tomImg = PhotoImage(file='./assets/done_for_tom.png')

button2 = tk.Button(frame, image=yestImg, borderwidth=0, bg='#444444', command=doneForYest)
button2.pack(side="left", padx=5, pady=2)

button3 = tk.Button(frame, image=tomImg, borderwidth=0, bg='#444444', command=no)
button3.pack(side="right", padx=5, pady=2)

button = tk.Button(frame, image=nowImg, borderwidth=0, bg='#444444', command=doneForNow)
button.pack(side="right", padx=5, pady=2)

frame.pack(expand=True, padx=10, pady=10)

window.mainloop()
