import pandas as pd

# Read the CSV file into a Pandas dataframe
df = pd.read_csv('/home/pranav125/Desktop/mycroft-core/skills/birthday-skill/birthdays.csv')

# Create a sentence containing all the data from the CSV file
for index, row in df.iterrows():
    name = row['Name']
    dob = row['DOB']
    city = row['City']
    sentence += f"{name} was born on {dob} in {city}. "

# Open a text file for writing
with open('morning.txt', 'w') as txtfile:
    # Write the sentence to the text file
    txtfile.write(sentence)