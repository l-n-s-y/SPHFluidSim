import pygame,datetime,sys

ROWS = 7
COLUMNS = 53

def load_cellart_from_file(filename):
    with open(filename,'r') as f:
        contents = f.read()


    try:
        cells = [[int(col) if int(col) <= 4 else 4 for col in list(row)] for row in contents.split("\n")][:-1]
    except ValueError:
        print(f"Invalid character in parsed artfile: {filename}")
        exit()

    print(cells)

    if len(cells) < ROWS:
        [cells.append([]) for _ in range(ROWS-len(cells))]
        print(len(cells))
    elif len(cells) > ROWS:
        print(len(cells))
        print(f"Too many ROWS in parsed artfile: {filename}")
        exit()

    return cells


def render(cells):
    size = (1280,960)
    screen = pygame.display.set_mode(size)

    global ROWS
    global COLUMNS

    start_date = datetime.date.today()

    #cells = [[2 for x in range(columns)] for y in range(rows)]
    print(cells)
    for i in range(len(cells)):
        row = cells[i]
        #for row in cells:
        if len(row) < COLUMNS:
            [cells[i].append(0) for _ in range(COLUMNS-len(row))]
        elif len(row) > COLUMNS:
            print(f"ROW #[{i}] is too big.")
            exit()

    print(cells)


    cell_width = 10
    cell_offset = 3

    drawn = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                exit()
        if drawn: continue

        screen.fill((0,0,0))

        current_x = 0
        current_y = 0

        print(f"Dimensions: {ROWS}x{COLUMNS} ({ROWS*COLUMNS} blocks)")

        

        for x in range(COLUMNS):
            for y in range(ROWS):
                #if i%7==0: # reset to top
                rect = pygame.Rect(current_x,current_y,cell_width,cell_width)
                try:

                    #print(cells[current_y-1][current_x-1])
                    #colour = (0,cells[current_y-1][current_x-1]*(255//4),0)
                    colour = (0,cells[y][x]*(255//4),0)
                    print(colour)
                except IndexError as e:
                    print(current_x,current_y,len(cells))
                    print(f"wuh-oh!\n{e}")
                pygame.draw.rect(screen, colour, rect)
                pygame.display.flip()
                current_y += cell_width + cell_offset

            current_x += cell_width + cell_offset
            current_y = 0

        drawn = True

debug_render_image = load_cellart_from_file("demo.txt")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        art_file = "demo.txt"
    else:
        art_file = sys.argv[1]
    
    art_cells = load_cellart_from_file(art_file)

    render(art_cells)
