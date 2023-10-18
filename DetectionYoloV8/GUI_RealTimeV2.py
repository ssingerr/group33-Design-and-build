import PySimpleGUI as sg
from ultralytics import YOLO
import cv2
import os
import glob
import threading

model = YOLO("best.pt")

layout = [
    [sg.Text("Please select the image folder to detect:"), sg.Input(key="-FOLDER-"), sg.FolderBrowse("Browse")],
    [sg.Text("Please enter the confidence threshold (0-1):"), sg.Input(key="-CONF-", default_text="0.5")],
    [sg.Button("Start Detection"), sg.Button("Stop Detection"), sg.Button("Exit")],
    [sg.Image(key="-IMAGE-ORIG-", size=(400, 300)), sg.Image(key="-IMAGE-DETECT-", size=(400, 300))],
    [sg.Image(filename='resized_accuracy.png', key="-ACCURACY-", size=(400, 300))],
    [sg.Text(key="-INFO-", size=(60, 1))],
]

window = sg.Window("YOLOv8 Object Detection", layout, size=(1280, 720))

image_files = []


def resize_image(image_path, size):
    img = cv2.imread(image_path)
    img_resized = cv2.resize(img, size)
    return cv2.imencode('.png', img_resized)[1].tobytes()


def detect_images():
    global image_files

    while True:
        all_image_files = sorted(glob.glob(os.path.join(folder_path, "*")))
        all_image_files = [f for f in all_image_files if os.path.splitext(f)[1] in [".jpg", ".png", ".bmp"]]
        new_image_files = list(set(all_image_files) - set(image_files))

        if len(new_image_files) > 10:
            new_image_files = new_image_files[-10:]

        image_files.extend(new_image_files)

        if not new_image_files:
            continue

        results = model.predict(new_image_files[0], save=True, conf=conf, save_txt=True)

        output_image = results[0].plot()
        _, output_image_bytes = cv2.imencode(".png", output_image)
        window["-IMAGE-DETECT-"].update(data=output_image_bytes.tobytes())

        orig_image_bytes = resize_image(new_image_files[0], (400, 300))
        window["-IMAGE-ORIG-"].update(data=orig_image_bytes)


while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Start Detection":
        folder_path = values["-FOLDER-"]
        conf = float(values["-CONF-"])

        if folder_path:
            threading.Thread(target=detect_images).start()
        else:
            sg.popup_error("Please select a valid folder!")
            continue

    elif event == "Stop Detection":
        image_files.clear()

window.close()
