import pygame

pygame.init()
pygame.display.set_caption("Some Title Goes Here")
canvas = pygame.display.set_mode((1200, 800))


def main():
    my_font = pygame.font.SysFont('Calibri', 20)
    rendered_text = my_font.render('This is some text', True, (0, 0, 255))
    canvas.blit(rendered_text, (200, 200))

    pygame.draw.rect(canvas, (255, 255, 255), (300, 300, 50, 50))

    points = [(400, 400), (400, 500), (500, 500), (500, 400), (450, 330), (400, 400)]
    pygame.draw.aalines(canvas, (0, 255, 0), True, points)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                canvas.fill((0, 0, 0))
                rendered_text = my_font.render('You clicked at '+str(event.pos), True, (0, 255, 0))
                canvas.blit(rendered_text, (300, 300))
        pygame.display.update()


main()
