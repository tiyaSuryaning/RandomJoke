from tkinter import *
import pyjokes

def show_joke():
    entry0.delete(0, 'end')
    joke = pyjokes.get_joke()
    entry0.insert(0, joke)

def btn_clicked():
    show_joke()

window = Tk()
window.title('Random Joke Generator')
window.geometry("400x200")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 200,
    width = 400,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    200.0, 100.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#658cff",
    highlightthickness = 0)

entry0.place(
    x = 49.88999938964844, y = 60,
    width = 300.2200012207031,
    height = 78)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 160, y = 155,
    width = 80,
    height = 30)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    170.5, 35.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()
