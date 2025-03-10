from tkinter import *
from tkinter import ttk

def clean_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

def initialize_main_window():
    global root
    root = Tk()
    root.title("Units Converter")
    root.configure(bg = "light blue")
    root.geometry("400x400")
    frm = ttk.Frame(root, padding = 10)
    return root

def main_menu(root):
    clean_screen(root)
    root_label_title = Label(root, text = "Units Converter", bg = "light blue", font = ("Arial", 20)).grid(row = 0, column = 0, padx=100)
    root_label_text = Label(root, text = "Choose a category to convert", bg = "light blue", font = ("Arial", 15)).grid(row = 1, column = 0, padx=100)
    root_temp_button = Button(root, text = "Temperature", command = lambda:temperature_menu(root)).grid(row = 2, column = 0, padx=100)
    root_distance_button = Button(root, text = "Distance", command = lambda:distance_menu(root)).grid(row = 3, column = 0, padx=100)
    root_weight_button = Button(root, text = "Weight", command = lambda:weight_menu(root)).grid(row = 4, column = 0, padx=100)
    root_quit = Button(root, text = "Quit", command = root.quit).grid(row = 5, column = 0)

def temperature_menu(root):
    clean_screen(root)
    root_label_title = Label(root, text = "Temperature Converter", bg = "light blue", font = ("Arial", 20)).grid(row = 0, column = 0, padx=100)
    root_label_text = Label(root, text = "Choose a conversion", bg = "light blue", font = ("Arial", 15)).grid(row = 1, column = 0, padx=100)
    root_temp_button = Button(root, text = "Celcius to Fahrenheit").grid(row = 2, column = 0, padx=100)
    root_distance_button = Button(root, text = "Fahrenheit to Celcius").grid(row = 3, column = 0, padx=100)
    root_quit = Button(root, text = "Go back", command = lambda:main_menu(root)).grid(row = 4, column = 0)

def distance_menu(root):
    clean_screen(root)
    root_label_title = Label(root, text = "Distance Converter", bg = "light blue", font = ("Arial", 20)).grid(row = 0, column = 0, padx=100)
    root_label_text = Label(root, text = "Choose a conversion", bg = "light blue", font = ("Arial", 15)).grid(row = 1, column = 0, padx=100)
    root_temp_button = Button(root, text = "Kilometer to Mile").grid(row = 2, column = 0, padx=100)
    root_distance_button = Button(root, text = "Mile to Kilometer").grid(row = 3, column = 0, padx=100)
    root_quit = Button(root, text = "Go back", command = lambda:main_menu(root)).grid(row = 4, column = 0)
    
def weight_menu(root):
    clean_screen(root)
    root_label_title = Label(root, text = "Weight Converter", bg = "light blue", font = ("Arial", 20)).grid(row = 0, column = 0, padx=100)
    root_label_text = Label(root, text = "Choose a conversion", bg = "light blue", font = ("Arial", 15)).grid(row = 1, column = 0, padx=100)
    root_temp_button = Button(root, text = "Kilogram to Pound").grid(row = 2, column = 0, padx=100)
    root_distance_button = Button(root, text = "Pound to Kilogram").grid(row = 3, column = 0, padx=100)
    root_quit = Button(root, text = "Go back", command = lambda:main_menu(root)).grid(row = 4, column = 0)

