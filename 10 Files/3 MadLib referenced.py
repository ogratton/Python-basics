read = open('story.txt', 'r')
storyFormat = read.read()

def tellStory():                                        
    userPicks = dict()                                  
    addPick('animal', userPicks)                        
    addPick('food', userPicks)                          
    addPick('city', userPicks)                          
    story = storyFormat.format(**userPicks)             
    print(story)                                        
                                                        
def addPick(cue, dictionary):                           
    '''Prompt for a user response using the cue string, 
    and place the cue-response pair in the dictionary.  
    '''                                                 
    prompt = 'Enter an example for ' + cue + ': '       
    response = input(prompt)                            
    dictionary[cue] = response                          
                                                        
tellStory()                                             
input('Press Enter to end the program.')  
