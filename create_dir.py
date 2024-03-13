import os
import subprocess

def create_directory_with_files(directory_name):
    # Create the directory
    os.makedirs(directory_name, exist_ok=True)

    # Define file names
    file1_name = os.path.join(directory_name, f"{directory_name}.txt")
    file2_name = os.path.join(directory_name, f"{directory_name}_cleaned.txt")

    # Create the files
    with open(file1_name, 'w') as file1:
        file1.write("")

    with open(file2_name, 'w') as file2:
        file2.write("")

    print(f"Directory '{directory_name}' created with files '{file1_name}' and '{file2_name}'.")


# Get the directory name from the user
directory_name = "in.ernet.dli.2015.343839"

# Call the function to create the directory and files
create_directory_with_files(directory_name)
