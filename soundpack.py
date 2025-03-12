import os
import shutil
import json
import tkinter as tk
import webbrowser
import subprocess
from tkinter import filedialog, messagebox, simpledialog

# Set up directories and config file
TEMP_DIR = os.path.join(os.path.expanduser("~"), "GTA_SoundPacks_Temp")
BACKUP_DIR = os.path.join(TEMP_DIR, "backup")
CONFIG_FILE = os.path.join(TEMP_DIR, "soundpacks.json")

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(BACKUP_DIR, exist_ok=True)

# Possible GTA Install Locations
POSSIBLE_GTA_PATHS = [
    os.path.join(drive, "SteamLibrary", "steamapps", "common", "Grand Theft Auto V", "x64", "audio", "sfx")
    for drive in ["C:\\", "D:\\", "G:\\"]
] + [
    os.path.join(drive, "Program Files (x86)", "Steam", "steamapps", "common", "Grand Theft Auto V", "x64", "audio", "sfx")
    for drive in ["C:\\", "D:\\", "G:\\"]
] + [
    os.path.join(drive, "Program Files", "Rockstar Games", "Grand Theft Auto V", "x64", "audio", "sfx")
    for drive in ["C:\\", "D:\\", "G:\\"]
] + [
    os.path.join(drive, "Program Files", "Epic Games", "GTAV", "x64", "audio", "sfx")
    for drive in ["C:\\", "D:\\", "G:\\"]
]

# Load saved settings (GTA folder + sound packs)
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"gta_folder": "", "sound_packs": {}}

# Save settings (GTA folder + sound packs)
def save_config():
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

config = load_config()

def find_gta_sfx_folder():
    """Find the GTA SFX folder from saved config or auto-detect."""
    if config["gta_folder"] and os.path.exists(config["gta_folder"]):
        return config["gta_folder"]

    for path in POSSIBLE_GTA_PATHS:
        if os.path.exists(path):
            messagebox.showinfo("Success", f"GTA SFX folder found: {path}")
            config["gta_folder"] = path
            save_config()
            return path

    messagebox.showerror("Error", "Unable to identify GTA SFX directory. Please select your SFX folder manually.")
    return ""

def select_gta_folder():
    """Let users manually set their GTA SFX folder and save it."""
    gta_folder = filedialog.askdirectory(title="Select GTA SFX Folder")
    if gta_folder:
        config["gta_folder"] = gta_folder
        save_config()
        gta_folder_var.set(gta_folder)

def backup_originals():
    """Backup the original GTA sound files."""
    gta_folder = config["gta_folder"]
    if not gta_folder:
        messagebox.showerror("Error", "Please select your GTA SFX folder first.")
        return

    resident_path = os.path.join(gta_folder, "resident.rpf")
    weapons_path = os.path.join(gta_folder, "weapons_player.rpf")

    if not os.path.exists(resident_path) or not os.path.exists(weapons_path):
        messagebox.showerror("Error", "Original files not found in the selected GTA SFX folder.")
        return

    shutil.copy(resident_path, os.path.join(BACKUP_DIR, "resident.rpf"))
    shutil.copy(weapons_path, os.path.join(BACKUP_DIR, "weapons_player.rpf"))
    messagebox.showinfo("Success", "Original files backed up successfully!")

def add_sound_pack():
    """Allow users to save multiple sound packs."""
    sound_pack_folder = filedialog.askdirectory(title="Select a Sound Pack Folder")
    if not sound_pack_folder:
        return

    pack_name = simpledialog.askstring("Save Sound Pack", "Enter a name for this sound pack:")
    if not pack_name:
        return

    config["sound_packs"][pack_name] = sound_pack_folder
    save_config()
    update_dropdown()
    messagebox.showinfo("Success", f"Sound pack '{pack_name}' saved!")

def apply_sound_pack():
    """Apply the selected sound pack from the dropdown menu."""
    gta_folder = config["gta_folder"]
    if not gta_folder:
        messagebox.showerror("Error", "Please select your GTA SFX folder first.")
        return

    selected_pack = sound_pack_var.get()
    if not selected_pack or selected_pack not in config["sound_packs"]:
        messagebox.showerror("Error", "Please select a valid sound pack.")
        return

    sound_pack_folder = config["sound_packs"][selected_pack]
    resident_pack = os.path.join(sound_pack_folder, "resident.rpf")
    weapons_pack = os.path.join(sound_pack_folder, "weapons_player.rpf")

    if not os.path.exists(resident_pack) or not os.path.exists(weapons_pack):
        messagebox.showerror("Error", "Selected sound pack is missing required files.")
        return

    shutil.copy(resident_pack, os.path.join(gta_folder, "resident.rpf"))
    shutil.copy(weapons_pack, os.path.join(gta_folder, "weapons_player.rpf"))
    messagebox.showinfo("Success", f"Sound pack '{selected_pack}' applied!")

def restore_original():
    """Restore the original GTA sound files."""
    gta_folder = config["gta_folder"]
    if not gta_folder:
        messagebox.showerror("Error", "Please select your GTA SFX folder first.")
        return

    resident_backup = os.path.join(BACKUP_DIR, "resident.rpf")
    weapons_backup = os.path.join(BACKUP_DIR, "weapons_player.rpf")

    if not os.path.exists(resident_backup) or not os.path.exists(weapons_backup):
        messagebox.showerror("Error", "No backup found. Backup your files first!")
        return

    shutil.copy(resident_backup, os.path.join(gta_folder, "resident.rpf"))
    shutil.copy(weapons_backup, os.path.join(gta_folder, "weapons_player.rpf"))
    messagebox.showinfo("Success", "Original files restored successfully!")

def update_dropdown():
    """Update the dropdown menu with saved sound packs."""
    sound_pack_dropdown["menu"].delete(0, "end")
    for name in config["sound_packs"].keys():
        sound_pack_dropdown["menu"].add_command(label=name, command=tk._setit(sound_pack_var, name))

def open_backup_folder():
    """Open the backup folder in File Explorer."""
    if not os.path.exists(BACKUP_DIR):
        messagebox.showerror("Error", "Backup folder does not exist.")
        return
    subprocess.Popen(f'explorer "{BACKUP_DIR}"')

def download_original():
    """Open the download link for the original files."""
    webbrowser.open("https://www.mediafire.com/file/afx2wcmd01bwpmc/original.rar/file")

# GUI Setup
root = tk.Tk()
root.title("GTA Sound Swapper - Chipy")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="GTA SFX Folder:").grid(row=0, column=0, sticky="w")
gta_folder_var = tk.StringVar()
gta_folder_var.set(find_gta_sfx_folder())
tk.Entry(frame, textvariable=gta_folder_var, width=50).grid(row=0, column=1, columnspan=2, pady=5)
tk.Button(frame, text="Browse", command=select_gta_folder).grid(row=0, column=3, padx=5)

tk.Button(frame, text="Restore Original", command=restore_original, width=20).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="Backup Original", command=backup_originals, width=20).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame, text="Download Original", command=download_original, width=20).grid(row=1, column=2, padx=5, pady=5)

sound_pack_var = tk.StringVar(root)
sound_pack_var.set("Select a Sound Pack")
if config["sound_packs"]:
    sound_pack_dropdown = tk.OptionMenu(frame, sound_pack_var, *config["sound_packs"].keys())
else:
    sound_pack_dropdown = tk.OptionMenu(frame, sound_pack_var, "No sound packs saved yet")
sound_pack_dropdown.grid(row=2, column=0, padx=5, pady=5)
tk.Button(frame, text="Apply Sound Pack", command=apply_sound_pack, width=20).grid(row=2, column=1, padx=5, pady=5)
tk.Button(frame, text="Add New Sound Pack", command=add_sound_pack, width=20).grid(row=2, column=2, padx=5, pady=5)


root.mainloop()
