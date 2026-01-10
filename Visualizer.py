# Teilaufgabe 3.4 Bildgebung

import gfx_stack
from Test_data import Normalised


COLOR_MAP = {
    'W': "Black",                       # Wand
    'G': "White",                       # Gang
    'B': "Topaz",                       # bereits besucht
    'A': "Golden Fizz",                 # Avatar (Idee für später: Blinken Grau/Gold)
    'S': "Atlantis",                    # Start
    'Z': "Mandy"                        # Ziel (Idee für später: Blinken Rot/hellrot)
}


def draw_labyrinth(Normalised):         #zeichnet Laby Pixel für Pixel
    for y in range(len(Normalised)):
        for x in range(len(Normalised[y])):
            feld = Normalised[y][x]
            farbe = COLOR_MAP[feld]
            gfx_stack.set_pixel((x, y), farbe)


def main():
                                   # Initialisierung Bild
    gfx_stack.init_once(surface_resolution=(len(Normalised[0]), len(Normalised)))

                                        # Hauptschleife
    while not gfx_stack.stop_prog:
        draw_labyrinth(Normalised)
        gfx_stack.event_loop()

    gfx_stack.quit_prog()


if _name_ == "_main_":
    main()