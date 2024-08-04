import os
from PIL import Image
import pytesseract


def ocr_image_to_text(image_path):
    # Load the image from the file path
    image = Image.open(image_path)

    # Perform OCR to extract text
    extracted_text = pytesseract.image_to_string(image)

    return extracted_text


def save_text_to_file(text, output_path):
    with open(output_path, "w") as file:
        file.write(text)


def process_images(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith(".png"):
            image_path = os.path.join(input_dir, filename)
            text = ocr_image_to_text(image_path)

            # Create output file path
            output_filename = os.path.splitext(filename)[0] + ".txt"
            output_path = os.path.join(output_dir, output_filename)

            # Save the extracted text to the file
            save_text_to_file(text, output_path)
            print(f"Processed {filename} -> {output_filename}")


if __name__ == "__main__":
    input_directory = "images"
    output_directory = "output"

    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Process all images in the input directory
    process_images(input_directory, output_directory)
