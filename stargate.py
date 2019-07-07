
import sys, pygame
from pygame.locals import *
from pygame import mouse

def draw_grid(screen, square_width, square_height, curr_colour_square, prev_colour_square):
    
    scr_height = screen.get_height()
    scr_width = screen.get_width()
    
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    # Create a 2 dimensional array. A two dimensional   
    # array is simply a list of lists.
    grid = []
    for row in range(int(scr_height / square_height)):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(int(scr_width / square_width)):
            grid[row].append(0)  # Append a cell
 
    # Set row 1, cell 5 to one. (Remember rows and
    # column numbers start at zero.)
    grid[1][5] = 1    
   
    width = square_width #int(1024 / square_width)
    height = square_width #int(768 / square_height)
    margin = 1
    for row in range(int(scr_height / square_height)):
        for column in range(int(scr_width / square_width)):
            color = WHITE
            if row == curr_colour_square[0] and column == curr_colour_square[1]:
                color = RED
                if prev_colour_square[0] != -1 or prev_colour_square[1] != -1:
                    grid[prev_colour_square[0]][prev_colour_square[1]] = WHITE
            pygame.draw.rect(screen,  color, [(margin + width) * column + margin, (margin + height) * row + margin, width, height])

def draw_hexagon(screen):
    poly_points = [ (20, 0), (40, 0), (60, 30), (40, 60), (20, 60), (0, 30) ] 
    image = pygame.Surface((60, 60)).convert_alpha
    # image.fill(TRANSPARENT)
    pygame.draw.polygon(image, 45, 45)
    pygame.draw.lines(image, pygame.Color("blue"), poly_points, 0)

def loop(screen, ball, ballrect):
    speed = [2, 2]
    obj_pos_delta = [0, 0]
    background_color = (0, 0, 0)
    ball_stopped = False
    offset_x = 0
    offset_y = 0
    (square_width, square_height) = [ 40, 40 ]
    margin = 1
    curr_colour_square = ( -1, -1)
    prev_colour_square = curr_colour_square

    # Used to manage how fast the screen updates
    
    clock = pygame.time.Clock()
    while True:
        screen.fill(background_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit()
            if event.type == USEREVENT:
                print("You have done a user initiated event!")
            elif event.type == KEYDOWN:
                print("Pressed a key. Let's do something.")
            elif event.type == MOUSEBUTTONDOWN:
                buttons_pressed = mouse.get_pressed()
                (pos_x, pos_y) = event.pos
                
                # note to self: // is the floor divider (10 // 3 = 3)
                column = pos_x // (square_width + margin)
                row = pos_y // (square_height + margin)
                
                # handle the left mouse button
                if buttons_pressed[0]:
                    obj_stop_point = event.pos
                    ball_stopped = ballrect.collidepoint(obj_stop_point[0], obj_stop_point[1])
                    prev_colour_square = curr_colour_square
                    curr_colour_square = (row, column)
                
                elif buttons_pressed[1]:
                    print("There's a middle button?!")
                
                # handle the right mouse button
                elif buttons_pressed[2]:
                    print("Context Menu")
                    
                    
                    
                print("Row: %d, Column: %d" % (row, column))
            elif event.type == MOUSEBUTTONUP:
                if ball_stopped:
                    ball_stopped = False
            elif event.type == MOUSEMOTION:
                if ball_stopped:
                    pos = event.pos
                    ballrect.x = pos[0] + offset_x
                    ballrect.y = pos[1] + offset_y
                    screen.blit(ball, ballrect)
                    continue
            else:
                if event.type == VIDEORESIZE:
                    print("Resizing the damn window!")
                print("Some other event happened: %d" % event.type)
        draw_grid(screen, square_width, square_height, curr_colour_square, prev_colour_square)
        # draw_hexagon(screen)
        if not ball_stopped:
            ballrect = ballrect.move(speed)
            if ballrect.left < 0 or ballrect.right > width:
                speed[0] = -speed[0]
            if ballrect.top < 0 or ballrect.bottom > height:
                speed[1] = -speed[1]
            screen.blit(ball, ballrect)
        clock.tick(60)
        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    size = width, height = 1024, 768
    screen = pygame.display.set_mode(size)
    ball = pygame.image.load("./images/ball.jpeg")
    loop(screen, ball, ball.get_rect())