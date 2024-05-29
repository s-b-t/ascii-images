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

def saveAsciiToTextFile(asciiImg):
    while True:
        filePath = input('Enter the file name for your art to be saved under: ')
    
        if filePath == '':
            print()
            print(boldText('You didn\'t provide a file name!'))
            print()
            # Asks for the file name again
            continue
        
        if not filePath.endswith('.txt'):
            filePath += '.txt'
            
        try:
            with open(filePath, 'w') as file:
                file.write(asciiImg)
                print()
                print("Art successfully saved to " + boldText(f'{filePath}'))
                # print()  
                # Exits the loop after successfully saving the file
                break
        except Exception as e:
            print("Error saving art to file: " + boldText(f'{e}'))
            print(boldText("Please try again with a valid file name."))

# Defines the images new height and width to be set proportionally to terminal size while accounting for the fact that terminal characters are generally 1.65 times taller than they are wide.
def resizeImage(image, newWidth):
    width, height = image.size
    aspectRatio = height / width / 1.65 
    newHeight = int(aspectRatio * newWidth)
    resizedImage = image.resize((newWidth, newHeight))
    return resizedImage

# Instance of PIL Image, converts the image to grayscale as a pre-processing step to process the image ("L" being Luminance), getting each pixel to represent a single value. Reduces the color information to shades of gray, mapping the image to a single channel of intensity which make the ASCII translation of the image much easier and more crisp
def grayify(image):
    grayscaleImage = image.convert("L")
    return grayscaleImage

# Converts and loops through each pixel of the image in grayscale to then recreate each pixel with ASCII characters based on each pixels intensity, asciiStr is the string of characters that visually represent the image
def pixelsToAscii(image):
    pixels = image.getdata()
    asciiStr = ""
    for pixel in pixels:
        asciiStr += ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]
    return asciiStr

# Centers the ASCII Image to the terminal depending on width and height
def centerAsciiArt(asciiArt, width, height):
    lines = asciiArt.split("\n")
    maxLineLength = max(len(line) for line in lines)

# If the maximum line length is less than the width, center the lines according to width, otherwise the lines don't need to be centered
    if maxLineLength < width:
        centeredLines = [line.center(width) for line in lines]
    else:
        centeredLines = lines

# If the length of the centered lines are less than the height, adjust the padding on top and bottom according to the height and width
    if len(centeredLines) < height:
        topPadding = (height - len(centeredLines)) // 2
        bottomPadding = height - len(centeredLines) - topPadding
        centeredLines = [' ' * width] * topPadding + centeredLines + [' ' * width] * bottomPadding

# Centered ASCII art is the result of the lines joining and centering themselves
    centeredAsciiArt = "\n".join(centeredLines)
    return centeredAsciiArt

# Tries to convert the image into ASCII as long as there is a valid file path entered, if not, alerts the user that the file path they entered does not exist
def convertImageToAscii(imagePath, outputWidth, outputHeight):
    try:
        image = Image.open(imagePath)
    except Exception as e:
        print("Unable to retrieve the image path you entered! --> " + boldText(f'{imagePath}') + " --> " + italicText(boldText('No such file or directory exist!')))
        print()
        return None

# Redefines image by resizing and grayscaling
    image = resizeImage(image, outputWidth)
    image = grayify(image)

# Defines the string of characters that visually represent the image, defines width, defines the string length, and joins the image together by looping through each character in the string 
    asciiStr = pixelsToAscii(image)
    imgWidth = image.width
    asciiStrLength = len(asciiStr)
    asciiImg = "\n".join([asciiStr[index:index + imgWidth] for index in range(0, asciiStrLength, imgWidth)])

# Centers the image according to outputWidth, outputHeight, and the string length of the ASCII characters that visually represent the image
    asciiImg = centerAsciiArt(asciiImg, outputWidth, outputHeight)

# Prints the ASCII image after grayscale, centering, width, height, and string of ASCII characters that visually represent the image are determined
    print(asciiImg)
    return asciiImg

def main():
    # Welcome Message is called and the function displays it
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
            print(boldText('You didn\'t provide an image path name!'))
            print()
            continue

        # Gets terminal size and sets outputWidth and outputHeight
        terminalSize = os.get_terminal_size()
        outputWidth = terminalSize.columns
        # Leaves one line for the prompt
        outputHeight = terminalSize.lines - 1

        # Uses imagePath, outputWidth, outputHeight to define the location and dimensions of the image
        asciiImg = convertImageToAscii(imagePath, outputWidth, outputHeight)

        if asciiImg:
            print()
            print(boldText(f'{imagePath}') + " successfully printed to terminal.")
            while True:
                saveToTextFile = input("\nWould you like to save the ASCII art to a text file? " + boldText('(Y/N)') + ": ").strip().lower()
                if saveToTextFile in ['y' or 'yes']:
                    print()
                    saveAsciiToTextFile(asciiImg)
                    print()
                    break
                elif saveToTextFile in ['n' or 'no']:
                    print()
                    print(boldText('ASCII art was not saved.'))
                    print()
                    break
                else:
                    print()
                    print('Please enter a valid response. ' + boldText('(Y/N)') + ': ')

if __name__ == "__main__":
    main()
