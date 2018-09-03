#Python Dictionaries allow you to connect pieces of related information.
#Each piece of info is stored as a key-value pair

games = {'foot_ball':'messi','cricket':'dhoni'}
print(games)

#Getting the key associated with Key
print(games['cricket'])

#Getting the value with Get

games_football = {games.get('foot_ball')}
print(games_football)

# Adding Key-value pair
games['hockey'] = 'India'
games['chess'] = 'Viswanathan'

print(games)

#changing value in dictionary

games['foot_ball'] = 'Neymar'
games['cricket'] = 'Kohli'

print(games)

#Deleting a Key-value pair
del games['cricket']
print(games)

#Looping thro' Dictionary

#You can loop thro' 3 ways 1) Loop thro' all the elements 2)Loop thro Key 3) Looping thro' Values

# store people languages

state_language ={
				 'TamilNadu': 'Tamil',
				 'Karnataka': 'Kannada',
				 'Telugana': 'Telugu',
				 'Delhi': 'Hindi'
				 }
				 
# Show Each state language info
for state, language in state_language.items():
	print(state +" : "+language)
	
#Looping thro Keys
for state in state_language.keys():
	print(state)
	
#Looping thro values
for language in state_language.values():
	print(language)
	
# Length of Dictionary
num_languages = len(state_language)
print(num_languages)