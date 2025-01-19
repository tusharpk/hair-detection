import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk


import numpy as np
import numpy

from tensorflow.keras.models import load_model

# Load the models
hair_model = load_model("hairs_model.keras")
#gender_model = load_model('gender_model.keras')
age_model = load_model("Age_Sex_Detection.keras")

# Create the GUI
top=tk.Tk()
top.geometry('500x500')
top.title('Gender And Long hair detector')
top.configure(background='#CDCDCD')

#initalizing a label
label1=Label(top,background='#CDCDCD',font=('arial',15,'bold'))
label2=Label(top,background='#CDCDCD',font=('arial',15,'bold'))
label3=Label(top,background='#CDCDCD',font=('arial',15,'bold'))
sign_image=Label(top)




# Define the prediction function
def detect(file_path):
    global Label_packed
    image=Image.open(file_path)
    image=image.resize((48,48))
    image=numpy.expand_dims(image,axis=0)
    image=np.array(image)
    image=np.delete(image,0,1)
    image=np.resize(image,(48,48,3))
    print(image.shape)
    sex_f=['Male','Female']
    image=np.array([image])/255
    pred=age_model.predict(image)
    
    pred=hair_model.predict(image)#make a
    hair_f=['short Hair', 'long Hair']
    hair=int(np.round(pred[0][0]))
    

    
    age=int(np.round(pred[1][0]))
    sex=int(np.round(pred[0][0]))

    
    
    #print("predicted gender is " +sex_f[sex])
    #print("predicted hair is " + hair_f[hair])

    #label1.configure(foreground="#011638", text=sex_f[sex])
    if age>20 and age<30:
        #if sex==1:
        label1.configure(foreground='#011638',text=hair_f[hair])

    else:  
        label2.configure(foreground='#011638',text=sex_f[sex])
            

  

                
                
#show detect button
def detect_button(file_path):
    detect_b=Button(top,text="detect image",command=lambda: detect(file_path),padx=10,pady=5)
    detect_b.configure(background='#223344',foreground='white',font=('arial',10,'bold'))
    detect_b.place(relx=0.79,rely=0.46)
    

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
        label1.configure(text='')
        label2.configure(text='')
        label3.configure(text='')
        detect_button(file_path)

    except:
        pass
        

upload=Button(top,text="upload a iamge",command=upload_image,padx=10,pady=5)
upload.configure(background='#223344',foreground='white',font=('arial',15,'bold'))
upload.pack(side='bottom',pady=39)
sign_image.pack(side='bottom',expand=True)
label1.pack(side='bottom',expand=True)
label2.pack(side='bottom',expand=True)
label3.pack(side='bottom',expand=True)
heading=Label(top,text='gender and hair detector',pady=20,font=('arial',15,'bold'))
heading.configure(background='#CDCDCD',foreground='#365654')
heading.pack()


top.mainloop() 

