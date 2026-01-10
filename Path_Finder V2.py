import Test_Data
import Start_End

# N, E, S, W
# r, f, l, b

forbidden_list = ['S', 'B', 'W']
rotation_list = ['r', 'f', 'l', 'b']

def get_next_direction(direction, rotation):
    if rotation == 'f':
        return direction

    if direction == 'N':
        if rotation == 'l':
            return 'W'
        if rotation == 'r':
            return 'E'
        if rotation == 'b':
            return 'S'
        
    if direction == 'E':
        if rotation == 'l':
            return 'N'
        if rotation == 'r':
            return 'S'
        if rotation == 'b':
            return 'W'

    if direction == 'S':
        if rotation == 'l':
            return 'E'
        if rotation == 'r':
            return 'W'
        if rotation == 'b':
            return 'N'

    if direction == 'W':
        if rotation == 'l':
            return 'S'
        if rotation == 'r':
            return 'N'
        if rotation == 'b':
            return 'E'

def get_field(check_direction, pos):
    if check_direction == 'N':
        return [pos[0]-1, pos[1]]
    if check_direction == 'E':
        return [pos[0], pos[1]+1]
    if check_direction == 'S':
        return [pos[0]+1, pos[1]]
    if check_direction == 'W':
        return [pos[0], pos[1]-1]
    
def get_next_move(pos, direction, lab_map, go_back_mode = False, rotation_index = 0):
    rotation = rotation_list[rotation_index]
    check_direction = get_next_direction(direction, rotation)
    check_field = get_field(check_direction, pos)
    if go_back_mode:
        if lab_map[check_field[0]][check_field[1]] != 'W':
            return check_field, check_direction
        return get_next_move(pos, direction, lab_map, True, rotation_index+1)
        
    else:         
        if not lab_map[check_field[0]][check_field[1]] in ['S', 'W', 'B']:
            return check_field, check_direction
        if rotation_index == 3:
            return get_next_move(pos, direction, lab_map, True, 0)
        else:
            return get_next_move(pos, direction, lab_map, False, rotation_index+1)
        
def move(pos, direction, lab_map):

    next_pos, next_direction = get_next_move(pos, direction, lab_map)
    lab_map = [['B' if element == 'A' else element for element in reihe] for reihe in lab_map]

    if lab_map[next_pos[0]][next_pos[1]] != 'S':
        lab_map[next_pos[0]][next_pos[1]] = 'A'
    return next_pos, next_direction, lab_map

def main():
    test_map = Test_Data.Normalised
    pos, target_pos = Start_End.findStartEnd(test_map)
    direction = 'W'

    while target_pos != pos:
        pos, direction, test_map = move(pos, direction, test_map)
        Test_Data.printData(test_map)


if __name__ == '__main__':
    main()

