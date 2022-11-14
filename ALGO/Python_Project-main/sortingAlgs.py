from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from bubblesort import BubbleSort
from quicksort import QuickSort
from mergesort import MergeSort
from linearsearch import LinearSearch
from binarysearch import BinarySearch

root = Tk()
root.title('PYTHON PROJECT')
root.maxsize(900, 600)
root.config(bg='black')

# variables
selected_alg = StringVar()
data = []
speed = 0.7


# function
def draw_data(data, color_array, popup):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalized_data = [i / max(data) for i in data]
    for i, height in enumerate(normalized_data):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))
    
    if popup == 1:
        messagebox.showinfo("MESSAGE", "Number Not Found In Data")
    elif popup == 2:
        messagebox.showinfo("MESSAGE", "Number Found In Data")
    root.update_idletasks()


def generate():
    global data
    data = arrayEntry.get()
    data = [int(n.strip()) for n in data.split(' ')]
    size = len(data)

    draw_data(data, ['red' for _ in range(size)],0)  # ['red', 'red' ,....]


def start_algorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        qs = QuickSort(data)
        qs.quick_sort(data, 0, len(data) - 1, draw_data, speed)
        draw_data(data, ['green' for _ in range(len(data))],0)

    elif algMenu.get() == 'Bubble Sort':
        bs = BubbleSort(data)
        bs.bubble_sort(draw_data, speed)
        draw_data(data, ['green' for _ in range(len(data))],0)

    elif algMenu.get() == 'Merge Sort':
        ms = MergeSort(data)
        ms.merge_sort(draw_data, speed)
        draw_data(data, ['green' for _ in range(len(data))],0)

    elif algMenu.get() == 'Linear Search':
        search = searchEntry.get()
        ls = LinearSearch(data, search)
        ls.linear_search(draw_data, speed)

    elif algMenu.get() == 'Binary Search':
        search = searchEntry.get()
        bs = BinarySearch(data, search)
        bs.binary_search(draw_data, speed)


# frame / base layout
ui_frame = Frame(root, width=600, height=200, bg='grey')
ui_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# User Interface Area
# Row[0]
Label(ui_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(ui_frame, textvariable=selected_alg, values=['Bubble Sort', 'Quick Sort', 'Merge Sort', 'Linear Search', 'Binary Search'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

Button(ui_frame, text="Start", command=start_algorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

Label(ui_frame, text="List of Numbers ", bg='grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)
arrayEntry = Entry(ui_frame)
arrayEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(ui_frame, text="Search for ", bg='grey').grid(row=2, column=0, padx=5, pady=5, sticky=W)
searchEntry = Entry(ui_frame)
searchEntry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

Button(ui_frame, text="Generate", command=generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
