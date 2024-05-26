from PIL import Image
import os, time, sys

# More detailed ASCII characters used to build the output text
ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

# Boldens text using ANSI escape characters when function is called
def boldText(text):
    return "\033[1m" + text + "\033[0m"

# Italicizes text using ANSI escape characters when function is called
def italicText(text):
    return "\033[3m" + text + "\033[0m"

# Defines how animateMessage writes the infoText characters 1 by 1 in .025s intervals giving the impression the program is typing to the user
def animateMessage(infoText, iterations):
    for _ in range(iterations):
        for char in infoText:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.025)

# Function to display the content of the infoText as well as animate the infoText in 1 iteration when user runs the program
def displayWelcomeMessage():
    infoText = "\nWelcome to the " + boldText('B33FWare Image2ASCII Converter') + "." + "\nAuthor: Steven Blake Tobias\n" + boldText("PSSST! ") + "This program runs best on full screen.\n" + "More info at " + boldText('www.github.com/s-b-t\n\n')
    iterations = 1
    animateMessage(infoText, iterations)

# Function to display the content of the Good Bye message when the user opts to QUIT (called later in the logic for if the user QUITs)
def displayByeMessage():
    byeText = "Thank you for using the " + boldText('B33FWare Image2ASCII Converter') + "." + " Goodbye!"
    iterations = 1
    animateMessage(byeText, iterations)


def main():
    displayWelcomeMessage()

    # Allows user to continue with the program as intended after the infoText displays
    input('Press ' + boldText("[Enter]") + ' or ' + boldText("[Return]") + ' to continue...\n')

    while True:
        # Allows user input to enter any image file they wish, or QUIT out of the program
        imagePath = input('Enter or paste the path of the image file you would like to convert to ASCII art ' + boldText('(to Quit, type QUIT)') + ": ")
        print()

        # If user decides to QUIT, Bye Message displays and exits the program
        if imagePath == 'QUIT':
            displayByeMessage()
            print('\n')
            sys.exit()

        # If user does not enter a file into the prompt, alert the user and keep displaying alert message until they enter valid input
        if not imagePath:
            print('You didn\'t provide an image file!')
            print()
            continue

        # Gets terminal size and sets outputWidth and outputHeight
        terminalSize = os.get_terminal_size()
        outputWidth = terminalSize.columns
        # Leaves one line for the prompt
        outputHeight = terminalSize.lines - 1

        # Uses imagePath, outputWidth, outputHeight to define the location and dimensions of the image
        convertImageToAscii(imagePath, outputWidth, outputHeight)

# Defines the images new height and width to be set proportionally to terminal size while accounting for the fact that terminal characters are generally 1.65 times taller than they are wide.
def resizeImage(image, newWidth):
    width, height = image.size
    aspectRatio = height / width / 1.65 
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
        print("Unable to open image file " + boldText(f'{imagePath}! ') + italicText(f'{e}\n'))
        return

    image = resizeImage(image, outputWidth)
    image = grayify(image)

    asciiStr = pixelsToAscii(image)
    imgWidth = image.width
    asciiStrLength = len(asciiStr)
    asciiImg = "\n".join([asciiStr[index:index + imgWidth] for index in range(0, asciiStrLength, imgWidth)])

    asciiImg = centerAsciiArt(asciiImg, outputWidth, outputHeight)

    print(asciiImg)
    return asciiImg

if __name__ == "__main__":
    main()
