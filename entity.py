from globals import *
import pygame, random

print("running entity.py")

class Entity():
    id_index = 0
    name_index = 0

    def new_id():
        Entity.id_index += 1
        return Entity.id_index - 1

    def new_name(self):
        Entity.name_index += 1
        return self.class_name + "_" + str(Entity.name_index - 1)

    def __init__(self, tile):
        self.id = Entity.new_id()
        MAP.add_entity_at(self, tile.x, tile.y)
        self.is_selected = False
        self.tile = tile
        self.class_name = type(self).__name__.lower()
        self.name = self.new_name()

    def select(self):
        self.is_selected = True

    def deselect(self):
        self.is_selected = False