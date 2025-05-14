import os
import sys

def create_or_edit_file(filename):
    """Creates a new Python file or edits an existing one."""
    mode = "w" if not os.path.exists(filename) else "a"
    print(f"{'Creating' if mode == 'w' else 'Editing'} file: {filename}")
    print("File Made! or Now Editiing file!")
    print("Type 'EOF' on a new line to save and exit. \n type Your Python Code Below: ")
    
    with open(filename, mode) as file:
        while True:
            line = input()
            if line.strip().upper() == "EOF":
                break
            file.write(line + "\n")

    print(f"File '{filename}' saved successfully!")

def list_files():
    """Lists all Python files in the current directory."""
    print("Available Python files:")
    for file in os.listdir():
        if file.endswith(".py"):
            print(f" - {file}")

def editor_menu():
    """Menu for the Python editor."""
    print("\n--- TS-PYTHON Editor ---")
    while True:
        print("\nOptions:")
        print("1. Create or Edit a Python File")
        print("2. List Python Files")
        print("3. Exit Editor")

        choice = input("Select an option (1-3): ")
        if choice == "1":
            filename = input("Enter the filename (e.g., script.py): ")
            create_or_edit_file(filename)
        elif choice == "2":
            list_files()
        elif choice == "3":
            print("Exiting Editor.")
            os.system("taskkill /F /IM cmd.exe")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    editor_menu()
