#####################################
###### Sprites Management File ######
#####################################
import sprites
import os
import pygame
import math
import random




### NOT MY CODE ###
# http://www.pygame.org/wiki/RotateCenter
# No name provided to credit.
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image



