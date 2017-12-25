# implementation of card game - Memory

import simplegui
import random
state=0
turns=0
card=[1,2]
list1=[0,1,2,3,4,5,6,7]
list2=[0,1,2,3,4,5,6,7]
d1={0:False,1:False,2:False,3:False,4:False,5:False,6:False,7:False}
d2={0:False,1:False,2:False,3:False,4:False,5:False,6:False,7:False}
# helper function to initialize globals
def new_game():
    global turns,state
    random.shuffle(list1)
    random.shuffle(list2)
    turns=0
    state=0
    for num in d1:
        d1[num]=False
    for num in d2:
        d2[num]=False

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state,turns,card
    num= pos[0] // 50
    if state == 0:
            if(num<8):
                num1=list1[num]
                if(d1[num1]==True):
                    d1[num1]=True
                else:
                    d1[num1]=True
                    state+=1
                    card[0]=num1
            else:
                num2=list2[num-8]
                if(d2[num2]==True):
                    d2[num2]=True
                else:
                    d2[num2]=True
                    state+=1
                    card[0]=num2
    elif state == 1:
            if(num<8):
                num1=list1[num]
                if(d1[num1]==True):
                    d1[num1]=True
                else:
                    d1[num1]=True
                    state+=1
                    card[1]=num1
            else:
                num2=list2[num-8]
                if(d2[num2]==True):
                    d2[num2]=True
                else:
                    d2[num2]=True
                    state+=1
                    card[1]=num2
            if(card[0]==card[1]):
                state=0
                turns+=1
    else:
        d1[card[0]]=False
        d1[card[1]]=False
        d2[card[0]]=False
        d2[card[1]]=False
        state=0
        if(num<8):
                num1=list1[num]
                if(d1[num1]==True):
                    d1[num1]=True
                else:
                    d1[num1]=True
                    state+=1
                    card[0]=num1
        else:
                num2=list2[num-8]
                if(d2[num2]==True):
                    d2[num2]=True
                else:
                    d2[num2]=True
                    state+=1
                    card[0]=num2
        turns+=1

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global state
    x=0
    y=50
    label.set_text("Turns:"+str(turns))
    for num in list1:
        if d1[num]==True:
            canvas.draw_text(str(num),(15+x,50),30,"White")
        else:
            canvas.draw_polygon([(x,0),(y,0),(y,100),(x,100)],1,"Red","Green")
        x+=50
        y+=50
    for num in list2:
        if d2[num]==True:
            canvas.draw_text(str(num),(15+x,50),30,"White")
        else:
            canvas.draw_polygon([(x,0),(y,0),(y,100),(x,100)],1,"Red","Green")
        x+=50
        y+=50

            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns:0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric