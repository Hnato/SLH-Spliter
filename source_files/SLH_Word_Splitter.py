import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox
import json
import os
import sys
from PIL import Image
try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
except ImportError:
    TkinterDnD = None

STARBUCKS_GREEN = "#00704A"
STARBUCKS_BROWN = "#362415"
WHITE = "#FFFFFF"

CONFIG_FILE = "config.json"

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class SLHWordSplitterFuturistic(TkinterDnD.Tk if TkinterDnD else tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("SLH Word Splitter 2026")
        self.geometry("650x950")
        self.minsize(600, 900)
        
        ctk.set_appearance_mode("light")
        
        icon_path = resource_path("source_files/SLH.ico")
        if os.path.exists(icon_path):
            try:
                self.after(200, lambda: self.iconbitmap(icon_path))
            except:
                pass

        self.words_per_segment = 1000
        self.segments = []
        self.load_settings()

        self.setup_ui()

    def load_settings(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                    config = json.load(f)
                    val = config.get("words_per_segment", 1000)
                    self.words_per_segment = max(100, min(16000, val))
            except:
                pass

    def save_settings(self):
        config = {"words_per_segment": self.words_per_segment}
        try:
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump(config, f)
        except:
            pass

    def setup_ui(self):
        self.configure(bg=WHITE)

        self.brand_frame = tk.Frame(self, bg=WHITE)
        self.brand_frame.pack(pady=(40, 20), fill="x")
        
        self.logo_label = ctk.CTkLabel(
            self.brand_frame, 
            text="☕", 
            font=ctk.CTkFont(family="Segoe UI Emoji", size=70),
            text_color=STARBUCKS_BROWN
        )
        self.logo_label.pack()

        self.title_label = ctk.CTkLabel(
            self.brand_frame, 
            text="SLH WORD SPLITTER", 
            font=ctk.CTkFont(family="Segoe UI", size=32, weight="bold"),
            text_color=STARBUCKS_GREEN
        )
        self.title_label.pack()

        self.main_container = ctk.CTkFrame(
            self, 
            fg_color=WHITE, 
            corner_radius=25,
            border_width=3,
            border_color=STARBUCKS_BROWN
        )
        self.main_container.pack(padx=30, pady=10, fill="both", expand=True)

        self.control_label = ctk.CTkLabel(
            self.main_container, 
            text="SEGMENT DENSITY", 
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=STARBUCKS_GREEN
        )
        self.control_label.pack(pady=(25, 5))

        self.slider_var = tk.IntVar(value=self.words_per_segment)
        self.slider = ctk.CTkSlider(
            self.main_container,
            from_=100,
            to=16000,
            number_of_steps=159,
            variable=self.slider_var,
            command=self.on_slider_change,
            button_color=STARBUCKS_BROWN,
            button_hover_color=STARBUCKS_GREEN,
            progress_color=STARBUCKS_GREEN,
            fg_color="#E0E0E0"
        )
        self.slider.pack(padx=40, pady=10, fill="x")

        self.value_display = ctk.CTkLabel(
            self.main_container,
            text=f"{self.words_per_segment} WORDS / PART",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=STARBUCKS_GREEN
        )
        self.value_display.pack(pady=(0, 10))

        self.file_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.file_frame.pack(padx=25, pady=(10, 5), fill="x")
        
        self.btn_select_file = ctk.CTkButton(
            self.file_frame,
            text="SELECT FILE (.txt)",
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=STARBUCKS_BROWN,
            text_color=WHITE,
            hover_color=STARBUCKS_GREEN,
            corner_radius=10,
            command=self.select_file
        )
        self.btn_select_file.pack(side="left", padx=(0, 10))
        
        self.file_info_label = ctk.CTkLabel(
            self.file_frame,
            text="Or drop file below",
            font=ctk.CTkFont(size=12, slant="italic"),
            text_color=STARBUCKS_BROWN
        )
        self.file_info_label.pack(side="left")

        self.input_area = ctk.CTkTextbox(
            self.main_container,
            fg_color=WHITE,
            text_color=STARBUCKS_GREEN,
            border_width=2,
            border_color=STARBUCKS_BROWN,
            corner_radius=15,
            font=ctk.CTkFont(family="Consolas", size=13)
        )
        self.input_area.pack(padx=25, pady=10, fill="both", expand=True)
        self.input_area.insert("1.0", "PASTE SOURCE TEXT OR DROP FILE HERE...")
        self.input_area.bind("<FocusIn>", lambda e: self.clear_placeholder())
        
        if TkinterDnD is not None:
            self.input_area.drop_target_register(DND_FILES)
            self.input_area.dnd_bind('<<Drop>>', self.handle_drop)

        self.btn_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.btn_frame.pack(pady=30)

        self.btn_split = ctk.CTkButton(
            self.btn_frame,
            text="ENGAGE SPLIT",
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color=STARBUCKS_GREEN,
            text_color=WHITE,
            hover_color="#00593B",
            corner_radius=12,
            border_width=2,
            border_color=STARBUCKS_BROWN,
            height=50,
            width=200,
            command=self.process_split
        )
        self.btn_split.pack(side="left", padx=10)

        self.btn_save = ctk.CTkButton(
            self.btn_frame,
            text="EXPORT SYSTEM",
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color=WHITE,
            border_width=2,
            border_color=STARBUCKS_BROWN,
            text_color=STARBUCKS_GREEN,
            hover_color="#F5F5F5",
            corner_radius=12,
            height=50,
            width=200,
            state="disabled",
            command=self.save_to_file
        )
        self.btn_save.pack(side="left", padx=10)

        self.footer_label = ctk.CTkLabel(
            self,
            text="Brewed with love and ☕ for you !!!\nBy Hnato",
            font=ctk.CTkFont(family="Segoe UI", size=12, slant="italic"),
            text_color=STARBUCKS_BROWN,
            justify="center",
            bg_color=WHITE
        )
        self.footer_label.pack(pady=25)

    def on_slider_change(self, val):
        self.words_per_segment = int(float(val))
        self.value_display.configure(text=f"{self.words_per_segment} WORDS / PART")
        self.save_settings()

    def clear_placeholder(self):
        content = self.input_area.get("1.0", "end-1c")
        if content == "PASTE SOURCE TEXT OR DROP FILE HERE...":
            self.input_area.delete("1.0", "end")

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.load_file_content(file_path)

    def handle_drop(self, event):
        file_path = event.data.strip('{}')
        if file_path.lower().endswith('.txt'):
            self.load_file_content(file_path)
        else:
            messagebox.showwarning("System Alert", "Only .txt files are supported for neural processing.")

    def load_file_content(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.input_area.delete("1.0", "end")
            self.input_area.insert("1.0", content)
            self.file_info_label.configure(text=f"Loaded: {os.path.basename(file_path)}", text_color=STARBUCKS_GREEN)
        except Exception as e:
            messagebox.showerror("IO Error", f"Failed to read file:\n{e}")

    def process_split(self):
        text = self.input_area.get("1.0", tk.END).strip()
        if not text or text == "PASTE SOURCE TEXT OR DROP FILE HERE...":
            messagebox.showwarning("System Alert", "No data detected. Please provide source text or file.")
            return

        words = text.split()
        limit = self.words_per_segment
        self.segments = [" ".join(words[i:i + limit]) for i in range(0, len(words), limit)]
        
        messagebox.showinfo("Neural Link Success", f"Core processing complete.\nGenerated {len(self.segments)} data segments.")
        self.btn_save.configure(state="normal")

    def save_to_file(self):
        if not self.segments: return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Digital Archive", "*.txt")],
            title="SELECT DESTINATION"
        )
        
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    for i, seg in enumerate(self.segments, 1):
                        f.write(f"--- [ NODE {i:03} ] ---\n{seg}\n\n")
                messagebox.showinfo("Archive Sync", "Data successfully exported to persistent storage.")
            except Exception as e:
                messagebox.showerror("IO Error", f"Sync failed:\n{e}")

if __name__ == "__main__":
    app = SLHWordSplitterFuturistic()
    app.mainloop()
