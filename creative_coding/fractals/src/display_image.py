import sys
import pygame

display_width = 600
display_height = 600
clock = pygame.time.Clock()
img = pygame.image.load('xzibit.png')

def rotate(surface, angle, pivot, offset):
    """Rotate the surface around the pivot point.

    Args:
        surface (pygame.Surface): The surface that is to be rotated.
        angle (float): Rotate by this angle.
        pivot (tuple, list, pygame.math.Vector2): The pivot point.
        offset (pygame.math.Vector2): This vector is added to the pivot.
    """
    rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect  # Return the rotated image and shifted rect.

window = pygame.display.set_mode((display_width,display_height))
# pygame.display.set_caption('A bit Racey')
for i in range(360):
    window.fill((0, 0, 0))
    # img_to_display = pygame.transform.rotate(img, i)
    # img_to_display = pygame.transform.rotozoom(img, i, 1)
    rotated_image, rect = rotate(img, i, (300, 300), pygame.math.Vector2(-115, 115))
    # window.blit(img_to_display, (300, 300))
    window.blit(rotated_image, rect)
    window.blit(rotated_image, rect)
    pygame.display.update()
    clock.tick(60)

# window = pygame.display.set_mode((display_width,display_height))
# # pygame.display.set_caption('A bit Racey')
# for i in range(360):
#     window.fill((0, 0, 0))
#     # img_to_display = pygame.transform.rotate(img, i)
#     img_to_display = pygame.transform.rotozoom(img, i, 1)
#     window.blit(img_to_display, (300, 300))
#     pygame.display.update()
#     clock.tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)


# clock = pygame.time.Clock()
# crashed = False
# carImg = pygame.image.load('racecar.png')

# def car(x,y):
#     gameDisplay.blit(carImg, (x,y))

# x =  (display_width * 0.45)
# y = (display_height * 0.8)
