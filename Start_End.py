# Autor: Leonhard Pieper
import Test_Data


def findStartEnd(data):
    start = [0, 0]
    end = [0, 0]
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'S':
                start[0]=i
                start[1]=j
            elif data[i][j] == 'Z':
                end[0]=i
                end[1]=j
    return start,end


def main():
    start,end = findStartEnd(Test_Data.Normalised)
    print("Start koordinates: ", start)
    print("End koordinates: ", end)

if __name__ == '__main__':
    main()