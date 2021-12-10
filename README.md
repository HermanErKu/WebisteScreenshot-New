# WebisteScreenshot-New
A program that takes screenshots of webpages and adds them to an HTML file


# Setup
To setup you need to import the libraries that you can find [here](requirements.txt)

You also may need to change [this](https://github.com/HermanErKu/WebisteScreenshot-New/blob/main/screenshot.py#L36) output folder in the python code, but you can read more about it [here](https://github.com/HermanErKu/WebisteScreenshot-New/blob/main/README.md#how-it-works)

# How to use
This is the steps to use the program
1. Download this entire project
2. Double click screenshot.py
3. Enter URL and how many seconds you want it to use between refreshes
4. Put mouse cursor in the corner of your screen when you are done
5. Double click sendToHTML.py
6. Open the index.html file and see all you screenshots nice in your browser

# Story
This is a project that i started on a very long time ago. I was not nearly as good at coding as i am now. I wanted to make a program that took screenshots of websites that used to often change so i could watch the change. Kinda like the [WayBack Machine](https://archive.org/web/). I tried coding it, but i failed. I then forgot the project until one day. I was sitting on the toilet when it just magically popped up in my head how I should do it. I then ran to my computer and started making it.

# How it works
This is how the program works

### [requirements.txt](https://github.com/HermanErKu/WebisteScreenshot-New/blob/main/requirements.txt)
1. Shows all the python libraries you have to install
PRO TIP : Save the file as ".bat" and double click to make it install for you

### [screenshot.py](https://github.com/HermanErKu/WebisteScreenshot-New/blob/main/screenshot.py)
1. It opens the webpage
2. It takes a screenshot of the webpage
3. A variable goes up by 1
4. It names the file with the variable value
5. The webpage refreshes

### [sendToHTML.py](https://github.com/HermanErKu/WebisteScreenshot-New/blob/main/sendToHTML.py)
1. Checks how many screenshots you have
2. Empties the html file for old screenshots
3. Adds all the new screenshot to the index.html file

### [index.html](https://github.com/HermanErKu/WebisteScreenshot-New/blob/main/index.html)
1. Takes info from  sendToHTML.py
2. Shows the pictures


# Future adds
[GUI](https://www.pygame.org/news)

Automatic [NGROK](https://ngrok.com/)
