
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class SlideshowApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SlideshowApp")
        self.image_directory = None 
        self.image_files = []
        self.images = []
        self.index = 0
        self.label = None
        self.bind("<Control-q>", self.quit)
        self.browse_image_directory()
        self.start_slideshow()

    def browse_image_directory(self):
        self.image_directory = filedialog.askdirectory()
        self.image_files = os.listdir(self.image_directory)

    def start_slideshow(self):
        for file in self.image_files:
            image = Image.open(os.path.join(self.image_directory, file))
            self.images.append(ImageTk.PhotoImage(image))
        self.show_slide()

    def show_slide(self):
        self.geometry("{}x{}+0+0".format(self.winfo_screenwidth(), 
            self.winfo_screenheight()))
        self.attributes("-fullscreen", True)
        self.configure(background='black')
        self.label = tk.Label(image=self.images[self.index], 
            bg='black')
        self.label.pack()
        filename = os.path.splitext(self.image_files[self.index])[0]
        tk.Label(self, text=filename, fg="white", bg="black",
            font=("Romantic", 40), anchor="nw").place(x=20, y=20)
        self.after(3000, self.next_slide)

    def next_slide(self):
        self.index += 1
        if self.index == len(self.image_files):
            self.index = 0
        self.label.destroy()
        self.show_slide()

if __name__ == "__main__":
    app = SlideshowApp()
    app.bind('<Control-q>', lambda event: app.destroy())
    app.bind('<Escape>', lambda event: app.destroy())
    app.mainloop()