from PIL import Image, ImageTk, ImageGrab
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename, asksaveasfile


def buttonpress(function, *args):
    value = function(*args)
    print(type(value))


def open_file():
    img_path = askopenfilename(title="Select A File", filetype=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    if img_path:
        canvas.imageList = []  # To get rid of garbage collector, empty list is added
        img = Image.open(img_path)
        img = img.resize((750, 500), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(img)
        created_image_id = canvas.create_image(450, 250, image=image)
        canvas.imageList.append(image)

        # Change button displays
        browse_button.grid_forget()
        logo_button.grid(column=1, row=5)
        text_button.grid(column=4, row=5)
        save_button.grid(column=7, row=5)
        return created_image_id


def add_logo():
    logo_path = askopenfilename(title="Select A File", filetype=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    if logo_path:
        canvas.logoList = []  # To get rid of garbage collector, empty list is added
        logo = Image.open(logo_path)
        logo = logo.resize((200, 200), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)
        canvas.create_image(450, 250, image=logo)
        canvas.logoList.append(logo)

        # Change button displays
        logo_button.grid_forget()
        text_button.grid(column=3, row=5)
        save_button.grid(column=6, row=5)


def on_drag(event):
    if canvas.selected != 1:
        # Calculate distance moved from last position
        dx, dy = event.x - canvas.startxy[0], event.y - canvas.startxy[1]
        # Move the selected item
        canvas.move(canvas.selected, dx, dy)
        # Update last position
        canvas.startxy = (event.x, event.y)


def on_click(event):
    selected = canvas.find_overlapping(event.x - 10, event.y - 10, event.x + 10,
                                       event.y + 10)  # List of selected items with mouse
    canvas.startxy = (event.x, event.y)  # Define "startxy" variable in canvas class

    if selected:
        canvas.selected = selected[-1]  # Select the top-most item #define "selected" variable in canvas class
    else:
        canvas.selected = None


def add_text():
    canvas.create_text(100, 10, fill="darkblue", font="Times 20 italic bold",
                       text="Click the bubbles that are multiples of two.")



def save_pic(widget):
    file = asksaveasfilename(filetypes=[('Portable Network Graphics', '*.png')])
    x = root.winfo_rootx() + 75
    y = root.winfo_rooty()
    x1 = x + widget.winfo_width() - 175
    y1 = y + widget.winfo_height()
    ImageGrab.grab().crop((x, y, x1, y1)).save(file + ".png")


root = tk.Tk()
root.geometry("900x600")
root.resizable(0, 0)
root.title("Photo Watermark Application")

canvas = tk.Canvas(root, width=900, height=500)
canvas.grid(column=0, row=0, columnspan=9, rowspan=5)

# Browse button
browse_text = tk.StringVar()
browse_button = tk.Button(root, command=lambda: buttonpress(open_file), textvariable=browse_text, font="Ariel",
                          bg="black",
                          fg="white",
                          height=2, width=10)
browse_text.set("Browse")
browse_button.grid(column=4, row=5)

# Add logo button
add_logo_text = tk.StringVar()
logo_button = tk.Button(root, command=add_logo, textvariable=add_logo_text, font="Ariel", bg="black", fg="white",
                        height=2, width=10)
add_logo_text.set("Add Logo")

# Add text button
add_text_text = tk.StringVar()
text_button = tk.Button(root, command=add_text, textvariable=add_text_text, font="Ariel", bg="black", fg="white",
                        height=2, width=10)
add_text_text.set("Add Text")

# Add save picture button
save_text_text = tk.StringVar()
save_button = tk.Button(root, command=lambda: save_pic(canvas), textvariable=save_text_text, font="Ariel", bg="black",
                        fg="white",
                        height=2, width=10)
save_text_text.set("Save Picture")

root.bind("<B1-Motion>", on_drag)  # B1-MOTION = Dragging items using mouse
root.bind("<Button-1>", on_click)  # BUTTON-1 = Left click with mouse

root.mainloop()