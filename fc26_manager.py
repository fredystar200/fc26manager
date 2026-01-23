import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import subprocess
from pathlib import Path

class FC26Installer:
    def __init__(self, root):
        self.root = root
        self.root.title("FC26 Not a Crack Installer")
        self.root.geometry("600x500")
        self.root.configure(bg="#1e1b4b")
        
        self.crack_folder = tk.StringVar()
        self.fc26_folder = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title = tk.Label(
            self.root, 
            text="FC26 Not a Crack Installer",
            font=("Arial", 20, "bold"),
            bg="#1e1b4b",
            fg="white"
        )
        title.pack(pady=20)
        
        # Subtitle
        subtitle = tk.Label(
            self.root,
            text="Manage your FC26 installation",
            font=("Arial", 10),
            bg="#1e1b4b",
            fg="#c4b5fd"
        )
        subtitle.pack(pady=(0, 20))
        
        # Crack folder selection
        crack_frame = tk.Frame(self.root, bg="#1e1b4b")
        crack_frame.pack(pady=10, padx=20, fill="x")
        
        tk.Label(
            crack_frame,
            text="Not a Crack Folder:",
            bg="#1e1b4b",
            fg="#c4b5fd",
            font=("Arial", 10)
        ).pack(anchor="w")
        
        crack_input_frame = tk.Frame(crack_frame, bg="#1e1b4b")
        crack_input_frame.pack(fill="x", pady=5)
        
        tk.Entry(
            crack_input_frame,
            textvariable=self.crack_folder,
            font=("Arial", 10),
            bg="#334155",
            fg="white",
            insertbackground="white"
        ).pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        tk.Button(
            crack_input_frame,
            text="Browse",
            command=self.select_crack_folder,
            bg="#7c3aed",
            fg="white",
            font=("Arial", 9),
            cursor="hand2"
        ).pack(side="right")
        
        # FC26 folder selection
        fc26_frame = tk.Frame(self.root, bg="#1e1b4b")
        fc26_frame.pack(pady=10, padx=20, fill="x")
        
        tk.Label(
            fc26_frame,
            text="FC26 Folder:",
            bg="#1e1b4b",
            fg="#c4b5fd",
            font=("Arial", 10)
        ).pack(anchor="w")
        
        fc26_input_frame = tk.Frame(fc26_frame, bg="#1e1b4b")
        fc26_input_frame.pack(fill="x", pady=5)
        
        tk.Entry(
            fc26_input_frame,
            textvariable=self.fc26_folder,
            font=("Arial", 10),
            bg="#334155",
            fg="white",
            insertbackground="white"
        ).pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        tk.Button(
            fc26_input_frame,
            text="Browse",
            command=self.select_fc26_folder,
            bg="#7c3aed",
            fg="white",
            font=("Arial", 9),
            cursor="hand2"
        ).pack(side="right")
        
        # Action buttons
        buttons_frame = tk.Frame(self.root, bg="#1e1b4b")
        buttons_frame.pack(pady=20, padx=20, fill="x")
        
        tk.Button(
            buttons_frame,
            text="Install Not a Crack",
            command=self.install_crack,
            bg="#059669",
            fg="white",
            font=("Arial", 11, "bold"),
            height=2,
            cursor="hand2"
        ).pack(fill="x", pady=5)
        
        tk.Button(
            buttons_frame,
            text="Uninstall Not a Crack",
            command=self.uninstall_crack,
            bg="#dc2626",
            fg="white",
            font=("Arial", 11, "bold"),
            height=2,
            cursor="hand2"
        ).pack(fill="x", pady=5)
        
        tk.Button(
            buttons_frame,
            text="Launch EDTD.exe",
            command=self.launch_edtd,
            bg="#2563eb",
            fg="white",
            font=("Arial", 11, "bold"),
            height=2,
            cursor="hand2"
        ).pack(fill="x", pady=5)
    
    def select_crack_folder(self):
        folder = filedialog.askdirectory(title="Select Not a Crack Folder")
        if folder:
            self.crack_folder.set(folder)
    
    def select_fc26_folder(self):
        folder = filedialog.askdirectory(title="Select FC26 Folder")
        if folder:
            self.fc26_folder.set(folder)
    
    def install_crack(self):
        crack_dir = self.crack_folder.get()
        fc26_dir = self.fc26_folder.get()
        
        if not crack_dir or not fc26_dir:
            messagebox.showerror("Error", "Please select both folders first")
            return
        
        try:
            # Folders to copy
            folders_to_copy = ['FAKE', '_FMM']
            
            # Files to copy
            files_to_copy = [
                'anadius.cfg',
                'anadius64.dll',
                'EAAntiCheat.GameServiceLauncher.exe',
                'FC26Plugin.Launcher.FMT.Javelin.dll'
            ]
            
            # Copy folders
            for folder in folders_to_copy:
                src = os.path.join(crack_dir, folder)
                dst = os.path.join(fc26_dir, folder)
                if os.path.exists(src):
                    if os.path.exists(dst):
                        shutil.rmtree(dst)
                    shutil.copytree(src, dst)
            
            # Copy regular files
            for file in files_to_copy:
                src = os.path.join(crack_dir, file)
                dst = os.path.join(fc26_dir, file)
                if os.path.exists(src):
                    shutil.copy2(src, dst)
            
            # Handle FC26_Showcase.exe rename and copy
            original_exe = os.path.join(fc26_dir, 'FC26_Showcase.exe')
            backup_exe = os.path.join(fc26_dir, 'FC26_Showcase_org.exe')
            
            # Backup original exe if not already backed up
            if os.path.exists(original_exe) and not os.path.exists(backup_exe):
                os.rename(original_exe, backup_exe)
            
            # Copy and rename FC26_Showcase fixed.exe
            fixed_exe_src = os.path.join(crack_dir, 'FC26_Showcase fixed.exe')
            if os.path.exists(fixed_exe_src):
                shutil.copy2(fixed_exe_src, original_exe)
            
            messagebox.showinfo("Success", "Not a crack installed successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Installation failed: {str(e)}")
    
    def uninstall_crack(self):
        fc26_dir = self.fc26_folder.get()
        
        if not fc26_dir:
            messagebox.showerror("Error", "Please select FC26 folder first")
            return
        
        try:
            folders_to_delete = ['FAKE', '_FMM']
            files_to_delete = [
                'anadius.cfg',
                'anadius64.dll',
                'EAAntiCheat.GameServiceLauncher.exe',
                'FC26_Showcase.exe',
                'FC26Plugin.Launcher.FMT.Javelin.dll'
            ]
            
            # Delete folders
            for folder in folders_to_delete:
                folder_path = os.path.join(fc26_dir, folder)
                if os.path.exists(folder_path):
                    shutil.rmtree(folder_path)
            
            # Delete files
            for file in files_to_delete:
                file_path = os.path.join(fc26_dir, file)
                if os.path.exists(file_path):
                    os.remove(file_path)
            
            # Restore original exe
            backup_exe = os.path.join(fc26_dir, 'FC26_Showcase_org.exe')
            original_exe = os.path.join(fc26_dir, 'FC26_Showcase.exe')
            
            if os.path.exists(backup_exe):
                os.rename(backup_exe, original_exe)
            
            messagebox.showinfo("Success", "Not a crack uninstalled and original files restored!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Uninstallation failed: {str(e)}")
    
    def launch_edtd(self):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            edtd_path = os.path.join(script_dir, 'EDTD.exe')
            
            if os.path.exists(edtd_path):
                subprocess.Popen([edtd_path])
                messagebox.showinfo("Success", "EDTD.exe launched!")
            else:
                messagebox.showerror("Error", "EDTD.exe not found in script directory")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FC26Installer(root)
    root.mainloop()
