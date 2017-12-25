# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
valhand1=0
valhand2=0
hand1=0
hand2=0
player=0
player1_1=0
player1_2=0
in_stand=False
count1=0
count2=0
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    global RANK,SUITS
    def __init__(self):
        # create Hand object
        self.cards=[]
        

    def __str__(self):
        ans = ""
        for i in range(len(self.cards)):
            ans += str(self.cards[i])
        return ans
# return a string representation of a hand

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)
        return self.cards

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value=0
        count=0
        for rank in self.cards:
            r=rank.get_rank()
            value=value+VALUES[r]
        for rank in self.cards:
            r=rank.get_rank()
            if r=='A':
                count+=1
            if(value<=11 and count>0):
                value=value+10
        return value
    def draw_hand1(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for c in self.cards:
            c.draw(canvas,pos)
            pos[0]+=80
            pos[1]+=50
        pos[0]-=160
        pos[1]-=100
        card_back_loc = (CARD_BACK_CENTER[0], 
                         CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_back_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    def draw_hand2(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for c in self.cards:
            c.draw(canvas,pos)
            pos[0]+=80
            pos[1]+=50
    def draw_hand3(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for c in self.cards:
            c.draw(canvas,pos)
            pos[0]+=80
            pos[1]+=50
    # define deck class 
class Deck:
    def __init__(self):
        self.deck_cards=[]	# create a Deck object
        for i in SUITS:
            for j in RANKS:
                self.deck_cards.append(Card(i,j))                                   
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck_cards)# use random.shuffle()

    def deal_card(self):
        card=self.deck_cards.pop(0)# deal a card object from the deck
        return card
    def __str__(self):
        ans = ""
        for i in range(len(self.deck_cards)):
            ans += str(self.deck_cards[i])
        return ans# return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play,valhand1,valhand2,hand1,hand2,player,player1_1,player1_2,in_stand,count1,count2
    if in_play:
        print "Dealer wins"
        count1+=1
    player=Deck()
    player.shuffle()
    player1_1=player.deal_card()
    player1_2=player.deal_card()
    player2_1=player.deal_card()
    player2_2=player.deal_card()
    hand1=Hand()
    hand2=Hand()
    hand1.add_card(player1_1)
    hand1.add_card(player1_2)
    hand2.add_card(player2_1)
    hand2.add_card(player2_2)
    valhand1=hand1.get_value()
    valhand2=hand2.get_value()
    print "hand1 = Dealers hand"
    print "hand2 =",hand2
    print "hand1 = Dealers hand"
    print "hand2 =",hand2.get_value()
    print "Hit or Stand?"
    label.set_text("Hit or Stand?")
    in_stand=False
    in_play = True
    outcome=str(count1)+"/"+str(count2)

def hit():
    global in_play,valhand2,hand2,player,count2,count1,outcome
    # replace with your code below
 
    # if the hand is in play, hit the player
    if in_play:
        label.set_text("Hit or Stand?")
        if valhand2<21:
            player2_3=player.deal_card()
            hand2.add_card(player2_3)
            valhand2=hand2.get_value()
        if valhand2==21:
            print "perfect 21 stand to see the result"
            label.set_text("perfect 21 stand to see the result")
        if valhand2>21:
            print "hand2 =",valhand2
            print "Busted"
            in_play=False
            count1+=1
            label.set_text("Busted")
            print "GAME OVER"
        else: print "hand2 =",valhand2
        print "Hit or stand"
    outcome=str(count1)+"/"+str(count2)           
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play,outcome,hand1,hand2,valhand1,valhand2,player,player1_1,player1_2,in_stand,count1,count2
    if in_play:
        in_stand=True
        if valhand1==valhand2:
            print "Dealer wins"
            count1+=1
            print "GAME OVER"
            in_play=False
        else:
            while valhand1<17:
                player1=player.deal_card()
                hand1.add_card(player1)
                valhand1=hand1.get_value()
            print "hand1 =",valhand1
            if valhand1>21:
                print "you win"
                print "GAME OVER"
                count2+=1
                in_play=False
            else:
                if valhand1>=valhand2:
                    print "Dealer wins"
                    print "GAME OVER"
                    count1+=1
                    in_play=False
                else:
                    print "you win"
                    print "GAME OVER"
                    count2+=1
                    in_play=False
     
    else:
        print "GAME OVER"
    outcome=str(count1)+"/"+str(count2)
            
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global hand1,hand2,player,in_stand,outcome
    hand1.draw_hand1(canvas, [200, 100])
    hand2.draw_hand2(canvas, [200, 300])
    canvas.draw_text("Dealer/You",(450,50),30,"Red")
    canvas.draw_text(outcome,(500,90),30,"Red")
    canvas.draw_text("BLACKJACK",(160,50),40,"darkblue")
    if in_stand:
        hand1.draw_hand3(canvas, [200, 100])
        label.set_text("Game Over")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)
label=frame.add_label(" ")

# get things rolling
deal()
frame.start()


# remember to review the gradic rubric