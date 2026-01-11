
import Path_Finder_V2
import Path_Finder_V3
import Test_Data
import time
import Start_End
import matplotlib.pyplot as plt
import Readout_V2
import Normalisieren


data = Readout_V2.readout_file("Labyrinth-3.txt")  # Daten "einlesen"

lab_map = Normalisieren.normalise(data)

start_pos, end_pos = Start_End.findStartEnd(lab_map)

start_time = time.perf_counter()
path_len1 = len(Path_Finder_V2.findPath(lab_map, start_pos, end_pos))
end_time = time.perf_counter()

time1 = end_time - start_time

start_time = time.perf_counter()
path_len2 = len(Path_Finder_V3.save_best_path(lab_map, start_pos, end_pos))
end_time = time.perf_counter()

time2 = end_time - start_time

times = [time1, time2]
values = ['Algorthmus 1', 'Algorythmus 2']

path_lens = [path_len1, path_len2]

plt.bar(values, times)
plt.title('Zeit')
plt.show()

plt.bar(values, path_lens)
plt.title('Schritte')
plt.show()



