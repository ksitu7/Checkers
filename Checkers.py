import pygame
import pygame_gui
from Checkers_Window.constants import SQUARE_SIZE, WIDTH, HEIGHT, RED, WHITE
from Checkers_Window.game import Game
from minimax.algorithm import minimax

pygame.init()

pygame.display.set_caption('Menu')

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.Surface((WIDTH, HEIGHT))
background.fill(pygame.Color('#000000'))
manager = pygame_gui.UIManager((WIDTH,HEIGHT))

pvp = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((330, 275), (150, 50)), text='Player vs. Player', manager=manager)
pva = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((330, 350), (150, 50)), text='Player vs. AI', manager=manager)
quitGame = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((330, 500), (150, 50)), text='Quit', manager=manager)
#rematch = None

clock = pygame.time.Clock()
is_running = True

gamemode = ""

def get_rol_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    pygame.display.set_caption('Checkers')
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while(run):
        clock.tick(FPS)

        if(gamemode == "pva"):
            if game.turn == WHITE:
                pygame.time.delay(100)
                value, new_board = minimax(game.get_board(), 3,WHITE, game)
                game.ai_move(new_board)
        
        if game.winner() != None:
            if(game.winner() == (255,0,0)):
                print("RED WINS!")
            else:
                print("WHITE WINS!")
            #rematch = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((330, 275), (150, 50)), text='Rematch?', manager=WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if(pos[0] > 800):
                    pass
                else:
                    row, col = get_rol_col_from_mouse(pos)
                    game.select(row,col)


        game.update()
        
    pygame.quit()


while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == pvp:
                    gamemode = "pvp"
                    main()
                if event.ui_element == pva:
                    gamemode = "pva"
                    main()
                #if event.ui_element == rematch:
                #    main()
                if event.ui_element == quitGame:
                    pygame.quit()

        manager.process_events(event)
    manager.update(time_delta)

    WIN.blit(background, (0, 0))
    manager.draw_ui(WIN)

    pygame.display.update()
#pygame.quit()