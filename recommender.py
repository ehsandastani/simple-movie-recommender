import json
from pathlib import Path
import time

'''
References: https://emojidb.org/error-emojis?utm_source=user_search
            https://www.geeksforgeeks.org/python/read-json-file-using-python/
            https://www.geeksforgeeks.org/python/pathlib-module-in-python/
            https://www.w3schools.com/python/ref_string_join.asp
'''


# I've defined default users as a global variable if users.json doesn't exist
DEFAULT_USERS = {
        "Ali": ["Inception", "Matrix"],
        "Sara": ["Titanic", "Inception"]
    }

# **************************************************************************
def load_users(file_path="users.json"):
    path = Path(file_path)  # creating 'path' instance
    if path.exists():
        with path.open("r") as json_file:
            return json.load(json_file)
        
    return DEFAULT_USERS.copy()


# **************************************************************************
def get_or_create_user(name):

    # loading the users file data
    users = load_users()

    # checking user existence
    if name not in users.keys():
        while True:
            try:
                count = int(input("\n➡️  How many movies do you want to enter (2 or 3)? "))
                if count in (2, 3):
                    break
                print("\n⚠️  Please enter only 2 or 3.\n")

            except ValueError:
                print("\n❗That was not a number! Try again...\n")
                continue
        
        movies = [] # user's favorite movies
        for i in range(count):
            movies.append(input(f"Enter your number {i + 1} favorite movie: ").strip())
        
        # adding into users' JSON data (dictionary)
        users[name] = movies

        # save updated users into users.json
        with open("users.json", "w") as json_file:
            json.dump(users, json_file, indent=4)

        print(f"\n✅ Dear '{name}'! Welcome to the best recomender system! 😎\n")
        time.sleep(3)

    else:
        print(f"\n👋 Welcome back, {name}! Your favorite movies are: {', '.join(users[name])}\n")
        time.sleep(3)


# **************************************************************************
def similarity(user1_movies, user2_movies) -> set:
    user1_movies_set = {m.lower() for m in user1_movies}
    user2_movies_set = {m.lower() for m in user2_movies}
    return user1_movies_set.intersection(user2_movies_set)


# **************************************************************************
def find_best_match(name, users):
    best_score = -1 # It is because of comparison in here: shared_movies_count > best_score => 0 > 0!. 
    best_match = None # person name!
    best_shared = set()

    for other_name, other_movies in users.items():
        if other_name == name:
            continue

        else:
            shared_movies = similarity(users[name], other_movies)
            shared_movies_count = len(shared_movies)

            if shared_movies_count > best_score:
                best_score = shared_movies_count
                best_match = other_name
                best_shared = shared_movies.copy()

            elif (shared_movies_count == best_score) and (best_score > 0):
                if other_name < best_match:
                    best_match = other_name
                    best_shared = shared_movies.copy()

    if best_score > 0:
        print(f"\n🎬 The best match for you, {name}, is {best_match} "
            f"with {best_score} shared movie(s): {', '.join(best_shared)}\n"
        )
        return best_match, best_shared
    
    else:
        print(f"\n⚠️  Sorry {name}, no shared movies were found with other users.\n")
        return None

# **************************************************************************
def recommend_for(name, users):
    best_match = find_best_match(name, users)

    if best_match is None:
        print("¯\_(ツ)_/¯ No recommendation available yet.\n")
        return
    
    match_name = best_match[0]
    match_movies = best_match[1] # => set 2
    all_match_name_movies = {m.lower() for m in users[match_name]} # => set 1
    to_recommend = all_match_name_movies.difference(match_movies) # => set 1 - set 2

    if to_recommend:
        print(f"✨ Our recommendation for you is to watch: {', '.join(to_recommend)}\n")
    else:
        print("¯\_(ツ)_/¯ No recommendation available yet.\n")
        


name = input("\nEnter your name: ").strip()
get_or_create_user(name)
recommend_for(name, load_users())