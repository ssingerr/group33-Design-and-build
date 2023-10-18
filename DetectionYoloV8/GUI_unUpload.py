import PySimpleGUI as sg  # Import the PySimpleGUI library for creating GUIs
from ultralytics import YOLO  # Import the YOLO object detection model from the Ultralytics library
import cv2  # Import the OpenCV library for image processing
import os  # Import the os library for interacting with the operating system
import glob  # Import the glob library for finding all the pathnames matching a specified pattern
import threading  # Import the threading library for creating threads

# Load a model
model = YOLO("best.pt")  # Load a pretrained model (recommended for training)

# Define the GUI layout
layout = [
    [sg.Text("Please select the image folder to detect:"), sg.Input(key="-FOLDER-"), sg.FolderBrowse("Browse")],
    [sg.Text("Please enter the confidence threshold (0-1):"), sg.Input(key="-CONF-", default_text="0.5")],
    [sg.Button("Start Detection"), sg.Button("Stop Detection"), sg.Button("Exit")],
    [sg.Image(key="-IMAGE-ORIG-", size=(400, 300)), sg.Image(key="-IMAGE-DETECT-", size=(400, 300))],
    [sg.Image(filename='resized_accuracy.png', key="-ACCURACY-", size=(400, 300))],
    [sg.Text(key="-INFO-", size=(60, 1))],
]

# Create the GUI window
window = sg.Window("YOLOv8 Object Detection", layout, size=(1280, 720))

# Initialize image_files to an empty list
image_files = []

# Function to resize image
def resize_image(image_path, size):
    img = cv2.imread(image_path)  # Read the image file
    img_resized = cv2.resize(img, size)  # Resize the image to the specified size
    return cv2.imencode('.png', img_resized)[1].tobytes()  # Convert the resized image to bytes and return it

# Function to detect images in a separate thread
def detect_images():
    global image_files  # Access the global variable image_files
    while image_files:  # Loop while there are still image files in the list
        # Predict on the next image file using YOLOv8 and save the results
        results = model.predict(image_files[0], save=True, conf=conf, save_txt=True)

        # Get the output image from the results and update the GUI image with it
        output_image = results[0].plot()
        _, output_image_bytes = cv2.imencode(".png", output_image)
        window["-IMAGE-DETECT-"].update(data=output_image_bytes.tobytes())

        # Update original image in GUI
        orig_image_bytes = resize_image(image_files[0], (400, 300))
        window["-IMAGE-ORIG-"].update(data=orig_image_bytes)

        # Remove the first image file from the list
        image_files.pop(0)

# Loop through the GUI events
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Start Detection":
        # Get the folder path and confidence threshold from the user input
        folder_path = values["-FOLDER-"]
        conf = float(values["-CONF-"])

        # Check if the folder path is valid
        if folder_path:
            # Get the list of image files in the folder
            image_files = glob.glob(os.path.join(folder_path, "*"))
            image_files = [f for f in image_files if os.path.splitext(f)[1] in [".jpg", ".png", ".bmp"]]

            # Check if there are any image files in the folder
            if not image_files:
                # Show an error message if there are no image files in the folder
                sg.popup_error("No image files in the folder!")
                continue

            # Start a new thread to detect images
            threading.Thread(target=detect_images).start()

        else:
            # Show an error message if the folder path is invalid
            sg.popup_error("Please select a valid folder!")
            continue

    elif event == "Stop Detection":
        # Clear the list of image files to stop detection
        image_files.clear()

# Close the GUI window when done
window.close()
