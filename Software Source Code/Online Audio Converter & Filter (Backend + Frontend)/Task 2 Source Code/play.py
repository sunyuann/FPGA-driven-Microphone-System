import pygame



def playAudio():
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound('pitch.wav')
    my_sound.play()
    pygame.time.wait(int(my_sound.get_length() * 1000))


#playAudio()