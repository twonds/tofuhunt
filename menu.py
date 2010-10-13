"""
Copyright 2001-2002 Christopher Zorn [zorncj@Musc.edu]

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
import gfx,sound,music

import pygame
from pygame.locals import *

buttons = []
hotspots = []
actions = []
button_image = []
button_rect = []

direction = "vertical"

position = (0,0) 

def hit_hotspot(target,clicked):
    hitbox = target.inflate(-5, -5)
    return hitbox.collidepoint(clicked)


def display():
    clock = pygame.time.Clock()
    i = 0
    for button in buttons:
        tmp_image,tmp_rect = gfx.load_image(button)
        if i==0:
            button_image = [tmp_image]
            button_rect = [tmp_rect]
        else :
            button_image.append(tmp_image)
            button_rect.append(tmp_rect)
            
        gfx.screen.blit(button_image[i],hotspots[i])
        pygame.display.flip()
        i = i + 1
    while 1:
        clock.tick(60)
        pygame.time.delay(20)
        for event in pygame.event.get():
            if event.type == QUIT:
                return 'exit'
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return 'exit'
            elif event.type == MOUSEBUTTONDOWN:
                # check for hotspots and preform the action
                j = 0
                for button in button_rect:
                    button.topleft = hotspots[j]
                    if hit_hotspot(button,pygame.mouse.get_pos()):
                        return actions[j]                
                    j = j + 1
                
                
