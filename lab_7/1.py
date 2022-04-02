# import pygame

# pygame.init()
# screen = pygame.display.set_mode((1280,960))
# screen.fill((0,0,0))
# done = False
# image1 = pygame.image.load('Clock.jpg')
# image2 = pygame.image.load('C1.png')
# image3 = pygame.image.load('C2.png')
# clock = pygame.time.Clock()

# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     screen.blit(image1,(0,0))
#     image1.blit(pygame.transform.rotate(image2,-6),(550,350))
#     image1.blit(pygame.transform.rotate(image3,-0.1),(550,350))
     
#     pygame.display.flip()


import pygame
import datetime
width,height = 800, 800
pygame.init()
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption('MICKEY CLOCK')
running = True
image = pygame.image.load('Clock.jpg')
hand1 = pygame.image.load('hand1.png')
hand2 = pygame.image.load('hand2.png')
while running:
    screen.blit(image,(-240,-80))
    key = pygame.key.get_pressed()
    current_time = datetime.datetime.now()
    second = current_time.second
    minute = current_time.minute
    anglesecond = second*6-56
    angleminute = minute*6+50
    img = pygame.transform.rotate(hand1,-anglesecond)
    x = img.get_width()/2
    y = img.get_height()/2
    img2=pygame.transform.rotate(hand2,-angleminute)
    x2 = img2.get_width()/2
    y2 = img2.get_height()/2
    screen.blit(img,(400-int(x),400 -int(y)))
    screen.blit(img2,(400-int(x2), 400-int(y2)))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    pygame.display.flip()