import tkinter
import random

# list of possible colors
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black',
          'Yellow', 'Orange', 'Cyan', 'Purple', 'Brown', ]

score = 0

#The game time left, initially 30 seconds

timeleft = 60

#Function that will start the game

def startGame(event):

    if timeleft == 60:
        #start the countdown timer.
        countdown()

    #run the function to
    # choose the next color.
    nextColor()

"""Function to choose and display the next color"""

def nextColor():
    # use the  globally declared 'score'
    #and 'play' variables above.
    global score
    global timeleft

    #if a game is currently in play
    if timeleft > 0:


        # make the text entry box active
        e.focus_set()

        """
        if the color typed is equal
        to the color of the text
        """

        if e.get().lower() == colors[1].lower() :
            score += 1

        #clear the text entry box.
        e.delete(0, tkinter.END)

        random.shuffle(colors)

        #Change the color to type, by changing the
        #text _and_ the color to a random color value
        label.config(fg = str(colors[1]), text = str(colors[0]))

        #update the score
        scoreLabel.config(text = 'Score: {}'.format(str(score)))

#Countdown timer function

def countdown():
    global timeleft

    #If a game is in play
    if timeleft > 0:

        #decrement the timer
        timeleft -= 1

        # update the time left label
        timeLabel.config(text = 'Time left {}'.format(str(timeleft)))

        #run the function again after one second
        timeLabel.after(1000, countdown)





#Driver code
#Create a GUI window
root = tkinter.Tk()

#Set the title
root.title('Guess the color')

# settin the size
root.geometry('375x200')

# adding an instruction label
instructions = tkinter.Label(root, text = 'Type the color of the words, '
                                          'and not the word text !'
                             , font = ('Helvetica', 12))

instructions.pack()

#add a score label

scoreLabel = tkinter.Label(root, text = 'Press enter to start ',
                           font = ('Helvetica', 12))

scoreLabel.pack()

# add a time left label

timeLabel = tkinter.Label(root, text = 'Time left{}'.format(str(timeleft)),
                           font = ('Helvetica', 12))

timeLabel.pack()

#add a label for displaying the color

label = tkinter.Label(root, font = ('Helvetica', 60))

label.pack()

#add a text entry box for typing in the colors
e = tkinter.Entry(root)


#running the 'start Game' function when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

# set the focus_set()
e.focus_set()

#start the GUI
root.mainloop()
