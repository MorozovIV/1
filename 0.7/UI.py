import eel

eel.init("web")
#eel.start("main html",size = (400,200), mode="chrome-app", port=9000) #mode = "chrome", edge ,electron, custom
eel.start('main.html', size=(250, 200), position=(500, 250)) #size=(400,200)