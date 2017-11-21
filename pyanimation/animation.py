"""
pyanimation
-----------
A python module to easily create animation
By Estevao Fonseca
License: MIT
"""
import pygame


class Animation:
    """A class to create animations objects from sprites images"""
    def __init__(self, image_path):
        """
        image_path: the path to the sprite file
        """
        self.x = 250
        self.y = 200
        self.ani_pos = 0
        self.ani_max = 0
        self.animation = []
        self.dict_of_rects = {}
        self.animation_speed = {}
        self.local_action = ""
        self.manual_list = []
        self.repeat_state = {}
        self.facing_right = True
        self.restart_ani = False
        self.load_sprites(image_path)

    def rect_list(self, xo, yo, sprite_width, sprite_height, cols, rows):
        """
        Build a list of rectangles sprites
        """
        rect = []
        for row in range(rows):
            for i in range(cols):
                rect.append(pygame.Rect(xo+sprite_width*i, yo+sprite_height*row, sprite_width, sprite_height))
        return rect

    def insert_frame(self, xo, yo, sprite_width, sprite_height):
        """
        Insert frame by frame manually
        xo,yo: initial points at the top left corner
        sprite_width,sprite_height: length of sprites
        """
        self.manual_list.append(pygame.Rect(xo, yo, sprite_width, sprite_height))

    def build_animation(self, action_name, repeat=True, duration=40):
        """
        Build Animation from the inserted frames
        and sets a name for the animation
        action_name: a name to an animaiton action
        repeat: True to perform a non-stop animation, False to run just once
        duration: duration of the animation in milliseconds
        """
        speed = round(duration/16.66)
        if speed <= 0:
            speed = 1
        self.ani_speed = speed
        self.animation_speed[action_name] = speed
        self.dict_of_rects[action_name] = self.manual_list
        self.manual_list = []
        self.repeat_state[action_name] = repeat
        self.action_name = action_name

    def erase_positions(self, action_name, indexes):
        """
        Erase a rectangle sprite of the self-generated rectangle list
        """
        indexes.sort()
        indexes.reverse()
        local_list = self.dict_of_rects[action_name]
        for item in indexes:
            local_list.pop(item)
        self.dict_of_rects[action_name] = local_list

    def repeat_position(self, action_name, ntimes, indexes):
        """
        Repeat a rectangle sprite of the self-generated rectangle list
        """
        indexes.sort()
        local_list = self.dict_of_rects[action_name]
        # append at the end n times
        while ntimes != 0:
            for item in indexes:
                local_list.append(local_list[item])
            ntimes = ntimes - 1

    def load_sprites(self, image_path):
        """
        Load the sprites image file
        """
        import os
        image_path = os.path.abspath(image_path)
        self.sprite_sheet = (pygame.image.load(image_path).convert_alpha())
        self.width, self.height = self.sprite_sheet.get_size()

    def create_animation(self, xo, yo, sprite_width, sprite_height, action_name, repeat=True, duration=40, **kwargs):
        """
        Create an intire animation and sets a label to the animation
        xo,yo: initial points at the top left corner
        sprite_width,sprite_height: length of sprites
        action_name: a name to an animaiton action
        repeat: True to perform a non-stop animation, False to run just once
        duration: duration of the animation in milliseconds

        Optional kwargs
        to use just some slices of a sprite image
        rows: a row is an horizontal sequence of sprites
        cols: the vertical separation of sprites
        """
        if kwargs:
            if "rows" in kwargs:
                rows = kwargs["rows"]
            if "cols" in kwargs:
                cols = kwargs["cols"]
        if not ('rows' in locals()):
            rows = int(self.height/sprite_height)
        if not ('cols' in locals()):
            cols = int(self.width/sprite_width)

        speed = round(duration/16.66)
        if speed <= 0:
            speed = 1
        self.ani_speed = speed
        self.animation_speed[action_name] = speed
        self.dict_of_rects[action_name] = self.rect_list(xo, yo, sprite_width, sprite_height, cols, rows)
        self.repeat_state[action_name] = repeat
        self.action_name = action_name

    def frame_list(self, action_name):
        return self.dict_of_rects[action_name]

    def run(self, action_name):
        """It allows the animation to start over each time it's called"""
        self.action_name = action_name
        # restart animation which play only once at time
        self.restart_ani = True

    def flip_animation(self, frame_list):
        """Flips animation to left or right"""
        try:
            cropped = self.sprite_sheet.subsurface(frame_list[self.ani_pos]).copy()
        except IndexError:
            print("List index out of range ocurred")
            self.ani_pos = 0
            cropped = self.sprite_sheet.subsurface(frame_list[self.ani_pos]).copy()
        if self.facing_right is False:
            cropped = pygame.transform.flip(cropped, True, False)
        return cropped

    def update_surface(self):
        """
        Run and update the animation
        Also flips the animation to righ or left as requested
        """
        # new animation starts at 0
        if self.local_action != self.action_name:
            self.ani_pos = 0
        self.local_action = self.action_name
        frame_list = self.frame_list(self.action_name)
        self.ani_max = len(frame_list)-1
        self.ani_speed -= 1
        # ani_speed is like a timer
        # when it reachs 0 it increments the loop
        if self.ani_speed == 0:
            self.ani_speed = self.animation_speed[self.action_name]
            # restart non-stop animation
            if (self.ani_pos == self.ani_max) and self.repeat_state[self.action_name]:
                self.ani_pos = 0
            # restart animation which play only once at time
            elif (self.ani_pos == self.ani_max) and self.restart_ani:
                self.ani_pos = 0
            # if it haven't reached the last frame it increments
            elif self.ani_pos < self.ani_max:
                self.ani_pos += 1
            self.restart_ani = False
        subsurface = self.flip_animation(frame_list)
        return subsurface
