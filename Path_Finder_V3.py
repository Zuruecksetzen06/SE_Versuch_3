# Paul Störr
import Test_Data
import Start_End
import copy

def generate_best_path(lab_map, start_pos, target_pos):
    finished = []
    known = [start_pos]
    new_known = []
    while target_pos not in known:
        for known_pos in known:
            if lab_map[known_pos[0]+1][known_pos[1]]  != 'W' and [known_pos[0]+1, known_pos[1]] not in finished and [known_pos[0]+1, known_pos[1]] not in known:
                new_known.append([known_pos[0]+1, known_pos[1]])
                lab_map[known_pos[0]+1][known_pos[1]] = 'Ä'
            if lab_map[known_pos[0]-1][known_pos[1]] != 'W' and [known_pos[0]-1, known_pos[1]] not in finished and [known_pos[0]-1, known_pos[1]] not in known:
                new_known.append([known_pos[0]-1, known_pos[1]])
                lab_map[known_pos[0]-1][known_pos[1]] = 'V'
            if lab_map[known_pos[0]][known_pos[1]+1] != 'W' and [known_pos[0], known_pos[1]+1] not in finished and [known_pos[0], known_pos[1]+1] not in known:
                new_known.append([known_pos[0], known_pos[1]+1])
                lab_map[known_pos[0]][known_pos[1]+1] = '<'
            if lab_map[known_pos[0]][known_pos[1]-1] != 'W' and [known_pos[0], known_pos[1]-1] not in finished and [known_pos[0], known_pos[1]-1] not in known:
                new_known.append([known_pos[0], known_pos[1]-1])
                lab_map[known_pos[0]][known_pos[1]-1] = '>'

        for known_element in known:
            finished.append(known_element)
        known = new_known
        new_known = []
    return lab_map

def mark_best_path(filled_map, start_pos, target_pos):
    path = [target_pos]
    avatar_postion = target_pos
    while avatar_postion != start_pos:
        if filled_map[avatar_postion[0]][avatar_postion[1]] == 'Ä':
            avatar_postion = [avatar_postion[0]-1, avatar_postion[1]]
        elif filled_map[avatar_postion[0]][avatar_postion[1]] == 'V':
            avatar_postion = [avatar_postion[0]+1, avatar_postion[1]]
        elif filled_map[avatar_postion[0]][avatar_postion[1]] == '>':
            avatar_postion = [avatar_postion[0], avatar_postion[1]+1]
        else: avatar_postion = [avatar_postion[0], avatar_postion[1]-1]
        path.append(avatar_postion)
    return path[::-1]
    

def save_best_path(lab_map, start_pos, target_pos):
    filled_map = generate_best_path(copy.deepcopy(lab_map), start_pos, target_pos)
    path = mark_best_path(filled_map, start_pos, target_pos)
    path_lst = []
    for pos in path:
        lab_map = [['B' if element == 'A' else element for element in reihe] for reihe in lab_map]
        lab_map[pos[0]][pos[1]] = 'A'
        path_lst.append(lab_map)
    return path_lst

def main():
    lab_map = Test_Data.Normalised
    start_pos, target_pos = Start_End.findStartEnd(lab_map)
    path_lst = save_best_path(lab_map, start_pos, target_pos)

    for map in path_lst:
        Test_Data.printData(map)

if __name__ == '__main__':
    main()


