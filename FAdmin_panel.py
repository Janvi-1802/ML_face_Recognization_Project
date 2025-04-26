from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from Ftrain import Training

class AdminPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Panel")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Background Image
        img1 = Image.open(r"C:\Users\janvi\Downloads\project sdp\frontend_img\bg.webp")
        img1 = img1.resize((screen_width, screen_height), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=screen_width, height=screen_height)

        # Title Label
        title_lbl = Label(bg_img, text="Admin Panel", font=("times new roman", 35, "bold"), fg="red", bg="white")
        title_lbl.place(x=0, y=5, width=screen_width, height=50)

        # Increase Button Size
        btn_size = 300  # Adjust button size
        button_spacing = 100  # Space between buttons

        # Load Button Images (Resized)
        # self.img_btn1 = ImageTk.PhotoImage(Image.open(r"C:\Users\janvi\Downloads\project sdp\frontend_img\user.jpg").resize((btn_size, btn_size), Image.LANCZOS))
        self.img_btn2 = ImageTk.PhotoImage(Image.open(r"C:\Users\janvi\Downloads\project sdp\frontend_img\training1.webp").resize((btn_size, btn_size), Image.LANCZOS))
        self.img_btn3 = ImageTk.PhotoImage(Image.open(r"C:\Users\janvi\Downloads\project sdp\frontend_img\view_Photo.jpg").resize((btn_size, btn_size), Image.LANCZOS))

        # Calculate X positions to center buttons
        total_width = (2 * btn_size) + ( button_spacing)
        start_x = (screen_width - total_width) // 2
        y_position = (screen_height // 2) - (btn_size // 2)  # Center vertically

        # Create Buttons
        # self.btn1 = Button(bg_img, image=self.img_btn1, command=self.function1, bd=0, cursor="hand2")
        # self.btn1.place(x=start_x, y=y_position, width=btn_size, height=btn_size)
        # btn1_1=Button(bg_img,text="Show Users",command=self.function1,cursor="hand2",font=("times new roman",25,"bold"),fg="red")
        # btn1_1.place(x=start_x, y=y_position+btn_size, width=btn_size, height=100)

        self.btn2 = Button(bg_img, image=self.img_btn2, command=self.TrainData, bd=0, cursor="hand2")
        self.btn2.place(x=start_x , y=y_position, width=btn_size, height=btn_size)
        btn2_1=Button(bg_img,text="Train the data",command=self.TrainData,cursor="hand2",font=("times new roman",25,"bold"),fg="red")
        btn2_1.place(x=start_x, y=y_position+btn_size, width=btn_size, height=100)

        self.btn3 = Button(bg_img, image=self.img_btn3, command=self.open_img, bd=0, cursor="hand2")
        self.btn3.place(x=start_x + (btn_size + button_spacing), y=y_position, width=btn_size, height=btn_size)
        btn3_1=Button(bg_img,text="View Photos",command=self.open_img,cursor="hand2",font=("times new roman",25,"bold"),fg="red")
        btn3_1.place(x=start_x+(btn_size)+(button_spacing), y=y_position+btn_size, width=btn_size, height=100)

    # Dummy functions for button actions
    def function1(self):
        print("Button 1 Clicked")

    def TrainData(self):
       self.new_window=Toplevel(self.root)
       self.new_window.state('zoomed')
       self.app=Training(self.new_window)

    def open_img(self):
        os.startfile("data")

if __name__ == "__main__":
    root = Tk()
    obj = AdminPanel(root)
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")  # Fullscreen window
    root.state('zoomed')
    root.mainloop()
