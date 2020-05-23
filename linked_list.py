m

class Node:
    def __init__(self, question, answer, attempts,
                 correct_attempts,last_answer, last_time, next=None):
        self.question = question
        self.answer = answer
        self.attempts = attempts
        self.correct_attempts = correct_attempts
        self.last_answer = last_answer
        self.last_time = last_time
        self.next = next

#this is the linked list we will be operating in, it contains a title and head
class SLinkedList:
    def __init__(self, title):
        self.head = None
        self.current = None
        self.title = title


#create a new series of flashcards
def add_series(series_name):
    blash = SLinkedList(series_name)
    print(blash.title)
    print(blash.head)
    return blash

#create a new flashcard
def add_flashcard(question, answer,last_time, series):
    #this should create a new flashcard node with the values required
    new = Node(question, answer, 0, 0, None, last_time)
    current = new

    #now we have to figure out where to put the flashcard in the series
    #if the series is empty add it as the head
    if series.head == None:
        series.head = new
    #otherwise traverse the list until the end and add it there
    else:
        next = head
        while next.next != None:
            next = next.next
        next.next = new

    return new

#function to move allow in sequence
def move_current(series):
    series.current = series.current.next

#function to update flashcard currently working on, i dont know how to select currently working on though
def update_flashcard(series, correct_status, time):
    x = series.current.attempts
    y = series.current.correct_attempts

    series.current.attempts = x + 1
    series.current.correct_attempts = y + 1

    series.current.last_answer = correct_status
    series.current.last_time = time

#list of existing topics of flashcards
topic_list = []
#
linkedlist_list = []

#there should be a build mode and a review mode the user selects before entering
mode = input("Would you like to create more flashcards,review or leave?")

while mode != 'leave':
  if mode == 'build':
  #user should have the option to build on existing database or create a new one
    print(topic_list)
    add_create = input("Please select from the above topics or enter new to create a new database: ")

    if add_create == 'new':
    #need to create else statement for this to build upon existing

    #get input from user to create a flashcard
      s = input("What is the topic? ")
    #please change the name blash at some point
      blash = SLinkedList(s)
    #add topic to topic list
      topic_list.append(blash.title)
      linkedlist_list.append(blash)

    elif add_create in topic_list:
      i = 0
      #check to make sure this works
      while add_create != topic_list[i]:
        i = i + 1

      blash = linkedlist_list[i]

    while input("would you like to create another question? ") == 'yes':
      question = input("What is your question? ")
      answer = input("What is your answer? ")

  #for now the question card will have basic info that you will have to update later
      new_flashcard = Node(question, answer,0, 0, None, 0, None)

      if blash.head == None:
        blash.head = new_flashcard
        blash.current = new_flashcard
      else:
    #so I'm pretty sure I've done something wrong here regarding memory so will have to make sure looper actually works
    #this appears to work to create flashcards
        looper = blash.head
        while looper.next != None:
          looper = looper.next

        looper.next = new_flashcard

    mode = input("what would you like to do now?")

  elif mode == 'review':
    print(topic_list)

    #pick a topic
    review_topic = input("What topic would you like to review? ")

    if review_topic in topic_list:
      j = 0
      while review_topic != topic_list[j]:
        j = j + 1

      flash_set = linkedlist_list[j]

      while flash_set.current.next != None:
          print(flash_set.current.question)

          if input("press y to see answer") == 'y':
            print(flash_set.current.answer)

            right_wrong = input("Did you get the question right or wrong? ")

            #updating the flashcard
            #still have to figure out how to update time
            flash_set.current.attempts += 1

            if right_wrong == 'right':
                flash_set.current.correct_attempts += 1
                flash_set.current.last_answer = 'right'
            else:
                flash_set.current.last_answer = 'wrong'
        

        flash_set.current = flash_set.current.next

      flash_set.current = flash_set.head

#this is a check to see how things went
#print(blash.head.question)
#print(blash.head.next.question)
