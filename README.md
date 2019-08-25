 # GroupMe Scraper
 A python script to parse *downloaded* GroupMe html webpages to count the number of messages each user has sent in the group.

## How It Works
- Navigate to your desired group.
- Scroll to the top of that group's messages
- Right click on a blank part of the page
- Click "save-as"
- Save the file in the same directory as this program

Then run the program.
It will read the local html webpage and append to a list, the name of the message sender for every message in the webpage.
Then it will print the total number of messages and print a dictionary with the number of messages sent by each member in ascending order. Then it will print a dictionary with the percentage of messages sent by each member in ascending order. Finally it will plot a bar graph of the number of messages sent by each member in ascending order.
