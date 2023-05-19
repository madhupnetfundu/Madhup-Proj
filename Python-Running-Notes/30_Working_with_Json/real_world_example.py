# For your introductory example, you’ll use JSONPlaceholder (https://jsonplaceholder.typicode.com/), a great source of fake JSON data for practice purposes.
# You’ll need to make an API request to the JSONPlaceholder service, so just use the requests package to do the heavy lifting. Add these imports at the top of your file:
import json
import requests

# Go ahead and make a request to the JSONPlaceholder API for the /todos endpoint. If you’re unfamiliar with requests, there’s actually a 
# handy json() method that will do all of the work for you, but you can practice using the json library to deserialize the text attribute 
# of the response object. It should look something like this:

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# All right, time for some action. You can see the structure of the data by visiting the endpoint in a browser, but here’s a sample TODO (https://jsonplaceholder.typicode.com/todos):
# {
# "userId": 1,
# "id": 1,
# "title": "delectus aut autem",
# "completed": false
# }


# There are multiple users, each with a unique userId, and each task has a Boolean completed property. Can you determine which users have completed the most tasks?
# Map of userId to number of complete TODOs for that user
todos_by_user = {}

# Increment complete TODOs count for each user.
for todo in todos:
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1

# Create a sorted list of (userId, num_complete) pairs.
top_users = sorted(todos_by_user.items(),
                   key=lambda x: x[1], reverse=True)

# Get the maximum number of complete TODOs.
max_complete = top_users[0][1]

# Create a list of all users who have completed
# the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

# you can now manipulate the JSON data as a normal Python object!

# >>> s = "s" if len(users) > 1 else ""
# >>> print(f"user{s} {max_users} completed {max_complete} TODOs")
# users 5 and 10 completed 12 TODOs

# That’s cool and all, but you’re here to learn about JSON. For your final task, you’ll create a JSON file that contains the completed TODOs for each of the users who completed the maximum number of TODOs.

# All you need to do is filter todos and write the resulting list to a file. For the sake of originality, you can call the output file filtered_data_file.json. There are many ways you could go about this, but here’s one:


# Define a function to filter out completed TODOs
# of users with max completed TODOS.
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count


# Write filtered TODOs to file.
with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)

# Run the script again and check out filtered_data_file.json to verify everything worked.
