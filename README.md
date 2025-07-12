📝 Simple To-Do List (Tkinter)

  A minimalistic desktop To‑Do List application built with Python and Tkinter. Tasks are stored locally in a .txt file (saveInfo.txt), making it lightweight, fast, and fully offline.

💡 Features
    Add new tasks

  Delete selected tasks

  Tasks persist between sessions via saveInfo.txt

  User-friendly error messages

  Simple, clean interface built with tkinter
  
🖥️ How to Run
  Requirements

  Python 3.x installed

  No additional libraries required (uses built-in tkinter)

  Steps
  Clone the repository: 
  
    git clone https://github.com/meloqp/To-Do-List.git

    cd To-Do-List

  Run the app:
  
    python todo.py

  Replace todo.py with the actual filename if different.

 📦 Create an Executable (.exe)  
  You can package the app into a standalone .exe file using PyInstaller.

  1. Install PyInstaller

    pip install pyinstaller

  2. Build the executable

    pyinstaller --onefile --windowed todo.py

    --onefile: packs everything into one .exe file

    --windowed: prevents the command-line window from appearing on launch (for GUI apps)

  3. Locate the executable

  After building, the .exe will appear in the dist/ folder. You can now run or share your app without requiring Python installed on other machines.

