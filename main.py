from classes.Filter import *
from helpers import *
from classes.ImagePost import ImagePost
from classes.TextPost import TextPost
from buttons import *
from classes.Heart import *

CENSORARR = ["idan", "flick", "damn", "flip"]

def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    purple_filter = Filter((30, 12, 121), 80)

    noa_kerel_post = ImagePost("Noa Kirel", "Israel", "Pouch yeah", "Images/noa_kirel.jpg")
    ronaldo_post = ImagePost("Ronaldo", "Portugal", "Suiii", "Images/ronaldo.jpg")
    hello_post = TextPost("User123", "unknown", "secret", "hello", WHITE, BLACK)
    fast_load_post = ImagePost("The Rizzler", "Mars", "#real", "Images/fast_load.jpg")
    flipped_camera_post = ImagePost("IlovePizza123", "Oven", "#Cypher camera", "Images/flipped_camera.jpg")
    my_name_is_post = ImagePost("Sage", "Valorant", "#Jett revive me Jett", "Images/my_name_is.jpg", purple_filter)

    picturesArr = [noa_kerel_post, ronaldo_post, hello_post, fast_load_post, flipped_camera_post, my_name_is_post]

    hearts = []

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if(mouse_in_button(like_button, pos)):
                    picturesArr[0].add_like()
                    hearts.append(Heart())
                elif(mouse_in_button(comment_button, pos)):
                    comm = read_comment_from_user()
                    comm = censor(comm, CENSORARR)
                    picturesArr[0].add_comment(comm)
                elif(mouse_in_button(click_post_button, pos)):
                    picturesArr = rotate_pictures(picturesArr)
                elif(mouse_in_button(view_more_comments_button, pos)):
                    picturesArr[0].view_more_comments()
                elif(mouse_in_button(share_button, pos)):
                    phone_num = read_comment_from_user()
                    picturesArr[0].share(phone_num)


        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        picturesArr[0].display()

        #Updates hearts on screen
        for heart in hearts:
            heart.move()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


def rotate_pictures(picturesArr):
    temp_picture = picturesArr[-1]
    for index_picture in range(len(picturesArr) - 1, 0, -1):
        picturesArr[index_picture] = picturesArr[index_picture - 1]
    picturesArr[0] = temp_picture
    return picturesArr

def censor(comm, censorArr):
    for censorStr in censorArr:
        if(censorStr in comm):
            comm = comm.replace(censorStr, len(censorStr) * '*')
    return comm

main()
