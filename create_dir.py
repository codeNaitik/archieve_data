import os
import subprocess

def create_directory_with_files(directory_name):

    os.makedirs(directory_name, exist_ok=True)


    file1_name = os.path.join(directory_name, f"{directory_name}.txt")
    file2_name = os.path.join(directory_name, f"{directory_name}_cleaned.txt")


    with open(file1_name, 'w') as file1:
        file1.write("")

    with open(file2_name, 'w') as file2:
        file2.write("")

    print(f"Directory '{directory_name}' created with files '{file1_name}' and '{file2_name}'.")



directory_name = "in.ernet.dli.2015.269041"


create_directory_with_files(directory_name)
