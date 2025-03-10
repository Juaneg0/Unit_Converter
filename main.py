import menu
import Converters.Temperature as convert_Temperature
import Converters.Distance as convert_Distance
import Converters.Weight as convert_Weight
from tkinter import *
from tkinter import ttk

root = menu.initialize_main_window()
menu.main_menu(root)

root.mainloop()