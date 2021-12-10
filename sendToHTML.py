import os

initial_count = 0
dir = "screenshots"

for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        initial_count += 1

def html():
    number = initial_count
    numberImage = 0


    htmlfile = open("test.html", "w")
    htmlfile.write("<html>\n")
    htmlfile.write("<link rel="'"icon" type="image/x-icon" href="https://images-html.hermanerku.repl.co/Bakgrunn.ico">\n')
    
    for i in range(number):
        print("number")
        numberImage = numberImage + 1
        htmlfile.write('<img src = "' + "screenshots\screenshot"+str(numberImage)+".png"'" alt ="'"screenshot" +str(numberImage)+ '" width="20%" height="20%">\n')
    
    htmlfile.write("</html>\n")
    htmlfile.close()

html()