from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from Fsignup import signup
from Flogin import Login

class Login_System:
    def __init__(self,root):
        self.root=root
        # self.root.geometry("1920x1080+0+0")
        self.root.title("login system")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        #bg image
        img1=Image.open(r"C:\Users\janvi\Downloads\project sdp\frontend_img\bg.webp")
        img1=img1.resize((screen_width,screen_height),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=screen_width,height=screen_height)

        title_lbl=Label(bg_img,text="Signup-login Face Recognition System",font=("times new roman",35,"bold"),fg="red")
        title_lbl.place(x=5,y=5,width=screen_width,height=45)


        #button 1 for sign up
        img2=Image.open(r"C:\Users\janvi\Downloads\project sdp\frontend_img\signup.png")
        img2=img2.resize((220,220),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(bg_img,image=self.photoimg2,command=self.signUP,cursor="hand2")
        b1.place(x=450,y=400,width=300,height=300)

        b1_1=Button(bg_img,text="Sign up",command=self.signUP,cursor="hand2",font=("times new roman",25,"bold"),fg="red")
        b1_1.place(x=450,y=700,width=300,height=40)

         #button 2 for login
        img3=Image.open(r"C:\Users\janvi\Downloads\project sdp\frontend_img\login1.png")
        img3=img3.resize((220,220),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(bg_img,image=self.photoimg3,command=self.login,cursor="hand2")
        b1.place(x=1150,y=400,width=300,height=300)

        b1_1=Button(bg_img,text="Login",command=self.login,cursor="hand2",font=("times new roman",25,"bold"),fg="red")
        b1_1.place(x=1150,y=700,width=300,height=40)



    #================functions ========================

    def signUP(self):
        self.new_window=Toplevel(self.root)
        self.new_window.state('zoomed')
        self.app=signup(self.new_window)

    def login(self):
        self.new_window=Toplevel(self.root)
        self.new_window.state('zoomed')
        self.app=Login(self.new_window)

    






if __name__ =="__main__":
    root=Tk()
    obj=Login_System(root)
    # root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")  # Fullscreen window
    root.state('zoomed')
    root.mainloop()