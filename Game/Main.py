
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtCore import QTimer

app = QApplication(sys.argv)


class Scene(QWidget):
    def __init__(self, x=600, y=400, speed=33, title="My Game"):
        super().__init__()

        self.setGeometry(50, 50, x, y)
        self.setWindowTitle(title)

        self.speed = speed

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTask)

    def start(self):
        self.timer.start(self.speed)

    def stop(self):
        self.timer.stop()

    def paintEvent(self, event):
        self.updateGame()

    # This should be overridden by your game
    def updateTask(self):
        self.update()



class Sprite():
    def __init__(self, thisScene, imageFile, xSize, ySize):
        self.width = xSize
        self.height = ySize
        self.animation = False
        self.scene = thisScene
        self.x = 0
        self.y = 0

        # Load our file
        self.file = QImage(imageFile)

    def update(self, offX=0, offY=0):
        self.draw(offX, offY)

    def draw(self, offX, offY):
        drawX = self.x - int(self.width / 2) - offX
        drawY = self.y - int(self.height / 2) - offY
        qp = QPainter(self.scene)
        qp.drawImage(drawX, drawY, self.file, )




class Game(Scene):
    def __init__(self):
        super().__init__(600, 600)
        self.spaceship = Sprite(self, "spaceship100.png", 100, 93)
        self.spaceship.y = 200
        self.spaceship.dx = 1
        self.spaceship.dy = 1


    def updateGame(self):
        print("My Update")
        self.spaceship.x += 2
        self.spaceship.y += 1

        # paint sprites
        self.spaceship.update()


myGame = Game()
myGame.start()
myGame.show()
sys.exit(app.exec_())

# Sean's Sprite Sheet
# https://opengameart.org/content/cat-fighter-sprite-sheet
# Cat by DogChicken @ OpenGameArt.org

# Lucas' sprite sheet
# https://opengameart.org/content/esquire-animated-classic-hero-edit
# Knight by Umz @http://umzgames.com/
# villan: https://opengameart.org/content/monster-green
# by PiXeRaT @ OpenGameArt.org

# Siqi's sprite sheet
# https://opengameart.org/content/wizard-warrior----hero
# https://opengameart.org/content/dark-alchemyst----villain


# Qingyun's sprite sheet
# https://opengameart.org/content/cute-monster-sprite-sheet(hero)
# https://opengameart.org/content/skull-monster-sprite-sheet(villain)


# Anthony's sprite sheet
# https://opengameart.org/content/dog-platformer-fighter
# No attribution needed

#
# Justin's sprite sheet
#

# By PixElthen


# Alex's sprite sheet
# https://opengameart.org/content/dude-with-arms
# by Iwan Gabovitch

