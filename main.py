#Autor: Leonhard Pieper

#!/usr/bin/env python3
# main
from pygame.examples.eventlist import img_on_off
import gfx_stack as gfx
import kommandozeilen_argumente as cmdargs

import Normalisieren
import Test_Data
import Start_End
import Visualizer
import Path_Finder_V2





def paint_smiley():
    """einfache Demonstration zum Zeichnen von Pixeln.
    Farbnamen sind im Modul gfx_stack.py zu finden."""
    gfx.set_pixel((30,20), "Black")
    gfx.set_pixel((31,20), "Black")
    gfx.set_pixel((30,21), "Black")
    gfx.set_pixel((31,21), "Light Steel Blue")

    gfx.set_pixel((50,21), "Light Steel Blue")
    gfx.set_pixel((51,21), "Black")
    gfx.set_pixel((50,20), "Black")
    gfx.set_pixel((51,20), "Black")

    gfx.set_pixel((30,30), "Mandy")
    gfx.set_pixel((32,32), "Brown")
    gfx.set_pixel((34,33), "Brown")
    gfx.set_pixel((36,34), "Brown")
    gfx.set_pixel((38,35), "Brown")

    gfx.set_pixel((40,35), "Brown")

    gfx.set_pixel((42,35), "Brown")
    gfx.set_pixel((44,34), "Brown")
    gfx.set_pixel((46,33), "Brown")
    gfx.set_pixel((48,32), "Brown")
    gfx.set_pixel((50,30), "Mandy")


# def main():
#     """Beispiel einer Mainfunktion für den Versuch."""
#
#     cmdargs.demo()
#
#     # Grafik-Fenster öffnen
#     # erzeuge eine 80 x 60 Pixel Zeichenfläche
#     # Passen Sie die Größe der Zeichenfläche, an die Größe des Labyrinths an!
#     gfx.init_once((80, 64))
#
#
#     # zeichnen, aktualisieren und auf Nutzereingaben warten
#     while not gfx.stop_prog:
#         # zeichnen des Testbildes
#         gfx.color_demo_paint_on_surface()
#
#         # Beispiel reagieren auf Space key
#         if gfx.space_key == True:
#             print("Leertaste registriert")
#             # Smiley zeichnen
#             paint_smiley()
#
#         gfx.event_loop()
#
#     # aufräumen
#     gfx.quit_prog()

# main entwurf eins
# def main():
#
#     data = Test_Data.Type1
#
#     map = Normalisieren.normalise(data)
#
#     pos, target = Start_End.findStartEnd(map)
#     direction = 'W'
#
#     while target != pos:
#         pos, direction, map = Path_Finder_V2.move(pos, direction, map)
#         Test_Data.printData(map)


# Ansatz: Weg speichern



def main():
    data = Test_Data.Type1  # Daten "einlesen"

    map = Normalisieren.normalise(data)     # Daten Normalisieren

    start, end = Start_End.findStartEnd(map)        #Start und endkoordinate finden

    path=Path_Finder_V2.findPath(map, start, end)       #Lösungsweg berechnen

    Visualizer.iluminate(path, 0.1)         #lösungsweg aufzeichnen


if __name__ == '__main__':
    main()



