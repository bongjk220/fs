import pygame, random, sys

WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
COLS, ROWS = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE

colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 165, 0),
    (128, 0, 128),
    (0, 255, 255)
]

tetrominoes = [
    [[1, 1, 1, 1]],
    [[2, 2], [2, 2]],
    [[0, 3, 0], [3, 3, 3]],
    [[4, 4, 0], [0, 4, 4]],
    [[0, 5, 5], [5, 5, 0]],
    [[6, 0, 0], [6, 6, 6]],
    [[0, 0, 7], [7, 7, 7]]
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

def draw_block(screen, color, x, y):
    # 입체감 있는 블록 그리기
    rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, (200,200,200), rect, 2)  # 테두리
    pygame.draw.line(screen, (255,255,255), rect.topleft, rect.topright, 2)
    pygame.draw.line(screen, (255,255,255), rect.topleft, rect.bottomleft, 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH+150, HEIGHT))  # 오른쪽 공간 확보
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 20)

    board = [[0]*COLS for _ in range(ROWS)]
    current_piece = Piece(COLS//2-2, 0, random.choice(tetrominoes))
    next_piece = Piece(COLS//2-2, 0, random.choice(tetrominoes))
    fall_time = 0
    score = 0
    high_scores = []

    running = True
    while running:
        screen.fill((0,0,0))
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time > 500:
            current_piece.y += 1
            if check_collision(board, current_piece):
                current_piece.y -= 1
                merge_piece(board, current_piece)
                board, cleared = clear_lines(board)
                score += cleared * 100
                current_piece = next_piece
                next_piece = Piece(COLS//2-2, 0, random.choice(tetrominoes))
                if check_collision(board, current_piece):
                    high_scores.append(score)
                    high_scores = sorted(high_scores, reverse=True)[:5]
                    print("Game Over! Score:", score)
                    print("Top 5:", high_scores)
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
                        for _ in range(3):
                            current_piece.rotate()
                elif event.key == pygame.K_SPACE:
                    # 빠른 하강
                    while not check_collision(board, current_piece):
                        current_piece.y += 1
                    current_piece.y -= 1

        # 보드 그리기
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]:
                    draw_block(screen, colors[board[i][j]], j*BLOCK_SIZE, i*BLOCK_SIZE)

        # 현재 블록 그리기
        for i, row in enumerate(current_piece.shape):
            for j, val in enumerate(row):
                if val:
                    draw_block(screen, colors[current_piece.color],
                               (current_piece.x+j)*BLOCK_SIZE,
                               (current_piece.y+i)*BLOCK_SIZE)

        # 점수 표시
        score_text = font.render(f"Score: {score}", True, (255,255,255))
        screen.blit(score_text, (WIDTH+20, 20))

        # Top5 표시
        y_offset = 60
        for idx, hs in enumerate(high_scores):
            hs_text = font.render(f"{idx+1}. {hs}", True, (255,255,255))
            screen.blit(hs_text, (WIDTH+20, y_offset))
            y_offset += 25

        # 다음 블록 미리보기
        preview_x, preview_y = WIDTH+50, 200
        for i, row in enumerate(next_piece.shape):
            for j, val in enumerate(row):
                if val:
                    draw_block(screen, colors[next_piece.color],
                               preview_x + j*BLOCK_SIZE,
                               preview_y + i*BLOCK_SIZE)

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
