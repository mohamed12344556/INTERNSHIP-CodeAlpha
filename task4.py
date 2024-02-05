import os
import shutil
from datetime import datetime

def organize_files(source_folder, destination_folder):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        return print(f"not {source_folder} found.")

    # Check if the destination folder exists, create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        return print(f"$ we made a new folder for you : {source_folder}")

    # List of file extensions to organize
    file_extensions = set(['.txt', '.pdf', '.jpg', '.png', '.xlsx', '.docx','.pptx'])

    # Read files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Check if the item is a file and not a folder
        if os.path.isfile(source_path):
            _, file_extension = os.path.splitext(filename)

            # Check if the file extension is in the desired list
            if file_extension in file_extensions:
                destination_path = os.path.join(destination_folder, file_extension[1:])
                # Move the file to the destination folder instead of copying
                shutil.move(source_path, destination_path)
                print(f"move {filename} to {destination_path}")

# Use the function to organize files based on their extensions
source_folder = r'C:\Users\ma512\Documents\ML\codealpha'
destination_folder = r'C:\Users\ma512\Documents\ML\codealpha\Organize Files'
organize_files(source_folder, destination_folder)

#############################################

def copy_and_update_files(source_folder, destination_folder):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        return print(f"file not exist {source_folder}")

    # Check if the destination folder exists, create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        return print(f"$ we made a new folder for you : {source_folder}")

    # List of file extensions to copy
    file_extensions = set(['.txt', '.pdf', '.jpg', '.png', '.xlsx', '.docx','.pptx'])

    # Read files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Check if the item is a file and not a folder
        if os.path.isfile(source_path):
            _, file_extension = os.path.splitext(filename)

            # Check if the file extension is in the desired list
            if file_extension in file_extensions:
                destination_path = os.path.join(destination_folder, filename)

                # Copy the file to the destination folder
                shutil.copy2(source_path, destination_path)
                print(f"copy  {source_folder} to {destination_path}")

                # Update data inside the file (this part can be customized as needed)
                with open(destination_path, 'a') as file:
                    file.write("\n Data updated.")

# Use the function to copy and update files
source_folder = r'C:\Users\ma512\Documents\ML\codealpha\Organize Files'
destination_folder = r'C:\Users\ma512\Documents\ML\codealpha\copy_and_update_files'
copy_and_update_files(source_folder, destination_folder)

##############################################

def organize_files_by_date(source_folder, destination_folder):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        print(f"not {source_folder} found.")
        return

    # Check if the destination folder exists, create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Read files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Check if the item is a file and not a folder
        if os.path.isfile(source_path):
            # Get the creation date of the file
            creation_time = os.path.getctime(source_path)
            creation_date = datetime.fromtimestamp(creation_time)

            # Create a subfolder with the year and month as the name
            subfolder_name = f"{creation_date.year}_{creation_date.month:02d}"
            destination_path = os.path.join(destination_folder, subfolder_name)

            # Check if the subfolder exists, create it if not
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            # Move the file to the subfolder
            shutil.move(source_path, os.path.join(destination_path, filename))
            print(f"copy {filename} to {destination_path}")

# Use the function to organize files based on their creation date
source_folder = r'C:\Users\ma512\Documents\ML\codealpha'
destination_folder = r'C:\Users\ma512\Documents\ML\codealpha\organize_files_by_date'
organize_files_by_date(source_folder, destination_folder)
