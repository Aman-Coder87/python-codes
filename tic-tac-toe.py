import pygame 

pygame.init()

#screen make
screen = pygame.display.set_mode([550 , 550])


#boxes
first = pygame.draw.rect(screen , (255,255,255) , (25,25,150,150))
second = pygame.draw.rect(screen , (255,255,255) , (200,25,150,150))
third = pygame.draw.rect(screen , (255,255,255) , (375,25,150,150))

fourth = pygame.draw.rect(screen , (255,255,255) , (25,200,150,150))
fifth = pygame.draw.rect(screen , (255,255,255) , (200,200,150,150))
sixth = pygame.draw.rect(screen , (255,255,255) , (375,200,150,150))

seventh = pygame.draw.rect(screen , (255 ,255,255) , (25,375,150,150))
eighth = pygame.draw.rect(screen , (255,255,255) , (200,375,150,150))
ninth = pygame.draw.rect(screen , (255,255,255) , (375,375,150,150))


#game loop
running = True 
while running :
	pygame.time.delay(100)
	
	for event in pygame.event.get() :
		
		if event.type == pygame.QUIT :
			running = False 
			
		if event.type == pygame.BUTTONUP() :
			pos = pygame.click.get_pos()
			
			if first.collidepoint(pos) :
				pygame.draw.rect(screen, (255,0,0) , (50,50,100,100))
	

# screen update					
	pygame.display.update()

pygame.quit()
			
		