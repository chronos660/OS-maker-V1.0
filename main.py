import tkinter as tk
from tkinter import colorchooser, messagebox

class OSSimulatorBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("OS Builder")
        self.root.geometry("400x400")
        self.root.config(bg="#2c3e50")

        # Default OS Settings
        self.bg_color = "#3498db"
        self.include_notepad = tk.BooleanVar(value=True)
        self.include_calc = tk.BooleanVar(value=True)

        self.create_builder_widgets()

    def create_builder_widgets(self):
        """Creates the configuration UI for the OS builder."""
        # Title
        title = tk.Label(self.root, text="OS Builder Configuration", font=("Arial", 16, "bold"), fg="#ecf0f1", bg="#2c3e50")
        title.pack(pady=20)

        # Color Selection Button
        self.color_btn = tk.Button(self.root, text="Choose Desktop Background", command=self.choose_color, bg="#e74c3c", fg="white", font=("Arial", 11))
        self.color_btn.pack(pady=15)

        # App Toggles Frame
        frame = tk.LabelFrame(self.root, text=" Include Apps ", fg="#ecf0f1", bg="#2c3e50", font=("Arial", 11), padx=10, pady=10)
        frame.pack(pady=15, fill="x", padx=40)

        chk_notepad = tk.Checkbutton(frame, text="Notepad Application", variable=self.include_notepad, bg="#2c3e50", fg="#2c3e50", font=("Arial", 10))
        chk_notepad.pack(anchor="w", pady=2)

        chk_calc = tk.Checkbutton(frame, text="Calculator Application", variable=self.include_calc, bg="#2c3e50", fg="#2c3e50", font=("Arial", 10))
        chk_calc.pack(anchor="w", pady=2)

        # Preview Button
        preview_btn = tk.Button(self.root, text="👁 Preview Custom OS", command=self.open_preview, bg="#2ecc71", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
        preview_btn.pack(pady=30)

    def choose_color(self):
        """Opens a color picker to set the desktop background."""
        color_code = colorchooser.askcolor(title="Choose background color")
        if color_code[1]:
            self.bg_color = color_code[1]
            self.color_btn.config(bg=self.bg_color)

    def open_preview(self):
        """Launches the TopLevel window acting as the OS Preview."""
        preview_win = tk.Toplevel(self.root)
        preview_win.title("OS Preview Mode")
        preview_win.geometry("800x500")
        preview_win.configure(bg=self.bg_color)

        # Desktop Environment Title
        desktop_label = tk.Label(preview_win, text="My Custom OS", font=("Arial", 24, "bold"), fg="white", bg=self.bg_color)
        desktop_label.pack(pady=50)

        # Taskbar / Desktop Shortcuts panel
        shortcut_frame = tk.Frame(preview_win, bg=self.bg_color)
        shortcut_frame.pack(side="bottom", fill="x", pady=20)

        # Conditionally render apps based on Builder choices
        if self.include_notepad.get():
            btn_notepad = tk.Button(shortcut_frame, text="📝 Notepad", command=lambda: self.launch_mock_app(preview_win, "Notepad"), font=("Arial", 11), width=12)
            btn_notepad.pack(side="left", padx=20)

        if self.include_calc.get():
            btn_calc = tk.Button(shortcut_frame, text="🧮 Calculator", command=lambda: self.launch_mock_app(preview_win, "Calculator"), font=("Arial", 11), width=12)
            btn_calc.pack(side="left", padx=20)
            
        if not self.include_notepad.get() and not self.include_calc.get():
            no_app_label = tk.Label(shortcut_frame, text="(No apps installed. Use the builder to add some!)", fg="white", bg=self.bg_color, font=("Arial", 10, "italic"))
            no_app_label.pack()

    def launch_mock_app(self, parent, app_name):
        """Creates a mock draggable/closable internal window for an app."""
        app_win = tk.Toplevel(parent)
        app_win.title(app_name)
        app_win.geometry("300x200")
        
        # Simple App layouts
        if app_name == "Notepad":
            text_area = tk.Text(app_win, wrap="word")
            text_area.pack(fill="both", expand=True)
            text_area.insert("1.0", "Type your notes here...")
        elif app_name == "Calculator":
            label = tk.Label(app_win, text="0", font=("Arial", 20), anchor="e", bg="white", fg="black", padx=10, pady=10)
            label.pack(fill="x", pady=10)
            
            grid_frame = tk.Frame(app_win)
            grid_frame.pack()
            
            # Tiny mock grid just for aesthetics
            buttons = ['7', '8', '9', '+', '4', '5', '6', '-']
            for i, btn_text in enumerate(buttons):
                r, c = divmod(i, 4)
                tk.Button(grid_frame, text=btn_text, width=5, command=lambda b=btn_text: messagebox.showinfo("Calc", f"Pressed {b}")).grid(row=r, column=c, padx=2, pady=2)

# Main Application Entry Loop
if __name__ == "__main__":
    root = tk.Tk()
    app = OSSimulatorBuilder(root)
    root.mainloop()
