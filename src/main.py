import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from generate_arbo import generate_arbo
from generate_script_js import generate_script_js
from generate_uploadImage_js import generate_uploadImage_js
from generate_style_css import generate_style_css

def generate_files():
    directory_path = directory_var.get()
    bg_color = color_entry1.get()
    primary_color = color_entry2.get()


    if all([directory_path, bg_color, primary_color]):
        # Generate tree path
        generate_arbo(directory_path)
        generate_script_js(directory_path)
        generate_uploadImage_js(directory_path)
        generate_style_css(directory_path, bg_color, primary_color)
        
        result_label.config(text="Gallery files have been generated.")

        print("Gallery files well generated, don't forget to minify !")
        print("Read readme.txt for implementation.\n")

        app.quit()
    else:
        result_label.config(text="Please provide all required fields.")

def select_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        directory_var.set(directory_path)

def open_color_picker1():
    color = colorchooser.askcolor()[1]
    color_entry1.delete(0, tk.END)
    color_entry1.insert(0, color)

def open_color_picker2():
    color = colorchooser.askcolor()[1]
    color_entry2.delete(0, tk.END)
    color_entry2.insert(0, color)

app = tk.Tk()
app.title("Darius GA Cookie Generator")

directory_var = tk.StringVar()

directory_label = tk.Label(app, text="Select Directory:")
directory_label.pack()
directory_entry = tk.Entry(app, textvariable=directory_var, width = 50)
directory_entry.pack()

select_directory_button = tk.Button(app, text="Browse", command=select_directory)
select_directory_button.pack()

# Create an Entry widget for entering color in hex format
cookie_entry_label = tk.Label(app, text="Enter bg color of the cookie pop-up (#hex format) :")
cookie_entry_label.pack()
color_entry1 = tk.Entry(app)
color_entry1.pack()

# Create a Button to open the color picker
color_picker_button = tk.Button(app, text="Or use color picker", command=open_color_picker1)
color_picker_button.pack()

# Create an Entry widget for entering color in hex format
cookie_entry_label = tk.Label(app, text="Enter primary color of the cookie pop-up (#hex format) :")
cookie_entry_label.pack()
color_entry2 = tk.Entry(app)
color_entry2.pack()

# Create a Button to open the color picker
color_picker_button = tk.Button(app, text="Or use color picker", command=open_color_picker2)
color_picker_button.pack()

blank_label = tk.Label(app, text="")
blank_label.pack()

generate_button = tk.Button(app, text="Generate", command=generate_files)
generate_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
