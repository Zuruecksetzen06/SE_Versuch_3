# Teilaufgabe 3.4 Bildgebung
import gfx_stack
from Test_Data import Normalised
import time


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
            #print(feld)
            farbe = COLOR_MAP[feld]
            gfx_stack.set_pixel((x, y), farbe)


def run_labyrinth_view(Normalised):
                                        #von außen abrufbar
    gfx_stack.init_once(
        surface_resolution=(len(Normalised[0]), len(Normalised))
    )

    while not gfx_stack.stop_prog:
        draw_labyrinth(Normalised)
        gfx_stack.event_loop()

    gfx_stack.quit_prog()

def iluminate(path, delay=0.1):  # <------- !Geschw.!          #Animieren des berechneten Lösungswegs durch Liste von Kartenzuständen

    # Initialisiere Grafik einmal
    gfx_stack.init_once(                                       #Initialisieren der Graphik (Einmalig, danach nur Zustandsänderung!)
        surface_resolution=(len(path[0][0]), len(path[0]))
    )

    step_index = 0

    while not gfx_stack.stop_prog and step_index < len(path):   #Zeuchnen des aktuellen Zustands
        #print(step_index)
        #print(path)
        #print(path[step_index])
        draw_labyrinth(path[step_index])

        time.sleep(delay)                                       #Kleine Zeigverzögerung zur Sichtbarmachung des Lösungswegs

        gfx_stack.event_loop()                                  #Fensterupdate bei Event

        step_index += 1                                         #Zähler des Lösungsschrittes wird erhöht-> nächster Lösungschritt



def main():
                                   # Initialisierung Bild
    run_labyrinth_view(Normalised)


if __name__ == "__main__":
    main()