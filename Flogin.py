from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import json

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Background image
        img1 = Image.open(r"C:\Users\janvi\Downloads\project sdp\frontend_img\bg.webp")
        img1 = img1.resize((screen_width, screen_height), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=screen_width, height=screen_height)

        # Title label
        title_lbl = Label(bg_img, text="Welcome to Login Page", font=("times new roman", 35, "bold"), fg="red")
        title_lbl.place(x=5, y=5, width=screen_width, height=45)

        # Login button with animation
        self.login_btn = Button(bg_img, text="Click Here to Login",command=self.face_recog, font=("times new roman", 20, "bold"), bg="blue", fg="white", cursor="hand2", relief=RIDGE)
        self.login_btn.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.login_btn.bind("<Enter>", self.on_enter)
        self.login_btn.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.login_btn.config(bg="darkblue", fg="yellow")

    def on_leave(self, event):
        self.login_btn.config(bg="blue", fg="white")

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            
            with open("email_to_id.json","r") as f:
                id_to_email={v:k for k,v in json.load(f).items()}
            
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                predicted_email=id_to_email.get(id,"Unknown ID")
                print(predicted_email)
                conn=mysql.connector.connect(host="localhost",user="root",password="Janvi@1802",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select name from user where email= %s",(predicted_email,))
                n=my_cursor.fetchone()
                # print(n)
                name=n[0]

                # my_cursor.execute("select email from user where ="+str(id))
                # r=my_cursor.fetchone()
                # r="+".join(r)
                

                if confidence>77:
                    cv2.putText(img,f"Name:{name}",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Email:{predicted_email}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"unknown face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]
        
            return coord 
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img 
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to face recognition",img)

            if cv2.waitKey(10)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    root.mainloop()

