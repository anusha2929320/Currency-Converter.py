import tkinter as tk
from tkinter import ttk, messagebox

# Currency Converter Application 
# Sample exchange rates (you can update these)
exchange_rates = {
    "USD": 1.0,       # Base currency
    "EUR": 0.85,
    "INR": 83.23,
    "GBP": 0.75,
    "JPY": 157.20
}

# Function to perform the currency conversion
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        if from_currency == to_currency:
            converted_amount = amount
        else:
            usd_amount = amount / exchange_rates[from_currency]
            converted_amount = usd_amount * exchange_rates[to_currency]

        result_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Set up the main window

root = tk.Tk()
root.title(" Currency Converter")
root.geometry("400x400")
root.configure(bg="#1a1a1a")

# Title Label
title_label = tk.Label(
    root,
    text=" Currency Converter",
    font=("Helvetica", 20, "bold"),
    fg="#00FFCC",
    bg="#1a1a1a"
)
title_label.pack(pady=20)

# Amount Entry Field
amount_entry = tk.Entry(root, font=("Helvetica", 16), width=14, justify="center")
amount_entry.pack(pady=10)
amount_entry.insert(0, "1")

# Currency Selection Dropdowns
from_currency_var = tk.StringVar(value="USD")
to_currency_var = tk.StringVar(value="INR")

currency_list = list(exchange_rates.keys())

from_dropdown = ttk.Combobox(root, textvariable=from_currency_var, values=currency_list, font=("Helvetica", 14), state="readonly", width=5)
from_dropdown.pack(pady=5)

to_dropdown = ttk.Combobox(root, textvariable=to_currency_var, values=currency_list, font=("Helvetica", 14), state="readonly", width=5)
to_dropdown.pack(pady=5)

# Convert Button
convert_button = tk.Button(
    root,
    text="Convert ",
    font=("Helvetica", 14),
    command=convert_currency,
    bg="#28a745",
    fg="white",
    width=12
)
convert_button.pack(pady=15)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 16),
    fg="#FFD700",
    bg="#1a1a1a"
)
result_label.pack(pady=10)

# Run the application loop
root.mainloop()
