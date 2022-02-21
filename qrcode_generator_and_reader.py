from PIL import Image, ImageTk
from resizeimage import resizeimage
import qrcode
import cv2
import tkinter

data= input("Enter the data to generate a QR Code for the same:")
qr_code = qrcode.make(data)
qr_code=resizeimage.resize_cover(qr_code,[190,190])
#qr_code.show()  // This will show qrcode in gallary temporarily without saving

#loc=data+".jpg"
#img.save(loc)  // This will save qrcode image in the current working folder

qr_window = tkinter.Tk()
qr_window.geometry("200x200")
qr_window.title('QR Code')
qr_window.configure(background='#FBFF7F')

place_holder=tkinter.Label(qr_window, text=" ", fg="white", bg='#FBFF7F', font=("Playfair Display", 20, 'bold'))
place_holder.place(x='5',y='5',width=190, height=190)

qr_codedis=ImageTk.PhotoImage(qr_code)
place_holder.config(image=qr_codedis)

qr_window.mainloop()

cont= input("Enter (y/n) to continue to QR Code Reader:")
if cont=="y":
    loc=input("Enter Absolute file location:")
    detector=cv2.QRCodeDetector()
    val, pts, st_code=detector.detectAndDecode(cv2.imread(loc))
    print(val)
