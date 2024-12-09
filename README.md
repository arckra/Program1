# Tugas Bahasa Pemrograman Pertemuan ke - 13


**CODE main.py**
```
import tkinter as tk
from view.input_form import InputForm
from view.mahasiswa import MahasiswaView
from data.mahasiswa import DataMahasiswa

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi Data Mahasiswa")

        self.data_mahasiswa = DataMahasiswa()

        self._create_widgets()

    def _create_widgets(self):
        """Membuat tombol utama aplikasi."""
        self.button_input = tk.Button(self.master, text="Input Mahasiswa", command=self.open_input_form)
        self.button_input.pack(pady=10)

        self.button_view = tk.Button(self.master, text="Lihat Daftar Mahasiswa", command=self.open_mahasiswa_view)
        self.button_view.pack(pady=10)

    def open_input_form(self):
        """Membuka form input di jendela baru."""
        self._open_new_window(InputForm)

    def open_mahasiswa_view(self):
        """Membuka daftar mahasiswa di jendela baru."""
        self._open_new_window(MahasiswaView)

    def _open_new_window(self, view_class):
        """Membantu membuka jendela baru dengan kelas tampilan tertentu."""
        new_window = tk.Toplevel(self.master)
        view_class(new_window, self.data_mahasiswa)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
```

# Jawaban dari code main.py
**Awal Mula**
![Screenshot 2024-12-09 205022](https://github.com/user-attachments/assets/cad9a88f-a7a6-44a0-8ef1-7aa0763ef0c2)


**Proses Input Data**
![Screenshot 2024-12-09 205107](https://github.com/user-attachments/assets/a97aada1-a35c-42a8-9bf0-83b94078a3c5)


**Menampilkan Data**
![Screenshot 2024-12-09 205245](https://github.com/user-attachments/assets/e376b5a4-0ade-41a7-9d9e-cc0fa9bac75c)


**Mencari Data sesuai kata kunci**
![Screenshot 2024-12-09 205310](https://github.com/user-attachments/assets/a8ebfc87-4881-43d5-8eba-813d9ced012c)


**Mengganti Data**
![Screenshot 2024-12-09 205344](https://github.com/user-attachments/assets/439cb1c1-0b40-43f3-943a-debb3eab3fa8)


**Menghapus Data**
![Screenshot 2024-12-09 205407](https://github.com/user-attachments/assets/76ea1419-60b4-4851-a8d3-e0dd2bdcd0be)


**SELESAI**
