# Anton Friedel
import Test_Data

def readout_file(filename):
    raw_data = []

    with open(filename, "r", encoding='utf-8') as file:
        for line_index, line in enumerate(file):
            line = line.strip()
            row = []
            for column_index, character in enumerate(line):
                row.append(character)
            raw_data.append(row)

    return raw_data

def main():
    Test_Data.printData(readout_file("Labyrinth-1.txt"))

if __name__ == '__main__':
    main()