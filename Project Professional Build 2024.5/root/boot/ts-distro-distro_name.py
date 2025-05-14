import time
import os
from ts_kernel_language.tskerlan import tskerlan
from shutdown_windows import shutdown_windows
import sys
from bootloader.BOOT.boot import boot
import bootloader.BOOT.boot
import datetime
from python.python import python
import webbrowser
from tkinter import messagebox

# Set epoch using UTC, since your system isn't detecting named time zones
epoch_start = datetime.datetime(2025, 4, 9, 0, 0, 0, tzinfo=datetime.timezone.utc)

# Function to get elapsed seconds
def get_seconds_since_epoch():
    now = datetime.datetime.now(datetime.timezone.utc)  # Use UTC to ensure compatibility
    elapsed_seconds = (now - epoch_start).total_seconds()
    return int(elapsed_seconds)

def fetch_today_news(repo_url):
    try:
       os.system("git clone " + repo_url)
    except Exception as e:
        print(f"Error occurred: {e}")

# Example Usage
repo_url = "https://github.com/Coolis1362/TS-NETWORK"

def check_for_gh():
    try:
        # Progress bar
        for step in range(100):
            print("#", end="", flush=True)
            time.sleep(0.05)

        # Check Git version
        exit_code = os.system("\ngh --version")
        if exit_code != 0:
            print("\nGitHub CLI is not installed or not found in PATH.")
            return False
        else:
            print("\nGitHub CLI is installed and accessible.")
            return True
    except Exception as e:
        print(f"Error occurred: {e}")

def check_for_git():
    try:
        # Progress bar
        for step in range(100):
            print("#", end="", flush=True)
            time.sleep(0.05)

        # Check Git version
        exit_code = os.system("\ngit --version")
        if exit_code != 0:
            print("\nGit is not installed or not found in PATH.")
            return False
        else:
            print("\nGit is installed and accessible.")
            return True
    except Exception as e:
        print(f"Error occurred: {e}")

def put_distro_name_here(): # Replace put_distro_name_here with the name of your distro
    MAIN_USER_NAME = "ADMIN_USER"
    DISTRO_NAME_PREFIX = "TS-DISTRO"
    DISTRO_NAME = "distro_name" # Replace distro_name with the name of your distro
    KERNEL_VERSION = "Project Professional Build 2024.5" 
    DISTRO_VERSION = "version name" # Replace This with Version name Of your Distor e.g TS-DISTRO MAIN >>1.0.1pa2<< (The >> and << Are Pointing to A Version Number As A Version number)
    GITHUB_RESPOS_URL = "https://github.com/Coolis1362/"
    TSCLI_VERSION = "1.0.1.1"
    current_folder = os.path.dirname(os.path.abspath(__file__))
    current_terminal_folder = os.getcwd()
    print(f"Welcome To {DISTRO_NAME_PREFIX} {DISTRO_NAME} KERNEL VERSION: {KERNEL_VERSION} DISTRO VERSION: {DISTRO_VERSION}!")
    time.sleep(2)
    print(f"This is Based on TS-KERNEL {KERNEL_VERSION}")
    time.sleep(2)
    print("Loading...")
    time.sleep(2)
    for step in range(100):
        print("#", end="", flush=True)
        time.sleep(0.05)
    
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(2)
    print("****************************************************************")
    print(f"*        WELCOME TO {DISTRO_NAME_PREFIX} {DISTRO_NAME}                      *") # The Spaces Depends On How Long The Distro Name
    print("*                        NO COPYRIGHT                          *")
    print("*             YOU CAN MAKE A DISTRO BASED ON IT!               *")
    print("*                  TYPE 'help' FOR COMMANDS                    *")
    print("****************************************************************")

    while True:
        os.chdir(current_folder)
        os.chdir("..")
        os.chdir("users")
        os.chdir(MAIN_USER_NAME)
        tsdistrocommand = input(f"{MAIN_USER_NAME}at{DISTRO_NAME}:in {os.getcwd()}"
                                "\n|"
                                "\n|"
                                "\n|"
                                "\n|"
                                "\n|"
                                "\n|"
                                "\n|"
                                "\n|----------------@ ")
        if tsdistrocommand == "help":
            print("Commands:")
            print("help - Show this help message")
            print("exit - Exit the console")
            print("clear - Clear the console")
            print("whoami - Show the current user")
            print("tskerlan - start The TS-KERNEL-LANAGUAGE Interpiler")
            print("tsdesktop - start TS-DESKTOP and end cmd.exe")
            print("switch user --USER - Switch to user USER")
            print("shutdown --host_os - Shutdown Windows")
            print("ts-package - starts ts-package")
            print("time - Tells The Time")
            print("admindo - If A Linux User Is Seeing this, It's the Same As sudo")
            print("ts-distro - Same As neofetch")
            print("tscli - Same As ts-distro But with tscli")
            print("python - Same As The python Command In Other Terminals And Shells")
            print("boot - Boot Again")
            print("msnetwork - Start The Microsoft Network")
            print("version - Show the version of the distro and kernel")
            print("git - Same As The git Command In Other Terminals And Shells")
            print("gh - Same As The gh Command In Other Terminals And Shells")
            print("ls - List files in the current directory")
            print("time --sys - Show The System Time")
            print("messagebox info - Show an info message box")
            print("messagebox error - Show an error message box")
            print("add your commands here") # Replace It With Your Comamnds and On

        elif tsdistrocommand == "exit":
            print("Exiting...")
            time.sleep(1)
            os.system("taskkill /F /IM cmd.exe")
            os._exit(0)

        elif tsdistrocommand == "clear":
            os.system("cls" if os.name == "nt" else "clear")

        elif tsdistrocommand == "whoami":
            print(f"Current user: {MAIN_USER_NAME}")

        elif tsdistrocommand == "tskerlan":
            try:
                tskerlan()
            except Exception as e:
              print(f"Error 305: An issue occurred while executing 'tskerlan': {e}")
        elif tsdistrocommand == "tsdesktop":
            try:
                os.chdir("C:\\Users\\<Username>\\<NestedFolder>\\Desktop\\TS-KERNEL VERSIONS\\1.x.x\\1.0.x\\TS-KERNEL 1.0.1\\Pre-alpha\\pa2\\root\\ts-desktop\\1.x.x\\1.0.x\\1.0.0\\")
                os.system("ts-desktop100")
                time.sleep(1)
                os.system("taskkill /F /IM cmd.exe")
                os._exit(0)
            except Exception as e:
                print(f"ERROR 758: ERROR FOUND ERROR: {e}")
        elif tsdistrocommand == "switch user --USER":
            MAIN_USER_NAME = "USER"
        
        elif tsdistrocommand == "shutdown --host_os":
            try:
                shutdown_windows()
            except Exception as e:
                print(f"ERROR CODE 575: {e}")
        elif tsdistrocommand == "ts-package":
            os.system("git clone https://github.com/Coolis1362/ts-package-OFFICAL-PACKAGE-MANAGER")
            os.chdir("ts-package-OFFICAL-PACKAGE-MANAGER\\ts-package\\main")
            os.system("ts-package.bat")
        elif tsdistrocommand == "distro":
            print(f"CURRENT DISTRO: {DISTRO_NAME}")
        elif tsdistrocommand == "time":
            print(datetime.datetime.now())
        elif tsdistrocommand == "admindo":
            while True:
                print("Starting admindo...")
                admindo_input = input("admindo>> ")
                if admindo_input == "package":
                 while True:
                     print("Welcome To The TS-KERNEL Store!")
                     admindo_package_input = input("admindo>> package ")
                     if admindo_package_input:
                         try:
                             if check_for_git():
                                 os.system(f"git clone {GITHUB_RESPOS_URL}/{admindo_package_input}")
                         except Exception as e:
                             print(f"Error: {e}")
                     elif admindo_package_input == "exit":
                         break
                elif admindo_input == "exit":
                    break
        elif tsdistrocommand == "ts-distro":
            print(f"djcdnjdjsnknckjnjcbdkd      Kernel Version: {KERNEL_VERSION}")
            print(f"djdjjdkmdkdnjdjbncidno       Distro: {DISTRO_NAME}")
            print(f"     jdjkidjdi                Distro Version: {DISTRO_VERSION}")
            print("     djdjjnfjd        ")
            print("     djdjjnfjd        ")
            print("     djdjjnfjd s-distro")
            print("     djdjjnfjd        ")
            print("     djdjjnfjd        ")
            print("     djdjjnfjd        ")
            print("     djdjjnfjd        ")
            print("     djdjjnfjd        ")
        
        elif tsdistrocommand == "tscli":
            print(f"\ndjcdnjdjsnknckjnjcbdkd      Kernel Version: {KERNEL_VERSION}")
            print("djdjjdkmdkdnjdjbncidno       Shell: tscli")
            print(f"     jdjkidjdi                Shell Version: {TSCLI_VERSION}")
            print("     djdjjnfjd        ")
            print("     djdjjnfjd        ")
            print("     djdjjnfjd scli")
            print("     djdjjnfjd        ")
            print("     djdjjnfjd        ")
            print("     djdjjnfjd        ")
            print("     djdjjnfjd        ")
            print("     djdjjnfjd        ")
        
        elif tsdistrocommand == "python":
            python()
        
        elif tsdistrocommand == "boot":
            print(f"BOOT: VERSION: {KERNEL_VERSION}")
            print("Booting Again...")
            time.sleep(1)
            try:
                os.system("ts-distro-distro_name.py")
            except:
                os.system("C:\\Users\\<Username>\\<NestedFolder>\\Documents\\GitHub\\TS-KERNEL-1.0.0\\1.x.x\\1.0.x\\TS-KERNEL 1.0.1\\Beta\\b2\\root\\boot\\ts-distro-distro_name.py")

        elif tsdistrocommand == "msnetwork":
            webbrowser.open("https:/msn.com")

        elif tsdistrocommand == "tsnetwork":
            fetch_today_news()
        
        elif tsdistrocommand == "version":
            print(f"TS-DISTRO {DISTRO_NAME} VERSION: {DISTRO_VERSION} KERNEL VERSION: {KERNEL_VERSION}")
        
        elif tsdistrocommand == "git":
            git_input = input("Enter the git command: ")
            if check_for_git():
                os.system(f"git {git_input}")
        
        elif tsdistrocommand == "gh":
            if check_for_gh():
                gh_input = input("Enter the gh command: ")
                os.system(f"gh {gh_input}")
        
        elif tsdistrocommand == "ls":
            print(f"IN {current_terminal_folder}:")
            print(os.system("dir" if os.name == "nt" else "ls"))

        elif tsdistrocommand == "time --sys":
            print(get_seconds_since_epoch())

        elif tsdistrocommand == "messagebox info":
            messagebox.showinfo("tscli", "Thank You for Using This Command To Test Out Info Message boxes!") 
        
        elif tsdistrocommand == "messagebox error":
            messagebox.showerror("tscli", "Thank You for Using This Command To Test Out Error Message boxes!")
        else:
            print(f"tscli: {tsdistrocommand}: Command Not Found In Code.")
            messagebox.showerror("tscli", f"tscli: {tsdistrocommand}: Command Not Found In Code.")



if __name__ == "__main__": # DON'T REMOVE THIS LINE
    if bootloader.BOOT.boot.bootos() == "1":
        KERNEL_VERSION = "Project Professional Build 2024.5"
        messagebox.showinfo("BOOTOS", f"This Will Boot {KERNEL_VERSION}")
        if boot():
            messagebox.showinfo("tscli", f"tscli And {KERNEL_VERSION} Will Boot Now")
            os.system("cls")
            put_distro_name_here() # REPLACE THIS LINE WITH THE NAME OF THE MAIN FUNCTION
        else:
         print("BOOT Failed")
         sys.exit(0)
    if bootloader.BOOT.boot.bootos() == "2":
        sys.exit(0)


# use auto-py-to-exe to Turn this Code To An .exe And replace The current .exe With Yours If auto-py-to-exe is not installed use pip install auto-py-to-exe to install it
# And Add C:\Users\<YourUsername>\AppData\Local\Programs\Python\<PythonVersion>\Lib\site-packages to Yuor PATH (Search How To Add It to PATHS)
# And Type in auto-py-to-exe In Your Terminal To Run It and Choose This File Yuo Had Edited and Choose The Output Folder As C:\Path\To\TS-KERNEL 1.0.0\root\boot\ And Choose The Icon You Want To Use And Click On Convert .py To .exe And Wait For It To Finish (Replace C:\Path\To\TS-KERNEL 1.0.0 With The Actal Path To Your TS-KERNEL 1.0.0 Folder) (AND DON'T FORGET TO TEST IT!)
# When You're Done Upload This To GitHub As Your Title Being Like TS-DISTRO Put Distro Here (REPLACE Put Distro Here WITH ACTAL NAME OF YOUR DISTRO) And Add A Description Like TS-DISTRO Put Distro Here Is A Distro Based On TS-KERNEL 1.0.0 And Add Tags Like TS-KERNEL, TS-DISTRO, Put Distro Here (REPLACE Put Distro Here WITH ACTAL NAME OF YOUR DISTRO) And Click On Publish And Wait For It To Finish (If You Don't Want To Upload It To GitHub Just Delete The .exe File And The .py File Will Be Left) And You're Done! Enjoy Your New Distro! (REPLACE Put Distro Here WITH ACTAL NAME OF YOUR DISTRO) (And Don't Forget To Replace The Name Of Your Distro In The Code!) (AND DON'T REMOVE THEESE LINES)