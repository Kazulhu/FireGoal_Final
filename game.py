# 23/02/2022 - First Time Ever using PyGame - Reference : "The ultimate introduction to Pygame" by Clear Code on YouTube

# Video Games are like movies, they're superposition of images/frames displayed fast enough (24 frames/second) so that
#   our brains will assume them as a fluent motion. In a game, images are generated while the game is running, at the
#   opposite of a movie (fixed images). Moreover, in a game, we constantly check the player's input to know which frame
#   should be drawn.

# What does Pygame do ?
#   It helps draw images.
#   Check input of the player w/o the input() method that would pause the code and would be useless for a game.
#   Useful to detect collisions, create text, timers...

# -------------------- Importing Modules -------------------- #

# Importing the Pygame module
from sys import exit
# Library imports
import pygame
import time
from random import randint
from pygame.locals import *

# pymunk imports
from pymunk import space
from pymunk.vec2d import Vec2d
# Importing the exit function from the sys module so
from sys import exit
# Importing the Pymunk module, a 2D physics library used for 2D rigid body physics in Python
import pymunk
# Set Pymunk to use Pygame to draw
import pymunk.pygame_util


# -------------------- 1) Create a window in Pygame -------------------- #

# Fonction permettant de créer un message sur l'écran
def creer_message(font, message, message_rect, color):
    message = font.render(message, True, color)
    screen.blit(message, message_rect)


def _draw_objects():
    """
    Draw the objects.
    :return: None
    """
    _space.debug_draw(_draw_options)


# Creation of the ball
def _create_ball():
    """
    Create a ball.
    :return None:
    """
    global body_ball
    mass = 10
    radius = 15
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
    body_ball = pymunk.Body(mass, inertia)
    body_ball.position = 680, 300
    shape = pymunk.Circle(body_ball, radius, (0, 0))
    shape.elasticity = 0.9
    shape.friction = 1
    _space.add(body_ball, shape)


def create_player1(fp_1):
    global foot1, shape1
    mass_head = 10
    radius_head = 30
    inertia = pymunk.moment_for_circle(mass_head, 0, radius_head, (0, 0))
    head = pymunk.Body(mass_head, inertia)
    head.position = player_rect.x + 30, player_rect.y + 30
    shape = pymunk.Circle(head, radius_head, (0, 0))
    shape.elasticity = 2.5
    shape.friction = 0.9
    _space.add(head, shape)

    # Creation of the foot

    mass_foot = 10
    radius_foot = 20
    inertia = pymunk.moment_for_circle(mass_foot, 0, radius_foot, (0, 0))
    foot1 = pymunk.Body(mass_foot, inertia)
    foot1.position = player_rect.x + 30, player_rect.y + 60
    shape1 = pymunk.Circle(foot1, radius_foot, (0, 0))
    shape1.elasticity = 4
    shape1.friction = 0
    _space.add(foot1, shape1)

    mass = 150
    moment = pymunk.moment_for_poly(mass, fp_1)

    # right flipper
    r_flipper_body = pymunk.Body(mass, moment)
    r_flipper_body.position = player_rect.x + 30, player_rect.y + 80
    r_flipper_shape = pymunk.Poly(r_flipper_body, fp_1)
    _space.add(r_flipper_body, r_flipper_shape)

    r_flipper_shape.group = 1
    r_flipper_shape.elasticity = 0.4


def create_player2(fp):
    global r_flipper_body, r_flipper_shape

    mass_head = 10
    radius_head = 30
    inertia = pymunk.moment_for_circle(mass_head, 0, radius_head, (0, 0))
    head = pymunk.Body(mass_head, inertia)
    head.position = player2_rect.x + 30, player2_rect.y + 30
    shape = pymunk.Circle(head, radius_head, (0, 0))
    shape.elasticity = 2.5
    shape.friction = 0.9
    _space.add(head, shape)

    mass_foot = 10
    radius_foot = 20
    inertia = pymunk.moment_for_circle(mass_foot, 0, radius_foot, (0, 0))
    foot = pymunk.Body(mass_foot, inertia)
    foot.position = player2_rect.x + 30, player2_rect.y + 60
    shape = pymunk.Circle(foot, radius_foot, (0, 0))
    shape.elasticity = 4
    shape.friction = 0
    _space.add(foot, shape)

    # Foot of the player

    # fp = [(10, -10), (-50, 0), (10, 10)] Modify fp[1][0] => direction of triangle
    mass = 150
    moment = pymunk.moment_for_poly(mass, fp)

    # right flipper
    r_flipper_body = pymunk.Body(mass, moment)
    r_flipper_body.position = player2_rect.x + 30, player2_rect.y + 80
    r_flipper_shape = pymunk.Poly(r_flipper_body, fp)
    _space.add(r_flipper_body, r_flipper_shape)

    """r_flipper_joint_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    r_flipper_joint_body.position = r_flipper_body.position
    j = pymunk.PinJoint(r_flipper_body, r_flipper_joint_body, (0, 0), (0, 0))
    s = pymunk.DampedRotarySpring(
        r_flipper_body, r_flipper_joint_body, 0.15, 20000000, 900000
    )
    _space.add(j, s)"""

    r_flipper_shape.group = 1
    r_flipper_shape.elasticity = 0.4


# Creation of static body like the ground or the goals
def _add_static_scenery():
    """
    Create the static bodies.
    :return: None
    """
    static_body = _space.static_body
    static_lines = [
        # Ground
        pymunk.Segment(static_body, (0.0, 580), (1360.0, 580), 1.0),

        # Right Goal
        pymunk.Segment(static_body, (1188.0, 460), (1360.0, 450), 3.0),
        # Left Goal
        pymunk.Segment(static_body, (0.0, 475), (156.0, 485), 3.0),
        # Left line
        pymunk.Segment(static_body, (0.0, 0), (0.0, 768), 1.0),
        # Right line
        pymunk.Segment(static_body, (1360, 0), (1360, 768), 1.0),
        # Top line
        pymunk.Segment(static_body, (0.0, 0), (1360, 0), 1.0),
    ]

    for line in static_lines:
        line.elasticity = 0.9
        line.friction = 0.9
    _space.add(*static_lines)


def __game__(player1_choice, player2_choice, player2_score, player1_score):
    global _space, player_rect, player2_rect, screen, _draw_options

    # Space
    _space = pymunk.Space()
    _space.gravity = (0.0, 1000.0)

    # Physics
    # Time step
    _dt = 1.0 / 90.0
    # Number of physics steps per screen frame
    _physics_steps_per_frame = 2

    # pygame
    pygame.init()
    screen = pygame.display.set_mode((1360, 768))
    _clock = pygame.time.Clock()

    _draw_options = pymunk.pygame_util.DrawOptions(screen)

    # Static barrier walls (lines) that the balls bounce off of
    _add_static_scenery()

    # Creating a window
    # screen = pygame.display.set_mode((width, height))
    # Most common width x height : 800x400, 1024x768, 1280x800, 1360x768, 1480x900, 1680x1050, 1920x1080
    screen = pygame.display.set_mode((1360, 768))
    screen_center = (680, 384)

    # Attributes a name to the Pygame window
    pygame.display.set_caption('Fire Goal')

    t = 18100  # 180000 milliseconds = 3 minutes 181000
    font = pygame.font.Font("assets/font.ttf", 20)
    font_score = pygame.font.Font("assets/font.ttf", 75)

    # Modifying the window's icon
    game_icon = pygame.image.load('sprites/game_icon.png').convert_alpha()
    pygame.display.set_icon(game_icon)

    # Initializing variable
    clock = pygame.time.Clock()

    # Font Initialization
    test_font = pygame.font.Font('font/Pixeltype.ttf', 35)

    # Initialize the Display Surface (=/= window), where all Regular Surfaces are displayed. It's like the background.
    # test_surface = pygame.Surface((100, 200))

    # convert_alpha() method is used so Pygame can work with files with better compatibility than png files, which becomes
    #   pretty important when we have dozens of pngs to display on screen in Pygame.
    # sky_surface = pygame.image.load("sprites/background/sky.png").convert_alpha()
    # sky_rect = sky_surface.get_rect(topleft=(0, 0))

    # The ".fill()" method is used to colour the "test-surface" Display Surface
    # test_surface.fill('Red')
    # ground_surface = pygame.image.load("sprites/background/ground.png").convert_alpha()
    # ground_rect_1 = ground_surface.get_rect(bottomleft=(0, 768))
    # ground_rect_2 = ground_surface.get_rect(bottomleft=(785, 768))

    # Test stadium as background
    image_background = "DA/backgrounds/{}.png".format(randint(1,8))
    stadium_surface = pygame.image.load(image_background).convert_alpha()
    stadium_rect = stadium_surface.get_rect(center=(680, 380))

    # render(text_i_want_to_write, boolean for anti-aliasing (smooth text's edges), color_in_which_text_is_written_in)
    # text_surface = test_font.render("Runner Game", False, "Black")  # or with RGB tuple :
    # text_surface = test_font.render("Runner Game", False, (64, 64, 64))
    # text_rect = text_surface.get_rect(center=(400, 25))

    # Importing the Snail's sprites.
    # snail_surface_1 = pygame.image.load('sprites/characters/snail/snail1.png').convert_alpha()
    # snail_surface_2 = pygame.image.load('sprites/characters/snail/snail2.png').convert_alpha()
    # snail_x_pos = 800
    #
    # Rectangle Method, more practical, easier manipulation of pngs/sprites movement, (topleft, midtop, topright, midright,
    #   bottomright, midbottom, bottomleft, midleft, center).
    # snail_rect = snail_surface_1.get_rect(bottomleft=(801, 232))

    # Importing Player's Sprite
    if player1_choice == 1:
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        jerry = pygame.image.load("DA/players/jerry/right/static.png").convert_alpha()
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        jerry_walk1_right = pygame.image.load("DA/players/jerry/right/walk/1.png").convert_alpha()
        jerry_walk2_right = pygame.image.load("DA/players/jerry/right/walk/2.png").convert_alpha()
        jerry_walk3_right = pygame.image.load("DA/players/jerry/right/walk/3.png").convert_alpha()
        jerry_walk4_right = pygame.image.load("DA/players/jerry/right/walk/4.png").convert_alpha()
        jerry_walk5_right = pygame.image.load("DA/players/jerry/right/walk/5.png").convert_alpha()
        jerry_walk6_right = pygame.image.load("DA/players/jerry/right/walk/6.png").convert_alpha()
        jerry_walk7_right = pygame.image.load("DA/players/jerry/right/walk/7.png").convert_alpha()
        jerry_walk8_right = pygame.image.load("DA/players/jerry/right/walk/8.png").convert_alpha()
        ##########################################################################################
        jerry_walk1_left = pygame.image.load("DA/players/jerry/left/walk/1.png").convert_alpha()
        jerry_walk2_left = pygame.image.load("DA/players/jerry/left/walk/2.png").convert_alpha()
        jerry_walk3_left = pygame.image.load("DA/players/jerry/left/walk/3.png").convert_alpha()
        jerry_walk4_left = pygame.image.load("DA/players/jerry/left/walk/4.png").convert_alpha()
        jerry_walk5_left = pygame.image.load("DA/players/jerry/left/walk/5.png").convert_alpha()
        jerry_walk6_left = pygame.image.load("DA/players/jerry/left/walk/6.png").convert_alpha()
        jerry_walk7_left = pygame.image.load("DA/players/jerry/left/walk/7.png").convert_alpha()
        jerry_walk8_left = pygame.image.load("DA/players/jerry/left/walk/8.png").convert_alpha()
        ##########################################################################################
        jerry_jump1_right = pygame.image.load("DA/players/jerry/right/jump/1.png").convert_alpha()
        jerry_jump2_right = pygame.image.load("DA/players/jerry/right/jump/2.png").convert_alpha()
        jerry_jump3_right = pygame.image.load("DA/players/jerry/right/jump/3.png").convert_alpha()
        jerry_jump4_right = pygame.image.load("DA/players/jerry/right/jump/4.png").convert_alpha()
        jerry_jump5_right = pygame.image.load("DA/players/jerry/right/jump/5.png").convert_alpha()
        ##########################################################################################
        jerry_jump1_left = pygame.image.load("DA/players/jerry/left/jump/1.png").convert_alpha()
        jerry_jump2_left = pygame.image.load("DA/players/jerry/left/jump/2.png").convert_alpha()
        jerry_jump3_left = pygame.image.load("DA/players/jerry/left/jump/3.png").convert_alpha()
        jerry_jump4_left = pygame.image.load("DA/players/jerry/left/jump/4.png").convert_alpha()
        jerry_jump5_left = pygame.image.load("DA/players/jerry/left/jump/5.png").convert_alpha()

        player1_surface = jerry

        pos_static = jerry

        animation_list_player1_jump_right = [jerry_jump1_right, jerry_jump2_right, jerry_jump3_right,
                                             jerry_jump4_right, jerry_jump5_right]
        animation_list_player1_jump_left = [jerry_jump1_left, jerry_jump2_left, jerry_jump3_left,
                                            jerry_jump4_left, jerry_jump5_left]
        animation_list_player1_right = [jerry_walk1_right, jerry_walk2_right, jerry_walk3_right, jerry_walk4_right,
                                        jerry_walk5_right, jerry_walk6_right, jerry_walk7_right, jerry_walk8_right]
        animation_list_player1_left = [jerry_walk1_left, jerry_walk2_left, jerry_walk3_left, jerry_walk4_left,
                                       jerry_walk5_left, jerry_walk6_left, jerry_walk7_left, jerry_walk8_left]

    elif player1_choice == 2:
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        red = pygame.image.load("DA/players/red/right/static.png").convert_alpha()
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        red_walk1_right = pygame.image.load("DA/players/red/right/walk/1.png").convert_alpha()
        red_walk2_right = pygame.image.load("DA/players/red/right/walk/2.png").convert_alpha()
        red_walk3_right = pygame.image.load("DA/players/red/right/walk/3.png").convert_alpha()
        red_walk4_right = pygame.image.load("DA/players/red/right/walk/4.png").convert_alpha()
        red_walk5_right = pygame.image.load("DA/players/red/right/walk/5.png").convert_alpha()
        red_walk6_right = pygame.image.load("DA/players/red/right/walk/6.png").convert_alpha()
        red_walk7_right = pygame.image.load("DA/players/red/right/walk/7.png").convert_alpha()
        red_walk8_right = pygame.image.load("DA/players/red/right/walk/8.png").convert_alpha()
        ##########################################################################################
        red_walk1_left = pygame.image.load("DA/players/red/left/walk/1.png").convert_alpha()
        red_walk2_left = pygame.image.load("DA/players/red/left/walk/2.png").convert_alpha()
        red_walk3_left = pygame.image.load("DA/players/red/left/walk/3.png").convert_alpha()
        red_walk4_left = pygame.image.load("DA/players/red/left/walk/4.png").convert_alpha()
        red_walk5_left = pygame.image.load("DA/players/red/left/walk/5.png").convert_alpha()
        red_walk6_left = pygame.image.load("DA/players/red/left/walk/6.png").convert_alpha()
        red_walk7_left = pygame.image.load("DA/players/red/left/walk/7.png").convert_alpha()
        red_walk8_left = pygame.image.load("DA/players/red/left/walk/8.png").convert_alpha()
        ##########################################################################################
        red_jump1_right = pygame.image.load("DA/players/red/right/jump/1.png").convert_alpha()
        red_jump2_right = pygame.image.load("DA/players/red/right/jump/2.png").convert_alpha()
        red_jump3_right = pygame.image.load("DA/players/red/right/jump/3.png").convert_alpha()
        red_jump4_right = pygame.image.load("DA/players/red/right/jump/4.png").convert_alpha()
        red_jump5_right = pygame.image.load("DA/players/red/right/jump/5.png").convert_alpha()
        ##########################################################################################
        red_jump1_left = pygame.image.load("DA/players/red/left/jump/1.png").convert_alpha()
        red_jump2_left = pygame.image.load("DA/players/red/left/jump/2.png").convert_alpha()
        red_jump3_left = pygame.image.load("DA/players/red/left/jump/3.png").convert_alpha()
        red_jump4_left = pygame.image.load("DA/players/red/left/jump/4.png").convert_alpha()
        red_jump5_left = pygame.image.load("DA/players/red/left/jump/5.png").convert_alpha()

        player1_surface = red

        pos_static = red

        animation_list_player1_jump_right = [red_jump1_right, red_jump2_right, red_jump3_right,
                                             red_jump4_right, red_jump5_right]
        animation_list_player1_jump_left = [red_jump1_left, red_jump2_left, red_jump3_left,
                                            red_jump4_left, red_jump5_left]
        animation_list_player1_right = [red_walk1_right, red_walk2_right, red_walk3_right, red_walk4_right,
                                        red_walk5_right, red_walk6_right, red_walk7_right, red_walk8_right]
        animation_list_player1_left = [red_walk1_left, red_walk2_left, red_walk3_left, red_walk4_left,
                                       red_walk5_left, red_walk6_left, red_walk7_left, red_walk8_left]

    elif player1_choice == 3:

        sanji = pygame.image.load("DA/players/sanji/right/static.png").convert_alpha()

        sanji_walk1_right = pygame.image.load("DA/players/sanji/right/walk/1.png").convert_alpha()
        sanji_walk2_right = pygame.image.load("DA/players/sanji/right/walk/2.png").convert_alpha()
        sanji_walk3_right = pygame.image.load("DA/players/sanji/right/walk/3.png").convert_alpha()
        sanji_walk4_right = pygame.image.load("DA/players/sanji/right/walk/4.png").convert_alpha()
        sanji_walk5_right = pygame.image.load("DA/players/sanji/right/walk/5.png").convert_alpha()
        sanji_walk6_right = pygame.image.load("DA/players/sanji/right/walk/6.png").convert_alpha()
        sanji_walk7_right = pygame.image.load("DA/players/sanji/right/walk/7.png").convert_alpha()
        sanji_walk8_right = pygame.image.load("DA/players/sanji/right/walk/8.png").convert_alpha()
        ##########################################################################################
        sanji_walk1_left = pygame.image.load("DA/players/sanji/left/walk/1.png").convert_alpha()
        sanji_walk2_left = pygame.image.load("DA/players/sanji/left/walk/2.png").convert_alpha()
        sanji_walk3_left = pygame.image.load("DA/players/sanji/left/walk/3.png").convert_alpha()
        sanji_walk4_left = pygame.image.load("DA/players/sanji/left/walk/4.png").convert_alpha()
        sanji_walk5_left = pygame.image.load("DA/players/sanji/left/walk/5.png").convert_alpha()
        sanji_walk6_left = pygame.image.load("DA/players/sanji/left/walk/6.png").convert_alpha()
        sanji_walk7_left = pygame.image.load("DA/players/sanji/left/walk/7.png").convert_alpha()
        sanji_walk8_left = pygame.image.load("DA/players/sanji/left/walk/8.png").convert_alpha()
        ##########################################################################################
        sanji_jump1_right = pygame.image.load("DA/players/sanji/right/jump/1.png").convert_alpha()
        sanji_jump2_right = pygame.image.load("DA/players/sanji/right/jump/2.png").convert_alpha()
        sanji_jump3_right = pygame.image.load("DA/players/sanji/right/jump/3.png").convert_alpha()
        sanji_jump4_right = pygame.image.load("DA/players/sanji/right/jump/4.png").convert_alpha()
        sanji_jump5_right = pygame.image.load("DA/players/sanji/right/jump/5.png").convert_alpha()
        ##########################################################################################
        sanji_jump1_left = pygame.image.load("DA/players/sanji/left/jump/1.png").convert_alpha()
        sanji_jump2_left = pygame.image.load("DA/players/sanji/left/jump/2.png").convert_alpha()
        sanji_jump3_left = pygame.image.load("DA/players/sanji/left/jump/3.png").convert_alpha()
        sanji_jump4_left = pygame.image.load("DA/players/sanji/left/jump/4.png").convert_alpha()
        sanji_jump5_left = pygame.image.load("DA/players/sanji/left/jump/5.png").convert_alpha()

        player1_surface = sanji

        pos_static = sanji

        animation_list_player1_jump_right = [sanji_walk1_right, sanji_jump2_right, sanji_jump3_right,
                                             sanji_jump4_right, sanji_jump5_right]
        animation_list_player1_jump_left = [sanji_jump1_left, sanji_jump2_left, sanji_jump3_left,
                                            sanji_jump4_left, sanji_jump5_left]
        animation_list_player1_right = [sanji_walk1_right, sanji_walk2_right, sanji_walk3_right, sanji_walk4_right,
                                        sanji_walk5_right, sanji_walk6_right, sanji_walk7_right, sanji_walk8_right]
        animation_list_player1_left = [sanji_walk1_left, sanji_walk2_left, sanji_walk3_left, sanji_walk4_left,
                                       sanji_walk5_left, sanji_walk6_left, sanji_walk7_left, sanji_walk8_left]

    if player2_choice == 1:

        jerry_left = pygame.image.load("DA/players/jerry/left/static.png").convert_alpha()

        jerry_walk1_right = pygame.image.load("DA/players/jerry/right/walk/1.png").convert_alpha()
        jerry_walk2_right = pygame.image.load("DA/players/jerry/right/walk/2.png").convert_alpha()
        jerry_walk3_right = pygame.image.load("DA/players/jerry/right/walk/3.png").convert_alpha()
        jerry_walk4_right = pygame.image.load("DA/players/jerry/right/walk/4.png").convert_alpha()
        jerry_walk5_right = pygame.image.load("DA/players/jerry/right/walk/5.png").convert_alpha()
        jerry_walk6_right = pygame.image.load("DA/players/jerry/right/walk/6.png").convert_alpha()
        jerry_walk7_right = pygame.image.load("DA/players/jerry/right/walk/7.png").convert_alpha()
        jerry_walk8_right = pygame.image.load("DA/players/jerry/right/walk/8.png").convert_alpha()
        ##########################################################################################
        jerry_walk1_left = pygame.image.load("DA/players/jerry/left/walk/1.png").convert_alpha()
        jerry_walk2_left = pygame.image.load("DA/players/jerry/left/walk/2.png").convert_alpha()
        jerry_walk3_left = pygame.image.load("DA/players/jerry/left/walk/3.png").convert_alpha()
        jerry_walk4_left = pygame.image.load("DA/players/jerry/left/walk/4.png").convert_alpha()
        jerry_walk5_left = pygame.image.load("DA/players/jerry/left/walk/5.png").convert_alpha()
        jerry_walk6_left = pygame.image.load("DA/players/jerry/left/walk/6.png").convert_alpha()
        jerry_walk7_left = pygame.image.load("DA/players/jerry/left/walk/7.png").convert_alpha()
        jerry_walk8_left = pygame.image.load("DA/players/jerry/left/walk/8.png").convert_alpha()
        ##########################################################################################
        jerry_jump1_right = pygame.image.load("DA/players/jerry/right/jump/1.png").convert_alpha()
        jerry_jump2_right = pygame.image.load("DA/players/jerry/right/jump/2.png").convert_alpha()
        jerry_jump3_right = pygame.image.load("DA/players/jerry/right/jump/3.png").convert_alpha()
        jerry_jump4_right = pygame.image.load("DA/players/jerry/right/jump/4.png").convert_alpha()
        jerry_jump5_right = pygame.image.load("DA/players/jerry/right/jump/5.png").convert_alpha()
        ##########################################################################################
        jerry_jump1_left = pygame.image.load("DA/players/jerry/left/jump/1.png").convert_alpha()
        jerry_jump2_left = pygame.image.load("DA/players/jerry/left/jump/2.png").convert_alpha()
        jerry_jump3_left = pygame.image.load("DA/players/jerry/left/jump/3.png").convert_alpha()
        jerry_jump4_left = pygame.image.load("DA/players/jerry/left/jump/4.png").convert_alpha()
        jerry_jump5_left = pygame.image.load("DA/players/jerry/left/jump/5.png").convert_alpha()

        player2_surface = jerry_left

        pos2_static = jerry_left

        animation_list_player2_jump_right = [jerry_jump1_right, jerry_jump2_right, jerry_jump3_right,
                                             jerry_jump4_right, jerry_jump5_right]
        animation_list_player2_jump_left = [jerry_jump1_left, jerry_jump2_left, jerry_jump3_left,
                                            jerry_jump4_left, jerry_jump5_left]
        animation_list_player2_right = [jerry_walk1_right, jerry_walk2_right, jerry_walk3_right, jerry_walk4_right,
                                        jerry_walk5_right, jerry_walk6_right, jerry_walk7_right, jerry_walk8_right]
        animation_list_player2_left = [jerry_walk1_left, jerry_walk2_left, jerry_walk3_left, jerry_walk4_left,
                                       jerry_walk5_left, jerry_walk6_left, jerry_walk7_left, jerry_walk8_left]

    elif player2_choice == 2:

        red_left = pygame.image.load("DA/players/red/left/static.png").convert_alpha()

        red_walk1_right = pygame.image.load("DA/players/red/right/walk/1.png").convert_alpha()
        red_walk2_right = pygame.image.load("DA/players/red/right/walk/2.png").convert_alpha()
        red_walk3_right = pygame.image.load("DA/players/red/right/walk/3.png").convert_alpha()
        red_walk4_right = pygame.image.load("DA/players/red/right/walk/4.png").convert_alpha()
        red_walk5_right = pygame.image.load("DA/players/red/right/walk/5.png").convert_alpha()
        red_walk6_right = pygame.image.load("DA/players/red/right/walk/6.png").convert_alpha()
        red_walk7_right = pygame.image.load("DA/players/red/right/walk/7.png").convert_alpha()
        red_walk8_right = pygame.image.load("DA/players/red/right/walk/8.png").convert_alpha()
        ##########################################################################################
        red_walk1_left = pygame.image.load("DA/players/red/left/walk/1.png").convert_alpha()
        red_walk2_left = pygame.image.load("DA/players/red/left/walk/2.png").convert_alpha()
        red_walk3_left = pygame.image.load("DA/players/red/left/walk/3.png").convert_alpha()
        red_walk4_left = pygame.image.load("DA/players/red/left/walk/4.png").convert_alpha()
        red_walk5_left = pygame.image.load("DA/players/red/left/walk/5.png").convert_alpha()
        red_walk6_left = pygame.image.load("DA/players/red/left/walk/6.png").convert_alpha()
        red_walk7_left = pygame.image.load("DA/players/red/left/walk/7.png").convert_alpha()
        red_walk8_left = pygame.image.load("DA/players/red/left/walk/8.png").convert_alpha()
        ##########################################################################################
        red_jump1_right = pygame.image.load("DA/players/red/right/jump/1.png").convert_alpha()
        red_jump2_right = pygame.image.load("DA/players/red/right/jump/2.png").convert_alpha()
        red_jump3_right = pygame.image.load("DA/players/red/right/jump/3.png").convert_alpha()
        red_jump4_right = pygame.image.load("DA/players/red/right/jump/4.png").convert_alpha()
        red_jump5_right = pygame.image.load("DA/players/red/right/jump/5.png").convert_alpha()
        ##########################################################################################
        red_jump1_left = pygame.image.load("DA/players/red/left/jump/1.png").convert_alpha()
        red_jump2_left = pygame.image.load("DA/players/red/left/jump/2.png").convert_alpha()
        red_jump3_left = pygame.image.load("DA/players/red/left/jump/3.png").convert_alpha()
        red_jump4_left = pygame.image.load("DA/players/red/left/jump/4.png").convert_alpha()
        red_jump5_left = pygame.image.load("DA/players/red/left/jump/5.png").convert_alpha()

        player2_surface = red_left

        pos2_static = red_left

        animation_list_player2_jump_right = [red_jump1_right, red_jump2_right, red_jump3_right,
                                             red_jump4_right, red_jump5_right]
        animation_list_player2_jump_left = [red_jump1_left, red_jump2_left, red_jump3_left,
                                            red_jump4_left, red_jump5_left]
        animation_list_player2_right = [red_walk1_right, red_walk2_right, red_walk3_right, red_walk4_right,
                                        red_walk5_right, red_walk6_right, red_walk7_right, red_walk8_right]
        animation_list_player2_left = [red_walk1_left, red_walk2_left, red_walk3_left, red_walk4_left,
                                       red_walk5_left, red_walk6_left, red_walk7_left, red_walk8_left]

    elif player2_choice == 3:

        sanji_left = pygame.image.load("DA/players/sanji/left/static.png").convert_alpha()

        sanji_walk1_right = pygame.image.load("DA/players/sanji/right/walk/1.png").convert_alpha()
        sanji_walk2_right = pygame.image.load("DA/players/sanji/right/walk/2.png").convert_alpha()
        sanji_walk3_right = pygame.image.load("DA/players/sanji/right/walk/3.png").convert_alpha()
        sanji_walk4_right = pygame.image.load("DA/players/sanji/right/walk/4.png").convert_alpha()
        sanji_walk5_right = pygame.image.load("DA/players/sanji/right/walk/5.png").convert_alpha()
        sanji_walk6_right = pygame.image.load("DA/players/sanji/right/walk/6.png").convert_alpha()
        sanji_walk7_right = pygame.image.load("DA/players/sanji/right/walk/7.png").convert_alpha()
        sanji_walk8_right = pygame.image.load("DA/players/sanji/right/walk/8.png").convert_alpha()
        ##########################################################################################
        sanji_walk1_left = pygame.image.load("DA/players/sanji/left/walk/1.png").convert_alpha()
        sanji_walk2_left = pygame.image.load("DA/players/sanji/left/walk/2.png").convert_alpha()
        sanji_walk3_left = pygame.image.load("DA/players/sanji/left/walk/3.png").convert_alpha()
        sanji_walk4_left = pygame.image.load("DA/players/sanji/left/walk/4.png").convert_alpha()
        sanji_walk5_left = pygame.image.load("DA/players/sanji/left/walk/5.png").convert_alpha()
        sanji_walk6_left = pygame.image.load("DA/players/sanji/left/walk/6.png").convert_alpha()
        sanji_walk7_left = pygame.image.load("DA/players/sanji/left/walk/7.png").convert_alpha()
        sanji_walk8_left = pygame.image.load("DA/players/sanji/left/walk/8.png").convert_alpha()
        ##########################################################################################
        sanji_jump1_right = pygame.image.load("DA/players/sanji/right/jump/1.png").convert_alpha()
        sanji_jump2_right = pygame.image.load("DA/players/sanji/right/jump/2.png").convert_alpha()
        sanji_jump3_right = pygame.image.load("DA/players/sanji/right/jump/3.png").convert_alpha()
        sanji_jump4_right = pygame.image.load("DA/players/sanji/right/jump/4.png").convert_alpha()
        sanji_jump5_right = pygame.image.load("DA/players/sanji/right/jump/5.png").convert_alpha()
        ##########################################################################################
        sanji_jump1_left = pygame.image.load("DA/players/sanji/left/jump/1.png").convert_alpha()
        sanji_jump2_left = pygame.image.load("DA/players/sanji/left/jump/2.png").convert_alpha()
        sanji_jump3_left = pygame.image.load("DA/players/sanji/left/jump/3.png").convert_alpha()
        sanji_jump4_left = pygame.image.load("DA/players/sanji/left/jump/4.png").convert_alpha()
        sanji_jump5_left = pygame.image.load("DA/players/sanji/left/jump/5.png").convert_alpha()

        player2_surface = sanji_left

        pos2_static = sanji_left

        animation_list_player2_jump_right = [sanji_walk1_right, sanji_jump2_right, sanji_jump3_right,
                                             sanji_jump4_right, sanji_jump5_right]
        animation_list_player2_jump_left = [sanji_jump1_left, sanji_jump2_left, sanji_jump3_left,
                                            sanji_jump4_left, sanji_jump5_left]
        animation_list_player2_right = [sanji_walk1_right, sanji_walk2_right, sanji_walk3_right, sanji_walk4_right,
                                        sanji_walk5_right, sanji_walk6_right, sanji_walk7_right, sanji_walk8_right]
        animation_list_player2_left = [sanji_walk1_left, sanji_walk2_left, sanji_walk3_left, sanji_walk4_left,
                                       sanji_walk5_left, sanji_walk6_left, sanji_walk7_left, sanji_walk8_left]

    ball_im = pygame.image.load("DA/ball/ball.png").convert_alpha()
    ball4 = pygame.image.load("DA/ball/ball4.png").convert_alpha()
    ball2 = pygame.image.load("DA/ball/ball2.png").convert_alpha()
    ball3 = pygame.image.load("DA/ball/ball3.png").convert_alpha()

    animation_list_ball = [ball_im,ball4,ball2,ball3]

    ball = ball_im

    # Creating the Player's Rectangle
    player_rect = player1_surface.get_rect(midbottom=(453, 625))
    player2_rect = player2_surface.get_rect(midbottom=(960, 625))


    # Enregistrer le temps actuel
    last_update = pygame.time.get_ticks()
    # Enregistrer les images dans une liste

    animation_cooldown = 100  # Le temps d'animation
    animation_cooldown_jump = 400
    frame = 0  # frame 0

    # Gravity
    # The longer you fall, the faster you fall (exponential) (*)
    # Gravity part separated into two different parts
    # Part 1 - Create a variable which will represent gravity and will be incremented because (*)
    # player's gravity initialized at 0
    player_gravity = 0
    player2_gravity = 0
    # boolean False when player touches ground, True otherwise
    player_is_jumping = False
    player2_is_jumping = False
    # player's gravity initialized at -20 to get one jump -- moved to event.key == pygame.K_SPACE part
    # player_gravity = -20

    # Initializing a dictionary which will contain pressed key
    dict_keys_press = {}

    # Creation of the ball and the player
    _create_ball()
    create_player1([(10, -10), (50, 0), (10, 10)])
    create_player2([(10, -10), (-50, 0), (10, 10)])

    # First issue, if we only run, the above code we'll create a window that'll close nearly instantly because code ends, so
    #   we need a while loop to maintain the window open:
    running = True
    while running:

        fp = [(10, -10), (-50, 0), (10, 10)]# Foot of player2
        fp1 = [(10, -10), (70, 0), (10, 10)]

        # Progress time forward
        for x in range(_physics_steps_per_frame):
            _space.step(_dt)

        pygame.display.flip()
        # Delay fixed time between frames
        _clock.tick(50)

        # pygame.event.get() method is a method that'll return every event of Pygame, in particular the quit event that we
        # need to prevent code from stopping itself right after the window creation

        # frames per second, number of frames/images displayed each second.
        fps = 60
        #
        dt = 1 / fps

        # Comptage des secondes
        seconds = (t - pygame.time.get_ticks()) // 1000

        if seconds == 0:
            running=False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Use the exit() function to shut down everything and avoid error because of the error we could get with the
                # Pygame un-initialization and the while loop still running
                exit()

            # Keyboard Event Input (pressed / released)
            # KEYDOWN is an event which is triggered when keyboard's keys are pressed.
            # KEYUP is an event which is triggered when keyboard's keys are released after being pressed.
            #
            # There are two things to memorize: we must use the key method to provide information about which key is pressed
            #   (keys = pygame.key.get_pressed()
            #   (if keys[pygame.K_SPACE]:
            #   (   print("Jump !"))
            #
            #   or we can use the the event.type/key method to do same like above
            #     the event.type is used here to know if a button is pressed/released, while the event.key method is used
            #     to know **which** keyboard button is pressed
            #
            # Why are we using two different methods (event and keys) to get user's input ?
            #   Later on, we'll be using classes to gather all the controls relevant to the class to the class we're
            #     working with in it. pygame.mouse (event.type) and pygame.keys (keys = pygame.key.get_pressed()) are great
            #     for that.

            # If a key is pressed
            elif event.type == pygame.KEYDOWN:
                dict_keys_press[event.key] = True
            # If the key is released after being pressed
            elif event.type == pygame.KEYUP:
                dict_keys_press[event.key] = False
            # if 'd' key pressed and player_rect.x <= 800 (not going above the window border)
            # if dict_keys_press.get(pygame.K_d) and player_rect.x <= 800:

            # Jump Feature Part 1
            # if a button of the keyboard is pressed
            if event.type == pygame.KEYDOWN:
                # if the button pressed is z
                if event.key == pygame.K_z and not player_is_jumping:
                    player_gravity = -20
                    player_is_jumping = True
                    player1_surface = pos_static

                if event.key == pygame.K_UP and not player2_is_jumping:
                    player2_gravity = -20
                    player2_is_jumping = True
                    player2_surface = pos2_static

                if event.key == pygame.K_SPACE:
                    if body_ball.position - r_flipper_body.position < Vec2d(0, 0):
                        v = Vec2d(-1, 0) * 20
                        body_ball.position += v

        # if 'RIGHT arrow' key pressed and player_rect.x <= 800 (not going above the window border)
        if dict_keys_press.get(pygame.K_d) and player_rect.right <= 1354:
            current_time = pygame.time.get_ticks()  # enregistrer le temps actuel
            player_rect.x += 5
            fp1 = [(10, -10), (70, 0), (10, 10)]
            if current_time - last_update >= animation_cooldown:  # Comparer le temps actuel et le dernier enregistrer pour savoir si le temps d'animation est finie
                frame += 1  # Ajouter 1 à frame pour changer d'image
                last_update = current_time  # le temps actuel devient le temps passé pour changer de sprite la prochaine fois
            if player_is_jumping:
                current_time = pygame.time.get_ticks()  # enregistrer le temps actuel
                if current_time - last_update >= animation_cooldown_jump:  # Comparer le temps actuel et le dernier enregistrer pour savoir si le temps d'animation est finie
                    frame += 1  # Ajouter 1 à frame pour changer d'image
                    last_update = current_time  # le temps actuel devient le temps passé pour changer de sprite la prochaine fois
                player1_surface = animation_list_player1_jump_right[frame % 5]
            else:
                player1_surface = animation_list_player1_right[frame % 8]

        # Right player 2
        if dict_keys_press.get(pygame.K_RIGHT) and player2_rect.right <= 1354:
            player2_rect.x += 5
            fp = [(10, -10), (70, 0), (10, 10)]
            current_time = pygame.time.get_ticks()  # enregistrer le temps actuel
            if current_time - last_update >= animation_cooldown:  # Comparer le temps actuel et le dernier enregistrer pour savoir si le temps d'animation est finie
                frame += 1  # Ajouter 1 à frame pour changer d'image
                last_update = current_time  # le temps actuel devient le temps passé pour changer de sprite la prochaine fois
            if player2_is_jumping:
                current_time = pygame.time.get_ticks()  # enregistrer le temps actuel
                if current_time - last_update >= animation_cooldown_jump:  # Comparer le temps actuel et le dernier enregistrer pour savoir si le temps d'animation est finie
                    frame += 1  # Ajouter 1 à frame pour changer d'image
                    last_update = current_time  # le temps actuel devient le temps passé pour changer de sprite la prochaine fois
                player2_surface = animation_list_player2_jump_right[frame % 5]
            else:
                player2_surface = animation_list_player2_right[frame % 8]

        # if 'q' key pressed and player_rect.x >= 0 (not going above the window border)
        # if dict_keys_press.get(pygame.K_q) and player_rect.x >= 0:

        # if 'LEFT arrow' key pressed and player_rect.x >= 0 (not going above the window border)
        if dict_keys_press.get(pygame.K_q) and player_rect.x >= 0:

            # Pareil qu'au dessus
            current_time = pygame.time.get_ticks()
            player_rect.x -= 5
            fp1 = [(10, -10), (-50, 0), (10, 10)]
            if current_time - last_update >= animation_cooldown:
                frame += 1
                last_update = current_time
            if player_is_jumping:
                current_time = pygame.time.get_ticks()  # enregistrer le temps actuel
                if current_time - last_update >= animation_cooldown_jump:  # Comparer le temps actuel et le dernier enregistrer pour savoir si le temps d'animation est finie
                    frame += 1  # Ajouter 1 à frame pour changer d'image
                    last_update = current_time  # le temps actuel devient le temps passé pour changer de sprite la prochaine fois
                player1_surface = animation_list_player1_jump_left[frame % 5]
            else:
                player1_surface = animation_list_player1_left[frame % 8]

        if dict_keys_press.get(pygame.K_LEFT) and player2_rect.x >= 0:
            player2_rect.x -= 5
            fp = [(10, -10), (-50, 0), (10, 10)]
            current_time = pygame.time.get_ticks()
            if current_time - last_update >= animation_cooldown:
                frame += 1
                last_update = current_time
            if player2_is_jumping:
                current_time = pygame.time.get_ticks()  # enregistrer le temps actuel
                if current_time - last_update >= animation_cooldown_jump:  # Comparer le temps actuel et le dernier enregistrer pour savoir si le temps d'animation est finie
                    frame += 1  # Ajouter 1 à frame pour changer d'image
                    last_update = current_time  # le temps actuel devient le temps passé pour changer de sprite la prochaine fois
                player2_surface = animation_list_player2_jump_left[frame % 5]
            else:
                player2_surface = animation_list_player2_left[frame % 8]

        # blit -- Block Image Transfer, allow to put one surface on another.

        # screen.blit(surface_i_want_to_place, (position_x, position_y))
        # screen.blit(sky_surface, (0, 0))
        # screen.blit(sky_surface, sky_rect)

        # The ground must be drawn after the sky surface, otherwise it will be hidden by the sky.
        # Displaying all the object from pymunk

        """"""""""""""""""""""""""""""""""""""""""
        screen.blit(stadium_surface, stadium_rect)
        _draw_objects()
        # Displaying stadium background

        #
        # Gravity
        # Part 2
        # print(f"player_gravity = {player_gravity}")
        # player_gravity is continuously incrementing
        # player_rect.y += player_gravity  # makes player go by -20 (up) if spacebar is pressed
        #                                  # makes player go by player_gravity (down) if player is in air
        # if player touches ground player gets a "resistance" (simulation) see line 241 - 244
        player_gravity += 1
        player2_gravity += 1
        # Apply the gravity variable to move the player downwards
        # += we increment which prevents the user of "teleporting"
        player_rect.y += player_gravity
        player2_rect.y += player2_gravity
        # Creating a ground
        # Height of ground is 625
        if player_rect.bottom >= 580:
            player_rect.bottom = 580
            player_is_jumping = False

        if player2_rect.bottom >= 580:
            player2_rect.bottom = 580
            player2_is_jumping = False

        screen.blit(player1_surface, player_rect)
        screen.blit(player2_surface, player2_rect)

        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
        else:
            ball = animation_list_ball[frame % 4]

        x, y = pymunk.pygame_util.to_pygame(body_ball.position, screen)
        screen.blit(ball, (int(x - 17.5), int(y - 17.5)))

        if x<0 or x>1360 or y<0 or y>768:
            body_ball.position = 680, 300

        if x <= 156 and y >= 500:
            player1_score += 1
            player_rect = player1_surface.get_rect(midbottom=(453, 625))
            player2_rect = player2_surface.get_rect(midbottom=(960, 625))
            body_ball.position = 680, 300

        elif x >= 1188 and y >= 500:
            player2_score += 1
            player_rect = player1_surface.get_rect(midbottom=(453, 625))
            player2_rect = player2_surface.get_rect(midbottom=(960, 625))
            body_ball.position = 680, 300

        # We need to remove the last object created else it will create an infinite amount of ball
        _space.remove(_space.shapes[-1], _space.shapes[-1].body)
        _space.remove(_space.shapes[-1], _space.shapes[-1].body)
        _space.remove(_space.shapes[-1], _space.shapes[-1].body)
        _space.remove(_space.shapes[-1], _space.shapes[-1].body)
        _space.remove(_space.shapes[-1], _space.shapes[-1].body)
        _space.remove(_space.shapes[-1], _space.shapes[-1].body)
        # Creation of a ball representing the player physical body
        create_player1(fp1)
        create_player2(fp)

        # Keyboard Input Part
        # Here we're using the pygame.key method, more specifically, the pygame.key.get_pressed() method which returns a
        #   tuple of booleans (0 and 1) indicating which key of the keyboard is pressed.
        # print(pygame.key.get_pressed())
        #
        # Storing this tuple into a "keys" variable


        # Afficher le timer
        if len(str(seconds % 60)) == 1:
            creer_message(font, '{}:0{}'.format(seconds // 60, seconds % 60), [650, 90, 20, 20], 'black')
        else:
            creer_message(font, '{}:{}'.format(seconds // 60, seconds % 60), [650, 90, 20, 20], 'black')

        # Afficher le score
        creer_message(font_score, '{}'.format(player2_score), [520, 65, 20, 20], 'red')
        creer_message(font_score, '{}'.format(player1_score), [795, 65, 20, 20], 'red')

        pygame.display.update()

        # Calling the draw Pymunk function to draw on the screen all the Ball's Physic Part
        """draw(space, screen, draw_options)"""
        # This is how fast my Pymunk simulation should go (concept pretty similar to the clock.tick one)
        """space.step(dt)"""
        # 1 frame/second <=> moving 10 pixels/second every frame/image
        # Ceiling/FPS limitation at 60 (600 pixels/second moving)
        clock.tick(fps)

    """stadium_surface = pygame.image.load("DA/backgrounds/dawn.png").convert_alpha()
    stadium_rect = stadium_surface.get_rect(center=(680, 380))
    screen.blit(stadium_surface, stadium_rect)
    creer_message(font, "Player _ has won!!!", [680, 275, 50, 50], 'black')
    slee"""