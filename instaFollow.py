import json
import sys
import os

followers = open('followers.json', 'r')
following = open('following.json', 'r')

followers_json = json.load(followers)
following_json = json.load(following)

# Global since multiple functions utilize the contents of this set
set_of_non_mutuals = set()

"""
Sorts through the following and compares it to the followers to check if the following
user follows the account back. If the user is in the following but not  followers,
we add them to the set of non mutuals.
"""
def check_all_non_mutuals(clean = 1):

    set_of_following = set()
    set_of_followers = set()

    for user in following_json['relationships_following']:
        set_of_following.add(user['string_list_data'][0]['value'])

    for user in followers_json['relationships_followers']:
        set_of_followers.add(user['string_list_data'][0]['value'])

    set_mutuals = set_of_followers and  set_of_followers

    for user in set_of_following:
        if user not in set_mutuals:
            set_of_non_mutuals.add(user)

    sorted_users = sorted(set_of_non_mutuals)

    if clean:
        for user in sorted_users:
            print(user)


"""
This function checks all non mutual accounts, sorts them how the user wants,
and then prints them out.The user can display all non mutuals, or sort them by
starting character. This allows for user readablility and for the user to be able
to break their non mutuals down into shorter chunks in the event they have a
large set of non mutuals.
"""

def check_all_non_mutuals_of_starting_char():
    list_of_char_names = []
    print("You will be prompted to enter a character of the starting letter of a username")
    print("if you dont have a prefered character, just press enter")
    char = input("What character do you want to check: ")

    assert len(char.strip()) <= 1, "characters can only have a length of 0 or 1"
    assert int(clean) == 0 or int(clean) == 1, "only input a value of 0 or 1"

    print("---------------------------------------------------------------------")
    if char == '':
        check_all_non_mutuals()

    for user in set_of_non_mutuals:
        if user[0] == char.lower().strip():
            list_of_char_names.append(user)
            print(user)
    if len(list_of_char_names) == 0 and char != '':
        print("No users of that starting char")
    print("---------------------------------------------------------------------")


print("Clean or Not clean?")
print("Clean (input: 1) does display all of the non mutuals")
clean = input("Not Clean (input: 0) doesn't display all of the non mutuals: ")
check_all_non_mutuals(int(clean))


"""
Checks the input of the user to see if they want to continue with the program.
Accounts for upper and lowercase Y/N inputs. Once the user inputs a N, the script
ends and clears the terminal.
"""
run = True
while run:
    check_all_non_mutuals_of_starting_char()
    advance = input("Continue?: Y or N: ")
    assert advance in ['N', 'Y', 'y', 'n'], "Only input Y or N"
    if advance.upper() == "N":
        run = False

os.system('cls' if os.name == 'nt' else 'clear')
