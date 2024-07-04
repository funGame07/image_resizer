from tkinter import *
from tkinter import filedialog
from image_resizer_module import *
from PIL import Image, ImageTk

def check_size(size):
    if size == "width" or size == "height":
        return 300
    else:
        try:
            return int(size)
        except:
            return 300
        
toplevels = []
def create_toplevel(path, w, h):
    global toplevels
    toplevels[0].destroy() if len(toplevels) else None

    toplevel = Toplevel(root)
    toplevel.title(f"{w}x{h}")
    photo = ImageTk.PhotoImage(file=path)
    img = Label(toplevel, text="hi", image=photo)
    img.image = photo
    img.pack()

    toplevels.append(toplevel)

def open_file():
    path = filedialog.askopenfilename(title="select image", filetypes=(("png files",".png"),))
    filepath.config(text="your image path: " + path)
    size = Image.open(path).size
    create_toplevel(path, *size)

def resize_image():
    width_img = check_size(width.get())
    height_img = check_size(height.get())

    path = filepath["text"][17:]
    image = Resize(path, width_img, height_img)
    image.resizing_image()

    filepath.config(text="success")
    create_toplevel(path, width_img, height_img)


root = Tk()
frame1 = Frame(
    root,
    padx=20,
    pady=20
)
frame1.pack()

Label(
    frame1,
    text="Select an image to resize",
    font=("arial", 20, "bold")
).pack()

Button(
    frame1,
    text="Open image",
    command=open_file
).pack()

filepath = Label(
    frame1,
    text="your image path: "
)
filepath.pack()

width= Entry(
    frame1,
    font=("times", 10),
    width=10
)
width.insert(0, "width")
width.bind("<FocusIn>", lambda x: width.delete(0,END))
width.pack()

height = Entry(
    frame1,
    font = ("times", 10),
    text="height",
    width=10
)
height.insert(0, "height")
height.bind("<FocusIn>", lambda x: height.delete(0,END))
height.pack()

Button(
    frame1,
    text="resize",
    command=resize_image
).pack()

img = Label(
    frame1,
)
img.pack()

root.mainloop()