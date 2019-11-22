teams = {                                      
  "astros": ["Altuve", "Correa", "Bregman"],  
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts']
  }

featured_team = teams.get('mets', 'nothing found')
print(featured_team)

"""
add new key value pairs to python dictionaries 


teams = {                                      # variable named teams
  "astros": ["Altuve", "Correa", "Bregman"],   # key named astros and a nested list
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

teams ['red sox'] = ['Price', 'Betts'] #add new key here- say teams then the list red sox and set it equal to a list containing Price and Betts

print(teams)
/////////////////////////////////////////////////////////////
From Benjamin Nicklaus to Everyone:  02:09 PM
teams = {
    "astros": ["Altuve", "Correa", "Bregman"],
    "angels": ["Trout", "Pujols"],
    "yankees": ["Judge","Stanton"],
    "red sox": ["Price", "Betts"],
}

featured_team = teams.get('mets', 'No featured team') #call the teams dictionary first then get which get takes 2 arguments takes the key and then the value, with a default value
#key look up above doesn't exist so it will print No Featured team

print(featured_team)///////////////////////////////////////////////////////////
"""