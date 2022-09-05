import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

# Save data from user clipboard into json
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

# Load data from json into user clipboard
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

# Clears all data
def clear_data(filepath):
    with open(filepath, "w"):
        pass

# Delete the specified key/value pair
def delete_data(filepath, key):
    with open(filepath, "r") as f:
        data = json.load(f)
    
    if key in data:
        del data[key]
        with open(filepath, "w") as k:
            json.dump(data, k)
        print("Key/Value pair successfully deleted.")
    else:
        print("No such key found.")

# Main
# CLI Argument Count Handler
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    # Save
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")
    # Load
    elif command == "load":
        key = input("Enter the key you wish to retrieve: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist")
    # List
    elif command == "list":
        print(data)
    # Clear
    elif command == "clear":
        confirmation = input("Please confirm: y/n")
        if confirmation == "y":
            clear_data(SAVED_DATA)
            print("Data cleared!")
        elif confirmation == "n":
            print("Clipboard clear aborted.")
        else:
            print("Unknown command. Process aborted.")
    # Del
    elif command == "del":
        key = input("Enter the key you wish to delete: ")
        delete_data(SAVED_DATA, key)
else:
    print("Please print exactly one command")