import PySimpleGUI as sg
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image
import time

class FileHandler(FileSystemEventHandler):
    def __init__(self, txt_folder, jpg_folder, save_folder):
        self.txt_folder = txt_folder
        self.jpg_folder = jpg_folder
        self.save_folder = save_folder

    def on_created(self, event):
        if event.is_directory:
            return None

        elif event.src_path.endswith(".txt"):
            filename = os.path.basename(event.src_path)
            jpg_file = os.path.join(self.jpg_folder, filename.replace('.txt', '.jpg'))
            for _ in range(100):
                try:
                    Image.open(jpg_file)
                    break
                except Exception:
                    time.sleep(0.1)
            else:
                return
            if os.path.isfile(jpg_file):
                shutil.copy2(jpg_file, self.save_folder)

def main():
    layout = [[sg.Text("TXT文件夹"), sg.Input(), sg.FolderBrowse()],
              [sg.Text("JPG文件夹"), sg.Input(), sg.FolderBrowse()],
              [sg.Text("保存文件夹"), sg.Input(), sg.FolderBrowse()],
              [sg.Button("开始监控"), sg.Button("退出")]]

    window = sg.Window("文件监控", layout)

    while True:
        event, values = window.read()
        if event == "开始监控":
            observer = Observer()
            event_handler = FileHandler(values[0], values[1], values[2])
            observer.schedule(event_handler, path=values[0], recursive=False)
            observer.start()
        elif event == "退出" or event == sg.WIN_CLOSED:
            break

    window.close()

if __name__ == "__main__":
    main()
