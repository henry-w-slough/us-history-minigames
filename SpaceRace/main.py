from slankpy.Screen import Screen
from slankpy.Camera import Camera
from slankpy.GameObject import GameObject
from slankpy.Objects import KinematicObject
from slankpy.UI import Label
import Player
import Explosion
import config as config
import pygame

PLAYER_WIDTH = 36
PLAYER_HEIGHT = 64
PLAYER_DISTANCE = 256


ZOOM_SCALE_FACTOR = 500
MAX_ZOOM = 1.2
MIN_ZOOM = 0.6

BACKGROUND_SPEED = 10


screen = Screen.Screen(800, 800)
screen.set_caption("Space Race")
screen.add_layer("background")
screen.add_layer("ui")
screen.add_layer("sprites")
screen.add_layer("center")
screen.add_layer("explosions")



backgrounds = []
for b in range(3):
    background = GameObject.GameObject(screen.width, screen.height, screen.layers["background"])
    background.sprite.add_sprites("SpaceRace/assets/background.png", "background", 1, 1)
    background.set_sprite("background", 0)
    background.viewport_y = -b * 800
    backgrounds.append(background)


for p in range(config.TOTAL_PLAYERS):
    player = Player.Player(PLAYER_WIDTH, PLAYER_HEIGHT, len(screen.layers["sprites"]), screen.layers["sprites"])
    player.set_position(player.id * PLAYER_DISTANCE, 0)


total_x = sum(p.rect.x for p in screen.layers["sprites"])
center_x = total_x // len(screen.layers["sprites"]) + (PLAYER_DISTANCE // 2) - (PLAYER_WIDTH // 2)

center = GameObject.GameObject(1, 1, screen.layers["center"])
center.set_position(center_x, 0)


camera = Camera.Camera(center)
camera.set_zoom(MAX_ZOOM)


info_ui = Label.Label(800, 800, "SpaceRace/assets/font.ttf", screen.layers["ui"])
info_ui.set_background_color((255, 255, 255, 0))
info_ui.set_text_color((255, 255, 255, 200))
info_ui.set_text("SPACE RACE")


running = True
while running:


    for b, background in enumerate(backgrounds):
        background.viewport_y += BACKGROUND_SPEED
        if background.viewport_y >= screen.height:
            background.viewport_y = -screen.height * (len(backgrounds) - 1)


    for player in screen.layers["sprites"]:
        if player.is_dead:
            info_ui.set_text(f"PLAYER {player.id+1} HAS DIED")
            info_ui.set_text_color((255, 255, 255, 200))
            explosion = Explosion.Explosion(100, 100, screen.layers["explosions"])
            explosion.viewport_y = 750
            explosion.viewport_x = player.rect.x
            player.kill()


    if info_ui.text_color != ((255, 255, 255, 0)):
        info_ui.set_text_color((255, 255, 255, info_ui.text_color[3]-1))

    total_y = 0
    all_player_y = []
    for s in screen.layers["sprites"].sprites():
        total_y += s.rect.y
        all_player_y.append(s.rect.y)


    midpoint = total_y // len(screen.layers["sprites"].sprites())
    center.set_position(PLAYER_DISTANCE, midpoint)


    if len(screen.layers["sprites"]) > 1:
        spread = max(p.rect.y for p in screen.layers["sprites"]) - min(p.rect.y for p in screen.layers["sprites"])
        zoom = max(MIN_ZOOM, min(MAX_ZOOM, ZOOM_SCALE_FACTOR / (spread + ZOOM_SCALE_FACTOR)))
        camera.set_zoom(zoom)


    if len(screen.layers["sprites"]) == 1:
        info_ui.set_text(f"PLAYER {list(screen.layers['sprites'])[0].id+1} WON")
        info_ui.viewport_y = 200
        info_ui.set_text_color((255, 255, 255, 255))


    if screen.has_quit():
        running = False


    camera.apply_offset(screen.layers["sprites"], screen.layers["center"])
    screen.visible_layer = camera.cull_layers(
        screen.layers["background"],
        screen.layers["sprites"],
        screen.layers["center"],
        screen.layers["explosions"]
    )
    screen.visible_layer.add(*screen.layers["ui"])
    screen.update()
    
