from slankpy.Screen import Screen
import Player


screen = Screen.Screen(800, 800)
screen.set_fill_color((100, 150, 100))




running = True
while running:


    if screen.has_quit():
        running = False

    
    screen.update()