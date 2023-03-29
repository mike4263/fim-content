import os
import chardet

input_directory = "content/legacy_fortune"
output_directory = "content/legacy_fortune2"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.listdir(input_directory):
    input_file_path = os.path.join(input_directory, filename)
    output_file_path = os.path.join(output_directory, filename)

    # Read the file as binary
    with open(input_file_path, "rb") as file:
        raw_data = file.read()

    # Detect encoding
    detected_encoding = chardet.detect(raw_data)["encoding"]

    # Decode the data using the detected encoding
    content = raw_data.decode(detected_encoding)

    # Write the data as UTF-8
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(content)

print("Conversion completed!")
