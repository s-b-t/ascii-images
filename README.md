### B33FWare ASCII Image2Art Converter

*Please Note: This program is still in its BETA/WIP stage.*

This program is meant showcase how creative you can be right in your terminal. It converts any image located in your project you want into ASCII art.

First, go to your terminal and navigate (using 'list' ```ls```, 'change directory' ```cd```, and 'back one directory' ```cd ..``` commands) to a suitable directory where you can save this program to.

When you're there, ```mkdir``` your folder name -- ```mkdir ascii-images``` is a suitable example.

Then, install Pillow right to the ```ascii-images``` (or whatever name you choose) project folder. To do this, type ```pip install pillow``` and press Enter.

```PIL``` aka ```pillow``` is used to assist the program in generating images to ASCII characters.

Once you've verified the ```pillow``` packages have finished installing, type and enter the following command to your ```ascii-images``` project folder:
  
  Windows: ```python main.py```
  
  MacOS: ```python3 main.py```

After you've received the greeting message/header, enter whatever image path you want and watch the magic happen!

---------------------------------------------------------------------------------------------------------------------------------------------------------------
### Important Details About Using This Program:

-- The image being generated HAS to be located in the project folder for this program. In other words, you cannot just simply type some random path name or grab another path name from 'Pictures', 'Documents' or even the Internet and hope an image will generate. 'Copying Relative Path' and pasting the image path name directly from your code editor into the prompt is the easiest method at the moment. I've set up folders already for you to drop images into, titled 'user-public' and 'user-images' with a test image titled 'space-robot1.PNG' inside of it. Use those for now, or rename them to your liking. If you're going to import just the Python script, then make your own images folder in the project. This will also allow you to have the image files you may have liked using, right in your project. You can of course, just delete the ones that you may not like.

-- To generate the BEST possible "resolution" of your text in the form of the image that you want, please feel free to change the font size of your terminal located in your terminal settings. The smaller the font, the more detail you will be shown per image that is generated.

-- When you're given the option to save to a text (```.txt```) file of the art after generating, just know that I defaulted the program to save your file as a ```.txt``` file simply because ASCII is generated in text and characters. Technically, there's other text file extensions you can use, but not right now in the current version of this program. I will implement that feature eventually, but for now a ```.txt``` file serves its purpose perfectly fine.
