from copy import deepcopy

class puzz:
    visited = []
    ham = 0
    man = 0
    listr = []
    listr1 = []
    listr2 = []
    listr3 = []

puzzle = []
goal_puzzle = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '0']
]

positions = [
    [0, 0],
    [0, 1],
    [0, 2],
    [1, 0],
    [1, 1],
    [1, 2],
    [2, 0],
    [2, 1],
    [2, 2]
]
goalVector = ['1', '2', '3', '4', '5', '6', '7', '8', '0']

def notInVisited(node):
    for i in range(len(puzz.visited)):
        if node[0] == puzz.visited[i][0] and node[1] == puzz.visited[i][1] and node[2] == puzz.visited[i][2]:
            return False
    return True

def abs(a):
    if a < 0:
        a = a*-1
    return a

def getPositions(node):
    pos = []
    for i in range(3):
        for j in range(3):
            pos.append([i, j, node[i][j]])
    return pos

def puzzle_print(p):
    str = ''
    for i in range(3):
        for j in range(3):
            if p[i][j] == '0':
                str += '  '
            else:
                str += p[i][j]+' '
        str += '\n'
    print(str)

with open('puzzle.txt','r') as f:
    for line in f:
        puzzle.append(line.strip().split(' '))
def sor(node):
    for i in range(0, len(node)):
        for j in range(i, len(node)):
            if node[j][-1] <= node[i][-1]:
                tmp = node[i]
                node[i] = node[j]
                node[j] = tmp
    return node

def Manhatann(node):
    Mdistance = 0
    pos = sor(getPositions(node))
    temp = pos[0]
    pos.pop(0)
    pos.append(temp)
    posg = getPositions(goal_puzzle)
    for i in range(8):
        if pos[i][-1] != '0':
            Mdistance += abs(posg[i][0] - pos[i][0]) + abs(posg[i][1] - pos[i][1])
    return Mdistance


def Hamming(node):
    nodeVector = []
    Hdistance = 0
    for i in range(3):
        for j in range(3):
            nodeVector.append(node[i][j])
    for k in range(len(nodeVector)):
        if nodeVector[k] != '0':
            if nodeVector[k] != goalVector[k]:
               Hdistance += 1
    return Hdistance

def moveUP(empty):
    state = deepcopy(puzz.visited[-1])
    if empty[0] < 2:
        state[empty[0]][empty[1]] = state[empty[0]+1][empty[1]]
        state[empty[0] + 1][empty[1]] = '0'
    return state

def moveDOWN(empty):
    state = deepcopy(puzz.visited[-1])
    if empty[0] > 0:
        state[empty[0]][empty[1]] = state[empty[0]-1][empty[1]]
        state[empty[0] - 1][empty[1]] = '0'
    return state

def moveLEFT(empty):
    state = deepcopy(puzz.visited[-1])
    if empty[1] < 2:
        state[empty[0]][empty[1]] = state[empty[0]][empty[1]+1]
        state[empty[0]][empty[1]+1] = '0'
    return state

def moveRIGHT(empty):
    state = deepcopy(puzz.visited[-1])
    if empty[1] > 0:
        state[empty[0]][empty[1]] = state[empty[0]][empty[1]-1]
        state[empty[0]][empty[1]-1] = '0'
    return state

def sort_pos(pos):
    for i in range(0, len(pos)):
        for j in range(i, len(pos)):
            if pos[j][-1][1] >= pos[i][-1][1]:
                tmp = pos[i]
                pos[i] = pos[j]
                pos[j] = tmp
    return pos


def sort_pos2(pos):
    for i in range(0, len(pos)):
        for j in range(i, len(pos)):
            if pos[j][-1][0] >= pos[i][-1][0]:
                tmp = pos[i]
                pos[i] = pos[j]
                pos[j] = tmp
    return pos

def sort_pos3(pos):
    for i in range(0, len(pos)):
        for j in range(i, len(pos)):
            if pos[j][-1][0] >= pos[i][-1][0] and pos[j][-1][1] >= pos[i][-1][1]:
                tmp = pos[i]
                pos[i] = pos[j]
                pos[j] = tmp
    return pos

def sort_pos1(pos):
    for i in range(0, len(pos)):
        for j in range(i, len(pos)):
            if pos[j][-1][1] == pos[i][-1][1]:
                if pos[j][-1][0] > pos[i][-1][0]:
                    tmp = pos[i]
                    pos[i] = pos[j]
                    pos[j] = tmp
            elif pos[j][-1][0] == pos[i][-1][0]:
                if pos[j][-1][1] > pos[i][-1][1]:
                    tmp = pos[i]
                    pos[i] = pos[j]
                    pos[j] = tmp
            elif pos[j][-1][0] > pos[i][-1][0] and pos[j][-1][1] > pos[i][-1][1]:
                tmp = pos[i]
                pos[i] = pos[j]
                pos[j] = tmp
    return pos


def getPOssibleMoves():
    empty = []
    pos = []
    f = False
    for i in range(3):
        for j in range(3):
            if puzz.visited[-1][i][j] == '0':
                empty = [i, j]
                f = True
                break
        if f:
            break
    st = moveDOWN(empty)
    if st != puzz.visited[-1]:
        pos.append(st)
        pos[-1].append([Manhatann(pos[-1]), Hamming(pos[-1])])
    st = moveLEFT(empty)
    if st != puzz.visited[-1]:
        pos.append(st)
        pos[-1].append([Manhatann(pos[-1]), Hamming(pos[-1])])
    st = moveRIGHT(empty)
    if st != puzz.visited[-1]:
        pos.append(st)
        pos[-1].append([Manhatann(pos[-1]), Hamming(pos[-1])])
    st = moveUP(empty)
    if st != puzz.visited[-1]:
        pos.append(st)
        pos[-1].append([Manhatann(pos[-1]), Hamming(pos[-1])])
    return pos


def getSequence(H, M, HE):
    steps = 0
    if H and M and HE:
        possibleMoves = sort_pos1(getPOssibleMoves())
    elif H and M and not HE:
        possibleMoves = sort_pos3(getPOssibleMoves())
    elif H and not M:
        possibleMoves = sort_pos(getPOssibleMoves())
    elif M and not H:
        possibleMoves = sort_pos2(getPOssibleMoves())
    while possibleMoves:
        node = possibleMoves[-1]
        e = notInVisited(node)
        while e and (puzz.man > 0 and puzz.ham > 0):
            steps += 1
            if steps > 1000:
                break
            possibleMoves.pop(-1)
            puzz.visited.append(node)
            puzz.ham = node[-1][1]
            puzz.man = node[-1][0]
            if puzz.man == 0 and puzz.ham == 0:
                break
            if H and M and HE:
                children = sort_pos1(getPOssibleMoves())
            elif H and M and not HE:
                children = sort_pos3(getPOssibleMoves())
            elif H and not M:
                children = sort_pos(getPOssibleMoves())
            elif M and not H:
                children = sort_pos2(getPOssibleMoves())
            if len(children) <= 0:
                item1 = puzz.visited[-1]
                puzz.ham = puzz.visited[-2][1]
                puzz.man = puzz.visited[-2][0]
                puzz.visited.pop(-1)
                if len(puzz.visited) > 0:
                    item2 = puzz.visited[-1]
                else:
                    break
                if H and M and HE:
                    orphans = sort_pos1(getPOssibleMoves())
                elif H and M and not HE:
                    orphans = sort_pos3(getPOssibleMoves())
                elif H and not M:
                    orphans = sort_pos(getPOssibleMoves())
                elif M and not H:
                    orphans = sort_pos2(getPOssibleMoves())
                if item1 == orphans[0]:
                    puzz.ham = puzz.visited[-2][-1][1]
                    puzz.man = puzz.visited[-2][-1][0]
                    puzz.visited.pop(-1)
            else:
                possibleMoves.extend(children)
            node = possibleMoves[-1]
            e = notInVisited(node)
        if puzz.man == 0 and puzz.ham == 0:
            break
        elif node[-1][1] > puzz.ham and node[-1][0] > puzz.man:
            if H and M and HE:
                children = sort_pos1(getPOssibleMoves())
            elif H and M and not HE:
                children = sort_pos3(getPOssibleMoves())
            elif H and not M:
                children = sort_pos(getPOssibleMoves())
            elif M and not H:
                children = sort_pos2(getPOssibleMoves())
            for i in range(len(children)):
                if children[i] in possibleMoves:
                    possibleMoves.remove(children[i])
            item1 = puzz.visited[-1]
            if len(puzz.visited) > 2:
                puzz.ham = puzz.visited[-2][-1][1]
                puzz.man = puzz.visited[-2][-1][0]
                puzz.visited.pop(-1)
            else:
                if len(puzz.visited) > 1:
                    puzz.visited.pop(-1)
                    puzz.ham = Hamming(puzz.visited[-1])
                    puzz.man = Manhatann(puzz.visited[-1])
            if len(puzz.visited) > 0:
                item2 = puzz.visited[-1]
            else:
                break
            if H and M and HE:
                orphans = sort_pos1(getPOssibleMoves())
            elif H and M and not HE:
                orphans = sort_pos3(getPOssibleMoves())
            elif H and not M:
                orphans = sort_pos(getPOssibleMoves())
            elif M and not H:
                orphans = sort_pos2(getPOssibleMoves())
            if item1 == orphans[0]:
                if len(puzz.visited) > 2:
                    puzz.ham = puzz.visited[-2][-1][1]
                    puzz.man = puzz.visited[-2][-1][0]
                    puzz.visited.pop(-1)
                else:
                    if len(puzz.visited) > 1:
                        puzz.visited.pop(-1)
                        puzz.ham = Hamming(puzz.visited[-1])
                        puzz.man = Manhatann(puzz.visited[-1])
        elif not e:
            possibleMoves.pop(-1)
        elif steps > 1000:
            break
    if len(puzz.visited) > 0 and steps < 1000:
        return puzz.visited
    else:
        return [False]



def solve():
    puzz.visited.append(puzzle)
    puzz.ham = Hamming(puzz.visited[-1])
    puzz.man = Manhatann(puzz.visited[-1])
    if puzz.man == 0 and puzz.ham == 0:
        print('it is already solved')
        return 0
    puzz.listr  = getSequence(True, False, False)#Hamming
    puzz.visited = []
    puzz.visited.append(puzzle)
    puzz.ham = Hamming(puzz.visited[-1])
    puzz.man = Manhatann(puzz.visited[-1])
    if puzz.man == 0 and puzz.ham == 0:
        print('it is already solved')
        return 0
    puzz.listr1 = getSequence(False, True, False)#MANN
    puzz.visited = []
    puzz.visited.append(puzzle)
    puzz.ham = Hamming(puzz.visited[-1])
    puzz.man = Manhatann(puzz.visited[-1])
    if puzz.man == 0 and puzz.ham == 0:
        print('it is already solved')
        return 0
    puzz.listr2 = getSequence(True, True, False)#H&M_m
    puzz.visited = []
    puzz.visited.append(puzzle)
    puzz.ham = Hamming(puzz.visited[-1])
    puzz.man = Manhatann(puzz.visited[-1])
    if puzz.man == 0 and puzz.ham == 0:
        print('it is already solved')
        return 0
    puzz.listr3 = getSequence(True, True, True)#H&M_h
    lens = [len(puzz.listr), len(puzz.listr1), len(puzz.listr2), len(puzz.listr3)]
    lis = lens.index(min(lens))
    if lens[lis] != 0:
        if lis == 0:
            if len(puzz.listr) > 1:
                for i in range(1, len(puzz.listr)-1):
                    print("-----------------------------")
                    puzzle_print(puzz.listr[i])
                return [len(puzz.listr)-1, 0]
            else:
                print('there is no solution')
                for i in range(1, len(puzz.visited) - 1):
                    print("-----------------------------")
                    puzzle_print(puzz.visited[i])
                return [-1, 1]
        elif lis == 1:
            if len(puzz.listr1) > 1:
                for i in range(1, len(puzz.listr1)-1):
                    print("-----------------------------")
                    puzzle_print(puzz.listr1[i])
                return [len(puzz.listr1)-1, 1]
            else:
                print('there is no solution')
                for i in range(1, len(puzz.visited) - 1):
                    print("-----------------------------")
                    puzzle_print(puzz.visited[i])
                return [-1, 1]
        elif lis == 2:
            if len(puzz.listr2) > 1:
                for i in range(1, len(puzz.listr2)-1):
                    print("-----------------------------")
                    puzzle_print(puzz.listr2[i])
                return [len(puzz.listr2)-1, 2]
            else:
                print('there is no solution')
                for i in range(1, len(puzz.visited) - 1):
                    print("-----------------------------")
                    puzzle_print(puzz.visited[i])
                return [-1, 1]
        elif lis == 3:
            if len(puzz.listr3) > 1:
                for i in range(1, len(puzz.listr3)-1):
                    print("-----------------------------")
                    puzzle_print(puzz.listr3[i])
                return [len(puzz.listr3)-1, 3]
            else:
                print('there is no solution')
                for i in range(1, len(puzz.visited) - 1):
                    print("-----------------------------")
                    puzzle_print(puzz.visited[i])
                return [-1, 1]



print("the initial puzzle is :")
print("-----------------------------")
puzzle_print(puzzle)

st = solve()

print("the goal puzzle is :")
print("-----------------------------")
puzzle_print(goal_puzzle)
print("-----------------------------")
if st[1] == 0:
    print('the minimum number using Hamming Distance of steps is ' + str(st[0]))
    print("---------------------------------------------------------------------------------------------------------------")
    print('if we use Manhattan Distance will be '+str(len(puzz.listr1)-1))
    print ('if we use Manhattan and Hamming Distance will be ' + str(len(puzz.listr2)-1))
    print ('if we use Manhattan and Hamming Distance another method in ordering will be ' + str(len(puzz.listr3)-1))
elif st[1] == 1:
    print('the minimum number using Manhattan Distance of steps is ' + str(st[0]))
    print("---------------------------------------------------------------------------------------------------------------")
    print('if we use Hamming Distance will be '+str(len(puzz.listr)-1))
    print ('if we use Manhattan and Hamming Distance will be ' + str(len(puzz.listr2)-1))
    print ('if we use Manhattan and Hamming Distance another method in ordering will be ' + str(len(puzz.listr3)-1))
elif st[1] == 2:
    print('the minimum number using Hamming and Manhattan Distance of steps is ' + str(st[0]))
    print("---------------------------------------------------------------------------------------------------------------")
    print('if we use Manhatann Distance will be '+str(len(puzz.listr1)-1))
    print ('if we use Hamming Distance will be ' + str(len(puzz.listr)-1))
    print ('if we use Manhatann and Hamming Distance another method in ordering will be ' + str(len(puzz.listr3)-1))
elif st[1] == 3:
    print('the minimum number using Hamming and Manhattan Distance (another method in ordering) of steps is ' + str(st[0]))
    print("---------------------------------------------------------------------------------------------------------------")
    print('if we use Manhatann Distance will be '+str(len(puzz.listr1)-1))
    print ('if we use Hamming Distance will be ' + str(len(puzz.listr)-1))
    print ('if we use Manhatann and Hamming Distance will be ' + str(len(puzz.listr2)-1))