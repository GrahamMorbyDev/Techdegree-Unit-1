attendees = ["Graham", "Ben", "Katie"]
attendees.append('Ashley')
attendees.extend(["James", "Gill"])
optional_invitees = ["Ben", "Dave"]
potential_attendees = attendees + optional_invitees
print("There are", len(potential_attendees), "potential attendees currently")

# Turn a list to a string
to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)

print("To: " + to_line)
print("To: " + cc_line)

# Turn back to a list
new_list = to_line.split(', ')
print(new_list)
