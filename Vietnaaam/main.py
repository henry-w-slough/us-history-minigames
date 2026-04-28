from slankpy.Screen import Screen
from slankpy.Camera import Camera
from slankpy.GameObject import GameObject
from slankpy.Map import MapLoader
import Player
import config


screen = Screen.Screen(800, 800)
screen.add_layer("tiles")
screen.add_layer("players")


for p in range(config.TOTAL_PLAYERS):
    new_player = Player.Player(25, 25, p, screen.layers["players"])
    new_player.sprite.add_sprites("Vietnaaam/assets/player_walk_forward.png", "walk_forward", 8, 1)
    new_player.set_size(48, 48)


screen_center = GameObject.GameObject(1, 1)
screen_center.set_position(screen.width//2, screen.height//2)

camera = Camera.Camera(screen_center)
camera.set_zoom(3.6)


map_data = MapLoader.load_map("Vietnaaam/assets/tilemap.tmj")
screen.layers["tiles"].add(*MapLoader.map_to_group(map_data, "Vietnaaam/assets/tileset.png", "tiles", 10, 10))


running = True
while running:


    if screen.has_quit():
        running = False


    camera.apply_offset(*screen.layers.values())
    screen.visible_layer = camera.cull_layers(*screen.layers.values())
    screen.update()