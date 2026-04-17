import pygame, random

# 게임 화면 크기
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
COLS, ROWS = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE

# 색상 정의
colors = [
    (0, 0, 0),       # 빈칸
    (255, 0, 0),     # 빨강
    (0, 255, 0),     # 초록
    (0, 0, 255),     # 파랑
    (255, 255, 0),   # 노랑
    (255, 165, 0),   # 주황
    (128, 0, 128),   # 보라
    (0, 255, 255)    # 청록
]

# 블록 모양 정의
tetrominoes = [
    [[1, 1, 1, 1]],                # I
    [[2, 2], [2, 2]],              # O
    [[0, 3, 0], [3, 3, 3]],        # T
    [[4, 4, 0], [0, 4, 4]],        # S
    [[0, 5, 5], [5, 5, 0]],        # Z
    [[6, 0, 0], [6, 6, 6]],        # J
    [[0, 0, 7], [7, 7, 7]]         # L
]

class Piece:
    def __init__(self, x, y, shape):
        self.x, self.y = x, y
        self.shape = shape
        self.color = random.randint(1, len(colors)-1)

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def check_collision(board, piece):
    for i, row in enumerate(piece.shape):
        for j, val in enumerate(row):
            if val:
                if (piece.x + j < 0 or piece.x + j >= COLS or
                    piece.y + i >= ROWS or
                    board[piece.y + i][piece.x + j]):
                    return True
    return False

def merge_piece(board, piece):
    for i, row in enumerate(piece.shape):
        for j, val in enumerate(row):
            if val:
                board[piece.y + i][piece.x + j] = piece.color

def clear_lines(board):
    new_board = [row for row in board if any(v == 0 for v in row)]
    cleared = ROWS - len(new_board)
    for _ in range(cleared):
        new_board.insert(0, [0]*COLS)
    return new_board, cleared

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    board = [[0]*COLS for _ in range(ROWS)]
    current_piece = Piece(COLS//2-2, 0, random.choice(tetrominoes))
    fall_time = 0
    score = 0

    running = True
    while running:
        screen.fill((0,0,0))
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time > 500:  # 블록 떨어지는 속도
            current_piece.y += 1
            if check_collision(board, current_piece):
                current_piece.y -= 1
                merge_piece(board, current_piece)
                board, cleared = clear_lines(board)
                score += cleared * 100
                current_piece = Piece(COLS//2-2, 0, random.choice(tetrominoes))
                if check_collision(board, current_piece):
                    print("Game Over! Score:", score)
                    running = False
            fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if check_collision(board, current_piece):
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if check_collision(board, current_piece):
                        current_piece.x -= 1
                elif event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if check_collision(board, current_piece):
                        current_piece.y -= 1
                elif event.key == pygame.K_UP:
                    current_piece.rotate()
                    if check_collision(board, current_piece):
                        for _ in range(3):  # 회전 취소
                            current_piece.rotate()

        # 보드 그리기
        for i in range(ROWS):
            for j in range(COLS):
                pygame.draw.rect(screen, colors[board[i][j]],
                                 (j*BLOCK_SIZE, i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

        # 현재 블록 그리기
        for i, row in enumerate(current_piece.shape):
            for j, val in enumerate(row):
                if val:
                    pygame.draw.rect(screen, colors[current_piece.color],
                                     ((current_piece.x+j)*BLOCK_SIZE,
                                      (current_piece.y+i)*BLOCK_SIZE,
                                      BLOCK_SIZE, BLOCK_SIZE), 0)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
