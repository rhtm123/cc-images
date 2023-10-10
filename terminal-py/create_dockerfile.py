def copy_file(source_file_name, destination_file_name):
    try:
        # Open the source file for reading
        with open(source_file_name, 'r') as source_file:
            # Read the content of the source file
            content = source_file.read()
        
        # Open the destination file for writing
        with open("Dockerfile", 'w') as destination_file:
            # Write the content to the destination file
            destination_file.write(content)
        
        print(f"Content copied from '{source_file_name}' to '{destination_file_name}' successfully.")
    except FileNotFoundError:
        print(f"The file '{source_file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    source_file_name = input("Enter the name of the source file: ")
    destination_file_name = "Dockerfile"
    
    copy_file(source_file_name, destination_file_name)
