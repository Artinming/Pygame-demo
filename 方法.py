import pygame
def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen = pygame.display.get_surface() #req'd when function moved into MyLibrary
    screen.blit(imgText, (x,y))
class man():
        def __init__(self,image,num1,num2=1):
                self.image = image
                self.num1 = num1 #设置帧数，示例图片有6帧
                self.num2 = num2
                self.rect = image.get_rect()#获取全图的框体数据，以此计算单帧框体
                self.rect.width //= num1
                self.rect.height //= num2
                #设置刷新率，数字越大刷新率越高，但因为示例图片只有6帧所以建议设低一点 否则闪的太凶
                self.thx=0
                self.thy=0
 
        def bian(self):
                if self.thx < self.num1:
                    self.rect.x = self.rect.width * self.thx 
                    self.thx += 1
                else:
                    self.thx = 0
                    
                if self.thy < self.num2:
                    self.rect.y = self.rect.height * self.thy
                    self.thy += 1
                else:
                    self.thy = 0

class kun(object):
    """
    云层对象
    """
    def __init__(self,ww, x, y):
        self.image = ww
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        self.rect.x -= 3  # 云层移动
        if self.rect.x < -400:  # 超出边界后重新在屏幕最右边绘制云层
            self.rect.x = 0


class huoqiu(pygame.sprite.Sprite):
    def __init__(self,image,speed,pinmu,x,y):

        super(huoqiu, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = speed
        self.pinmu = pinmu
        self.x = x
        self.y = y
    def update(self):
        self.x += self.speed
        if self.x <= -20:
            self.kill()
        if self.x >= 800 - 40 + 20:
            self.kill()
        self.pinmu.blit(self.image,(self.x,self.y))
