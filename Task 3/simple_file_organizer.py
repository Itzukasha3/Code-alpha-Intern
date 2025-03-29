# Simple File Organizer
# This script organizes files in a directory into category folders based on file type

import os  # For file and directory operations
import shutil  # For moving files

def organize_files(directory):
    """
    Organizes files in the specified directory into categories.
    
    Args:
        directory (str): The path to the directory to organize
    """
    print(f"Organizing files in: {directory}")
    
    # Create category directories if they don't exist
    categories = ["Documents", "Images", "Videos", "Music", "Other"]
    
    for category in categories:
        category_path = os.path.join(directory, category)
        # Create the directory if it doesn't exist
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            print(f"Created directory: {category}")
    
    # File extension mappings - what category each file type belongs to
    extensions = {
        # Documents
        ".pdf": "Documents",
        ".doc": "Documents",
        ".docx": "Documents",
        ".txt": "Documents",
        ".xlsx": "Documents",
        ".pptx": "Documents",
        
        # Images
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",
        ".gif": "Images",
        
        # Videos
        ".mp4": "Videos",
        ".avi": "Videos",
        ".mov": "Videos",
        
        # Music
        ".mp3": "Music",
        ".wav": "Music",
    }
    
    # Counters to track progress
    moved_count = 0
    total_count = 0
    
    # Process each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories and this script file
        if os.path.isdir(file_path) or filename == os.path.basename(__file__):
            continue
            
        total_count += 1
        
        # Get the file extension (like .pdf, .jpg)
        file_extension = os.path.splitext(filename)[1].lower()
        
        # Determine which category the file belongs to
        if file_extension in extensions:
            category = extensions[file_extension]
        else:
            category = "Other"  # Default for unknown file types
        
        # Create the destination path
        destination = os.path.join(directory, category, filename)
        
        try:
            # Move the file to its category folder
            shutil.move(file_path, destination)
            print(f"Moved: {filename} to {category}")
            moved_count += 1
        except Exception as e:
            print(f"Error moving {filename}: {str(e)}")
    
    # Show summary
    print("\nOrganization complete!")
    print(f"Processed {total_count} files")
    print(f"Successfully moved {moved_count} files")

def main():
    """Main function to run the script."""
    print("=" * 50)
    print("SIMPLE FILE ORGANIZER")
    print("=" * 50)
    print("This script will organize your files into folders by type.")
    
    # Get the directory to organize
    while True:
        directory = input("\nEnter the directory path to organize (or press Enter for current directory): ").strip()
        
        # Use current directory if nothing is entered
        if not directory:
            directory = os.getcwd()
            print(f"Using current directory: {directory}")
        
        # Check if the directory exists
        if os.path.exists(directory) and os.path.isdir(directory):
            break
        else:
            print("Error: That directory doesn't exist. Please try again.")
    
    # Ask for confirmation before proceeding
    print(f"\nReady to organize files in: {directory}")
    print("Files will be moved into categories: Documents, Images, Videos, Music, Other")
    confirm = input("Do you want to proceed? (y/n): ").lower()
    
    if confirm == 'y' or confirm == 'yes':
        organize_files(directory)
    else:
        print("Operation cancelled.")

# This is the entry point of the script
if __name__ == "__main__":
    main() 