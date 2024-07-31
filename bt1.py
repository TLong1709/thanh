import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, width=300, height=300):
        # Khởi tạo cửa sổ chính
        self.root = tk.Tk()
        self.root.title("Untitled - Notepad")
        self.root.geometry(f'{width}x{height}')
        
        # Tạo khu vực văn bản
        self.text_area = tk.Text(self.root)
        self.text_area.pack(expand=True, fill=tk.BOTH)
        
        # Tạo thanh cuộn
        self.scroll_bar = tk.Scrollbar(self.text_area)
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.text_area.yview)
        
        # Tạo thanh menu
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        # Menu Tệp
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)  # Tạo tệp mới
        self.file_menu.add_command(label="Open", command=self.open_file)  # Mở tệp
        self.file_menu.add_command(label="Save", command=self.save_file)  # Lưu tệp
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit_application)  # Thoát ứng dụng
        
        # Menu Chỉnh sửa
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut)  # Cắt
        self.edit_menu.add_command(label="Copy", command=self.copy)  # Sao chép
        self.edit_menu.add_command(label="Paste", command=self.paste)  # Dán
        
        # Menu Trợ giúp
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About Notepad", command=self.show_about)  # Giới thiệu về Notepad
    
    def new_file(self):
        self.root.title("Untitled - Notepad")
        self.text_area.delete(1.0, tk.END)  # Xóa nội dung văn bản hiện tại
    
    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())  # Đọc và hiển thị nội dung tệp
            self.root.title(f'{file_path} - Notepad')
    
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))  # Lưu nội dung văn bản hiện tại vào tệp
            self.root.title(f'{file_path} - Notepad')
    
    def quit_application(self):
        self.root.destroy()  # Đóng ứng dụng
    
    def show_about(self):
        messagebox.showinfo("Notepad", "Original Version")  # Hiển thị thông tin về Notepad
    
    def cut(self):
        self.text_area.event_generate("<<Cut>>")  # Thực hiện thao tác cắt
    
    def copy(self):
        self.text_area.event_generate("<<Copy>>")  # Thực hiện thao tác sao chép
    
    def paste(self):
        self.text_area.event_generate("<<Paste>>")  # Thực hiện thao tác dán
    
    def run(self):
        self.root.mainloop()  # Bắt đầu vòng lặp chính của ứng dụng

if __name__ == "__main__":
    notepad = Notepad(width=600, height=400)  # Tạo đối tượng Notepad với kích thước cửa sổ 600x400
    notepad.run()  # Chạy ứng dụng
