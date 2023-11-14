import os
import subprocess
import shutil

# Define the variable for the folder name
certificato_variable = input("Inserisci il nome del certificato: ")

# Convert the variable to lowercase for the folder name
certificato_folder = os.path.join("..", "certificati", f"certificato-{certificato_variable.lower()}")

# Define the paths
generate_sh_path = os.path.abspath("./generate.sh")

try:
    # Run the script using Git Bash in the current working directory
    subprocess.run([r"C:\Program Files\Git\bin\bash.exe", generate_sh_path], check=True)

    # Create the folder if it doesn't exist inside the root/certificati directory
    os.makedirs(os.path.join(os.getcwd(), certificato_folder), exist_ok=True)

    # Move the generated files to the folder
    shutil.move("server.key", os.path.join(certificato_folder, "server.key"))
    shutil.move("server.crt", os.path.join(certificato_folder, "server.crt"))

    print("SSL certificates generated successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
