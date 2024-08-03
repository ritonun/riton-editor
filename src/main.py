import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


current_selected_file = 'None'


def select_file():
    global current_selected_file

    filetypes = (
        ('video files', '*.mp4, *.m4v'),
        ('All files', '*.*'))

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='~/',
        filetypes=filetypes)

    current_selected_file = filename
    return filename


class FileFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self._create_widgets()

    def _select_file(self):
        select_file()
        self.file_name.set(current_selected_file)

    def _create_widgets(self):
        r, c = 0, 0
        # label
        self.files_label = ttk.Label(self, text='FILES')
        self.files_label.grid(row=0, column=0, sticky=tk.N)

        # filedialog button
        self.file_button = ttk.Button(self, text='Select file', command=self._select_file)
        self.file_button.grid(row=r+1, column=c)

        # filename display
        self.file_name = tk.StringVar(self, current_selected_file)
        self.file_name_label = ttk.Label(self, textvar=self.file_name)
        self.file_name_label.grid(row=r+2, column=c)


class ExtractFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self._create_widgets()

    def _create_widgets(self):
        r, c = 0, 0
        ttk.Label(self, text='EXTRACT\n-------').grid(row=0, column=0, columnspan=2)

        ttk.Label(self, text='Start time:').grid(row=r+1, column=c)
        self.start_time_entry = ttk.Entry(self, text='HH:MM:SS')
        self.start_time_entry.grid(row=r+1, column=c+1)

        ttk.Label(self, text='End time:').grid(row=r+2, column=c)
        self.end_time_entry = ttk.Entry(self, text='HH:MM:SS')
        self.end_time_entry.grid(row=r+2, column=c+1)



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Riton Editor')
        self.geometry('500x150')
        self.resizable(0, 0)

        # layout on root window
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)

        self._create_widgets()

    def _create_widgets(self):
        file_frame = FileFrame(self)
        file_frame.grid(row=0, column=0)

        extract_frame = ExtractFrame(self)
        extract_frame.grid(row=0, column=1)



if __name__ == '__main__':
    app = App()
    app.mainloop()