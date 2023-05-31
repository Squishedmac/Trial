import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from roboflow import Roboflow

rf = Roboflow(api_key="0VK6gyxfXpoP0MWuxqCD")
project = rf.workspace().project("age-gander")
model = project.version(2).model

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()  
        self.title("Gender and Age Prediction")
        self.geometry(f"{1300}x{900}")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 2), weight=1)
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Clear",command=self.sidebar_button_event2)
        self.sidebar_button_1.grid(row=1, column=0, padx=0, pady=0)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Select Image", command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=0, column=0, padx=0, pady=100)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Select Images using the button above, the images have to be jpg \n the image will be predicted using an api to a model \nthats hosted remotely so an active internet connection is required", anchor="w")
        self.appearance_mode_label.grid(row=1, column=0, padx=20, pady=(500,0))
        
    
    def sidebar_button_event(self):
        global img
        f_types = [('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        model.predict(filename, confidence=40, overlap=30).save("prediction.jpg")
        dark_image=Image.open("prediction.jpg")
        self.my_image = customtkinter.CTkImage(dark_image,size=(dark_image.size[0],dark_image.size[1]))
        self.image_label = customtkinter.CTkLabel(app,text="", image=self.my_image)  
        self.image_label.grid(row=0, column=1, padx=20, pady=10)

    def sidebar_button_event2(self):
        #self.grid_columnconfigure(1, weight=1)
        #self.grid_rowconfigure((0, 2), weight=1)
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0,fg_color="transparent")
        self.sidebar_frame.grid(row=0, column=1, rowspan=10, sticky="nsew")
        return 


if __name__ == "__main__":
    app = App()
    app.mainloop()
     # Keep the window open