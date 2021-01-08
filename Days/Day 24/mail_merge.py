# Day 24 project - Mail Merge.

# Relative file paths for required files.
invited_names_file = "./Input/Names/invited_names.txt"
starting_letter_file = "./Input/Letter/starting_letter.docx"
output_folder = "./Output/ReadyToSend"

# Get a list of all the names from the invited_names file.
with open(invited_names_file) as names:
    all_names = names.readlines()

# Get the contents of the starting letter.
with open(starting_letter_file) as starting_letter:
    letter = starting_letter.read()

# Loop through the list of names and replace "[name]" in the starting letter
# with each person's name and also create a new_file "letter_for_{persons_name}"
# and write it in that file.
for name in all_names:
    # Remove the newline(\n) from the end of the name.
    stripped_name = name.rstrip()
    invitation_letter = letter.replace("[name]", stripped_name)
    # Write a final invitation letter and save it in a new docx file.
    with open(f"{output_folder}/letter_for_{stripped_name}.docx", "w") as invitation:
        invitation.write(invitation_letter)
