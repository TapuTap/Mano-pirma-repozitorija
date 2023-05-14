# implementation of card game - Memory
# (c) 2013 boxmein
# MIT license if applicable
# prefers being run in CodeSkulptor
# Live: http://www.codeskulptor.org/#user14_m6ycUKSq7n_0.py
# (live url's last digits may change)

import PySimpleGUI, random, math

# ---   Constants  ---
C_PAD = 5  		# some spacing between cards
C_WIDTH = 50		# how wide a card image is
C_HEIGHT = 100		# how high a card image is
C_S = 16 			# card count. must be even!!
DEBUG = False
DEBUG = True		# y'know
# --- / Constants ---

framew = 0			# Frame width
frameh = 0			# Frame height
c_array = []		# Array of Card objects.
turns = 0			# How many turns were taken? 
clickedcard = None	# The card last clicked. 
cardstohide = []	# Cards marked for hiding
turnlabel = None	# Label on which to display turns
motlabel = None		# Motivation Label v1.0 


# :) 
motivation = ["Good job!", "Yes!", "Awesome!", "Radical!",
              "Mathematical!", "You're on fire!", "Neat!",
              "Keep at it!", "Prosperous!", "Great job!",
              "Nice!", "[INSERT HOMETOWN HERE]", 
              "[INSERT MOTIVATION HERE]"]

## Initialization and bounds check. 
def init():
    global c_array, frame, framew, frameh
    global turnlabel, motlabel
    
    ## 1. Frame size setup by card count. 
    if C_S <= 16:
        framew = (C_WIDTH + C_PAD) * C_S
        frameh = C_HEIGHT + 2*C_PAD + (12*10 if DEBUG else 0)
        
    ## 1.4545. Doubles as a card limit!
    else:
        print("Too many cards used!")
        exit()
    ## 1.99. Card count bounds check
    if C_S % 2: 
        print("Card count can't be an odd number!")
        exit()
    if C_S <= 0:
        print ("Too little cards used :(")
        exit()
    
    
    ## 2. Frame setup
    frame = PySimpleGUI.create_frame("Memory", framew, frameh)
    frame.add_button("Restart Game", restart)
    turnlabel = frame.add_label("Turns: (none)")
    motlabel = frame.add_label("")
    if DEBUG: 
        frame.add_label("Debug buttons:")
        frame.add_button("Hide marked cards", hideCards)
    frame.set_mouseclick_handler(mouseclick)
    frame.set_draw_handler(draw)
    frame.start()
    
    ## 3. (Re)Start game
    restart()


## When the game is restarted
def restart (): 
    global c_array, turns
    ## 1. Reset turn count
    turns = 0
    
    ## 2. Reset card array and assign them values
    ids = range(0, C_S/2) * 2
    random.shuffle(ids) 
    c_array = []
    for i in range(C_S): 
        c = Card(ids[i])
        c.x = i * (C_WIDTH + C_PAD) + C_PAD
        c.y = C_PAD
        c_array.append(c)

## Draws a card onto the screen
## This is where most of the magic happens for drawing
def drawCard(can, card):  
    global c_array, frame
    if card.hidden:
        can.draw_polygon(
                         [(card.x, card.y), 
                          (card.x+C_WIDTH, card.y), 
                          (card.x+C_WIDTH, card.y+C_HEIGHT), 
                          (card.x, card.y+C_HEIGHT)
                          ], 1, "White", "Gray")
        if DEBUG: 
            ## Text is bottom center :) 
            tw = frame.get_canvas_textwidth(str(card.value), 36, "sans-serif")
            can.draw_text(str(card.value), (card.x+C_WIDTH/2-tw/2, card.y+C_HEIGHT), 36, "White", "sans-serif")
            
    else: 
        ## Text is bottom center :) 
        tw = frame.get_canvas_textwidth(str(card.value), 36, "sans-serif")
        can.draw_polygon(
                         [(card.x, card.y), 
                          (card.x+C_WIDTH, card.y), 
                          (card.x+C_WIDTH, card.y+C_HEIGHT), 
                          (card.x, card.y+C_HEIGHT)
                          ], 1, "Gray", ("Silver" if card.paired else"White"))
        can.draw_text(str(card.value), (card.x+C_WIDTH/2-tw/2, card.y+C_HEIGHT), 36, "Black", "sans-serif")

## Main logic function, handles clicks
def mouseclick(pos):
    global clickedcard, cardstohide, turns
    global motlabel, motivation
    
    hideCards()
    
    # Crude mouse click range handling
    for each in c_array: 
        if ((each.x < pos[0] < each.x+C_WIDTH) and
            (each.y < pos[1] < each.y+C_HEIGHT) and
            each.hidden):
            # Delete cards marked for deletion
            turns += 1
            updateLabel(turns)
            each.hidden = False
            
            ## 1. If there's already a card active
            if clickedcard: 
                # 1.1. If the clicked card has the same value
                if clickedcard.value == each.value: 
                    print("Matched cards %s and %s !" % (clickedcard, each))
                    motlabel.set_text(motivation[random.randrange(0, len(motivation))])
                    clickedcard.paired = each.paired = True
                    clickedcard = None
                    checkWin()
                # 1.2. If the cards differ
                else: 
                    print("Failed to match cards %s and %s, hiding" % (clickedcard, each))
                    cardstohide.extend([clickedcard, each])
                    clickedcard = None
            else: 
                clickedcard = each
            # stop going through the rest if the clicked one was found
            return

## Draw loop for cards and debug text.
def draw(c):
    global c_array, turns, clickedcard, cardstohide
    for each in c_array:
        drawCard(c, each)
    if DEBUG: 
        global framew, frameh
        c.draw_text("DEBUG: True, cards: %d, card-w: %d, card-h: %d, card-padding: %d" %(C_S, C_WIDTH, C_HEIGHT, C_PAD), (5, 122), 12, "silver", "sans-serif")
        c.draw_text("frame-width: %d, frame-height: %d" % (framew, frameh), (5, 134), 12, "silver", "sans-serif")
        c.draw_text("turns-taken: %d, card-array: %s" % (turns, c_array), (5, 146), 12, "silver", "sans-serif")
        c.draw_text("cards-to-hide: %s, clicked-card: %s" % (repr(cardstohide),repr(clickedcard)), (5,158), 12, "silver", "sans-serif")
        if clickedcard is not None:
            c.draw_text("pairing-card: (x: %d, y: %d, hidden: %d, value: %d)" % (clickedcard.x, clickedcard.y, clickedcard.hidden, clickedcard.value), (5,170), 12, "silver", "sans-serif")

## Hide all the cards marked for hiding
def hideCards ():
    global cardstohide
    for each in cardstohide:
        each.hidden = True
    cardstohide = []

## Update the turn count label
def updateLabel(turns):
    global turnlabel
    turnlabel.set_text("Turns: %d" % turns)

## Check whether or not the user has winrar
def checkWin():
    global c_array
    for each in c_array: 
        if not each.paired:
            return False
    return True
    
## Card class to hold some values for me
class Card: 
    x = 0
    y = 0
    hidden = True
    paired = False
    # 0 .. CARDS/2
    value = 0
    def __init__ (self, value): 
        self.value = value
    # Yay string concatenation
    def __repr__ (self):
        return "<%d>" % self.value

## initialize everything
init()


#

# Always remember to review the grading rubric
## Rubric: 
# 1. 16 cards in arbitrary layout 
# 2. 8 unique pairs of cards
# 3. ignores clicks on exposed cards
# 4. a click exposes the card at the start of the game
# 5. if unpaired is exposed: second card click exposes second card
# 6. if unexposed clicked + two unpaired exposed: hides last two, exposes clicked
# 7. if unexposed 1 + expose 1 click + match the two: shows the two, ends turn
# 8. pairs of cards remain exposed until new game
# 9. reset button
# 10. reset button shuffles cards

# Thanks for reviewing!