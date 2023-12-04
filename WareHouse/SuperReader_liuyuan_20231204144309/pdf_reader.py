'''
Module for rendering PDF files in the Reader App.
'''
import fitz  # PyMuPDF
import tkinter as tk
from tkinter import Canvas, Button
from PIL import Image, ImageTk
class PDFReader:
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(self.root)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.current_page = 0
        self.document = None
    def display_pdf(self, file_path):
        self.document = fitz.open(file_path)
        self.add_navigation()
        self.show_page(self.current_page)
    def show_page(self, page_number):
        self.canvas.delete("all")  # Clear the previous image
        page = self.document.load_page(page_number)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        photo = ImageTk.PhotoImage(image=img)
        self.canvas.create_image(10, 10, image=photo, anchor='nw')
        self.canvas.image = photo  # Keep a reference to avoid garbage collection
    def next_page(self):
        if self.document is not None and self.current_page < self.document.page_count - 1:
            self.current_page += 1
            self.show_page(self.current_page)
    def prev_page(self):
        if self.document is not None and self.current_page > 0:
            self.current_page -= 1
            self.show_page(self.current_page)
    def add_navigation(self):
        frame = tk.Frame(self.root)
        frame.pack(side=tk.RIGHT, fill=tk.Y)
        prev_button = Button(frame, text="Previous", command=self.prev_page)
        prev_button.pack(side=tk.TOP, fill=tk.X)
        next_button = Button(frame, text="Next", command=self.next_page)
        next_button.pack(side=tk.TOP, fill=tk.X)