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
import gfx,sound,music

import pygame
from pygame.locals import *

class Tofu(pygame.sprite.Sprite):
    " Animate a tofu across the screen "
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.image, self.rect = gfx.load_image('thetofu.bmp', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 30, 30
        self.move = 2
        self.stopped = 0

    def update(self):
        self._move()

    def _move(self):
        "move the tofu across the screen"
        if self.stopped == 100: return # stop moving
        newpos = self.rect.move((self.move, 0))
        self.move = +self.move
        self.stopped = self.stopped + 1
        newpos = self.rect.move((self.move, self.move))
        self.rect = newpos


    def start(self,background):
        clock = pygame.time.Clock()
        thetofu = pygame.sprite.RenderPlain(self)
        if pygame.font:
            font = pygame.font.Font("data/fonts/font.ttf", 36)
            text = font.render("Brought to you buy....", 1, (255, 10, 10))
            gfx.screen.blit(background, (0, 0))
            gfx.screen.blit(text, (30,30))            
            pygame.display.flip()
            pygame.time.delay(900)
        
        while 1:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    return
                elif event.type == MOUSEBUTTONDOWN:
                    return                
                
            thetofu.update()
            gfx.screen.blit(background,(0,0))
            thetofu.draw(gfx.screen)
            if self.stopped == 100:
                font = pygame.font.Font("data/fonts/font.ttf", 36)
                text = font.render(".com", 1, (255, 10, 10))
                gfx.screen.blit(text, (370,322))            
            pygame.display.flip()
            
        
