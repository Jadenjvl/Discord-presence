import tkinter as tk
from pypresence import Presence
import time

# Replace 'YOUR_CLIENT_ID' with your Discord application's client ID
client_id = '1275241701866213396'

def update_presence():
    activity_type = activity_type_var.get()
    state = state_entry.get() if state_entry.get() else "Available"  # Default state
    details = details_entry.get()
    large_image = large_image_entry.get()
    small_image = small_image_entry.get()
    button1_label = button1_label_entry.get()
    button1_url = button1_url_entry.get()
    button2_label = button2_label_entry.get()
    button2_url = button2_url_entry.get()
    party_size_current = int(party_size_current_entry.get()) if party_size_current_entry.get() else 0
    party_size_max = int(party_size_max_entry.get()) if party_size_max_entry.get() else 0

    buttons = []
    if button1_label and button1_url:
        buttons.append({"label": button1_label, "url": button1_url})
    if button2_label and button2_url:
        buttons.append({"label": button2_label, "url": button2_url})

    presence_data = {
        "state": state,
        "details": details,
        "large_image": large_image,
        "small_image": small_image,
        "buttons": buttons,
    }

    if party_size_current > 0 and party_size_max > 0:
        presence_data["party_size"] = [party_size_current, party_size_max]

    if activity_type == "Playing":
        RPC.update(**presence_data)
    elif activity_type == "Watching":
        presence_data["details"] = f"Watching {details}"
        RPC.update(**presence_data)
    elif activity_type == "Listening":
        presence_data["details"] = f"Listening to {details}"
        RPC.update(**presence_data)
    elif activity_type == "Streaming":
        presence_data["details"] = f"Streaming {details}"
        RPC.update(**presence_data)

def start_presence():
    global RPC
    RPC = Presence(client_id)
    RPC.connect()
    update_presence()

def close_presence():
    RPC.close()
    root.quit()

def update_fields():
    activity_type = activity_type_var.get()

    if activity_type == "Playing":
        state_entry.configure(state='normal')
        details_label.configure(text="Game Title:")
        party_frame.grid(row=8, column=0, columnspan=2)
        state_frame.grid(row=2, column=0, columnspan=2)
    else:
        state_entry.configure(state='disabled')
        party_frame.grid_remove()
        state_frame.grid_remove()
        if activity_type == "Watching":
            details_label.configure(text="Video/Stream Title:")
        elif activity_type == "Listening":
            details_label.configure(text="Music/Podcast Title:")
        elif activity_type == "Streaming":
            details_label.configure(text="Stream Title:")

# GUI Setup
root = tk.Tk()
root.title("Discord Rich Presence Customizer")

# Activity Type Selection
tk.Label(root, text="Activity Type:").grid(row=0, column=0)
activity_type_var = tk.StringVar(value="Playing")
activity_type_menu = tk.OptionMenu(root, activity_type_var, "Playing", "Watching", "Listening", "Streaming", command=lambda _: update_fields())
activity_type_menu.grid(row=0, column=1)

# State and Details
state_frame = tk.Frame(root)
state_frame.grid(row=2, column=0, columnspan=2)
tk.Label(state_frame, text="State:").grid(row=0, column=0)
state_entry = tk.Entry(state_frame)
state_entry.grid(row=0, column=1)

tk.Label(root, text="Details:").grid(row=3, column=0)
details_label = tk.Label(root, text="Game Title:")
details_label.grid(row=3, column=0)
details_entry = tk.Entry(root)
details_entry.grid(row=3, column=1)

# Images (required)
tk.Label(root, text="Large Image Key:").grid(row=4, column=0)
large_image_entry = tk.Entry(root)
large_image_entry.grid(row=4, column=1)

tk.Label(root, text="Small Image Key:").grid(row=5, column=0)
small_image_entry = tk.Entry(root)
small_image_entry.grid(row=5, column=1)

# Buttons
tk.Label(root, text="Button 1 Label:").grid(row=6, column=0)
button1_label_entry = tk.Entry(root)
button1_label_entry.grid(row=6, column=1)

tk.Label(root, text="Button 1 URL:").grid(row=7, column=0)
button1_url_entry = tk.Entry(root)
button1_url_entry.grid(row=7, column=1)

tk.Label(root, text="Button 2 Label:").grid(row=8, column=0)
button2_label_entry = tk.Entry(root)
button2_label_entry.grid(row=8, column=1)

tk.Label(root, text="Button 2 URL:").grid(row=9, column=0)
button2_url_entry = tk.Entry(root)
button2_url_entry.grid(row=9, column=1)

# Party Size
party_frame = tk.Frame(root)
party_frame.grid(row=10, column=0, columnspan=2)
tk.Label(party_frame, text="Party Size (Current):").grid(row=0, column=0)
party_size_current_entry = tk.Entry(party_frame)
party_size_current_entry.grid(row=0, column=1)

tk.Label(party_frame, text="Party Size (Max):").grid(row=1, column=0)
party_size_max_entry = tk.Entry(party_frame)
party_size_max_entry.grid(row=1, column=1)

# Buttons for actions
start_button = tk.Button(root, text="Start Rich Presence", command=start_presence)
start_button.grid(row=11, column=0, columnspan=2)

update_button = tk.Button(root, text="Update Rich Presence", command=update_presence)
update_button.grid(row=12, column=0, columnspan=2)

close_button = tk.Button(root, text="Close", command=close_presence)
close_button.grid(row=13, column=0, columnspan=2)

root.mainloop()
