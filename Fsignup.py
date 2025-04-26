from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os,random
import numpy as np

class signup:
    def __init__(self,root):
        self.root=root
        # self.root.geometry("1920x1080+0+0")
        self.root.title("login system")

        #----variables---
        self.var_gender=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

     #bg image
        img1=Image.open(r"C:\Users\janvi\Downloads\project sdp\frontend_img\bg.webp")
        img1=img1.resize((screen_width,screen_height),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=screen_width,height=screen_height)

        title_lbl=Label(bg_img,text="Welcome to sign up page",font=("times new roman",35,"bold"),fg="red")
        title_lbl.place(x=5,y=5,width=screen_width,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=30,y=60,width=screen_width-70,height=screen_height-190)

        #label frame 
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="signup",font=("times new roman",25,"bold"))
        left_frame.place(x=300,y=70,width=1000,height=780)


        user_detail_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="User details ",font=("times new roman",22,"bold"))
        user_detail_frame.place(x=35,y=75,width=900,height=300)

        gender_label=Label(user_detail_frame,text="Gender",font=("times new roman",20,"bold"))
        gender_label.grid(row=0,column=0,padx=8,pady=15)
        gender_combo=ttk.Combobox(user_detail_frame,textvariable=self.var_gender,font=("times new roman",20,"bold"),width=20,state="readonly")
        gender_combo["values"]=("Select gender","Female","Male","Other")
        gender_combo.current(0)
        gender_combo.grid(row=0,column=1,padx=2,pady=15)

        name_label=Label(user_detail_frame,text="Name",font=("times new roman",20,"bold"))
        name_label.grid(row=1,column=0,padx=8,sticky=W)
        name_entry=ttk.Entry(user_detail_frame,textvariable=self.var_name,width=40,font=("times new roman",20,"bold"))
        name_entry.grid(row=1,column=1,padx=8,sticky=W)

        email_label=Label(user_detail_frame,text="Email",font=("times new roman",20,"bold"))
        email_label.grid(row=2,column=0,padx=8,pady=15,sticky=W)
        email_entry=ttk.Entry(user_detail_frame,textvariable=self.var_email,width=50,font=("times new roman",20,"bold"))
        email_entry.grid(row=2,column=1,padx=8,pady=15,sticky=W)

        #radio button for photo taking
        self.var_radio1=StringVar(value="")
        radiobutton1=ttk.Radiobutton(user_detail_frame,variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radiobutton1.grid(row=3,column=0)

        btn_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=60,y=500,width=900,height=170)

        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take photo Sample",width=50,font=("times new roman",13,"bold"),bg="green",fg="black")
        take_photo_btn.grid(row=1,column=0,padx=120,pady=10)

        save_btn=Button(btn_frame,text="Sign Up",command=self.add_data,width=50,font=("times new roman",13,"bold"),bg="green",fg="black")
        save_btn.grid(row=0,column=0,padx=120,pady=10)


        #--------function---------
    def add_data(self):
        if self.var_gender.get()=="Select gender" or self.var_name.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_radio1.get()=="":
            messagebox.showerror("Error","Please select a take photo sample option",parent=self.root)
        else:
           
            # store the data into database 
            try:
                 conn=mysql.connector.connect(host="localhost",user="root",password="Janvi@1802",database="face_recognizer")
                 my_cursor=conn.cursor()
            #fields: name,email, gender, photoSample
                 my_cursor.execute("INSERT INTO USER (name, email, gender, photo_sample) VALUES(%s, %s, %s, %s)",(
                self.var_name.get(),
                self.var_email.get(),
                self.var_gender.get(),
                self.var_radio1.get()
            ))
                 conn.commit()
                 conn.close()
                 messagebox.showinfo("Success","Congratulations !!! sign up successfully...",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    def augment_image(image):

        #filp image horizontally
        if random.choice([True,False]):
            image=cv2.flip(image,1)

        #rotate image randomly(-15 to 15 degrees)
        angle=random.uniform(-15,15)
        h,w=image.shape[:2]
        M=cv2.getRotationMatrix2D((w//2,h//2),angle,1)
        image=cv2.warpAffine(image,M,(w,h))

        #adjust brightness
        factor=random.uniform(0.7,1.3)
        image=np.clip(image*factor,0,255).astype(np.uint8)

        #add gaussian noise 
        noise=np.random.normal(0,10,image.shape).astype(np.uint8)
        image=cv2.add(image,noise)

        return image

    #--------generate data set
    def generate_dataset(self):
        if self.var_gender.get()=="Select gender" or self.var_name.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_radio1.get()=="":
            messagebox.showerror("Error","Please select a take photo sample option",parent=self.root)
        else:
            try:
                # conn=mysql.connector.connect(host="localhost",user="root",password="Janvi@1802",database="face_recognizer")
                # my_cursor=conn.cursor()
                # my_cursor.execute("select* from user")
                # myresult=my_cursor.fetchall()
                # id=0
                # for x in myresult:
                #     id+=1
                # my_cursor.execute("update user set ")

                # face_classifier= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                # def face_cropped(img):
                #     #image will be converted to gray color
                #     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                #     #scaling factor->1.3
                #     #minimum neighbour->5 
                #     faces=face_classifier.detectMultiScale(gray,1.3,5)

                #     for(x,y,w,h)in faces:
                #         face_cropped=img[y:y+h,x:x+w]
                #         return face_cropped
                    
                # cap=cv2.VideoCapture(0)
                # img_id=0
                # while True:
                #     ret,my_frame=cap.read()
                #     if face_cropped(my_frame) is not None :
                #         img_id+=1
                #     face=cv2.resize(face_cropped(my_frame),(450,450))
                #     face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                #     file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"     
                #     cv2.imwrite(file_name_path)
                #     cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                #     cv2.imshow("Cropped face",face)

                #     if cv2.waitKey(1)==13 or int(img_id)==100:
                #         break
                # cap.release()
                # cv2.destroyAllWindows()
                # messagebox.showinfo("Result","Generated dataset....")       
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


                def augment_image(image):

                    #filp image horizontally
                    if random.choice([True,False]):
                        image=cv2.flip(image,1)

                    #rotate image randomly(-15 to 15 degrees)
                    angle=random.uniform(-15,15)
                    h,w=image.shape[:2]
                    M=cv2.getRotationMatrix2D((w//2,h//2),angle,1)
                    image=cv2.warpAffine(image,M,(w,h))

                    #reduce size
                    small=cv2.resize(image,(w//2,h//2))
                    resized=cv2.resize(small,(w,h),interpolation=cv2.INTER_LINEAR)

                    #blur 
                    blurred=cv2.GaussianBlur(resized,(5,5),0
                                             )
                    #adjust brightness
                    factor=random.uniform(0.7,1.3)
                    image=np.clip(image*factor,0,255).astype(np.uint8)

                    #add gaussian noise 
                    noise=np.random.normal(0,10,image.shape).astype(np.uint8)
                    image=cv2.add(image,noise)

                    return image
                

                def face_cropped(img):
    # Convert image to grayscale
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    # If no face is detected, return None
                    if len(faces) == 0:
                        return None

    # Crop the first face found
                    for (x, y, w, h) in faces:
                        face_crop = img[y:y+h, x:x+w]
                        augmented_face=augment_image(face_crop)
                        return augmented_face  # Return the first detected face

# Capture video
                cap = cv2.VideoCapture(0)
                img_id = 0
                user_id = self.var_email.get()  # Define a valid user ID

                while True:
                    ret, my_frame = cap.read()
    
                    if not ret:
                        print("Error: Failed to capture frame.")
                        break

                    face = face_cropped(my_frame)

                    if face is not None:
                        img_id += 1
                        face = cv2.resize(face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        
                        # Ensure data directory exists
                        if not os.path.exists("data"):
                            os.makedirs("data")
        
                        file_name_path = f"data/user.{user_id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)

                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

    # Stop capturing after 1000 images or when 'Enter' key (ASCII 13) is pressed
                    if cv2.waitKey(1) == 13 or img_id == 1000:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generated dataset successfully!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
           
        
if __name__ =="__main__":
    root=Tk()
    obj=signup(root)
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")  # Fullscreen window

    root.mainloop()