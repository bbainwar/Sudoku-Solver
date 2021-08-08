#import module
import pygame
pygame.font.init()
#set window size
screen = pygame.display.set_mode((499, 499))
pygame.display.set_caption("SUDOKU SOLVER")
dif = 500 // 9

#board
grid = [[1, 0, 0, 4, 8, 9, 0, 0, 6],
        [7, 3, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 1, 2, 9, 5],
        [0, 0, 7, 1, 2, 0, 6, 0, 0],
        [5, 0, 0, 7, 0, 3, 0, 0, 8],
        [0, 0, 6, 0, 9, 5, 7, 0, 0],
        [9, 1, 4, 6, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 3, 7],
        [8, 0, 0, 5, 1, 2, 0, 0, 4]]

font1 = pygame.font.SysFont("comicsans", 40)

#drawing the GUI
def draw():
    for i in range(9):
        for j in range(9):
            if grid[j][i] != 0:
                pygame.draw.rect(screen, (0, 150, 0), (i * dif, j * dif, dif + 1, dif + 1))
                text1 = font1.render(str(grid[j][i]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 2
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)

#check if entered value is valid or not
def valid(bo, pos, num):
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
        if bo[i][pos[1]] == num and pos[1] != i:
            return False
    box_x = pos[1]//3
    box_y = pos[0]//3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

#find empty position in board
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None

#solving the board
def solve(bo):
    find = find_empty(bo)
    if find:
        row, col = find
    else:
        return True
    screen.fill((255, 255, 255))
    draw()
    pygame.display.update()
    for i in range(1, 10):
        if valid(bo, (row, col), i):
            bo[row][col] = i
            pygame.display.update()
            pygame.time.delay(100)
            if solve(bo): #recursion
                return True
            bo[row][col] = 0 # triggers backtracking
            screen.fill((255, 255, 255))
            draw()
            pygame.display.update()
    return False

#main program
run = True
flag = 0
while run:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                flag = 1
    if flag == 1:
        solve(grid)
    draw()
    pygame.display.update()
pygame.quit()
