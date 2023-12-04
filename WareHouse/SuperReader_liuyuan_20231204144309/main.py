'''
Main application script for the Reader App.
'''
import tkinter as tk
from tkinter import filedialog
from pdf_reader import PDFReader
from epub_reader import EPUBReader
class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Reader App")
        self.create_menu()
    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu_bar)
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path.endswith('.pdf'):
            reader = PDFReader(self.root)
            reader.display_pdf(file_path)
            reader.add_navigation()
        elif file_path.endswith('.epub'):
            reader = EPUBReader(self.root)
            reader.display_epub(file_path)
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()