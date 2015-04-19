# import div for "proper" no floor division
from __future__ import division

# import globals
import Client_GlobalData
import Client_GlobalData_Config
import Client_Cade_Data

# import pygame and other python mods
import pygame
import pygame.mixer
mixer = pygame.mixer
import wx
from pygame.locals import *

if Client_GlobalData.DEBUG_APP == True:
    # import gui modules
    from ocempgui.widgets import *
    from ocempgui.widgets.components import TextListItem
    from ocempgui.widgets.Constants import *

# import code
import Client_Cade_Cursors

def SetCursor(cursor_type):
    hotspot = None
    for y in range(len(cursor_type)):
        for x in range(len(cursor_type[y])):
            if cursor_type[y][x] in ['x', ',', 'O']:
                hotspot = x,y
                break
        if hotspot != None:
            break
    if hotspot == None:
        raise Exception("No hotspot specified for cursor '%s'!" %cursor_type)
    s2 = []
    for line in cursor_type:
        s2.append(line.replace('x', 'X').replace(',', '.').replace('O','o'))
    cursor, mask = pygame.cursors.compile(s2, 'X', '.', 'o')
    size = len(cursor_type[0]), len(cursor_type)
    pygame.mouse.set_cursor(size, hotspot, cursor, mask)

def cade_main():
    #initialize and prepare screen
    pygame.init()
    mainClock = pygame.time.Clock()
    pygame.font.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print ('Warning, no sound')
        pygame.mixer = None
    # grab the layout from sqldb for the system selected or general if has more than one type of roms in list?
    # to code

    layout_directory = "./layouts/retro_black_1024x768/"
    # open and load layout file into list
    file_handle = open(layout_directory + "layout.lay")
    layout_file_lines = file_handle.readlines()
    file_handle.close
    # set main window size
    screen = pygame.display.set_mode((int(layout_file_lines[0]),int(layout_file_lines[1])), 0, 24)
    pygame.display.set_caption('MameHub Arrange Hub!Cade')
    if Client_GlobalData.DEBUG_APP == True:
        # create GUI object
        gui = Renderer()
        gui.screen = screen
    # background filler
    screen.fill(Color(int(layout_file_lines[2])))
    # load background image
    background_img = pygame.image.load(layout_directory + layout_file_lines[3].strip())


    # set up the fonts
##    smallFont = pygame.font.SysFont(None, 20)
##    basicFont = pygame.font.SysFont(None, 24)
##    titleFont = pygame.font.SysFont(None, 48)
##    guessFont = pygame.font.SysFont(None, 36)
##    bannerFont = pygame.font.SysFont(None, 64)

    # preload images
    image_mh = pygame.image.load("../images/mh.png")
    image_mh = pygame.transform.scale(image_mh,(100,100))

    #main game loop
    done = 0
    SetCursor(Client_Cade_Cursors.cursor_arrow)
    while not done:
##        text = basicFont.render("Test data", True, Client_Cade_Data.BLUE,Client_Cade_Data.WHITE)
##        screen.blit(text, (350,130))
        screen.blit(background_img, (0,0))

        #pygame.draw.circle(screen, Client_Cade_Data.WHITE, (500,157),32,0)
        screen.blit(image_mh, (10,10))
        screen.blit(image_mh, (10,(int(layout_file_lines[1]) - 110)))

        pygame.display.update()
        if Client_GlobalData.DEBUG_APP == True:
            # Draw GUI
            gui.update()
            #gui.draw(gui.screen)

        mainClock.tick(50)
        for event in pygame.event.get():
            if event.type == QUIT:
                done = 1
                break
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    done = 1
                    break
                # player one joystick
                if event.key == K_UP:  # up arrow
                    pass
                elif event.key == K_DOWN:  # down arrow
                    pass
                elif event.key == K_RIGHT:  # right arrow
                    pass
                elif event.key == K_LEFT:  # left arrow
                    pass
                # player 1 buttons
                elif event.key == K_LCTRL:  # button 1
                    pass
                elif event.key == K_LALT:  # button 2
                    pass
                elif event.key == K_SPACE:  #button 3
                    pass
                elif event.key == K_LSHIFT:  #button 4
                    pass
                elif event.key == K_Z:  #button 5
                    pass
                elif event.key == K_X:  #button 6
                    pass
                elif event.key == K_1:  # button start one players
                    pass
                # player 2 joystick
                elif event.key == K_R: # up
                    pass
                elif event.key == K_F: # down
                    pass
                elif event.key == K_D: # left
                    pass
                elif event.key == K_G: # right
                    pass
        if Client_GlobalData.DEBUG_APP == True:
            # pass event to gui
            gui.distribute_events((event))

    pygame.mixer.quit()
    pygame.font.quit()
    pygame.quit()
    #exit()
