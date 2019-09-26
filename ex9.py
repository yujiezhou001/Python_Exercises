# Map
# Engine
# Scene
#   Death
#   Central Corridor
#   Laser Weapon Armory 
#   The Bridge
#   Escape Pod

# The structure of the game

# Map
#     next_scene
#     opening_scene
# Engine 
#     play
# Scene
#     enter
#     Death
#     Central Corridor
#     Laser Weapon Armory * The Bridge
#     Escape Pod

#Scene is an object
class Scene(object):

    def enter(self):
        pass
#Engine is an object
class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass
#Death is an instance of Scene object
class Death(Scene):

    def enter(self):
        pass
#CentralCorridor is an instance of Scene object
class CentralCorridor(Scene):

    def enter(self):
        pass
#LaserWeaponArmory is an instance of Scene object
class LaserWeaponArmory(Scene):

    def enter(self):
        pass
#TheBridge is an instance of Scene object
class TheBridge(Scene):

    def enter(self):
        pass
#EscapePod is an instance of Scene object
class EscapePod(Scene):

    def enter(self):
        pass
#Map is an object
class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass
#First create a map which selects a start_scene
a_map = Map('central_corridor')
#Then create a game with engine using the established map
a_game = Engine(a_map)
#Start the engine and run the game
a_game.play()
