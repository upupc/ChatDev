'''
Module for rendering EPUB files in the Reader App.
'''
from ebooklib import epub
import tkinter as tk
from tkinter import Canvas, Text
class EPUBReader:
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(self.root)
        self.text_widget = Text(self.canvas)
        self.text_widget.pack(fill=tk.BOTH, expand=True)
        self.canvas.pack(fill=tk.BOTH, expand=True)
    def display_epub(self, file_path):
        epub_book = epub.read_epub(file_path)
        # Assuming we are just displaying the text of the first item
        content = epub_book.get_items_of_type(ebooklib.ITEM_DOCUMENT)[0].get_body_content().decode('utf-8')
        self.text_widget.insert('1.0', content)