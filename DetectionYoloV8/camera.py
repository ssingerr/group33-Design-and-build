import cv2
import time
import threading
import os
import PySimpleGUI as sg

class CameraCapture:
    def __init__(self, camera_index=0, save_path='./', fps=60):
        self.camera_index = camera_index
        self.save_path = save_path
        self.fps = fps
        self.is_capturing = False

    def start_capture(self):
        # 创建新的文件夹
        try:
            if not os.path.exists(self.save_path):
                os.makedirs(self.save_path)
        except Exception as e:
            print(f'Error creating directory: {e}')
            return

        self.is_capturing = True
        self.capture_thread = threading.Thread(target=self.capture)
        self.capture_thread.start()

    def stop_capture(self):
        self.is_capturing = False
        if self.capture_thread.is_alive():
            self.capture_thread.join()

    def capture(self):
        try:
            cap = cv2.VideoCapture(self.camera_index)
            if not cap.isOpened():
                print('Error opening video capture')
                return

            frame_duration = 1.0 / self.fps
            start_time = time.time()

            while self.is_capturing:
                ret, frame = cap.read()
                if ret:
                    elapsed_time = time.time() - start_time
                    image_name = f'{elapsed_time:.2f}.jpg'
                    try:
                        cv2.imwrite(os.path.join(self.save_path, image_name), frame)
                    except Exception as e:
                        print(f'Error saving image: {e}')
                time.sleep(frame_duration)

            cap.release()
        except Exception as e:
            print(f'Error capturing images: {e}')

camera_capture = CameraCapture(save_path='./new_folder/')

layout = [[sg.Button('开始', key='start'), sg.Button('结束', key='stop')]]

window = sg.Window('Camera Capture', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'start':
        camera_capture.start_capture()
    elif event == 'stop':
        camera_capture.stop_capture()

window.close()
