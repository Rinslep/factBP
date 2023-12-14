import numpy as np
import tkinter as tk

# Define grid size and cell size
n = 10  # Default grid size
cell_size = 20  # Default cell size

# Create a NumPy array to store the grid colors
grid_colors = np.full((n, n), "gray")

def toggle_color(event):
    x, y = event.x, event.y
    col, row = x // cell_size, y // cell_size

    if selected_color is not None:
        grid_colors[row, col] = selected_color
        update_buffer()

def select_color(color):
    global selected_color
    selected_color = color


def start_drag(event):
    global is_drawing
    is_drawing = True

def end_drag(event):
    global is_drawing
    is_drawing = False

def drag_color(event):
    if is_drawing:
        x, y = int(event.x), int(event.y)
        if 0 <= x < canvas_width and 0 <= y < canvas_height:
            toggle_color(event)

def click_color(event):
    x, y = event.x, event.y
    col, row = x // cell_size, y // cell_size
    toggle_color(event)

def open_dimensions_window():
    dimensions_window.deiconify()

def update_grid():
    global canvas_width, canvas_height, cell_size

    n = int(grid_size_entry.get())
    new_cell_size = int(cell_size_entry.get())

    cell_size = new_cell_size
    canvas_width = n * cell_size
    canvas_height = n * cell_size

    canvas.config(scrollregion=(0, 0, canvas_width, canvas_height))
    reposition_buttons()  # Update button positions

    grid_colors.fill("gray")  # Reset grid to gray cells

    # Update dimensions and window geometry
    update_dimensions_labels()
    update_buffer()

def reposition_buttons():
    for button in color_buttons:
        button.destroy()

    button_colors = {
        'darkslategray': '#2f4f4f', 'brown': '#a52a2a',
        'darkgreen': '#006400', 'darkkhaki': '#bdb76b',
        'indigo': '#4b0082', 'red': '#ff0000',
        'orange': '#ffa500', 'yellow': '#ffff00',
        'lime': '#00ff00', 'mediumspringgreen': '#00fa9a',
        'aqua': '#00ffff', 'blue': '#0000ff',
        'fuchsia': '#ff00ff', 'dodgerblue': '#1e90ff',
        'deeppink': '#ff1493', 'lightpink': '#ffb6c1'
    }

    for i, (color_name, color_code) in enumerate(button_colors.items()):
        button = tk.Button(left_frame, text=color_name, bg=color_code, width=10, height=1, command=lambda c=color_code: select_color(c))
        button.grid(row=i, column=0, sticky="w")


# Function to determine complementary color
def complementary_color_name(color):
    r, g, b = root.winfo_rgb(color)
    r, g, b = 65535 - r, 65535 - g, 65535 - b
    return "#{:04x}{:04x}{:04x}".format(r, g, b)


def update_dimensions_labels():
    # Update dimensions labels in the second window
    main_window_dimensions_label.config(text=f"Main Window: {root.winfo_width()}x{root.winfo_height()}")
    left_frame_dimensions_label.config(text=f"Left Frame: {left_frame.winfo_width()}x{left_frame.winfo_height()}")
    middle_frame_dimensions_label.config(text=f"Middle Frame: {middle_frame.winfo_width()}x{middle_frame.winfo_height()}")
    settings_frame_dimensions_label.config(text=f"Settings Frame: {settings_frame.winfo_width()}x{settings_frame.winfo_height()}")


def update_buffer():
    buffer.delete("all")  # Clear the buffer
    for row in range(n):
        for col in range(n):
            color = grid_colors[row, col]
            buffer.create_rectangle(
                col * cell_size, row * cell_size,
                (col + 1) * cell_size, (row + 1) * cell_size,
                fill=color, outline="black"
            )
    canvas.update()
    canvas.create_image(0, 0, anchor="nw", image=buffer_data)

# Create the main application window
root = tk.Tk()
root.title("Resizable Grid")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Define a maximum window size (90% of the screen size)
max_width = int(screen_width * 0.9)
max_height = int(screen_height * 0.9)
root.maxsize(max_width, max_height)

# Create a frame for the left column (buttons) with a border
left_frame = tk.Frame(root, relief="solid", borderwidth=2)
left_frame.grid(row=0, column=0, sticky="n")

canvas_width = n * cell_size
canvas_height = n * cell_size

# Create a frame for the middle column (grid) with a border
middle_frame = tk.Frame(root, relief="solid", borderwidth=2)
middle_frame.grid(row=0, column=1, sticky="n")

canvas = tk.Canvas(middle_frame, width=canvas_width, height=canvas_height, scrollregion=(0, 0, canvas_width, canvas_height))
canvas.pack()

# Create an off-screen buffer for double buffering
buffer_data = tk.PhotoImage(width=canvas_width, height=canvas_height)
buffer = tk.Canvas(buffer_data, width=canvas_width, height=canvas_height)

# Create a frame for the right column (settings) with a border
settings_frame = tk.Frame(root, relief="solid", borderwidth=2)
settings_frame.grid(row=0, column=2, sticky="n")

grid_size_label = tk.Label(settings_frame, text="Grid Size:")
grid_size_label.grid(row=0, column=0)
grid_size_entry = tk.Entry(settings_frame)
grid_size_entry.insert(0, str(n))
grid_size_entry.grid(row=0, column=1)

cell_size_label = tk.Label(settings_frame, text="Cell Size:")
cell_size_label.grid(row=1, column=0)
cell_size_entry = tk.Entry(settings_frame)
cell_size_entry.insert(0, str(cell_size))
cell_size_entry.grid(row=1, column=1)

update_button = tk.Button(settings_frame, text="Update Grid", command=update_grid)
update_button.grid(row=2, column=0, columnspan=2)

color_buttons = []

reposition_buttons()  # Position the buttons initially

# Create a second window to display dimensions
dimensions_window = tk.Toplevel(root)
dimensions_window.title("Window Dimensions")
dimensions_window.withdraw()  # Hide the dimensions window initially

main_window_dimensions_label = tk.Label(dimensions_window, text="Main Window: N/A")
main_window_dimensions_label.grid(row=0, column=0, sticky="w")

left_frame_dimensions_label = tk.Label(dimensions_window, text="Left Frame: N/A")
left_frame_dimensions_label.grid(row=1, column=0, sticky="w")

middle_frame_dimensions_label = tk.Label(dimensions_window, text="Middle Frame: N/A")
middle_frame_dimensions_label.grid(row=2, column=0, sticky="w")

settings_frame_dimensions_label = tk.Label(dimensions_window, text="Settings Frame: N/A")
settings_frame_dimensions_label.grid(row=3, column=0, sticky="w")

# Create a button in the settings frame to open the dimensions window
open_dimensions_button = tk.Button(settings_frame, text="Open Dimensions", command=open_dimensions_window)
open_dimensions_button.grid(row=3, column=0, columnspan=2)

# Calculate initial dimensions for the window
root.update_idletasks()
left_frame_width = left_frame.winfo_reqwidth()
middle_frame_width = middle_frame.winfo_reqwidth()
settings_frame_width = settings_frame.winfo_reqwidth()
max_frame_height = max(left_frame.winfo_reqheight(), middle_frame.winfo_reqheight(), settings_frame.winfo_reqheight())
root.geometry(f"{left_frame_width + middle_frame_width + settings_frame_width}x{max_frame_height}")

# Update dimensions labels
update_dimensions_labels()

# Initialize selected color and drawing flag
selected_color = None
is_drawing = False

# Bind mouse events to canvas
canvas.bind('<Button-1>', toggle_color)
canvas.bind('<ButtonPress-1>', start_drag)
canvas.bind('<ButtonRelease-1>', end_drag)
canvas.bind('<B1-Motion>', drag_color)
canvas.bind('<ButtonRelease-1>', click_color)

# Start the main loop
root.mainloop()
