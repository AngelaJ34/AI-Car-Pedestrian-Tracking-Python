import cv2

# Please uncomment each file below Car Image
#img_file = 'Car_Photo.jpg'
video = cv2.VideoCapture('Tesla Dashcam Accident.mp4')
#video = cv2.VideoCapture('Dashcam_Pedestrians.mp4')


# Our pre-trained car and pedestrian classifiers
car_tracker_file = 'cars.xml'
pedestrian_tracker_file = 'haarcascade_fullbody.xml'

# create car classifier. classifier identifies the object: person, car, etc.
car_tracker = cv2.CascadeClassifier(car_tracker_file)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)

# while loop for video will iterate infinitely
while True:

# Read the one frame in the video. video.read() returns a tuple
    (read_succesful, frame) = video.read()
    
    if read_succesful:
        # Must convert to grayscale as a valid frame, otherwise will break loop
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    
    # detect cars AND Pedestrians in the image of any scale. Data for x and y
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)
    
    # Draw rectangles around the cars pulled from x and y cordinates, height width to display color red
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

     # Draw rectangles around people pulled from x and y cord, height width to display color yellow
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    # Display the color image with the cars and faces spotted
    # When it converts to grayscale it will compute it faster
    cv2.imshow('Car_Detector', frame)

    # Dont autoclose (Wait here in the code and listen for a key to press)
    cv2.waitKey(1)

    # print statement below is used to confirm no errors (uncheck if necessary)
    #print("Code Complete")