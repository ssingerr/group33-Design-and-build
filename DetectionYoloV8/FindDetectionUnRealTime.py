import os
import shutil
import PySimpleGUI as sg

def copy_images(txt_folder, jpg_folder, output_folder):
    txt_files = [f for f in os.listdir(txt_folder) if f.endswith('.txt')]
    jpg_files = [f for f in os.listdir(jpg_folder) if f.endswith('.jpg')]

    for txt_file in txt_files:
        corresponding_jpg = txt_file.replace('.txt', '.jpg')
        if corresponding_jpg in jpg_files:
            shutil.copy(os.path.join(jpg_folder, corresponding_jpg), output_folder)

def main():
    layout = [
        [sg.Text('TXT文件夹'), sg.Input(), sg.FolderBrowse()],
        [sg.Text('JPG文件夹'), sg.Input(), sg.FolderBrowse()],
        [sg.Text('输出文件夹'), sg.Input(), sg.FolderBrowse()],
        [sg.Button('开始复制'), sg.Button('退出')]
    ]

    window = sg.Window('复制同名JPG图像', layout)

    while True:
        event, values = window.read()
        if event == '开始复制':
            copy_images(values[0], values[1], values[2])
            sg.popup('复制完成！')
        if event == '退出' or event == sg.WIN_CLOSED:
            break

    window.close()

if __name__ == '__main__':
    main()
