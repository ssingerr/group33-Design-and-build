import os
import time
import threading
from PIL import ImageGrab
import PySimpleGUI as sg
import tkinter as tk

def capture_screen(capture_folder, capture_rate, region, start_time):
    os.makedirs(capture_folder, exist_ok=True)  # Create the folder if it doesn't exist

    while True:
        screen = ImageGrab.grab(bbox=region)  # Capture the screen within the specified region

        elapsed_time = time.time() - start_time  # Calculate the elapsed time
        screen.save(os.path.join(capture_folder, f"{elapsed_time}.jpg"))  # Save the screenshot

        time.sleep(1 / capture_rate)  # Wait for some time before capturing again

def end_capture():
    global window
    window.close()

def main():
    global window

    layout = [[sg.Text("Please select a region on the screen")],  # Prompt the user to select a region on the screen
              [sg.Button("Select Region")],  # Button: Select Region
              [sg.Button("Start Capture")],  # Button: Start Capture
              [sg.Button("End Capture")]]  # Button: End Capture

    window = sg.Window("Screen Capture", layout)  # Create a window

    region = None

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancel"):
            break
        elif event == "Select Region":
            region = sg.popup_get_text("Please enter the region (format: x1,y1,x2,y2)")  # Prompt the user to enter the region coordinates
            region = tuple(map(int, region.split(',')))  # Convert the string to a tuple of integers
        elif event == "Start Capture" and region is not None:
            start_time = time.time()  # Record the start time
            threading.Thread(target=capture_screen, args=("screenshot", 60, region, start_time), daemon=True).start()  # Start capturing
        elif event == "End Capture":
            end_capture()

    window.close()

if __name__ == "__main__":
    main()
