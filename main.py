import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from payloads.reverse_shells import ReverseShellPayloads
from payloads.xss import XSSPayloads
from payloads.sql_injection import SQLiPayloads
from payloads.ssti import SSTIPayloads
from payloads.command_injection import CommandInjectionPayloads
from utils import save_to_file

class DarkBluePayloadGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Payload Generator - by Victor Santana")
        self.root.geometry("800x650")
        self.root.minsize(700, 600)
        
        # Dark blue color scheme
        self.primary_dark = '#0a192f'    # Navy blue
        self.secondary_dark = '#172a45'   # Dark blue
        self.accent_blue = '#64ffda'      # Teal accent
        self.text_light = '#ccd6f6'       # Light blue text
        self.highlight_blue = '#1e90ff'   # Bright blue
        self.warning_red = '#ff5555'      # Soft red
        
        self.configure_styles()
        self.setup_ui()
        self.create_menu()

    def configure_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Main styles
        self.style.configure('.', 
                           background=self.secondary_dark, 
                           foreground=self.text_light,
                           font=('Segoe UI', 9))
        
        # Frame styles
        self.style.configure('TFrame', background=self.secondary_dark)
        self.style.configure('Header.TFrame', background=self.primary_dark)
        
        # Label styles
        self.style.configure('TLabel', 
                           background=self.secondary_dark, 
                           foreground=self.text_light)
        self.style.configure('Header.TLabel', 
                           background=self.primary_dark, 
                           foreground=self.accent_blue,
                           font=('Segoe UI', 12, 'bold'))
        
        # Button styles
        self.style.configure('TButton', 
                           background=self.primary_dark,
                           foreground=self.text_light,
                           bordercolor=self.accent_blue,
                           font=('Segoe UI', 9))
        self.style.map('TButton',
                      background=[('active', self.highlight_blue)],
                      foreground=[('active', self.primary_dark)])
        
        self.style.configure('Accent.TButton', 
                           background=self.highlight_blue,
                           foreground=self.primary_dark,
                           font=('Segoe UI', 9, 'bold'))
        
        # Entry and Combobox styles
        self.style.configure('TEntry', 
                           fieldbackground='#2a3f5f',
                           foreground=self.text_light,
                           insertcolor=self.text_light)
        
        self.style.configure('TCombobox',
                           fieldbackground='#2a3f5f',
                           foreground=self.text_light,
                           selectbackground=self.highlight_blue)
        
        # Text widget style
        self.style.configure('Text.TFrame', background='#1a2a3a')

    def setup_ui(self):
        # Main container
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Header
        header_frame = ttk.Frame(main_container, style='Header.TFrame')
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(header_frame, 
                 text="Payload Generator", 
                 style='Header.TLabel').pack(side=tk.LEFT, padx=10)
        
        # Configuration frame
        config_frame = ttk.LabelFrame(main_container, 
                                    text="Configuration", 
                                    padding=10,
                                    style='TFrame')
        config_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Payload type selection
        ttk.Label(config_frame, text="Payload Type:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.payload_type = ttk.Combobox(config_frame, values=[
            "Reverse Shell", "XSS", "SQL Injection", "SSTI", "Command Injection"
        ], state='readonly')
        self.payload_type.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5)
        self.payload_type.bind("<<ComboboxSelected>>", self.toggle_options)
        
        # Reverse Shell options (hidden initially)
        self.rs_options_frame = ttk.Frame(config_frame)
        ttk.Label(self.rs_options_frame, text="LHOST:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.lhost = ttk.Entry(self.rs_options_frame)
        self.lhost.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5)
        
        ttk.Label(self.rs_options_frame, text="LPORT:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.lport = ttk.Entry(self.rs_options_frame)
        self.lport.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)
        self.rs_options_frame.grid(row=1, column=0, columnspan=2, sticky=tk.EW, pady=5)
        self.rs_options_frame.grid_remove()
        
        # Generate button
        btn_frame = ttk.Frame(config_frame)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        ttk.Button(btn_frame, 
                  text="Generate Payloads", 
                  style='Accent.TButton',
                  command=self.generate_payloads).pack(side=tk.LEFT, padx=5)
        
        # Results frame
        results_frame = ttk.LabelFrame(main_container, 
                                     text="Generated Payloads", 
                                     padding=10)
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Text widget with scrollbar
        text_frame = ttk.Frame(results_frame, style='Text.TFrame')
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.result_text = tk.Text(text_frame, 
                                 wrap=tk.WORD,
                                 bg='#1a2a3a',
                                 fg=self.text_light,
                                 insertbackground=self.text_light,
                                 selectbackground=self.highlight_blue,
                                 yscrollcommand=scrollbar.set,
                                 font=('Consolas', 10))
        self.result_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.result_text.yview)
        
        # Status bar
        self.status_bar = ttk.Label(main_container, 
                                  text="Ready",
                                  relief=tk.SUNKEN,
                                  anchor=tk.W,
                                  style='TLabel')
        self.status_bar.pack(fill=tk.X, pady=(5, 0))
        
        # Configure grid weights
        config_frame.columnconfigure(1, weight=1)
        self.rs_options_frame.columnconfigure(1, weight=1)

    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0, bg=self.secondary_dark, fg=self.text_light)
        file_menu.add_command(label="Save Payloads", command=self.save_to_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0, bg=self.secondary_dark, fg=self.text_light)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)
        
        self.root.config(menu=menubar)

    def toggle_options(self, event):
        if self.payload_type.get() == "Reverse Shell":
            self.rs_options_frame.grid()
        else:
            self.rs_options_frame.grid_remove()

    def generate_payloads(self):
        payload_type = self.payload_type.get()
        if not payload_type:
            messagebox.showerror("Error", "Please select a payload type", parent=self.root)
            return

        payloads = []
        
        try:
            self.status_bar.config(text="Generating payloads...")
            self.root.update_idletasks()
            
            if payload_type == "Reverse Shell":
                lhost = self.lhost.get()
                lport = self.lport.get()
                if not lhost or not lport:
                    messagebox.showerror("Error", "LHOST and LPORT are required for Reverse Shell", parent=self.root)
                    return
                generator = ReverseShellPayloads(lhost, lport)
                payloads = generator.generate()
            
            elif payload_type == "XSS":
                generator = XSSPayloads()
                payloads = generator.generate()
            
            elif payload_type == "SQL Injection":
                generator = SQLiPayloads()
                payloads = generator.generate()
            
            elif payload_type == "SSTI":
                generator = SSTIPayloads()
                payloads = list(generator.generate().values())
            
            elif payload_type == "Command Injection":
                generator = CommandInjectionPayloads()
                payloads = generator.generate()

            # Display results
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Generated {len(payloads)} {payload_type} payloads:\n\n", 'highlight')
            self.result_text.insert(tk.END, "\n".join(payloads))
            self.status_bar.config(text=f"Generated {len(payloads)} {payload_type} payloads")
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate payloads: {str(e)}", parent=self.root)
            self.status_bar.config(text="Error generating payloads")

    def save_to_file(self):
        payloads = self.result_text.get(1.0, tk.END).strip().split("\n")
        if not payloads or payloads == [""]:
            messagebox.showerror("Error", "No payloads to save", parent=self.root)
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("JSON Files", "*.json"), ("All Files", "*.*")],
            title="Save Payloads"
        )
        if file_path:
            try:
                save_to_file(payloads, file_path)
                self.status_bar.config(text=f"Payloads saved to {file_path}")
                messagebox.showinfo("Success", f"Payloads saved successfully to:\n{file_path}", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}", parent=self.root)

    def show_about(self):
        about_text = """Payload Generator - Security Toolkit
Version 1.0

A professional tool for generating security testing payloads.
Developed for penetration testers and security researchers.

© 2023 Security Team"""
        messagebox.showinfo("About", about_text, parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = DarkBluePayloadGenerator(root)
    root.mainloop()