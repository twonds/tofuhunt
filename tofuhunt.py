#!/usr/bin/env python
"""
Copyright 2001-2006 Christopher Zorn [zorncj@Musc.edu]

This file is part of Tofuhunt.

    Tofuhunt is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    Tofuhunt is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Tofuhunt; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

"""
import sys, os
import gfx,sound,music,pictures,thetofu,high_scores,menu

import pygame
from pygame.locals import *
from datetime import datetime

def init():
    global background,title,clock
    #Initialize Everything
    pygame.init()
    gfx.init()   
    # load some global images
    background,back_rect = gfx.load_image("background.png")
    title,title_rect = gfx.load_image("title.png")
    gfx.screen.blit(background,(0,0))
    gfx.screen.blit(title,(120,20))
    pygame.display.flip()
    # load and set some defaults
    game_state = 0
    clock = pygame.time.Clock()
    #load some global sounds

    # load some music

    # wait till mouse is clicked or loops interates 1000 times
    i = 0
    while 1:
        clock.tick(60)
        if i==200: return
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                return                
        gfx.screen.blit(background,(0,0))
        gfx.screen.blit(title,(120,20))
        pygame.display.flip()
        i = i + 1

def game_menu():
    global screen,background,title,clock
    menu.buttons = ['new_game.png','exit.png']
    menu.hotspots = [(200,410),(510,410)]
    menu.actions = ['new_game','exit']
    menu.direction = "horizontal"
    menu.position = (400,400)
    gfx.screen.blit(background,(0,0))
    gfx.screen.blit(title,(120,20))
    pygame.display.flip()
    return menu.display()
    
def init_game():
    global score,time, last_ttime, level,picture,hints,background,small_title
    global exit,exit_rect,score_time,level_img,hint_bar,hint_x,num_correct
    #global first,second,third,fourth,fifth
    num_correct = [1,2,3,4,5]
    score = 0
    time = 1250
    last_ttime = datetime.now()
    "load picture list "
    picture = pictures.Pictures()
    
    level = 1
    hints = 3
    "load up the images"
    small_title,small_title_rect = gfx.load_image("small_title.png")
    exit,exit_rect = gfx.load_image("menu.png")
    score_time,score_time_rect = gfx.load_image("score_time.png")
    level_img,level_img_rect = gfx.load_image("level.png")
    hint_bar,hint_bar_rect = gfx.load_image("hint_bar.png")
    hint_x,hint_x_rect = gfx.load_image("hint_x.png")
    
    "draw everything"
    gfx.screen.blit(background,(0,0))
    gfx.screen.blit(small_title,(20,20))
    gfx.screen.blit(exit,(580,500))
    gfx.screen.blit(score_time,(530,30))
    gfx.screen.blit(level_img,(350,30))
    gfx.screen.blit(hint_bar,(530,115))
    picture.get_pic()
    picture.draw_pics()

    #pygame.display.flip()

def next_level():
    global score,time,last_ttime,level,picture,hints,background,small_title
    global exit,exit_rect,score_time,level_img,hint_bar,hint_x,num_correct
    #global first,second,third,fourth,fifth
    num_correct = [1,2,3,4,5]
    time = 1250
    last_ttime = datetime.now()
    level = level + 1
      
    "draw everything"
    gfx.screen.blit(background,(0,0))
    gfx.screen.blit(small_title,(20,20))
    gfx.screen.blit(exit,(580,500))
    gfx.screen.blit(score_time,(530,30))
    gfx.screen.blit(level_img,(350,30))
    gfx.screen.blit(hint_bar,(530,115))
    
    picture.get_pic()
    picture.draw_pics()

def hit_hint(clicked):
    hint_rect = Rect(580,120,290,62)
    hitbox = hint_rect.inflate(-5, -5)
    return hitbox.collidepoint(clicked)

def hit_exit(target,clicked):
    target.topleft = (580,500)
    hitbox = target.inflate(-5, -5)
    return hitbox.collidepoint(clicked)
    

def game_loop():
    global clock,last_ttime, score,time,level,picture,hints,background,small_title
    global exit,exit_rect,score_time,level_img,hint_bar,hint_x
    #global first,second,third,fourth,fifth
    " play tofuhunt, it rocks :) "
    
    init_game()

    while 1:
        clock.tick(60)
        if hints == 0:
            gfx.screen.blit(hint_x,(602,132))
            gfx.screen.blit(hint_x,(654,132))
            gfx.screen.blit(hint_x,(708,132))
        elif hints == 1:
            gfx.screen.blit(hint_x,(654,132))
            gfx.screen.blit(hint_x,(708,132))
        elif  hints == 2:  
            gfx.screen.blit(hint_x,(708,132))

        # draw level and score and time
        gfx.screen.blit(score_time,(530,30))
        if pygame.font:            
            font = pygame.font.Font("data/fonts/font.ttf", 18)
            text = font.render(str(level), 1, (255, 10, 10))
            gfx.screen.blit(text, (391,70))
            font = pygame.font.Font("data/fonts/font.ttf", 14)
            text = font.render(str(score), 1, (255, 10, 10))
            gfx.screen.blit(text, ((740-(len(str(score))*5)),50))

        ttime = datetime.now()
        ttime = int((ttime.hour*60*60)+(ttime.minute*60)+ttime.second)
        lttime = int((last_ttime.hour*60*60)+(last_ttime.minute*60)+last_ttime.second)
                
        time_delta = ttime - lttime 
        
        j = 0
        while j<(time/10):
            red_bar,red_bar_rect= gfx.load_image("bar.png")        
            gfx.screen.blit(red_bar,(625+j,82))
            
            j = j + 1
            
        if_hit = 0
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                return 'exit' 
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return 'main_menu'
            elif event.type == MOUSEBUTTONDOWN:
                if picture.is_diff(pygame.mouse.get_pos()):
                    score = score + 100;
                    if_hit = 1
                    break
                elif hit_hint(pygame.mouse.get_pos()):
                    if_hit = 1
                    # draw the hint pics
                    if hints>0:
                        if hints == 1:
                            gfx.screen.blit(hint_x,(602,132))
                            hints = hints - 1
                        elif hints == 2:
                            gfx.screen.blit(hint_x,(654,132))
                            hints = hints - 1
                        elif hints == 3:
                            gfx.screen.blit(hint_x,(708,132))
                            hints = hints - 1
                            
                        picture.next_diff()
                    break
                elif hit_exit(exit_rect,pygame.mouse.get_pos()):
                    return 'main_menu'
        if if_hit == 0:
            time = time - time_delta
        else :
            if_hit = 0
        last_ttime = datetime.now()
        if picture.num_correct == 5:
            great,great_rect = gfx.load_image("great.png",(10,10,10))
            gfx.screen.blit(great,(325,230))
            pygame.display.flip()
            pygame.time.delay(1000)
            next_level()
            continue

        if time <= 0:  
            game_over,go_rect = gfx.load_image("game_over.png",(10,10,10))
            gfx.screen.blit(game_over,(325,230))
            pygame.display.flip()
            pygame.time.delay(800)
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    return 'main_menu'
        else :
            time = time - (level+time_delta)
    
    
        # draw level and score and time
        gfx.screen.blit(score_time,(530,30))
        if pygame.font:            
            font = pygame.font.Font("data/fonts/font.ttf", 18)
            text = font.render(str(level), 1, (255, 10, 10))
            gfx.screen.blit(text, (391,70))
            font = pygame.font.Font("data/fonts/font.ttf", 14)
            text = font.render(str(score), 1, (255, 10, 10))
            gfx.screen.blit(text, ((740-(len(str(score))*5)),50))
                
        j = 0
        while j<(time/10):
            red_bar,red_bar_rect= gfx.load_image("bar.png")        
            gfx.screen.blit(red_bar,(625+j,82))
            #pygame.display.update(625+j,82,red_bar_rect.width,red_bar_rect.height)
            j = j + 1
        
        pygame.display.flip()
        pygame.time.delay(1)

def main():
    global screen,background,title,clock
    # go through some intro stuff
    init()
    tofu_intro = thetofu.Tofu()
    tofu_intro.start(background)
    action = game_menu()
    
    while 1:
        if action == 'new_game':
            action = game_loop()
            continue
        elif action == 'main_menu':
            action = game_menu()
            continue
        elif action == 'exit':
            # quit the game?
            pygame.quit()
            return       
        else :
            print "Error in game"
            pygame.quit()
            return
    

if __name__ == '__main__': main()

