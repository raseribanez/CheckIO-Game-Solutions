# Non Unique Elements
# This isn't mission 3 - if you go back to the main menu (elementary)
# you will see other missions. This one was called:
# Non Unique Elements

# So I didn't mess around with this one. Here it is..As it needs to be to nail the mission
# Or is it ? By the time you finish solving my fiddly riddles you could have figured out how
# to write the code

def checkio(data):
    newlist = []
    for i in data:
        if data.count(i) > 1:
            newlist.append(i)

return newlist
