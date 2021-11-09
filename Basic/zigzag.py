import pygame
pattern = '*' * 8
while True:
    for i in range(4,0,-1):
        pattern2 = ' ' * i
        print(pattern2, end='')
        print(pattern)
        pygame.time.delay(100)
    for i in range(0,4):
        pattern2 = ' ' * i
        print(pattern2, end='')
        print(pattern)
        pygame.time.delay(100)