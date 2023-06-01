import pygame

# Constants
MINIMUM_TRAIL_LENGTH_FACTOR = 0.5

class Slice_Target:

    def __init__(self, canvas, x_pos, x_speed, y_pos, y_speed, gravity, type, images, sound, delay):
        
        # Constants
        self.ADJUST_X_SPEED_CHOPPED_PART_1 = 0.5
        self.ADJUST_X_SPEED_CHOPPED_PART_2 = 2

        # Init miscellaneous variables
        self.canvas=canvas
        self.type = type
        self.status = "flying"                 
        self.images = images
        self.rectangle = self.images[0].get_rect()
        self.scored = False # For scorekeeping in game logic
        self.sound = sound
        self.delay = delay
        
        # Init variables for position and movement
        self.x_pos = x_pos
        self.x_speed = x_speed
        self.y_pos = self.max_y_pos = y_pos
        self.y_speed = y_speed
        self.gravity = gravity     

        self.target_rect = pygame.Rect(0,0,0,0)

    def update(self, mouse_x, mouse_y, mouse_pressed, trail_length_factor):
        
        self.trail_length_factor = trail_length_factor # Needed to see how long the trail is. 
                                                       # If it's to short target will not be sliced to prevent onnly touching

        # Wait with updating until the delay is 0
        if self.delay > 0:
            self.delay -= 1
            return

        # Update if still flying and not touched
        if self.status == "flying":
            # Adjust position and y speed
            self.x_pos += self.x_speed
            self.y_pos += self.y_speed
            self.y_speed += self.gravity
        
            # See if target is sliced (not only touched)
            #target_rect = pygame.Rect(self.x_pos-self.width, self.y_pos-self.width, self.width*2, self.width*2)            
            if mouse_pressed and self.rectangle.collidepoint(mouse_x, mouse_y) and self.trail_length_factor >= MINIMUM_TRAIL_LENGTH_FACTOR:
                self.status = "chopped"
                pygame.mixer.Sound.play(self.sound)
                # Create 2 objects to fall down
                self.x1_pos = self.x2_pos = self.x_pos
                self.y1_pos = self.y2_pos = self.y_pos

                # Change the x speed of those object to make them g=fall apart
                if self.x_speed > 0:
                    self.x1_speed = self.x_speed * self.ADJUST_X_SPEED_CHOPPED_PART_1
                    self.x2_speed = self.x_speed * self.ADJUST_X_SPEED_CHOPPED_PART_2
                else:
                    self.x1_speed = self.x_speed * self.ADJUST_X_SPEED_CHOPPED_PART_2
                    self.x2_speed = self.x_speed * self.ADJUST_X_SPEED_CHOPPED_PART_1            

        # Update if chopped
        if self.status == "chopped":
            # Adjust position and y speed
            self.x1_pos += self.x1_speed
            self.y1_pos += self.y_speed
            self.x2_pos += self.x2_speed
            self.y2_pos += self.y_speed
            
            self.y_speed += self.gravity*3

        # See if flight of target is complete (either chopped or not)
        if self.status == "chopped" and self.y1_pos > self.max_y_pos:            
            self.status = "succes"
        if self.status == "flying" and self.y_pos > self.max_y_pos:                    
            self.status = "failed"            
        
    def draw(self):
        # Draw if target is not yet touched
        if self.status == "flying":
            self.rectangle = self.canvas.blit(self.images[0], (self.x_pos, self.y_pos))              

        # Draw target if chopped         
        if self.status == "chopped":
            self.canvas.blit(self.images[1], (self.x1_pos, self.y1_pos)) 
            self.canvas.blit(self.images[2], (self.x2_pos, self.y2_pos)) 