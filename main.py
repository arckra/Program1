import tkinter as tk
from view.input_form import InputForm
from view.mahasiswa import MahasiswaView

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi Data Mahasiswa")

        # Tombol untuk membuka form input
        self.button_input = tk.Button(master, text="Input Mahasiswa", command=self.open_input_form)
        self.button_input.pack(pady=10)

        # Tombol untuk membuka daftar mahasiswa
        self.button_view = tk.Button(master, text="Lihat Daftar Mahasiswa", command=self.open_mahasiswa_view)
        self.button_view.pack(pady=10)

    def open_input_form(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = InputForm(self.new_window)

    def open_mahasiswa_view(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = MahasiswaView(self.new_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()