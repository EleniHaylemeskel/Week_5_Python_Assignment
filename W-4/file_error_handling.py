def modify_content(line):
    # Example modification: make it uppercase
    return line.upper()

def main():
    input_filename = input("Enter the name of the file to read: ")

    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found.")
        return
    except IOError:
        print(f"❌ Error: Could not read the file '{input_filename}'.")
        return

    # Modify each line
    modified_lines = [modify_content(line) for line in lines]

    output_filename = "modified_" + input_filename
    try:
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)
        print(f"✅ Modified content written to '{output_filename}' successfully.")
    except IOError:
        print(f"❌ Error: Could not write to the file '{output_filename}'.")

if __name__ == "__main__":
    main()
# This script reads a file, modifies its content, and writes the modified content to a new file.