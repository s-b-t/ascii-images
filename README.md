<h1 align="center">B33FWare Image2ASCII Converter</h1>

### Introduction

Welcome to the B33FWare Image2ASCII Converter! This program is designed to creatively convert images into ASCII art directly in your terminal. Each pixel in your desired image is mapped, scaled, and transformed into a corresponding ASCII character, resulting in a unique representation of your desired image.

*Note: This program is currently in its BETA/WIP stage, and new features and improvements will be added eventually.*

### Prerequisites

Before getting started, ensure you have Python installed on your system. This program will also require the Pillow library (Python Image Library) aka ```PIL``` to handle image processing.

### Getting Started

**Step 1: Clone the Repository**

First, you'll need to clone this repository to your local machine. Open your terminal and run the following command:

```git clone https://github.com/s-b-t/ascii-images.git```

This will create a directory named ```ascii-images``` containing the project files.

**Step 2: Navigate to the Project Directory**

Change into the project directory:

```cd ascii-images```

**Step 3: Install Required Libraries**

The program requires the Pillow library (```PIL```) for image processing. Install it using ```pip```:

```pip install pillow```

If you're on MacOS or Linux you *may* need to use ```pip3``` instead:

```pip3 install pillow```

**Step 4: Run the Program**

1. Ensure your image file is in the project directory ```user-public/user-images``` which will already be available to you after cloning.
2. Run the program.

Windows:

```python main.py```

MacOS/Linux:

```python3 main.py```

**Step 5: Convert an Image to ASCII**

1. After running the program, a greeting message will appear.
2. Press Enter to continue.
3. Enter (or paste) the path to your image file when prompted to do so. (i.e. ```user-public/user-images/space-robot1.png```)
4. The program will then generate and display the ASCII art in your terminal!

---------------------------------------------------------------------------------------------------------------------------------------------------------------
### Important Details About Using This Program

-- The image being generated HAS to be located in the main project folder for this program. In other words, you cannot just simply type some random image path name or grab another image path name from ```Pictures```, ```Documents```, or even the Internet and hope the image will generate. I will eventually implement the user being able to choose from any image path off their computer or potentially allowing image URLs from the internet.

-- ```Copy Relative Path``` or ```Copy Path``` and pasting the image path name directly from your code editor into the prompt is the easiest method at the moment. This method assumes that you have already set up an images folder and have images in the folder that you would like to use. I've set up folders already for you to drop images into, titled ```user-public/user-images``` with a test image titled ```space-robot1.PNG``` inside of it. Use those for now, or rename them to your liking.

-- If you're going to import just the Python script, make your own images folder in the project folder. I know this isn't perfectly ideal, but this will also allow you to have the image files you may love using, right in your project. You can of course, just delete the ones you may not like.

-- To generate the BEST possible "resolution" of your text in the form of the image that you want, please reduce your terminal font size located in your terminal settings. Alternatively, you can just ```ctrl/cmd``` + (```+```) or (```-```) to manipulate the zoom level in your terminal. Ideally you would want to change the zoom level before you print the image to the terminal. The smaller the font, the more detail you will be shown per image that is generated. When you start playing around with smaller font sizes/zoom levels, you instantly see how much detail is missing from the image and vice versa. Remember, the ASCII characters directly correlate to each pixel in the image so if your font size is larger, you are allowing the program to give you less detail than it actually can.

-- When you're given the option to save to a text (```.txt```) file of the art after generating, just know that I defaulted the program to save your file as a ```.txt``` file simply because ASCII is always generated in text and characters. The user does not have to add an extension when entering a file name, just the name. Technically, there's other text file extensions you can use, but not right now in the current version of this program. I will implement that feature as another default eventually, but for now a default of the ```.txt``` file serves its purpose perfectly fine.
