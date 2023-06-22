class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteTakingApp:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)
        print("Note added successfully!")

    def view_notes(self):
        if self.notes:
            for index, note in enumerate(self.notes):
                print(f"Note {index+1}:")
                print(f"Title: {note.title}")
                print(f"Content: {note.content}")
                print("------------------------")
        else:
            print("No notes found!")

    def delete_note(self, note_index):
        if note_index < len(self.notes):
            del self.notes[note_index]
            print("Note deleted successfully!")
        else:
            print("Invalid note index!")

# Create an instance of the NoteTakingApp class
app = NoteTakingApp()

while True:
    print("Note-taking App")
    print("1. Add a Note")
    print("2. View Notes")
    print("3. Delete a Note")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        app.add_note(title, content)
    elif choice == "2":
        app.view_notes()
    elif choice == "3":
        note_index = int(input("Enter the index of the note to delete: "))
        app.delete_note(note_index - 1)
    elif choice == "4":
        print("Thank you for using the Note-taking App!")
        break
    else:
        print("Invalid choice. Please try again.")
