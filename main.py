#Autor: Leonhard Pieper (Primär), Anton Friedel, Paul Störr, Claas Malberg

from pygame.examples.eventlist import img_on_off
import gfx_stack as gfx
import kommandozeilen_argumente as cmdargs

import Normalisieren
import Test_Data
import Start_End
import Visualizer
import Path_Finder_V2
import Readout_V2

filename = "Labyrinth-1.txt"
delay = 0.1

def main():
    data = Readout_V2.readout_file(filename)  # Daten "einlesen"

    map = Normalisieren.normalise(data)     # Daten Normalisieren

    start, end = Start_End.findStartEnd(map)        #Start und endkoordinate finden

    path=Path_Finder_V2.findPath(map, start, end)       #Lösungsweg berechnen

    Visualizer.iluminate(path, delay)         #lösungsweg aufzeichnen


if __name__ == '__main__':
    main()

