import sys


class Process:
    def __init__(self, nome, durataBurst, priorita):
        self.nome = nome
        self.durataBurst = durataBurst
        self.priorita = priorita


def fcfs(processi, numProcessi, durataProcessi):
    tma = calculateTma(processi)
    sequence = ''
    for processo in processi:
        sequence += processo.nome + "->"
    print(sequence[:-2], end='')
    print(' TMA: ' + str(tma))
    pass


def sfj(processi, numProcessi, durataProcessi):
    sfj_processi = sorted(processi, key=lambda x: x.durataBurst)
    sequence = ''
    for processo in sfj_processi:
        sequence += processo.nome + "->"
    print(sequence[:-2], end='')
    tma = calculateTma(sfj_processi)

    print(' TMA: ' + str(tma))
    pass


def priorita(processi, numProcessi, durataProcessi):
    priorita_processi = sorted(processi, key=lambda x: x.priorita)
    sequence = ''
    for processo in priorita_processi:
        sequence += processo.nome + "->"
    print(sequence[:-2], end='')
    tma = calculateTma(priorita_processi)

    print(' TMA: ' + str(tma))
    pass


def round_robin(processi, numProcessi, durataProcessi):
    toberemoved_processi = processi
    previous_burst = []
    tma = 0

    while len(toberemoved_processi) > 0:
        for index, process in enumerate(toberemoved_processi):
            if process.durataBurst >= durataProcessi:
                process.durataBurst -= durataProcessi
                previous_burst.append((process.nome, durataProcessi))
            elif process.durataBurst > 0:
                previous_burst.append((process.nome, process.durataBurst))
                process.durataBurst = 0

        toberemoved_processi = [x for x in toberemoved_processi if x.durataBurst > 0]

    sequence = ''
    for processo in previous_burst:
        sequence += processo[0] + "->"
    print(sequence[:-2], end='')
    previous_burst.reverse()

    tma = 0
    for processo in processi:
        index_proc = [x for x, y in enumerate(previous_burst) if y[0] == processo.nome]
        temp = 0
        for proc in previous_burst[index_proc[0]:]:
            if processo.nome != proc[0]:
                temp += proc[1]
        tma += temp
    tma /= len(processi)
    print(' TMA: ' + str(tma))
    pass


def calculateTma(processi):
    tma = 0
    for index, process in enumerate(processi):
        if index != 0:
            temp = 0
            for previous in processi[:index]:
                temp += previous.durataBurst
            tma += temp
    return tma / len(processi)


def main(filename):
    file = open(filename, "r")
    firstLine = file.readline().replace('\n', '')
    firstLine = firstLine.split(' ')[1:]
    numProcessi = int(firstLine[0])
    durataProcessi = int(firstLine[1])
    processi = []
    riga = file.readline()
    while riga != "":
        extracted = riga.replace('\n', '') \
            .replace('  ', ' ') \
            .split(' ')
        processi.append(
            Process(extracted[0], int(extracted[1]), int(extracted[2]))
        )
        riga = file.readline()
    file.close()
    print('FCFS: ', end='')
    fcfs(processi, numProcessi, durataProcessi)
    print('SJF: ', end='')
    sfj(processi, numProcessi, durataProcessi)
    print('Priorità: ', end='')
    priorita(processi, numProcessi, durataProcessi)
    print('Round Robin: ', end='')
    round_robin(processi, numProcessi, durataProcessi)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Errore: inserire il nome del file")
        exit(1)
    main(sys.argv[1])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
