# Autor: Leonhard Pieper
import Test_Data

def determinType(data):             #Datenformat der eingehenden Daten bestimmen
    dataType = 1
    for i in range(len(data)):
        for j in range (len(data[0])):
            if data[i][j] == 'X':
                dataType = 2
                return dataType
    return dataType


def normalise(data):    #Normalisirt die Daten auf den selbsgewählten Standart
    dataType = determinType(data)
    #print("dataType= ", dataType)

    normalisedData = []

    perimiter = []

    for j in range(len(data[0])+2):
        perimiter.append('W')
    normalisedData.append(perimiter)


    for i in range(len(data)):
        normalisedDataRow = []
        normalisedDataRow.append('W')
        for j in range(len(data[0])):

            if dataType == 1:
                if data[i][j] == 'S':
                    normalisedDataRow.append('S')
                elif data[i][j] == 'W':
                    normalisedDataRow.append('W')
                elif data[i][j] == '.':
                    normalisedDataRow.append('G')
                elif data[i][j] == 'Z':
                    normalisedDataRow.append('Z')
                else:
                    normalisedDataRow.append(data[i][j])



            elif dataType == 2:
                if data[i][j] == 'S':
                    normalisedDataRow.append('S')
                elif data[i][j] == 'X':
                    normalisedDataRow.append('W')
                elif data[i][j] == 'W':
                    normalisedDataRow.append('G')
                elif data[i][j] == 'Z':
                    normalisedDataRow.append('Z')
                else:
                    normalisedDataRow.append(data[i][j])

        normalisedDataRow.append('W')
        normalisedData.append(normalisedDataRow)

    normalisedData.append(perimiter)

    return normalisedData

def main():
    Test_Data.printData(normalise(Test_Data.Type1))
    Test_Data.printData(normalise(Test_Data.Type2))


if __name__ == '__main__':
    main()