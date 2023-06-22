import tkinter as tk
from tkinter import ttk, messagebox
import json
from ttkbootstrap import Style

#Create the Notebook window.
root=tk.Tk()
root.title("Notes App")
root.geometry("500x500")
style=Style(theme='journal')
style=ttk.Style()

style.configure("TNotebook.Tab",font=("TkDefaultFont", 14, "bold"))

#Create a Notebook

notebook=ttk.Notebook(root,style="TNotebook")

#Lode Saved Notes

notes={}
try:
    with open("notes.json","r") as f:
        notes=json.load(f)
except FileNotFoundError:
    pass

#Create nootes to hold notes
notebook=ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

#Function to add notes
def Add_Note():
    note_frame=ttk.Frame(notebook,padding=10)
    notebook.add(note_frame,text="New Note")

    title_lable=ttk.Label(note_frame,text="Title:")
    title_lable.grid(row=0, column=0, padx=10, pady=10, sticky="W")

    title_entry=ttk.Entry(note_frame,width=40)
    title_entry.grid(row=0, column=1, padx=10, pady=10)

    content_lable=ttk.Label(note_frame,text="Content:")
    content_lable.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    content_entry=tk.Text(note_frame,width=40, height=10)
    content_entry.grid(row=1, column=1, padx=10,pady=10)

    #Function to save note
    def Save_Note():
        title=title_entry.get()
        content=content_entry.get("1.0",tk.END)

        #add note to dictionary
        notes[title]=content.strip()
        with open("notes.json","w") as f:
            json.dump(notes,f)

        note_content=tk.Text(notebook, width=40,height=10)
        note_content.insert(tk.END, content)
        notebook.forget(notebook.select())
        notebook.add(note_content, text=title)

    save_button=ttk.Button(note_frame,text="Save", 
                           command=Save_Note, style="secondary.TButton")
    save_button.grid(row=2, column=1, padx=10, pady=10) 

def load_notes():
    try:
        with open("notes.json", "r") as f:
            notes = json.load(f)

        for title, content in notes.items():
            # Add the note to the notebook
            note_content = tk.Text(notebook, width=40, height=10)
            note_content.insert(tk.END, content)
            notebook.add(note_content, text=title)

    except FileNotFoundError:
        # If the file does not exist, do nothing
        pass

load_notes()

def delete_Notes():
    current_tab=notebook.index(notebook.select())
    note_title=notebook.tab(current_tab,"text")
    confirm=messagebox.askyesno("Delete Note",f"Are You Sure You want to Delete {note_title}?")

    if confirm:
        notebook.forget(current_tab)

        notes.pop(note_title)

        with open("notes.json","w") as f:
            json.dump(notes,f)

new_button=ttk.Button(root,text="New Note", command=Add_Note, style="info.TButton")
new_button.pack(side=tk.LEFT,padx=10,pady=10)

delete_Button=ttk.Button(root,text="Delete",command=delete_Notes, style="primary.TButton")
delete_Button.pack(side=tk.LEFT,padx=10,pady=10)

root.mainloop()
