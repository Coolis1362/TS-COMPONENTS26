import os
import subprocess
import sys

def run_script(filename):
    """Runs a Python script."""
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        return

    print(f"Running script: {filename}")
    try:
        result = subprocess.run(["python", filename], capture_output=True, text=True)
        print("Output:\n", result.stdout)
        if result.stderr:
            print("Errors:\n", result.stderr)
    except Exception as e:
        print(f"Error running script: {e}")

def console_menu():
    """Menu for the Python console."""
    print("\n--- TS-PYTHON Console ---")
    while True:
        print("\nOptions:")
        print("1. Run a Python File")
        print("2. Exit Console")

        choice = input("Select an option (1-2): ")
        if choice == "1":
            filename = input("Enter the filename (e.g., script.py): ")
            run_script(filename)
        elif choice == "2":
            print("Exiting Console.")
            os.system("taskkill /F /IM cmd.exe")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    console_menu()
