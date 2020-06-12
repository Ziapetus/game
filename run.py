import pygame


class Carrace():
    def __init__(self):
        pygame.init()
        self.gold = (255, 251, 0)
        self.black = (0, 0, 0)
        self.speed = 0
        self.spd = [0, 0]
        self.angle = 360
        self.run()

# 背景初始化
    def bginit(self):
        bgsize = width, height = 600, 400
        bgcolor = self.black
        self.screen = pygame.display.set_mode(bgsize)
        pygame.display.set_caption('wild race')

# 跑道初始化
    def roadinit(self):

        rlist = [(100, 100), (500, 100), (500, 300), (100, 300)]
        road1 = pygame.draw.lines(self.screen, self.gold, True, rlist, 50)
        corner1 = pygame.draw.circle(self.screen, self.gold, (100, 100), 25)
        corner2 = pygame.draw.circle(self.screen, self.gold, (500, 100), 25)
        corner3 = pygame.draw.circle(self.screen, self.gold, (500, 300), 25)
        corner4 = pygame.draw.circle(self.screen, self.gold, (100, 300), 25)

# 赛车初始化
    def initcar(self):
        self.car = pygame.image.load('./car.png')
        carrect = self.car.get_rect()
        carrect = carrect.move(90, 200)
        self.pos = [90, 200]
        self.newcar = pygame.transform.rotate(self.car, self.angle)

        self.newrect = self.newcar.get_rect(center=carrect.center)

        self.screen.blit(self.car, carrect)

# 更新赛车位置
    def updatecar(self):
        self.spd = self.carmove(self.speed, self.angle)
        self.newcar = pygame.transform.rotate(self.car, self.angle)
        self.newrect = self.newcar.get_rect(center=self.newrect.center)
        self.newrect = self.newrect.move(self.spd)
        self.pos[0] += self.spd[0]
        self.pos[1] += self.spd[1]

# 赛车移动控制（偷懒版）
    def carmove(self, a, b):
        b0, b1 =0, 0
        while b < 0:
            b += 360
        while b > 360:
            b -= 360

        if b > 180 and b < 360:
            b0 = 1
        elif b > 0 and b <180:
            b0 = -1
        elif b == 360 or b ==180:
            b0 = 0
        if b > 90 and b < 270:
            b1 = 1
        elif b == 90 or b == 270:
            b1 = 0
        elif b != 90 or b != 270:
            b1 = -1


        return [a*b0, a*b1]

# 运行
    def run(self):
        self.bginit()

        self.initcar()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit('退出')
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.angle -= 45

                    elif event.key == pygame.K_LEFT:
                        self.angle += 45

                    elif event.key == pygame.K_UP and self.speed < 4:
                        self.speed += 1
                    elif event.key == pygame.K_DOWN and self.speed > 0:
                        self.speed -= 1


            self.updatecar()
            posPix = list(self.screen.get_at(self.pos))[0:3]
            if posPix == [0, 0, 0]:
                self.speed = 0
                self.angle = 360
                self.initcar()
            self.screen.fill(self.black)
            self.roadinit()



            self.screen.blit(self.newcar, self.newrect)
            pygame.display.update()
            fclock = pygame.time.Clock()
            fclock.tick(100)







if __name__ == '__main__':

    Carrace()




