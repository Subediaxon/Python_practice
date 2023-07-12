from time import sleep;
from random import randrange;

leftWidth = 40
gapWidth = 20
WIDTH = 100

# Display the tunnel segment:
rightWidth = WIDTH - gapWidth - leftWidth
print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))

while(True):
    random = randrange(1,6)
    
    if (random < 4) and (leftWidth > 5):
        leftWidth = leftWidth - random
        rightWidth = rightWidth + random
        print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))
        sleep(0.07)
    elif (random > 3) and (rightWidth > 10):
        leftWidth = leftWidth + random
        rightWidth = rightWidth - random
        print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))
        sleep (0.07)
    else:
        print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))
        sleep (0.07)
    
    