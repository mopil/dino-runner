from pygame import init
from pygame.time import delay
import main
from settings import *
import sys
import game

class GameOver:
    score = 0
    result_score = 0 
    rank = '???'
    timing = 0

    #temporary
    result_rank = 32
    high = 300
    time_delay = 10
    result_state = False

    def init():
        GameOver.score = 0
        GameOver.rank = "???"
        GameOver.timing = 0
        GameOver.time_delay = 10
        GameOver.result_state = False

    def saveScore(score):
        GameOver.result_score = score

    def over(gui):
        surface.fill((255, 255, 255))
        screen.blit(surface, (0, 0))
        cactus_obj.drawAll(screen)
        terrain_obj.drawAll(screen)
        screen.blit(rex_over, (rex.player.x, 245))
        gui.display_game_over()
        gui.display_game_retry()

    def overRun():
        GameOver.init()
        #sound_finish.play()
        while True:
            surface.fill((255, 255, 255))
            screen.blit(surface, (0, 0))
            over = pygame.Rect(280, 20, 230, 70)
            text = pygame.Rect(170, 40, 460, 280)
            pygame.draw.rect(screen, DKGRAY, text)
            pygame.draw.rect(screen, LTGRAY, over)
            GameOver.display_result(gui)

            #exit = pygame.Rect(640, 270, 53, 40)
            #retry = pygame.Rect(110, 260, 45, 48)
            #pygame.draw.rect(screen, LTGRAY, exit)
            #pygame.draw.rect(screen, DKGRAY, retry)

            if GameOver.result_state == True:
                textsurface_retry = gui.font.render(f'Retry', False ,(0,0,0))
                gui.screen.blit(textsurface_retry, (90, 300))
                textsurface_retry = gui.font.render(f'Exit', False ,(0,0,0))
                gui.screen.blit(textsurface_retry, (640, 300))
            terrain_obj.drawAll(screen)
            screen.blit(rex_over, (rex.player.x, 245))
            screen.blit(cactus, (rex.player.x + 540, 268))
            gui.display_game_over()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    location = pygame.mouse.get_pos()
                    if location[0] >= 110 and location[0] <= 155 and location[1] >= 260 and location[1]<=308:
                        return "gamerun"
                    if location[0] >= 640 and location[0] <= 693 and location[1] >= 270 and location[1]<=310:
                        return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_x:
                        return "quit"
                if event.type == pygame.QUIT :
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
                            
    def display_result(gui):
        text_rank = gui.font.render(f'Your Rank : {GameOver.rank}', False, (0, 0, 0))
        gui.screen.blit(text_rank, (290, 110))
        text_score = gui.font.render(f'Your Score : {GameOver.score}' , False, (0, 0, 0))
        gui.screen.blit(text_score, (285, 180))
        text_score = gui.font.render(f'Your Highest Score : {GameOver.high}' , False, (0, 0, 0))
        gui.screen.blit(text_score, (220, 250))
        delay(GameOver.time_delay)
        if(GameOver.score < GameOver.result_score):
            if(GameOver.result_score > 1000):
                GameOver.time_delay -= int(GameOver.time_delay * 2/3)
            else:
                GameOver.time_delay -= int(GameOver.time_delay * 2/5)
            GameOver.score += 0.5
        if(GameOver.score == GameOver.result_score):
            GameOver.timing += 1
            if(GameOver.timing == 3):
                delay(500)
                GameOver.rank = "{}".format(GameOver.result_rank)
                sound_jump.play()
            if(GameOver.score > GameOver.high and GameOver.timing == 5):
                delay(500) 
                GameOver.high = GameOver.score   
                sound_jump.play()
            if(GameOver.timing == 7):
                delay(500)
                GameOver.result_state = True
                sound_jump.play()
                