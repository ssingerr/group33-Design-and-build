import PySimpleGUI as sg  # Import the PySimpleGUI library for creating GUIs
from ultralytics import YOLO  # Import the YOLO object detection model from the Ultralytics library
import cv2  # Import the OpenCV library for image processing
import os  # Import the os library for interacting with the operating system
import glob  # Import the glob library for finding all the pathnames matching a specified pattern

# Load a model
model = YOLO("best.pt")  # Load a pretrained model (recommended for training)

# Define the GUI layout
layout = [
    [sg.Text("Please select the image folder to detect:"), sg.Input(key="-FOLDER-"), sg.FolderBrowse("Browse")],
    [sg.Text("Please enter the confidence threshold (0-1):"), sg.Input(key="-CONF-", default_text="0.5")],
    [sg.Button("Start Detection"), sg.Button("Next Image"), sg.Button("Exit")],
    [sg.Image(key="-IMAGE-", size=(480, 270))],
    [sg.Text(key="-INFO-", size=(60, 1))],
    [sg.Image(filename='resized_accuracy.png', key="-ACCURACY-", size=(480, 270))],
]

# Create the GUI window
window = sg.Window("YOLOv8 Object Detection", layout, size=(1280, 720))

# Initialize image_files to an empty list
image_files = []

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

        else:
            # Show an error message if the folder path is invalid
            sg.popup_error("Please select a valid folder!")
            continue

        # Predict on the first image file using YOLOv8
        results = model.predict(image_files[0], save=True, conf=conf, save_txt=True)

        # Get the output image and accuracy from the results
        output_image = results[0].plot()

        # Convert the output image to bytes and update the GUI image with it
        _, output_image_bytes = cv2.imencode(".png", output_image)
        window["-IMAGE-"].update(data=output_image_bytes.tobytes())

        # Remove the first image file from the list
        image_files.pop(0)

    elif event == "Next Image" and image_files:
        # Predict on the next image file using YOLOv8
        results = model.predict(image_files[0], conf=conf)

        # Get the output image from the results and update the GUI image with it
        output_image = results[0].plot()
        _, output_image_bytes = cv2.imencode(".png", output_image)
        window["-IMAGE-"].update(data=output_image_bytes.tobytes())

        # Remove the first image file from the list
        image_files.pop(0)

    elif not image_files:
        window["-INFO-"].update("All images have been recognized")

# Close the GUI window
window.close()
