# Author: Kevon Nelson
# Version: 1.0.0
# Date: March 2024
# Purpose: Randon NPC generator for Dungeons and Dragons

import tkinter as tk
from random import choice
from npc_functions import * # generator functions

# constants
WINDOW_TITLE = "D&D NPC Generator"
WINDOW_SIZE = '600x400+50+50'
FRAME_PADDING = 20
FIELD_HEIGHT = 1
FIELD_WIDTH = 40

# NPC attributes
NPC_FIELDS = [
    ("Name", generateName),
    ("Race", generateRace),
    ("Gender", generateGender),
    ("Personality", generatePersonality),
    ("Background", generateBackground),
    ("Relationship Status", generateRelationStatus),
    ("Orientation", generateOrientation),
    ("Age Group", generateAge)
]


# establish display field
def displayField(frame, label_text, generator_function, row):
    result = generator_function()
    text = tk.Text(master=frame, height=FIELD_HEIGHT, width=FIELD_WIDTH)
    text.grid(column=1, row=row, pady=2)
    text.insert(tk.END, result)
    text.config(state=tk.DISABLED) # make field read-only
    tk.Label(frame, text=label_text, justify=tk.RIGHT).grid(column=0, row=row, padx=5)


# template for generate buttons
def create_generateButton(input_frame, display_frame, label_text, generator_function, row):
    tk.Label(input_frame, text=label_text).grid(column=0, row=row, padx=5, sticky=tk.E)
    tk.Button(
        input_frame, 
        text="Generate", 
        command=lambda r=row: displayField(display_frame, label_text, generator_function, r)
        ).grid(column=1, row=row, padx=5)


def display_all_fields(display_frame):
    for row, (label, generator_function) in enumerate(NPC_FIELDS, start=0):
        displayField(display_frame, label, generator_function, row)

def setFrames(root):
    # display frame
    display_frame = tk.Frame(root, width=300, height=400, borderwidth=2, relief="solid")
    display_frame.grid(column=0, row=0, padx=FRAME_PADDING, pady=FRAME_PADDING)

    # input frame
    input_frame = tk.Frame(root, width=300, height=400, borderwidth=2, relief="solid")
    input_frame.grid(column=1, row=0, padx=FRAME_PADDING, pady=FRAME_PADDING)

    # generate buttons
    for row, (label, generator_function) in enumerate(NPC_FIELDS):
        create_generateButton(input_frame, display_frame, label, generator_function, row)

    # generate all button
    tk.Button(
        input_frame,
        text="Generate All",
        command=lambda: display_all_fields(display_frame)
    ).grid(column=0, row=len(NPC_FIELDS) + 1, columnspan=2, pady=10)

    return input_frame, display_frame

def main():
    root = tk.Tk()
    root.geometry(WINDOW_SIZE)
    root.title(WINDOW_TITLE)

    setFrames(root)
    root.mainloop()

if __name__ == "__main__":
    main()