@echo off

:: Define the target directory
set TARGET_DIR=C:\Users\<actual_username>\<nested_folder_name>\Desktop\TS-COMPONENTS25\TSPYTHON

:: Check if the current directory matches the target
if "%cd%" neq "%TARGET_DIR%" (
    echo Current directory does not match the target directory.
    
    echo Navigating to the target directory...
    cd /d "%TARGET_DIR%"
    :: Start the first Python script in a new Command Prompt window
    start cmd /k boot\editor.exe
    :: Start the second Python script in another new Command Prompt window
    start cmd /k boot\console.exe
    echo Both . files are now running in their own windows!
    pause

) else (
    echo Already in the target directory: "%TARGET_DIR%".
    :: Start the first Python script in a new Command Prompt window
    start cmd /k python boot\editor.py
    :: Start the second Python script in another new Command Prompt window
    start cmd /k python boot\console.py
    echo Both scripts are now running in their own windows!
    pause

)

pause
