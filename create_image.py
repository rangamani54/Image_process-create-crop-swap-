import cv2
import numpy as np

#Image with all values zero
photo = np.zeros((750,1380,3))

#for border
photo[0:20, 0:1360]=[0,255,255]
photo[20:750, 0:20]=[255,80,0]
photo[730:750, 20:1380]=[0,255,255]
photo[0:750, 1360:1380]=[255,80,0]

#for white
#photo[20:730, 20:1360]=[180,68,63]

#for M
photo[100:600, 40:60]=[255,0,0]
photo[100:120, 60:140]=[0,180,0]
photo[100:290, 140:160]=[0,255,0]
photo[290:310, 140:200]=[0,255,0]
photo[100:310, 200:220]=[0,255,0]
photo[100:120, 220:300]=[0,255,0]
photo[100:600, 300:320]=[255,0,0]

#for O
photo[120:580, 360:380]=[0,255,255]
photo[100:120, 380:620]=[255,0,0]
photo[120:580, 620:640]=[0,255,255]
photo[580:600, 380:620]=[255,0,0]

#for D
photo[100:600, 680:700]=[0,255,0]
photo[100:120, 700:920]=[0,255,255]
photo[140:560, 940:960]=[0,255,0]
photo[580:600, 700:920]=[0,255,255]

#for S
photo[100:120, 1020:1240]=[255,0,0]
photo[120:350,1000:1020]=[0,255,255]
photo[350:370, 1020:1240]=[255,0,0]
photo[370:580, 1240:1260]=[0,255,255]
photo[580:600, 1000:1240]=[255,0,0]

def show_image(name, image_name):
    cv2.imshow(name, image_name)
    cv2.waitKey()
    cv2.destroyAllWindows()

show_image("testing", photo)



