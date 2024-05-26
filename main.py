from PIL import Image
import os

# More detailed ASCII characters used to build the output text
ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

def resize_image(image, new_width):
    width, height = image.size
    aspect_ratio = height / width / 1.65  # Adjust aspect ratio for terminal display
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]
    return ascii_str

def center_ascii_art(ascii_art, width, height):
    lines = ascii_art.split("\n")
    max_line_length = max(len(line) for line in lines)
    
    if max_line_length < width:
        centered_lines = [line.center(width) for line in lines]
    else:
        centered_lines = lines
    
    if len(centered_lines) < height:
        top_padding = (height - len(centered_lines)) // 2
        bottom_padding = height - len(centered_lines) - top_padding
        centered_lines = [' ' * width] * top_padding + centered_lines + [' ' * width] * bottom_padding
    
    centered_ascii_art = "\n".join(centered_lines)
    return centered_ascii_art

def convert_image_to_ascii(image_path, output_width, output_height):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}. {e}")
        return

    image = resize_image(image, output_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[index:index + img_width] for index in range(0, ascii_str_len, img_width)])

    ascii_img = center_ascii_art(ascii_img, output_width, output_height)

    print(ascii_img)
    return ascii_img

# Get user input for the image path
image_path = input("Enter the path of your image file: ")

# Terminal size
terminal_size = os.get_terminal_size()
output_width = terminal_size.columns
output_height = terminal_size.lines - 1  # Leave one line for the prompt

convert_image_to_ascii(image_path, output_width, output_height)



