import cv2

# img = cv2.imread("qr.png") # read image

cam = cv2.VideoCapture(0) # open camera

detector = cv2.QRCodeDetector() # create detector object

while True:
    ret, frame = cam.read() # ret--- return true or false ,frame was read or not

    if not ret:
        print("Failed to capture image")
        break

    data, bbox, _ = detector.detectAndDecode(frame) # detect qr code

    if data:
        print("QR Code Data:", data)

    cv2.imshow("QR Code Scanner", frame) # show image
    if cv2.waitKey(1) & 0xFF == ord(''):
        break

cam.release()
cv2.destroyAllWindows() # release camera and close window