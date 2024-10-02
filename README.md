# hksuperG

The developed code serves as a tool for generating random number combinations with specific constraints, commonly used in betting games or lotteries. This code allows users to input the number of combinations they want to generate, the bet values for four-digit (4D), three-digit (3D), and two-digit (2D) combinations, as well as a list of four-digit combinations that should be excluded from the results. The code comprises several key components, including the initialization of global variables for digit names and number limits, the `generate_kombinasi` function to generate valid random number combinations, and the `main` function to handle user input and display the results. During the process, the code ensures that the generated number combinations do not include any of the forbidden combinations and constructs the result strings in the desired format for use in betting games or simulations. Consequently, this code not only assists in generating random number combinations but also provides additional control to avoid specific numbers, making it a flexible and useful tool in the context of number-based betting.

# ANNOUNCEMENT!!

GIT CLONE READY!!

`https://github.com/kingashari/hksuperG`

dead numbers are ready to use again, bugs have been fixed, download version 2.0.3 on release if this is using the version without dead numbers download **RELOAD** version 2.0.2. the git clone folder has been updated, if you have previously saved an update with `git pull` on the repository

**RELOAD** has been release

# update version
about updates can be seen at releases

# coming soon
coming in website to universal useing

1.6 there are changes

2.3 coming soon feature adding totally bet

HONGKONG | SDYNEY | SINGAPORE ready to auto-play numbers in the 2.3 update 


# build
Visual Studio Code

v1.89 april 2024

Python version

Python 3.11.9

# maintenace
If it's not available yet, it means it's still in development mode

bet mode available NOW

totally not available

dead number data is now available automatically in update 1.7

# web version ?

The web version will come, maybe it won't be long in 2-3 weeks, this will probably use the first version, maybe use WAP mode because here we are looking for easy access. I will add some important features first before rolling out the web version. version 1.9? version 2.0 or 2.1? Don't know.

There is no continuation of the web version yet, because there are still many additional features that might be useful, but don't worry, this will be made as soon as possible

if you want to help me develop the website you only contact me in profile :)

# NOTE!!

In the version 1.6 update, we decided to remove a feature that I found to be unnecessary. After careful consideration and thorough research, I have decided to eliminate the dead number feature. This will be replaced with a feature that allows users to eliminate numbers that have already been drawn or that they believe will not be drawn.

in 1.7 if the dead number has an error or can't be run, you can replace it in the Python script, look for the code 
'url = 'xxxxxxxxxxxxxxx'
and contact me, I'll give you a small update

Angka Main (AM1) First Digit XX11

Angka Main (AM2) Second Digit 11XX

Angka Ikut (AI) 

# GUI EDITION NOW AVAILABLE!!
Here is a description of the changes to the GUI (Graphical User Interface) after the update:

### 1. **Scraping Button**
- Added the **"Scrape Number Not Out"** button which automatically downloads data from the site and displays the results in the GUI. The scraping results are displayed horizontally to make them neater and easier to see.
- This button is located after the combination input and before the output results, so that users can easily scrape before calculating the number combination.

### 2. **Scraping Result Display**
- The scraping results are displayed in the **"Scraping Result:"** label which is updated to show the numbers that did not come out, with a horizontal format to maximize space usage.
- This content is wrapped in a label that supports a text length that can be set with the `wraplength` attribute to keep the text visible in the set area.

### 3. **Combination Result Display**
- After pressing the **"Generate Combination"** button, the number combination results will appear in the **"Combination Result:"** label with a horizontal display, where the results are displayed neatly in sequence.

### 4. **Bet Calculation Result Display**
- This section displays the 4D, 3D, and 2D calculation results in the label **"Bet Result (4D, 3D, 2D):"**.
- The calculation results are also clearly divided, each part (4D, 3D, and 2D) is separated by certain characters, such as an asterisk (*), for easy reading.

### 5. **Copy Paste Button**
- **The "Copy Bet Result" button** is placed after the calculation results to make it easier for users to copy the 4D, 3D, and 2D calculation results to the clipboard.
- After the user presses this button, a notification message will appear to inform that the results have been successfully copied to the clipboard, providing a more interactive experience.

### 6. **Improved User Interaction**
- Users can now directly copy bet results (4D, 3D, 2D) with one click without having to select the text manually.
- Additional notifications with `messagebox` provide clear feedback on whether the results were successfully copied or whether the scraping was successful.

This update makes the GUI more intuitive, responsive, and makes it easier for users to quickly manage scraping results and numerical calculations.

