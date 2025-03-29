# File Organizer Script

A simple Python script to automate the organization of files in a directory by sorting them into categorized folders based on file types.

## Features

- Organizes files into folders based on their file extensions
- Creates a detailed log file of all operations
- Simple command-line interface
- No advanced libraries required (only uses Python standard library)
- Sorts files into categories like Documents, Images, Videos, etc.

## Requirements

- Python 3.6 or higher

## How to Use

1. Save the `file_organizer.py` script to your computer
2. Open a command prompt or terminal
3. Navigate to the directory where you saved the script
4. Run the script with the command:
   ```
   python file_organizer.py
   ```
5. When prompted, enter the path of the directory you want to organize
   - You can press Enter to use the current directory
6. Confirm the operation when prompted

## File Organization Structure

The script will organize files into the following structure:

```
Your_Directory/
│
├── Documents/
│   ├── PDFs/
│   ├── Word/
│   ├── Text/
│   ├── Excel/
│   └── Presentations/
│
├── Images/
├── Videos/
├── Audio/
├── Archives/
├── Programming/
│   ├── Python/
│   ├── Java/
│   └── Web/
│
└── Miscellaneous/
```

## Warning

This script **moves** files from their original location. It does not create copies. Make sure you have backups of important files before running the script on directories containing critical data.

## Example Usage

```
===============================================================
FILE ORGANIZER - Automatic File Organization Tool
===============================================================

Enter the directory path to organize (or press Enter for current directory): C:\Users\YourName\Downloads

Ready to organize files in: C:\Users\YourName\Downloads
This will move your files into categorized folders.
Do you want to proceed? (y/n): y

Created directory: C:\Users\YourName\Downloads\Documents\PDFs
Created directory: C:\Users\YourName\Downloads\Images
Created directory: C:\Users\YourName\Downloads\Archives

File organization complete!
Processed 45 files, moved 45 files
Log file created: C:\Users\YourName\Downloads\file_organization_log_2023-07-15_14-30-22.txt 