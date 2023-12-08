import tkinter as tk
import tkinter.messagebox as msgbox
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BMIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("600x400")
        
        self.weight_var = tk.DoubleVar()
        self.height_var = tk.DoubleVar()
        self.bmi_var = tk.StringVar()
        self.history_file = "bmi_history.txt"  #File to store historical data

        label = tk.Label(root, text="BMI Calculator", font=("Helvetica", 16))
        label.pack(pady=10)
        weight_label = tk.Label(root, text="Weight (kg)")
        weight_label.pack()
        weight_entry = tk.Entry(root, textvariable=self.weight_var)
        weight_entry.pack()
        height_label = tk.Label(root, text="Height (m)")
        height_label.pack()
        height_entry = tk.Entry(root, textvariable=self.height_var)
        height_entry.pack()

        calculate_button = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi)
        calculate_button.pack(pady=10)
        bmi_label = tk.Label(root, text="BMI")
        bmi_label.pack()
        bmi_entry = tk.Entry(root, textvariable=self.bmi_var, state='readonly')
        bmi_entry.pack()

        save_button = tk.Button(root, text="Save Data", command=self.save_data)
        save_button.pack(pady=10)

        view_history_button = tk.Button(root, text="View Historical Data", command=self.view_history)
        view_history_button.pack()

        trend_button = tk.Button(root, text="Plot BMI Trend", command=self.plot_bmi_trend)
        trend_button.pack()

    def calculate_bmi(self):
        weight = self.weight_var.get()
        height = self.height_var.get()
        if weight <= 0 or height <= 0:
            msgbox.showerror("Error", "Weight and Height must be positive values.")
            return

        bmi = weight / (height ** 2)
        self.bmi_var.set(f"{bmi:.2f}")

    def save_data(self):
        weight = self.weight_var.get()
        height = self.height_var.get()
        bmi = self.bmi_var.get()
        if weight > 0 and height > 0:
            with open(self.history_file, "a") as file:
                file.write(f"Weight: {weight} kg, Height: {height} m, BMI: {bmi}\n")
            msgbox.showinfo("Success", "Data saved successfully.")
        else:
            msgbox.showerror("Error", "Invalid data. Please calculate BMI first.")

    def view_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as file:
                historical_data = file.read()
                msgbox.showinfo("Historical Data", historical_data)
        else:
            msgbox.showinfo("Historical Data", "No historical data available.")

    def plot_bmi_trend(self):
        if not os.path.exists(self.history_file):
            msgbox.showinfo("BMI Trend", "No historical data to plot.")
            return

        weights = []
        heights = []
        bmis = []

        with open(self.history_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("Weight"):
                    parts = line.split(",")
                    weight_str = parts[0].split(":")[1].strip()
                    height_str = parts[1].split(":")[1].strip()
                    bmi_str = parts[2].split(":")[1].strip()

                    weight = float(weight_str.split("kg")[0].strip())
                    height = float(height_str.split("m")[0].strip())
                    bmi = float(bmi_str)

                    weights.append(weight)
                    heights.append(height)
                    bmis.append(bmi)

        fig, ax = plt.subplots()
        ax.plot(weights, bmis, label="Weight vs. BMI")
        ax.plot(heights, bmis, label="Height vs. BMI")
        ax.set_xlabel("Weight (kg) / Height (m)")
        ax.set_ylabel("BMI")
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()
