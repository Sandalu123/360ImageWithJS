import cv2
vidcap = cv2.VideoCapture('VID_20220305_205405.mp4')
success,image = vidcap.read()
count = 0
counW = 0
while success:
    if(count % 10 == 0):
        counW += 1
        filename = "images/"+str(counW)+".jpg"
        cv2.imwrite(filename, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('Read a new frame: ',count, success)
    else:
        success,image = vidcap.read()
        print('Read a new frame: ',count, success)
    count += 1