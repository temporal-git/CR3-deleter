import os
from send2trash import send2trash
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from tkinter import ttk
from tkinter import *


class CR3Deleter:
    def __init__(self, root):
        self.root = root
        self.root.title('Удаление RAW ver 0.3')
        self.root.iconbitmap('camera-icon.ico')
        self.root.geometry("500x350+1000+300")

        self.path = ""

        s = ttk.Style()
        s.configure('my.TButton', font=("Helvetica", 15))

        frame = Frame(self.root, bg="#56ADF0", bd=5)
        frame.pack(pady=10, padx=10, fill=X)

        self.e_path = ttk.Entry(frame)
        self.e_path.pack(side=LEFT, ipady=2, expand=True, fill=X)

        btn_dialog = ttk.Button(frame, text="Выбрать папку", command=self.choose_dir)
        btn_dialog.pack(side=LEFT, padx=5)

        btn_start = ttk.Button(self.root, text="Start", style="my.TButton", command=self.start_deletion)
        btn_start.pack(fill=X, padx=10)

        # Создаем Canvas и Scrollbar для прокрутки
        self.canvas = Canvas(self.root)
        self.scrollbar = Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.pack(side=RIGHT, fill=Y)

    def choose_dir(self):
        rep_folder = askdirectory()
        dir_folder = rep_folder.replace('/', '\\')
        self.e_path.delete(0, END)
        self.e_path.insert(0, dir_folder)
        self.path = dir_folder

    def start_deletion(self):
        if self.path:
            file_extension_cr3 = r".CR3"
            file_extension_jpg = r".JPG"
            file_extension_xmp = r".xmp"

            cr3_list = [j for j in os.listdir(self.path) if j.endswith(file_extension_cr3)]
            jpg_list = [k for k in os.listdir(self.path) if k.endswith(file_extension_jpg)]
            xmp_list = [h for h in os.listdir(self.path) if h.endswith(file_extension_xmp)]

            # Получаем имена файлов без расширений
            cr3_names = {j.rsplit(".", 1)[0] for j in cr3_list}
            jpg_names = {k.rsplit(".", 1)[0] for k in jpg_list}

            # Находим файлы .CR3, для которых нет соответствующих .JPG
            files_to_delete = cr3_names - jpg_names

            for i in files_to_delete:
                try:
                    # Удаляем файл .CR3
                    send2trash(os.path.join(self.path, i + '.CR3'))
                    self.show_message(f'Файл успешно удален в корзину: {i}.CR3')

                    # Удаляем соответствующий файл .XMP, если он существует
                    if i + '.xmp' in xmp_list:
                        send2trash(os.path.join(self.path, i + '.xmp'))
                        self.show_message(f'Файл успешно удален в корзину: {i}.xmp вместе с {i}.CR3')

                except FileNotFoundError:
                    self.show_message(f'Файл не найден: {i}.CR3 или {i}.xmp')

            messagebox.showinfo('Успех', 'Поиск дубликатов и их удаление прошло успешно')
        else:
            messagebox.showwarning('Внимание', 'Выберите папку с фотографиями')

    def show_message(self, message):
        label_s = Label(self.scrollable_frame, text=message)
        label_s.pack()


if __name__ == "__main__":
    root = Tk()
    app = CR3Deleter(root)
    root.mainloop()
