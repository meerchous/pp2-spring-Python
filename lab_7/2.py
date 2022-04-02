import pygame

pygame.init()
screen = pygame.display.set_mode((600,500))
screen.fill((128,128,128))
done = False
clock = pygame.time.Clock()
Playlist = pygame.USEREVENT +  1
tracklist = ['1.mp3', '2.mp3', '3.mp3']
pygame.mixer.music.set_endevent(Playlist)
current = 0 
pygame.mixer.music.load( '1.mp3' )
pygame.mixer.music.play()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.mixer:
            print('The song ended!')
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]: pygame.mixer.music.pause()
    if pressed[pygame.K_LCTRL]:
        pygame.mixer.music.unpause()
    if pressed[pygame.K_RIGHT]:
        if current >= 2:
            current = 0
            pygame.mixer.music.load(tracklist[current])
            pygame.mixer.music.play()
        else:
            current += 1
            pygame.mixer.music.load(tracklist[current])
            pygame.mixer.music.play()
    if pressed[pygame.K_LEFT]:
        if current <= 0:
            current = 2
            pygame.mixer.music.load(tracklist[current])
            pygame.mixer.music.play()
        else:
            current -= 1
            pygame.mixer.music.load(tracklist[current])
            pygame.mixer.music.play()
    if pressed[pygame.K_UP]:
        pygame.mixer.music.set_volume(1.5)
    if pressed[pygame.K_DOWN]:
        pygame.mixer.music.set_volume(0.5)  
    clock.tick(10)
