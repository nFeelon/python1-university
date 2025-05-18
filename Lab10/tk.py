import tkinter as tk
from tkinter import ttk, messagebox
import math
from PIL import Image, ImageTk
import os

class SuperPriloz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор площадей")
        self.geometry("550x650")
        self.configure(bg="#f0f0f0")
        self.resizable(False, True)
        # self.iconbitmap(default="logo.ico")
 
        self.title_font = ("Arial", 12, "bold")
        self.label_font = ("Arial", 12)
        self.button_font = ("Arial", 12, "bold")
        
        self.create_widgets()
        self.bind_events()
    
    def create_widgets(self):
        self.header_frame = tk.Frame(self, bg="blue")
        self.header_frame.pack(fill=tk.X)
        
        self.title_label = tk.Label(self.header_frame, text="Калькулятор площадей", 
            font=self.title_font, bg="blue", fg="white", pady=10)
        self.title_label.pack()

        self.main_frame = tk.Frame(self, bg="#f0f0f0")
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.shape_label = tk.Label(self.main_frame, text="Выберите фигуру:", 
            font=self.label_font, bg="#f0f0f0")
        self.shape_label.grid(row=0, column=0, sticky="w", pady=10)
        
        self.shapes = ["Квадрат", "Треугольник", "Круг"]
        self.shape_var = tk.StringVar(value=self.shapes[0])
        self.shape_combobox = ttk.Combobox(self.main_frame, textvariable=self.shape_var, 
            values=self.shapes, font=self.label_font, state="readonly", width=15)
        self.shape_combobox.grid(row=0, column=1, sticky="w", pady=10)
        
        self.params_frame = tk.LabelFrame(self.main_frame, text="Параметры", 
            font=self.label_font, bg="#f0f0f0", padx=10, pady=10)
        self.params_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=10)
        
        self.result_frame = tk.LabelFrame(self.main_frame, text="Результат", 
            font=self.label_font, bg="#f0f0f0", padx=10, pady=10)
        self.result_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=10)
        
        self.result_label = tk.Label(self.result_frame, text="Площадь: ", 
            font=self.label_font, bg="#f0f0f0")
        self.result_label.pack(anchor="w")
        
        self.round_var = tk.BooleanVar(value=True)
        self.round_check = tk.Checkbutton(self.main_frame, text="Округлить результат", 
            variable=self.round_var, font=self.label_font, bg="#f0f0f0", activebackground="#e0e0e0")
        self.round_check.grid(row=3, column=0, sticky="w", pady=5)
        
        self.units_frame = tk.LabelFrame(self.main_frame, text="Единицы измерения", 
            font=self.label_font, bg="#f0f0f0", padx=10, pady=5)
        self.units_frame.grid(row=4, column=0, columnspan=2, sticky="nsew", pady=5)
        
        self.unit_var = tk.StringVar(value="см²")
        units = ["см²", "м²", "км²"]
        
        for i, unit in enumerate(units):
            tk.Radiobutton(self.units_frame, text=unit, variable=self.unit_var, value=unit,
                font=self.label_font, bg="#f0f0f0", activebackground="#e0e0e0").grid(row=0, column=i, padx=20)
        
        self.calc_button = tk.Button(self.main_frame, text="Рассчитать", font=self.button_font,
            bg="blue", fg="white", activebackground="blue", activeforeground="white",
            padx=15, pady=5, command=self.calculate_area)
        self.calc_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.setup_square_inputs()
    
    def bind_events(self):
        self.shape_combobox.bind("<<ComboboxSelected>>", self.on_shape_change)
        self.calc_button.bind("<Enter>", lambda e: self.calc_button.config(bg="green"))
        self.calc_button.bind("<Leave>", lambda e: self.calc_button.config(bg="blue"))
    
    def on_shape_change(self, event=None):
        for widget in self.params_frame.winfo_children():
            widget.destroy()
        
        shape = self.shape_var.get()
        if shape == "Квадрат":
            self.setup_square_inputs()
        elif shape == "Треугольник":
            self.setup_triangle_inputs()
        elif shape == "Круг":
            self.setup_circle_inputs()
    
    def setup_square_inputs(self):
        tk.Label(self.params_frame, text="Сторона квадрата:", 
            font=self.label_font, bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
        
        self.square_side = tk.Entry(self.params_frame, font=self.label_font, width=10)
        self.square_side.grid(row=0, column=1, sticky="w", pady=5)
        
        self.load_shape_image("square")
    
    def setup_triangle_inputs(self):
        tk.Label(self.params_frame, text="Сторона a:", font=self.label_font, bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
        self.tri_a = tk.Entry(self.params_frame, font=self.label_font, width=10)
        self.tri_a.grid(row=0, column=1, sticky="w", pady=5)
        
        tk.Label(self.params_frame, text="Сторона b:", font=self.label_font, bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
        self.tri_b = tk.Entry(self.params_frame, font=self.label_font, width=10)
        self.tri_b.grid(row=1, column=1, sticky="w", pady=5)
        
        tk.Label(self.params_frame, text="Сторона c:", font=self.label_font, bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)
        self.tri_c = tk.Entry(self.params_frame, font=self.label_font, width=10)
        self.tri_c.grid(row=2, column=1, sticky="w", pady=5)
        
        self.load_shape_image("triangle")
    
    def setup_circle_inputs(self):
        tk.Label(self.params_frame, text="Радиус круга:", font=self.label_font, bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
        self.circle_radius = tk.Entry(self.params_frame, font=self.label_font, width=10)
        self.circle_radius.grid(row=0, column=1, sticky="w", pady=5)
        
        self.load_shape_image("circle")
    
    def load_shape_image(self, shape_name):
        img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
        img_path = os.path.join(img_dir, f"{shape_name}.png")
        
        img_frame = tk.Frame(self.params_frame, bg="#f0f0f0")
        img_frame.grid(row=0, column=2, rowspan=3, padx=20, pady=5)
        
        img = Image.open(img_path)
        img = img.resize((200, 100))
        photo = ImageTk.PhotoImage(img)
        img_label = tk.Label(img_frame, image=photo, bg="#f0f0f0")
        img_label.image = photo
        img_label.pack()
    
    def calculate_area(self):
        try:
            shape = self.shape_var.get()
            area = 0
            
            match shape:
                case "Квадрат":
                    side = float(self.square_side.get())
                    area = side ** 2
                    formula = f"S = a^2 = {side}^2 = {area}"

                case "Треугольник":
                    a = float(self.tri_a.get())
                    b = float(self.tri_b.get())
                    c = float(self.tri_c.get())
                    
                    if a + b <= c or a + c <= b or b + c <= a:
                        messagebox.showerror("Ошибка", "Треугольник с такими сторонами не существует!")
                        return
                    
                    s = (a + b + c) / 2
                    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                    formula = f"S = sqrt(s(s-a)(s-b)(s-c))\nгде s = (a+b+c)/2 = {s}\nS = {area}"
                
                case "Круг":
                    radius = float(self.circle_radius.get())
                    area = math.pi * radius ** 2
                    formula = f"S = πr^2 = π * {radius}^2 = {area}"
            
            if self.round_var.get():
                area = round(area, 2)
            
            unit = self.unit_var.get()
            self.result_label.config(text=f"Площадь: {area} {unit}\n\nФормула: {formula}")
            
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

app = SuperPriloz()
app.mainloop()