import cv2
import numpy as np
from tkinter import *
from tkinter import messagebox as mb
from tkinter.filedialog import *
from PIL import Image
import time
import os

#-----Create a values-----
scale_brightness = None
scale_improve = None
scale_repetitions = None
path_to_file = None
#-------------------------







#-----Work functions------
#+++++Choose file function
def choose(event):
    global path_to_file
    path_to_file = askopenfilename()
    path_to_file_array = path_to_file.split(".")
    path_to_file_array.reverse()
    if str(path_to_file_array[0]) == "png" or str(path_to_file_array[0]) == "jpg":
        img = cv2.imread(path_to_file)
        height, width, _ = img.shape
        label_path_file["text"] = str(path_to_file)
        label_file_height["text"] = "height: "
        label_file_width["text"] = "width: "
        label_file_height["text"] = label_file_height["text"] + str(height) + "px"
        label_file_width["text"] = label_file_width["text"] + str(width) + "px"
        img = cv2.imread(path_to_file)
        cv2.imshow("image", img)
    else:
        path_to_file == None
        mb.showerror("Error type", "File can't be ."+path_to_file_array[0]) 
    root.mainloop()
#+++++++++++++++++++++++++







#++++Gaus improve img func    
def gaus(event):
    global path_to_file
    out_range = 0


    if check_gaus.get() == 1 and path_to_file != None:
        img = cv2.imread(path_to_file)
        grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gaus = cv2.adaptiveThreshold(grayscaled, scale_gaus.get(), cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
        cv2.imshow("gaus", gaus)

        
    elif check_gaus_improve.get() == 1 and path_to_file != None:
        img = cv2.imread(path_to_file)
        grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, scale_gaus_improve.get())
        path = 'improve.jpg'
        cv2.imwrite(os.path.join(path), gaus)
        time.sleep(2)
        for i in range(scale_gaus_improve_rep.get()):
            image_improve = Image.open(path)
            pixdata = image_improve.load()
            for y in range(2,image_improve.size[1]-2):
                for x in range(2,image_improve.size[0]-2):
                    
                    #1
                    if  ((((((((((0 <= pixdata[x, y] <= 5)
                    and (250 <= pixdata[x-1, y] <= 255))
                    and (250 <= pixdata[x+1, y] <= 255))
                    and (250 <= pixdata[x, y-1] <= 255))
                    and (250 <= pixdata[x, y+1] <= 255))
                    and (250 <= pixdata[x-1, y+1] <= 255))
                    and (250 <= pixdata[x+1, y+1] <= 255))
                    and (250 <= pixdata[x-1, y-1] <= 255))
                    and (250 <= pixdata[x+1, y-1] <= 255))):
                        pixdata[x, y] = 255

                    #2
                    elif  ((((((((((0 <= pixdata[x, y] <= 5)
                    and (0 <= pixdata[x-1, y] <= 5))
                    and (250 <= pixdata[x+1, y] <= 255))
                    and (250 <= pixdata[x, y-1] <= 255))
                    and (250 <= pixdata[x, y+1] <= 255))
                    and (250 <= pixdata[x-1, y+1] <= 255))
                    and (250 <= pixdata[x+1, y+1] <= 255))
                    and (250 <= pixdata[x-1, y-1] <= 255))
                    and (250 <= pixdata[x+1, y-1] <= 255))):
                        pixdata[x, y] = 255
                        pixdata[x-1, y] = 255

                    #3
                    elif  ((((((((((0 <= pixdata[x, y] <= 5)
                    and (250 <= pixdata[x-1, y] <= 255))
                    and (250 <= pixdata[x+1, y] <= 255))
                    and (250 <= pixdata[x, y-1] <= 255))
                    and (0 <= pixdata[x, y+1] <= 5))
                    and (250 <= pixdata[x-1, y+1] <= 255))
                    and (250 <= pixdata[x+1, y+1] <= 255))
                    and (250 <= pixdata[x-1, y-1] <= 255))
                    and (250 <= pixdata[x+1, y-1] <= 255))):
                        pixdata[x, y] = 255
                        pixdata[x, y+1] = 255

                    #4
                    elif  ((((((((((0 <= pixdata[x, y] <= 5)
                    and (250 <= pixdata[x-1, y] <= 255))
                    and (0 <= pixdata[x+1, y] <= 5))
                    and (250 <= pixdata[x, y-1] <= 255))
                    and (250 <= pixdata[x, y+1] <= 255))
                    and (250 <= pixdata[x-1, y+1] <= 255))
                    and (250 <= pixdata[x+1, y+1] <= 255))
                    and (250 <= pixdata[x-1, y-1] <= 255))
                    and (250 <= pixdata[x+1, y-1] <= 255))):
                        pixdata[x, y] = 255
                        pixdata[x+1, y] = 255

                    #5    
                    elif  ((((((((((0 <= pixdata[x, y] <= 5)
                    and (250 <= pixdata[x-1, y] <= 255))
                    and (250 <= pixdata[x+1, y] <= 255))
                    and (0 <= pixdata[x, y-1] <= 5))
                    and (250 <= pixdata[x, y+1] <= 255))
                    and (250 <= pixdata[x-1, y+1] <= 255))
                    and (250 <= pixdata[x+1, y+1] <= 255))
                    and (250 <= pixdata[x-1, y-1] <= 255))
                    and (250 <= pixdata[x+1, y-1] <= 255))):
                        pixdata[x, y] = 255
                        pixdata[x, y-1] = 255
                        
                    else: pass
            image_improve.save(path)
                    
        for y in range(image_improve.size[1]):
            for x in range(image_improve.size[0]):
                if 250 <= pixdata[x,y] <= 254:
                    pixdata[x,y] = 255
                if 0 <= pixdata[x,y] <= 5:
                    pixdata[x,y] = 0
        image_improve.save(path)
        img = cv2.imread(path)
        cv2.imshow("gaus improve", img)

        
    else:
        mb.showerror("Check error", "You must to check a checkbox|Gaus|\n or choose file") 
#+++++++++++++++++++++++++









        
#++++Filter color on img++
def filter_(event):
    label_hsv_1["text"] = "FROM: ("+str(scale_h_1.get())+", "+str(scale_s_1.get())+", "+str(scale_v_1.get())+")"
    label_hsv_2["text"] = "TO: ("+str(scale_h_2.get())+", "+str(scale_s_2.get())+", "+str(scale_v_2.get())+")"

    if check_filter.get() == 1 and path_to_file != None:
        color_range_line = cv2.imread("color_range_line.jpg")
        color_range_circle = cv2.imread("color_range_circle.jpg")
        img = cv2.imread(path_to_file)

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hsv_2 = cv2.cvtColor(color_range_line, cv2.COLOR_BGR2HSV)
        hsv_3 = cv2.cvtColor(color_range_circle, cv2.COLOR_BGR2HSV)
        
        lower_color = np.array([scale_h_1.get(),scale_s_1.get(),scale_v_1.get()])
        upper_color = np.array([scale_h_2.get(),scale_s_2.get(),scale_v_2.get()])
    
        mask = cv2.inRange(hsv, lower_color, upper_color)
        result = cv2.bitwise_or(img,img, mask= mask)
        mask_2 = cv2.inRange(hsv_2, lower_color, upper_color)
        result_2 = cv2.bitwise_or(color_range_line,color_range_line, mask= mask_2)
        mask_3 = cv2.inRange(hsv_3, lower_color, upper_color)
        result_3 = cv2.bitwise_or(color_range_circle,color_range_circle, mask= mask_3)
        
        cv2.imshow("filter", result)
        cv2.imshow("color_range_line", result_2)
        cv2.imshow("color_range_circle", result_3)
#+++++++++++++++++++++++++




#++++Cancle scale func++++
def cancle(event):
    scale_h_1.set(0)
    scale_s_1.set(0)
    scale_v_1.set(0)
    scale_h_2.set(255)
    scale_s_2.set(255)
    scale_v_2.set(255)
#+++++++++++++++++++++++++

#-------------------------





if __name__ == "__main__":
    root = Tk()
    check_gaus = IntVar()
    check_gaus_improve = IntVar()
    check_filter = IntVar()
    check_hromakey = IntVar()
    root.title("Improve")
    root.geometry("500x520")
    root.configure(background="silver")

    button_choose_file = Button(root, font=("Verdana", 10), text="Choose file", bg="white", fg="black", activebackground="black", activeforeground="white", height = 1, width = 10)
    button_choose_file.place(x = 10, y = 10)
    button_choose_file.bind("<Button-1>", choose)

    #----------GAUS----------
    checkbutton_gaus = Checkbutton(root, text = "Gaus", variable = check_gaus, onvalue = 1, offvalue = 0, height=0, width = 11)
    checkbutton_gaus.place(x = 10, y = 150)
    checkbutton_gaus_improve = Checkbutton(root, text = "Gaus with improve", variable = check_gaus_improve, onvalue = 1, offvalue = 0, height=0, width = 15)
    checkbutton_gaus_improve.place(x = 120, y = 150)
    
    scale_gaus = Scale(root, variable=scale_brightness, orient="horizontal", to=255, label="brightness")
    scale_gaus.place(x = 10, y = 180)
    scale_gaus_improve = Scale(root, variable=scale_improve, orient="horizontal", to=5, length=127, label="quality")
    scale_gaus_improve.place(x = 120, y = 180)
    scale_gaus_improve_rep = Scale(root, variable=scale_repetitions, orient="vertical", from_=1, to=6, width=25, length=83, label="repeat improvements")
    scale_gaus_improve_rep.place(x = 255, y = 150)

    button_gaus = Button(root, font=("Verdana", 10), text="Apply", bg="white", fg="black", activebackground="black", activeforeground="white", height = 1, width = 10)
    button_gaus.place(x = 10, y = 245)
    button_gaus.bind("<Button-1>", gaus)
    #------------------------

    #----------FILTER----------
    checkbutton_filter = Checkbutton(root, text = "Filter", variable = check_filter, onvalue = 1, offvalue = 0, height=0, width = 22)
    checkbutton_filter.place(x = 10, y = 300)
    
    scale_h_1 = Scale(root, variable=scale_brightness, orient="vertical", to=255, length=130, label="H1", command=filter_)
    scale_h_1.place(x = 10, y = 330)
    scale_s_1 = Scale(root, variable=scale_brightness, orient="vertical", to=255, length=130, label="S1", command=filter_)
    scale_s_1.place(x = 87, y = 330)
    scale_v_1 = Scale(root, variable=scale_brightness, orient="vertical", to=255, length=130, label="V1", command=filter_)
    scale_v_1.place(x = 164, y = 330)

    scale_h_2 = Scale(root, variable=scale_brightness, orient="vertical", to=255, length=130, label="H2", command=filter_)
    scale_h_2.place(x = 240, y = 330)
    scale_s_2 = Scale(root, variable=scale_brightness, orient="vertical", to=255, length=130,  label="S2", command=filter_)
    scale_s_2.place(x = 317, y = 330)
    scale_v_2 = Scale(root, variable=scale_brightness, orient="vertical", to=255, length=130,  label="V2", command=filter_)
    scale_v_2.place(x = 394, y = 330)

    scale_h_1.set(0)
    scale_s_1.set(0)
    scale_v_1.set(0)
    scale_h_2.set(255)
    scale_s_2.set(255)
    scale_v_2.set(255)
    
    label_hsv_1 = Label(root, font=("Verdana", 10), bg="silver", text="FROM: ("+str(scale_h_1.get())+", "+str(scale_s_1.get())+", "+str(scale_v_1.get())+")", height=1, width = 18)
    label_hsv_2 = Label(root, font=("Verdana", 10), bg="silver", text="TO: ("+str(scale_h_2.get())+", "+str(scale_s_2.get())+", "+str(scale_v_2.get())+")", height=1, width = 18)
    label_hsv_1.place(x = 200, y = 300)
    label_hsv_2.place(x = 350, y = 300)

    button_back = Button(root, font=("Verdana", 10), text="Cancel", bg="white", fg="black", activebackground="black", activeforeground="white", height = 1, width = 10)
    button_back.place(x = 10, y = 470)
    button_back.bind("<Button-1>", cancle)
    #------------------------

    label_path_file = Label(root, font=("Verdana", 10), bg="silver", text="", height=1, width = 30)
    label_path_file.place(x = 10, y = 40)

    label_file_height = Label(root, font=("Verdana", 10), text="height: ", height=1, width = 15)
    label_file_width = Label(root, font=("Verdana", 10), text="width: ", height=1, width = 15)
    label_file_height.place(x = 350, y = 10)
    label_file_width.place(x = 350, y = 40)
    
    label_tools = Label(root, font=("Verdana", 15), text="Tools:", bg="white", fg="black", height = 1 , width =38)
    label_tools.place(x = 0, y = 100)
    
    root.mainloop()
