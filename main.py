from PIL import Image
import os

# More detailed ASCII characters used to build the output text
ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

def resizeImage(image, newWidth):
    width, height = image.size
    aspectRatio = height / width / 1.65  # Adjust aspect ratio for terminal display
    newHeight = int(aspectRatio * newWidth)
    resizedImage = image.resize((newWidth, newHeight))
    return resizedImage

def grayify(image):
    grayscaleImage = image.convert("L")
    return grayscaleImage

def pixelsToAscii(image):
    pixels = image.getdata()
    asciiStr = ""
    for pixel in pixels:
        asciiStr += ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]
    return asciiStr

def centerAsciiArt(asciiArt, width, height):
    lines = asciiArt.split("\n")
    maxLineLength = max(len(line) for line in lines)
    
    if maxLineLength < width:
        centeredLines = [line.center(width) for line in lines]
    else:
        centeredLines = lines
    
    if len(centeredLines) < height:
        topPadding = (height - len(centeredLines)) // 2
        bottomPadding = height - len(centeredLines) - topPadding
        centeredLines = [' ' * width] * topPadding + centeredLines + [' ' * width] * bottomPadding
    
    centeredAsciiArt = "\n".join(centeredLines)
    return centeredAsciiArt

def convertImageToAscii(imagePath, outputWidth, outputHeight):
    try:
        image = Image.open(imagePath)
    except Exception as e:
        print(f"Unable to open image file {imagePath}. {e}")
        return

    image = resizeImage(image, outputWidth)
    image = grayify(image)

    asciiStr = pixelsToAscii(image)
    imgWidth = image.width
    asciiStr_len = len(asciiStr)
    asciiImg = "\n".join([asciiStr[index:index + imgWidth] for index in range(0, asciiStr_len, imgWidth)])

    asciiImg = centerAsciiArt(asciiImg, outputWidth, outputHeight)

    print(asciiImg)
    return asciiImg

# Get user input for the image path
imagePath = input("Enter the path of your image file: ")

# Terminal size
terminalSize = os.get_terminalSize()
outputWidth = terminalSize.columns
outputHeight = terminalSize.lines - 1  # Leave one line for the prompt

convertImageToAscii(imagePath, outputWidth, outputHeight)



