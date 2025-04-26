from tkinter import *
from PIL import Image, ImageTk
import os
import numpy as np
import cv2
from tkinter import messagebox
import json

class Training:
    def __init__(self, root):
        self.root = root
        self.root.title("Training Window")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Background Image
        img1 = Image.open(r"C:\Users\janvi\Downloads\project sdp\frontend_img\bg.webp")
        img1 = img1.resize((screen_width, screen_height), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=screen_width, height=screen_height)

        # Title Label
        title_lbl = Label(bg_img, text="Training Window", font=("times new roman", 35, "bold"), fg="red", bg="white")
        title_lbl.place(x=0, y=5, width=screen_width, height=50)

        # Left Side - Big Image
        img2 = Image.open(r"C:\Users\janvi\Downloads\project sdp\frontend_img\a1.jpg")  # Replace with your image path
        img2 = img2.resize((screen_width // 2, int(screen_height * 0.7)), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        left_img = Label(bg_img, image=self.photoimg2)
        left_img.place(x=50, y=screen_height // 4, width=screen_width // 2, height=int(screen_height * 0.5))

        # Right Side - Button
        btn_frame = Frame(bg_img, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=(screen_width // 2) + 200, y=(screen_height // 3), width=500, height=200)

        train_btn = Button(btn_frame, text="Train Data", font=("times new roman", 20, "bold"), bg="blue", fg="white", cursor="hand2", command=self.train_data)
        train_btn.place(relx=0.5, rely=0.5, anchor=CENTER, width=200, height=70)

    def train_data(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        email_to_id={}
        current_id=0
        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            #change in future 

            filename=os.path.split(image)[1]  
            id=(filename.split('.')[1])+"."+filename.split('.')[2]
           
            #map email to numeric id
            if id not in email_to_id:
                email_to_id[id]=current_id
                current_id+=1


            numeric_id=email_to_id[id]
            
            faces.append(imageNp)
            ids.append(numeric_id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()

        with open("email_to_id.json","w") as f:
            json.dump(email_to_id,f,indent=4)
        messagebox.showinfo("Result","training dataset completed")

if __name__ == "__main__":
    root = Tk()
    obj = Training(root)
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")  # Fullscreen window
    root.mainloop()
