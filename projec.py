import tkinter as tk

def calculate():
    try:
        p = float(principal_var.get())
        t = float(time_var.get())
        r = float(rate_var.get())
        si = (p * t * r) / 100
        ci = p * ((1 + r / 100) ** t) - p
        si_label.config(text=f"Simple Interest: {si:.2f}")
        ci_label.config(text=f"Compound Interest: {ci:.2f}")
    except:
        si_label.config(text="Invalid input")
        ci_label.config(text="")

root = tk.Tk()
root.geometry("400x400")
root.title("Age Calculator App")
root.configure(bg="#e6f2ff")

frame = tk.Frame(root, bg="#e6f2ff")
frame.pack(pady=40)

tk.Label(frame, text="Principal:", bg="#e6f2ff", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
principal_var = tk.StringVar()
tk.Entry(frame, textvariable=principal_var, width=20).grid(row=0, column=1, pady=5)

tk.Label(frame, text="Time (years):", bg="#e6f2ff", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
time_var = tk.StringVar()
tk.Entry(frame, textvariable=time_var, width=20).grid(row=1, column=1, pady=5)

tk.Label(frame, text="Rate (%):", bg="#e6f2ff", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
rate_var = tk.StringVar()
tk.Entry(frame, textvariable=rate_var, width=20).grid(row=2, column=1, pady=5)

tk.Button(root, text="Calculate", command=calculate, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)
si_label = tk.Label(root, text="", bg="#e6f2ff", font=("Arial", 12))
si_label.pack()
ci_label = tk.Label(root, text="", bg="#e6f2ff", font=("Arial", 12))
ci_label.pack()

root.mainloop()