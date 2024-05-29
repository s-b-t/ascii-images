### B33FWare ASCII Image2Art Converter

*This program is still in its BETA/WIP stage. I will be updating more functionality and features continually.*

This program is meant to showcase how creative you can be right in your terminal. In the logic of the program, each pixel of the user's desired image directly corresponds to an ASCII character and is designed to map, scale, grayscale, and print the exact ASCII representation of the desired image to the user's terminal.

First, go to your terminal and navigate (using 'list' ```ls```, 'change directory' ```cd```, and 'back one directory' ```cd ..``` commands) to a suitable directory where you can save this program to.

When you're there, ```mkdir``` your folder name -- ```mkdir ascii-images``` is a suitable example.

Then, install Pillow right to the ```ascii-images``` (or whatever name you choose) project folder. To do this, type ```pip install pillow``` and press Enter.

```PIL``` aka ```pillow``` is used to assist the program in generating images to ASCII characters.

Once you've verified the ```pillow``` packages have finished installing, type and enter the following command to your ```ascii-images``` project folder:
  
  Windows: ```python main.py```
  
  MacOS: ```python3 main.py```

After you've received the greeting message/header, enter whatever image path you want (as long as they're located in your project) and watch the magic happen!

---------------------------------------------------------------------------------------------------------------------------------------------------------------
### Important Details About Using This Program:

-- The image being generated HAS to be located in the main project folder for this program. In other words, you cannot just simply type some random image path name or grab another image path name from 'Pictures', 'Documents', or even the Internet and hope the image will generate. I will eventually implement the user being able to choose from any image path off their computer or potentially allowing image URLs from the internet.

-- 'Copy Relative Path' or 'Copy Path' and pasting the image path name directly from your code editor into the prompt is the easiest method at the moment. This method assumes that you have already set up an images folder and have images in the folder that you would like to use. I've set up folders already for you to drop images into, titled 'user-public' and 'user-images' with a test image titled 'space-robot1.PNG' inside of it. Use those for now, or rename them to your liking.

-- If you're going to import just the Python script, make your own images folder in the project folder. I know this isn't perfectly ideal, but this will also allow you to have the image files you may love using, right in your project. You can of course, just delete the ones you may not like.

-- To generate the BEST possible "resolution" of your text in the form of the image that you want, please reduce your terminal font size located in your terminal settings. The smaller the font, the more detail you will be shown per image that is generated. When you start playing around with smaller font sizes, you instantly see how much detail is missing from the image. Remember, the ASCII characters directly correlate to each pixel in the image so if your font size is larger, you are allowing the program to give you less detail than it actually can.

-- When you're given the option to save to a text (```.txt```) file of the art after generating, just know that I defaulted the program to save your file as a ```.txt``` file simply because ASCII is always generated in text and characters. The user does not have to add an extension when entering a file name, just the name. Technically, there's other text file extensions you can use, but not right now in the current version of this program. I will implement that feature as another default eventually, but for now a default of the ```.txt``` file serves its purpose perfectly fine.
