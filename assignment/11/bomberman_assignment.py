"""
Team Member(s), ordered by contribution:
Features Added:
    1. Junhao Guo
    2.
"""
from animations import QtGui, QtCore, QApplication, QSound, AnimatedScene, AnimatedItem, MessageItem
import random
import glob

blockCoordinates = [(0, 64*4), (64*1, 64*2), (64*1, 64*3), (64*2, 64*4), (64*3, 0), (64*3, 64*1), (64*3, 64*1), (64*3, 64*7)]

class Bomberman(AnimatedItem):
    def __init__(self, scene, x=0, y=0):
        super().__init__(scene, x, y)
        self.animations.add("down", glob.glob("Sprites/Bomberman/Front/*"), interval=25)
        self.animations.add("up", glob.glob("Sprites/Bomberman/Back/*"), interval=25)
        self.animations.add("right", glob.glob("Sprites/Bomberman/Side/*"), interval=25)
        self.animations.add("left", glob.glob("Sprites/Bomberman/Side/*"), interval=25, horizontal_flip=True)
        self.animations.add("flash", [glob.glob("Sprites/Bomberman/Front/*")[0], None] * 4, interval=100)
        self.set_default_image("down")
        # only the lower part (defined by collision_rect) of Bomberman can collide with other sprites
        self.collision_rect = QtCore.QRect(10, self.image.height() // 3 * 2, self.image.width() - 20, self.image.height() // 3)
        self.setZValue(9999)  # bomberman is always on top of other sprites
        
        #properties
        self.speed = 8  # how many pixels to move per frame
        self.timer = QtCore.QTimer()  #set a timer to avoid contiuously placing bomb
        self.timer.timeout.connect(self.updateTimer)
        self.startTimer()

    def startTimer(self):
        self.timer.start(2000)
    def updateTimer(self):
        self.placeOk = True

    def move_left(self):
        self.setX(self.x() - self.speed)
    def move_right(self):
        self.setX(self.x() + self.speed)
    def move_up(self):
        self.setY(self.y() - self.speed)
    def move_down(self):
        self.setY(self.y() + self.speed)
    def place_bomb(self):
        if self.placeOk:
            Bomb(self.scene, self.x() + self.collision_rect.x(), self.y() + self.collision_rect.y())
            self.placeOk = False
            self.startTimer()
        else:
            pass

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Up:
            if self.y()-64 < self.y()+64-8*self.speed >= 0:
                self.animations.play("up", on_transition=self.move_up)
        if key == QtCore.Qt.Key_Down:
            if self.y()+128 < self.scene.height():
                self.animations.play("down", on_transition=self.move_down)
        if key == QtCore.Qt.Key_Left:
            if (self.x() > 0):
                self.animations.play("left", on_transition=self.move_left)
        if key == QtCore.Qt.Key_Right:
            if self.x()+64 < self.scene.width():
                self.animations.play("right", on_transition=self.move_right)
        if key == QtCore.Qt.Key_Return:
            self.place_bomb()
        if key == QtCore.Qt.Key_Enter:
            self.place_bomb()

    def on_collision(self, other):
        if isinstance(other, Flame):
            # if a Bomberman is hit by a flame, he will be destroyed
            self.destroy()
        if isinstance(other, Block):
            self.setX((self.x()+32)//64*64)
            self.setY((self.y()+32)//64*64)

    def destroy(self):
        self.animations.play("flash", on_completion=super().destroy)
        message = MessageItem(self.scene)
        message.add("Player 2 Won!")

class Creep(AnimatedItem):
    def __init__(self, scene, x=0, y=0):
        super().__init__(scene, x, y)
        self.animations.add("down", glob.glob("Sprites/Bomberman/Front/*"), interval=25)
        self.animations.add("up", glob.glob("Sprites/Bomberman/Back/*"), interval=25)
        self.animations.add("right", glob.glob("Sprites/Bomberman/Side/*"), interval=25)
        self.animations.add("left", glob.glob("Sprites/Bomberman/Side/*"), interval=25, horizontal_flip=True)
        self.animations.add("flash", [glob.glob("Sprites/Bomberman/Front/*")[0], None] * 4, interval=100)
        self.set_default_image("down")
        self.collision_rect = QtCore.QRect(10, self.image.height() // 3 * 2, self.image.width() - 20, self.image.height() // 3)
        self.setZValue(9998)  # bomberman is always on top of other sprites

        #properties
        self.speed = 8  # how many pixels to move per frame
        self.timer = QtCore.QTimer()  #set a timer to avoid contiuously placing bomb
        self.timer.timeout.connect(self.updateTimer)
        self.startTimer()

    def startTimer(self):
        self.timer.start(2000)
    def updateTimer(self):
        self.placeOk = True

    def move_left(self):
        self.setX(self.x() - self.speed)

    def move_right(self):
        self.setX(self.x() + self.speed)

    def move_up(self):
        self.setY(self.y() - self.speed)

    def move_down(self):
        self.setY(self.y() + self.speed)

    def place_bomb(self):
        if self.placeOk:
            Bomb(self.scene, self.x() + self.collision_rect.x(), self.y() + self.collision_rect.y())
            self.placeOk = False
            self.startTimer()
        else:
            pass

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_W:
            if self.y()-64 < self.y()+64-8*self.speed >= 0:
                self.animations.play("up", on_transition=self.move_up)
        if key == QtCore.Qt.Key_S:
            if self.y()+128 < self.scene.height():
                self.animations.play("down", on_transition=self.move_down)
        if key == QtCore.Qt.Key_A:
            if (self.x() > 0):
                self.animations.play("left", on_transition=self.move_left)
        if key == QtCore.Qt.Key_D:
            if self.x()+64 < self.scene.width():
                self.animations.play("right", on_transition=self.move_right)
        elif key == QtCore.Qt.Key_Space:
            self.place_bomb()

    def on_collision(self, other):
        if isinstance(other, Flame):
            self.destroy()
        if type(other) == Block:
            self.setX((self.x()+32)//64*64)
            self.setY((self.y()+32)//64*64)

    def destroy(self):
        self.animations.play("flash", on_completion=super().destroy)
        message = MessageItem(self.scene)
        message.add("Player 1 Won!")

class Block(AnimatedItem):
    def __init__(self, scene, x=0, y=0):
        super().__init__(scene, x, y)
        self.animations.add("block", ["Sprites/Blocks/SolidBlock.png"], non_stop=False)
        self.set_default_image("block")

class Bomb(AnimatedItem):
    def __init__(self, scene, x=0, y=0):
        super().__init__(scene, x//64*64, y//64*64)
        self.animations.add("bomb", glob.glob("Sprites/Bomb/*"), repeat=3, interval=300)
        self.set_default_image("bomb")
        self.animations.play("bomb", on_completion=self.explode)
        self.explosion_sound = QSound("bomb_explosion.wav")

    def explode(self):
        self.explosion_sound.play()
        self.destroy()
        # flame settings
        Flame(self.scene, self.x(), self.y())
        Flame(self.scene, self.x(), self.y()+64)
        Flame(self.scene, self.x(), self.y()-64)
        Flame(self.scene, self.x()+64, self.y())
        Flame(self.scene, self.x()-64, self.y())

    # def checkBlock(self, x, y):
    #     okayToPlace = True
    #     for blockX, blockY in blockCoordinates:
    #         if x == blockX+8 and y == blockY+8:
    #             okayToPlace = False
    #     return okayToPlace

class Flame(AnimatedItem):
    def __init__(self, scene, x=0, y=0):
        super().__init__(scene, x, y)
        self.animations.add("flame", glob.glob("Sprites/Flame/*"), interval=250)
        self.set_default_image("flame")
        self.animations.play("flame", on_completion=self.destroy)
        self.collidable = False

if __name__ == "__main__":
    app = QApplication([])
    scene = AnimatedScene(640, 640)
    scene.setBackgroundBrush(QtGui.QColor(200, 250, 200))  # set background color

    # placing players
    Bomberman(scene, 0, 0)
    Creep(scene, 64*9, 64*9)

    #placing blocks
    Block(scene, 0, 64*4)
    Block(scene, 64*1, 64*2)
    Block(scene, 64*1, 64*3)
    Block(scene, 64*1, 64*4)
    Block(scene, 64*2, 64*4)
    Block(scene, 64*3, 0)
    Block(scene, 64*3, 64*1)
    Block(scene, 64*3, 64*7)
    Block(scene, 64*4, 64*1)
    Block(scene, 64*4, 64*3)
    Block(scene, 64*4, 64*4)
    Block(scene, 64*4, 64*6)
    Block(scene, 64*4, 64*7)
    Block(scene, 64*4, 64*8)
    Block(scene, 64*4, 64*9)
    Block(scene, 64*5, 64*1)
    Block(scene, 64*5, 64*7)
    Block(scene, 64*6, 64*3)
    Block(scene, 64*7, 64*3)
    Block(scene, 64*7, 64*4)
    Block(scene, 64*7, 64*5)
    Block(scene, 64*8, 64*3)
    Block(scene, 64*9, 64*3)


    app.exec()
