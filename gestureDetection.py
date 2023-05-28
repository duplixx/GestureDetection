# import os
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/home/duplixx/.local/lib/python3.8/site-packages/cv2/qt/plugins'
import cv2
import mediapipe as mp
import imutils
# from PIL import Image

# Initializing mediapipe hands
mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
# img=Image.open(r"./hand_image.jpeg") 
# Processing the input image
def process_image(img,hands):
    # Converting the input to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(gray_image)

    # Returning the detected hands to the calling function
    return results

# Drawing landmark connections
def draw_hand_connections(img, results):
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape

                # Finding the coordinates of each landmark
                cx, cy = int(lm.x * w), int(lm.y * h)

                # Printing each landmark ID and coordinates
                # on the terminal
                print(id, cx, cy)

                # Creating a circle around each landmark
                cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

            # Drawing the landmark connections
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    return img

def main():
    # Initialize mediapipe hands

    hands = mpHands.Hands()
    # Replace 0 with the video path to use a pre-recorded video
    cap = cv2.VideoCapture('./handVideo.mp4')
    while True:
        # Taking the input
        success, image = cap.read()
        image = imutils.resize(image, width=500, height=500)
        results = process_image(image, hands)
        image = draw_hand_connections(image, results)

        # Displaying the output
        cv2.imshow("Hand tracker", image)

        # Program terminates when the 'q' key is pressed
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
