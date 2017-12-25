# template for "Stopwatch: The Game"
import simplegui
# define global variables
time="0.00.0"
count=0
score=0
counter=0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time
    a="0"
    b="00"
    c="0"
    st=str(t)
    if(len(st)==4):
        num=t/1000
        if(num<6):
            num=t/10
            min=num/60
            a=str(min)
            sec=num%60
            sec=str(sec)
            if(len(sec)==1):
                b="0"+sec
            else:
                b=str(sec)
            rem=t%10
            c=str(rem)
        else:
            timer.stop()
    elif(len(st)==3):
        num=t/100
        if(num<6):
            rem=t%100
            b2=rem/10
            b=str(num)+str(b2)
            rem=rem%10
            c=str(rem) 
        else:
            num=t/600
            diff=t-600
            a=str(num)
            rem=diff%10
            rem=str(rem)
            b1=diff/10
            b2=str(b1)
            if(len(b2)==1):
                b="0"+b2
                c=str(rem)
            else:
                b3=b1/10
                b4=b1%10
                b=str(b3)+str(b4)
                c=str(rem)
    elif(len(st)==2):
        num=t/10
        b="0"+str(num)
        rem=t%10
        c=str(rem)
    else:
        c=st[0]
    time=a+":"+b+":"+c
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
def stop():
    timer.stop()
    global score
    global counter
    if(time[5]=="0"):
        score+=1
    else:
        counter+=1
def reset():
    timer.stop()
    global counter
    global score
    global time
    time="0.00.0"
    counter=0
    score=0
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    count+=1
    format(count)

# define draw handler
def draw(canvas):
    canvas.draw_text(time,(90,160),50,"red")
    canvas.draw_text("Score:"+str(score)+"/"+str(counter),(190,30),20,"white")
    
# create frame
frame=simplegui.create_frame("STOPWATCH",300,300)
timer=simplegui.create_timer(100,timer_handler)
# register event handlers
frame.set_draw_handler(draw)
frame.add_button("START",start,100)
frame.add_button("STOP",stop,100)
frame.add_button("RESET",reset,100)

# start frame
frame.start()

# Please remember to review the grading rubric
