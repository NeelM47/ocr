#from paddleocr import PaddleOCR
#
#def extract_text(png_file, output_txt_file):
#    try:
#        # Initialize PaddleOCR
#        ocr = PaddleOCR(use_angle_cls=True, lang='en')
#        
#        # Perform OCR on the input image
#        result = ocr.ocr(png_file)
#        
#        # Extract and format the text from the results
#        text = "\n".join([line[1][0] for line in result[0]])
#        
#        # Save the extracted text to a .txt file
#        with open(output_txt_file, "w") as file:
#            file.write(text)
#        
#        print(f"Text extracted and saved to {output_txt_file}")
#    except Exception as e:
#        print(f"Error: {e}")
#
#if __name__ == "__main__":
#    # Hardcoded file names
#    input_png = "input.png"  # Replace with your PNG file path
#    output_txt = "output.txt"  # Replace with your desired output file path
#    
#    extract_text(input_png, output_txt)
import os
from paddleocr import PaddleOCR

def extract_text(png_files, output_txt_file):
    #ocr = PaddleOCR(use_gpt=True, lang='en')
    ocr = PaddleOCR(use_angle_cls=True, lang='en')

    try:
        for png_file in png_files:
            # Perform OCR on the input image
            result = ocr.ocr(png_file)

            # Extract and format the text from the results
            text = "\n".join([line[1][0] for line in result[0]])

            # Append the extracted text to the output file
            with open(output_txt_file, "a") as file:  # 'a' for append mode
                file.write(f"\n\nText from {png_file}:\n{text}\n")

            print(f"Text extracted from {png_file} and appended to {output_txt_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Get all .png files in the current directory
    png_files = [f for f in os.listdir() if f.endswith(".png")]

    # Specify the output text file
    output_txt = "output_txt.txt"

    # Extract text from all PNG files and append to the output file
    extract_text(png_files, output_txt)

