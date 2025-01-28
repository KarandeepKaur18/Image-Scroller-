# from tkinter import *
# from PIL import ImageTk,Image

# root = Tk()
# root.title("Rich World Scroll")

# img1= ImageTk.PhotoImage(Image.open("C:/Users/Acer-Pc/OneDrive/Documents/PYTHON/PYTHON/TKINTER/Tkinter_B_Image_viewer/Images/coding1.jpg"))
# img2 = ImageTk.PhotoImage(Image.open("C:/Users/Acer-Pc/OneDrive/Documents/PYTHON/PYTHON/TKINTER/Tkinter_B_Image_viewer/Images/coding1.jpg"))
# img3 = ImageTk.PhotoImage(Image.open("C:/Users/Acer-Pc/OneDrive/Documents/PYTHON/PYTHON/TKINTER/Tkinter_B_Image_viewer/Images/coding1.jpg"))
# img4 = ImageTk.PhotoImage(Image.open("C:/Users/Acer-Pc/OneDrive/Documents/PYTHON/PYTHON/TKINTER/Tkinter_B_Image_viewer/Images/coding1.jpg"))
# img5 = ImageTk.PhotoImage(Image.open("C:/Users/Acer-Pc/OneDrive/Documents/PYTHON/PYTHON/TKINTER/Tkinter_B_Image_viewer/Images/coding1.jpg"))



# mylabel = Label(image=img1)
# mylabel.grid(row=1,column=15,columnspan=3)

# # index= 
# list1=[img2,img3,img4,img5]
# list2=[img1,img2,img3,img4,img5]

# def Next_image():
    
#     global mylabel , list1
#     i=list1.pop(0)
#     mylabel.config(image=i)
      

# def Previous_Image():
#     global mylabel, i ,list1,list2
#     # i=list1.pop(0)
#     list1.insert(0,i)
   
#     for j in range(0,len(list2)):

#         if(list2[j]==i):
#             mylabel.config(image=list2[j-1])
#             break
    
#         else:
#             continue
    
        
        

# Button_Back = Button(root,text="Previous",command=Previous_Image)
# Button_Back.grid(row=3,column=1)

# Button_Exit = Button(root,text="Exit",command=root.quit)
# Button_Exit.grid(row=3,column=2)

# Button_Next = Button(root,text="Next Image ",command=Next_image)
# Button_Next.grid(row=3,column=3)



# root.mainloop()





from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Rich World Scroll")

# Resize images
def load_image(path, size=(500, 500)):  # Resize to 500x500
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.LANCZOS))

# Load and resize images
img1 = load_image("C:/Users/Acer-Pc/OneDrive/Documents/PYTHON/PYTHON/TKINTER/Tkinter_B_Image_viewer/Images/scroll1.jpg")
img2 = load_image("C:/Users/Acer-Pc/OneDrive/Documents/PYTHON/PYTHON/TKINTER/Tkinter_B_Image_viewer/Images/scroll2.jpg")
img3 = load_image("C:/Users/Acer-Pc/OneDrive/Documents/PYTHON/PYTHON/TKINTER/Tkinter_B_Image_viewer/Images/scroll3.jpg")
img4 = load_image("C:/Users/Acer-Pc/OneDrive/Documents/PYTHON/PYTHON/TKINTER/Tkinter_B_Image_viewer/Images/scroll4.jpg")
img5 = load_image("C:/Users/Acer-Pc/OneDrive/Documents/PYTHON/PYTHON/TKINTER/Tkinter_B_Image_viewer/Images/scroll5.jpg")
img5 = load_image("C:/Users/Acer-Pc/OneDrive/Documents/PYTHON/PYTHON/TKINTER/Tkinter_B_Image_viewer/Images/scroll6.jpg")
img5 = load_image("C:/Users/Acer-Pc/OneDrive/Documents/PYTHON/PYTHON/TKINTER/Tkinter_B_Image_viewer/Images/scroll7.jpg")
img5 = load_image("C:/Users/Acer-Pc/OneDrive/Documents/PYTHON/PYTHON/TKINTER/Tkinter_B_Image_viewer/Images/scroll9.jpg")

# Image lists
list1 = [img2, img3, img4, img5]
list2 = [img1, img2, img3, img4, img5]

# Display the first image
mylabel = Label(image=img1)
mylabel.grid(row=1, column=1, columnspan=3, pady=20)

# Current index tracker
current_index = 0

# Next Image functionality
def Next_image():
    global mylabel, current_index, list2
    current_index += 1
    if current_index >= len(list2):
        current_index = 0  # Loop back to the first image
    mylabel.config(image=list2[current_index])

# Previous Image functionality
def Previous_Image():
    global mylabel, current_index, list2
    current_index -= 1
    if current_index < 0:
        current_index = len(list2) - 1  # Loop back to the last image
    mylabel.config(image=list2[current_index])

# Buttons
Button_Back = Button(root, text="Previous", command=Previous_Image)
Button_Back.grid(row=3, column=1, padx=10, pady=10, sticky="e")

Button_Exit = Button(root, text="Exit", command=root.quit)
Button_Exit.grid(row=3, column=2, padx=10, pady=10)

Button_Next = Button(root, text="Next Image", command=Next_image)
Button_Next.grid(row=3, column=3, padx=10, pady=10, sticky="w")

# Center alignment for the layout
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()
