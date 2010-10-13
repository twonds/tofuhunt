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
import sys, os,random,string,xml.dom.minidom
import gfx,sound,music
from xml.dom.minidom import parse, parseString


import pygame
from pygame.locals import *

class Pictures:
    def __init__(self):
        # open images, diff_images, and maps
        # right now we just open brians_house
        self.images = os.listdir("data/pics/")
        self.unused = self.images
        self.diff_dir = os.listdir("data/pics/diff")
        self.map_dir = os.listdir("data/pics/maps/")        
        self.correct = [1,2,3,4,5]
        self.num_correct = 0
        
    def get_pic(self):
        self.correct = [1,2,3,4,5]
        self.num_correct = 0
        j = 0
        random.seed()
        while 1:
            
            if len(self.unused)>0:
                #image = self.images[rand]
                rand =  random.randrange(0,len(self.unused))
                image = self.unused.pop(rand)
                
            elif len(self.unused)<=0:
                self.unused = self.images
                rand =  random.randrange(0,len(self.unused))
                image = self.unused.pop(rand)
                
            name = string.split(image,'.')
            
            if len(name) == 2:
                self.image = image
                self.pic_name = name[0]
                self.map = self.pic_name + ".map"
                self.map = "data/pics/maps/" + self.pic_name + ".map"
                #print self.map
                dom1        = parse(self.map) # parse the XML map
                areas       = dom1.getElementsByTagName("AREA")
                self.first  = areas[0].getAttribute("COORDS")
                self.second = areas[1].getAttribute("COORDS")
                self.third  = areas[2].getAttribute("COORDS")
                self.fourth = areas[3].getAttribute("COORDS")
                self.fifth  = areas[4].getAttribute("COORDS")
                return            
            j = j + 1
        
        
    def draw_pics(self):
        self.diff_image,self.diff_rect = gfx.load_image("pics/diff/"+self.image)
        self.reg_image,self.reg_rect = gfx.load_image("pics/"+self.image)
        gfx.screen.blit(self.reg_image,(20,200))
        gfx.screen.blit(self.diff_image,(403,200))
        

    def is_diff(self,clicked):
        if self.num_correct <5:
            for x in self.correct:
                if x != 0:
                    if x == 1:
                        tmp_arr = string.split(str(self.first),',')
                        first   = int(tmp_arr.pop(0)) + 20
                        second  = int(tmp_arr.pop(0)) + 200
                        third   = int(tmp_arr.pop(0)) - (first-20)
                        fourth  = int(tmp_arr.pop(0)) - (second-200)             
                                                     
                        tmp_rect = Rect(first,second,third,fourth)
                        
                        hitbox = tmp_rect.inflate(+5, +5)
                        if hitbox.collidepoint(clicked):
                            self.correct[0] = 0
                            self.num_correct = self.num_correct + 1
                            pygame.draw.ellipse(gfx.screen, (255,0,0), tmp_rect,3)
                            pygame.draw.ellipse(gfx.screen, (255,0,0),
                                                (first+383,second,third,fourth)
                                                ,3)
                            return 1
                        
                        tmp_arr = string.split(str(self.first),',')
                        first   = int(tmp_arr.pop(0)) + 403
                        second  = int(tmp_arr.pop(0)) + 200
                        third   = int(tmp_arr.pop(0)) - (first-403)
                        fourth  = int(tmp_arr.pop(0)) - (second-200)             
                        
                                      
                        tmp_rect = Rect(first,second,third,fourth)
                        
                        hitbox = tmp_rect.inflate(+5, +5)
                        if hitbox.collidepoint(clicked):
                            self.correct[0] = 0
                            self.num_correct = self.num_correct + 1
                            pygame.draw.ellipse(gfx.screen, (255,0,0), tmp_rect,3)
                            pygame.draw.ellipse(gfx.screen, (255,0,0),
                                                (first-383,second,third,fourth)
                                                ,3)
                            return 1
                    elif x == 2:
                        tmp_arr = string.split(str(self.second),',')
                        first   = int(tmp_arr.pop(0)) + 20
                        second  = int(tmp_arr.pop(0)) + 200
                        third   = int(tmp_arr.pop(0)) - (first-20)
                        fourth  = int(tmp_arr.pop(0)) - (second-200)         
                        tmp_rect = Rect(first,second,third,fourth)
                        
                        hitbox = tmp_rect.inflate(+5, +5)
                        if hitbox.collidepoint(clicked):
                            self.correct[1] = 0
                            self.num_correct = self.num_correct + 1
                            pygame.draw.ellipse(gfx.screen, (255,0,0), tmp_rect,3)
                            pygame.draw.ellipse(gfx.screen, (255,0,0),
                                                (first+383,second,third,fourth)
                                                ,3)
                            return 1
                        
                        tmp_arr = string.split(str(self.second),',')
                        first   = int(tmp_arr.pop(0)) + 403
                        second  = int(tmp_arr.pop(0)) + 200
                        third   = int(tmp_arr.pop(0)) - (first-403)
                        fourth  = int(tmp_arr.pop(0)) - (second-200)             
                                      
                        tmp_rect = Rect(first,second,third,fourth)
                        
                        hitbox = tmp_rect.inflate(+5, +5)
                        if hitbox.collidepoint(clicked):
                            self.correct[1] = 0
                            self.num_correct = self.num_correct + 1
                            pygame.draw.ellipse(gfx.screen, (255,0,0), tmp_rect,3)
                            pygame.draw.ellipse(gfx.screen, (255,0,0),
                                                (first-383,second,third,fourth)
                                                ,3)
                            return 1                        
                    elif x == 3:
                        tmp_arr = string.split(str(self.third),',')
                        first   = int(tmp_arr.pop(0)) + 20
                        second  = int(tmp_arr.pop(0)) + 200
                        third   = int(tmp_arr.pop(0)) - (first-20)
                        fourth  = int(tmp_arr.pop(0)) - (second-200)             
                        
                                      
                        tmp_rect = Rect(first,second,third,fourth)
                        
                        hitbox = tmp_rect.inflate(+5, +5)
                        if hitbox.collidepoint(clicked):
                            self.correct[2] = 0
                            self.num_correct = self.num_correct + 1
                            pygame.draw.ellipse(gfx.screen, (255,0,0), tmp_rect,3)
                            pygame.draw.ellipse(gfx.screen, (255,0,0),
                                                (first+383,second,third,fourth)
                                                ,3)
                            return 1
                        
                        tmp_arr = string.split(str(self.third),',')
                        first   = int(tmp_arr.pop(0)) + 403
                        second  = int(tmp_arr.pop(0)) + 200
                        third   = int(tmp_arr.pop(0)) - (first-403)
                        fourth  = int(tmp_arr.pop(0)) - (second-200)             
                        
                                      
                        tmp_rect = Rect(first,second,third,fourth)
                        
                        hitbox = tmp_rect.inflate(+5, +5)
                        if hitbox.collidepoint(clicked):
                            self.correct[2] = 0
                            self.num_correct = self.num_correct + 1
                            pygame.draw.ellipse(gfx.screen, (255,0,0), tmp_rect,3)
                            pygame.draw.ellipse(gfx.screen, (255,0,0),
                                                (first-383,second,third,fourth)
                                                ,3)
                            return 1                        
                    elif x == 4:
                        tmp_arr = string.split(str(self.fourth),',')
                        first   = int(tmp_arr.pop(0)) + 20
                        second  = int(tmp_arr.pop(0)) + 200
                        third   = int(tmp_arr.pop(0)) - (first-20)
                        fourth  = int(tmp_arr.pop(0)) - (second-200)             
                        tmp_rect = Rect(first,second,third,fourth)
                        
                        hitbox = tmp_rect.inflate(+5, +5)
                        if hitbox.collidepoint(clicked):
                            self.correct[3] = 0
                            self.num_correct = self.num_correct + 1
                            pygame.draw.ellipse(gfx.screen, (255,0,0), tmp_rect,3)
                            pygame.draw.ellipse(gfx.screen, (255,0,0),
                                                (first+383,second,third,fourth)
                                                ,3)
                            return 1
                        
                        tmp_arr = string.split(str(self.fourth),',')
                        first   = int(tmp_arr.pop(0)) + 403
                        second  = int(tmp_arr.pop(0)) + 200
                        third   = int(tmp_arr.pop(0)) - (first-403)
                        fourth  = int(tmp_arr.pop(0)) - (second-200)             
                        tmp_rect = Rect(first,second,third,fourth)
                        
                        hitbox = tmp_rect.inflate(+5, +5)
                        if hitbox.collidepoint(clicked):
                            self.correct[3] = 0
                            self.num_correct = self.num_correct + 1
                            pygame.draw.ellipse(gfx.screen, (255,0,0), tmp_rect,3)
                            pygame.draw.ellipse(gfx.screen, (255,0,0),
                                                (first-383,second,third,fourth)
                                                ,3)
                            return 1                        
                    elif x == 5:
                        tmp_arr = string.split(str(self.fifth),',')
                        first   = int(tmp_arr.pop(0)) + 20
                        second  = int(tmp_arr.pop(0)) + 200
                        third   = int(tmp_arr.pop(0)) - (first-20)
                        fourth  = int(tmp_arr.pop(0)) - (second-200)             
                        tmp_rect = Rect(first,second,third,fourth)
                        
                        hitbox = tmp_rect.inflate(+5, +5)
                        if hitbox.collidepoint(clicked):
                            self.correct[4] = 0
                            self.num_correct = self.num_correct + 1
                            pygame.draw.ellipse(gfx.screen, (255,0,0), tmp_rect,3)
                            pygame.draw.ellipse(gfx.screen, (255,0,0),
                                                (first+383,second,third,fourth)
                                                ,3)
                            return 1
                        
                        tmp_arr = string.split(str(self.fifth),',')
                        first   = int(tmp_arr.pop(0)) + 403
                        second  = int(tmp_arr.pop(0)) + 200
                        third   = int(tmp_arr.pop(0)) - (first-403)
                        fourth  = int(tmp_arr.pop(0)) - (second-200)             
                        tmp_rect = Rect(first,second,third,fourth)
                        
                        hitbox = tmp_rect.inflate(+5, +5)
                        if hitbox.collidepoint(clicked):
                            self.correct[4] = 0
                            self.num_correct = self.num_correct + 1
                            pygame.draw.ellipse(gfx.screen, (255,0,0), tmp_rect,3)
                            pygame.draw.ellipse(gfx.screen, (255,0,0),
                                                (first-383,second,third,fourth)
                                                ,3)
                            return 1                                                    
                            
    def next_diff(self):
        # advance to the next diff
        #for x in self.num_correct:
        if self.num_correct <5:
            while 1:
                rand =  random.randrange(0,5)
                
                if self.correct[rand] != 0 :
                    self.num_correct = self.num_correct + 1
                    # draw ellipse
                    if self.correct[rand] == 1:
                        tmp_arr = string.split(str(self.first),',')
                    if self.correct[rand] == 2:
                        tmp_arr = string.split(str(self.second),',')          
                    if self.correct[rand] == 3:
                        tmp_arr = string.split(str(self.third),',')
                    if self.correct[rand] == 4:
                        tmp_arr = string.split(str(self.fourth),',')
                    if self.correct[rand] == 5:
                        tmp_arr = string.split(str(self.fifth),',')
                        
                    first   = int(tmp_arr.pop(0)) + 403
                    second  = int(tmp_arr.pop(0)) + 200
                    third   = int(tmp_arr.pop(0)) - (first-403)
                    fourth  = int(tmp_arr.pop(0)) - (second-200)             
                                          
                    tmp_rect = Rect(first,second,third,fourth)
                    pygame.draw.ellipse(gfx.screen, (255,0,0), tmp_rect,3)
                    pygame.draw.ellipse(gfx.screen, (255,0,0),
                                        (first-383,second,third,fourth)
                                        ,3)
                    self.correct[rand] = 0
                    return
            
