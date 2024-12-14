def read_and_modify_file(input_filename, output_filename):
    try:
        # Try opening the input file in read mode
        with open(input_filename, 'r') as infile:
            # Read the content of the file
            content = infile.read()

        # Modify the content (convert to uppercase in this example)
        modified_content = content.upper()

        # Try writing the modified content to a new output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File has been successfully modified and saved as {output_filename}")

    except FileNotFoundError:
        # This error occurs if the input file does not exist
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError as e:
        # Catch any I/O errors (e.g., file permissions issues)
        print(f"Error: An I/O error occurred: {e}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

def main():
    # Ask the user for the input and output filenames
    input_filename = input("Enter the filename to read from: ")
    output_filename = input("Enter the filename to save the modified content: ")
    
    # Call the function to read, modify, and write the file
    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
