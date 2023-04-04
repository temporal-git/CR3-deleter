import os
from send2trash import send2trash
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from tkinter import ttk
from tkinter import *


def choose_dir():
    rep_folder = askdirectory()
    dir_folder = rep_folder.replace('/', '\\')
    e_path.delete(0, END)
    e_path.insert(0, dir_folder)

def f_start():
    folder = e_path.get()
    if folder:
        file_extension = r".CR3"
        file_extension2 = r".JPG"

        cr3_list = [j for j in os.listdir(folder) if j.endswith(file_extension)]
        jpg_list = [k for k in os.listdir(folder) if k.endswith(file_extension2)]

        folder_list = cr3_list + jpg_list

        clear_list = []


        for item in folder_list:
            item = item.rsplit(".")[0]
            clear_list.append(item)

        final_list = [elem for elem in clear_list if clear_list.count(elem) == 1]


        for i in final_list:
            try:
                send2trash(folder + '\\' + i + '.CR3') # рабочий вариант
                send2trash(folder + '\\' + i + '.xmp')
                print('Файл успешно удален в корзину: ' + str(i),'.CR3')
                print('Файл успешно удален в корзину: ' + str(i),'.xmp')
                l = Label(root, text = 'Файл успешно удален в корзину: ' + str(i) + '.CR3 вместе с '+ str(i) + '.xmp')
                l.pack()
            except FileNotFoundError:
                print('Файл успешно удален в корзину: ' + str(i), '.CR3')
                l = Label(root, text='Файл успешно удален в корзину: ' + str(i) + '.CR3')
                l.pack()
        messagebox.showinfo('Успех', 'Поиск дубликатов и их удаление прошло успешно')
    else:
        messagebox.showwarning('Внимание', 'Выберите папку с фотографиями')


root = Tk()
root.title('Удаление RAW ver 0.2')
root.iconbitmap('camera-icon.ico') # ico
root.geometry("500x350+1000+300")

s = ttk.Style()
s.configure('my.TButton', font=("Helvetica", 15))

frame = Frame(root, bg="#56ADFF", bd=5)
frame.pack(pady=10, padx=10, fill=X)

e_path = ttk.Entry(frame)
e_path.pack(side=LEFT, ipady=2, expand=True, fill=X)

btn_dialog = ttk.Button(frame, text="Выбрать папку", command=choose_dir)
btn_dialog.pack(side=LEFT, padx=5)

btn_start = ttk.Button(root, text="Start", style="my.TButton", command=f_start)
btn_start.pack(fill=X, padx=10)



root.mainloop()