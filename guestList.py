# Making a list of Guests to Invite

myGuests = ['Mike', 'Paul', 'Rogers', 'Philliam', 'Apollo', 'John']

# Inviting my Guests
# Guest1 = 'Mike'
print("Dear " + myGuests[0].title() + " \nYou are invited for my party that i have  \n\t")
print("Dear " + myGuests[1].title() + " \nYou are invited for my party that i have organized\n\t")
print("Dear " + myGuests[2].title() + " \nYou are invited for my party that i have organized\n\t")
print("Dear " + myGuests[3].title() + " \nYou are invited for my party that i have organized\n\t")
print("Dear " + myGuests[4].title() + " \nYou are invited for my party that i have organized\n\t")
print("Dear " + myGuests[5].title() + " \nYou are invited for my party that i have organized\n\t")

# Guest Who Wont make it
print("Guest " + myGuests[3] + " Wont make it to the party")

newGuest = myGuests[3] = "Kyagulanyi"
print(myGuests)

# new invite messages

print("Dear " + myGuests[0].title() + " \nYou are invited for my party that i have  \n\t")
print("Dear " + myGuests[1].title() + " \nYou are invited for my party that i have organized\n\t")
print("Dear " + myGuests[2].title() + " \nYou are invited for my party that i have organized\n\t")
print("Dear " + myGuests[3].title() + " \nYou are invited for my party that i have organized\n\t")
print("Dear " + myGuests[4].title() + " \nYou are invited for my party that i have organized\n\t")
print("Dear " + myGuests[5].title() + " \nYou are invited for my party that i have organized\n\t")

# Bigger table

print("Just found a bigger dinner table so inviting more guests")

myGuests.insert(0, 'Obwalinga')
print(myGuests)

# appending guests to the list

myGuests.append('Ronaldo')
print(myGuests)

# length of my string
print(len(myGuests))
