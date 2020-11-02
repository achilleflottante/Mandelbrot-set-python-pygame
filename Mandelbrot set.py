import pygame


pygame.init()
dim = 512

pygame.display.set_caption('Mandelbrot')
screen = pygame.display.set_mode((dim, dim))



def generate_mandelbrot(dim, sizex, sizey, centerx, centery):

    print(sizex, sizey)
    for y in range(512):
        for x in range(512):
            truex = x-(dim/2)
            truey = y-(dim/2)
            c = complex(truex*(sizex/dim)+centerx,truey*(sizey/dim)+centery)
            z = complex(0,0)
            counter = 0
            while abs(z) < 2 and counter < 1000:
                z = c**2+z
                counter += 1
            if abs(z) < 2:
                screen.set_at((x, y), (0, 0, 0))
            else:

                #color = pygame.color.Color(0)
                #hue = (counter)%360
                #saturation =100
                #value = 100
                #alpha = 100
                #color.hsva = (hue,saturation,value,alpha)
                color = (255-(counter*20)%255, 255- (counter*20)%255, 255 )

                screen.set_at((x, y), color)

    screen.set_at((256, 256), (255, 255, 255))

truedim = 4
centerx = 0
centery = 0
X = -0.840719
Y = 0.22442

running = True

while running == True:



    generate_mandelbrot(dim, truedim, truedim, centerx, centery)
    truedim = truedim/2

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()