def split(input_filename):
    with open(input_filename, "r") as input_file:
        file_number = 1
        for line in input_file:
            file_number_str = f"{file_number:03d}" 
            output_filename = f"PWST-{file_number_str}.txt"

            with open(output_filename, "w") as output_file:
                output_file.write(line)

            file_number += 1


input_filename = "SuperAwesomeFile.bin"
split(input_filename)
