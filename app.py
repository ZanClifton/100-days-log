from database import add_entry, create_table, get_entries
from art import logo

menu = """What do you want to do today?

1) Add a new entry
2) View all entries
3) Exit

Enter a number: """

welcome = "Welcome to your 100 Days Log!"

entry_display_format = f"""
"""


def prompt_new_entry():
    """Prompts new entry and passes details to add_entry function"""
    day = input("Which 100 Days of Code day is this? ")
    activity = input("What have you learned today? ")
    thoughts = input("What are your thoughts about that? ")
    date = input("Enter the date: ")
    add_entry(entry_activity=activity,
              entry_thoughts=thoughts, entry_date=date, entry_day=day)


def view_entries(entries):
    """Prints entries from array received as argument"""
    for entry in entries:
        print(
            f"""
    Day: {entry["day"]}/100
    Date: {entry["date"]}
    Activity: {entry["activity"]}
    Thoughts: {entry["thoughts"]}

    +++++++++++++++++
        """)


print(logo)
print(welcome)
create_table()

while (user_choice := int(input(menu))) != 3:
    # deal with user input
    if user_choice == 1:
        prompt_new_entry()

    elif user_choice == 2:
        view_entries(entries=get_entries())

    else:
        print("Invalid option! Try again.")
