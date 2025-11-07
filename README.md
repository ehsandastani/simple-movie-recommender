# 🎬 Simple Movie Recommender (CLI)

This is a very simple command-line movie recommender written in Python.  
It stores users and their favorite movies in a JSON file (`users.json`) and recommends movies to a user based on the most similar existing user.

## 📁 Project Structure
```bash
simple-movie-recommender/
├── recommender.py # main script (CLI)
├── users.json # users and their favorite movies (created/updated at runtime)
└── README.md
```

## 🧠 How it works
1. The program asks for your name.
2. If you already exist in `users.json`, it loads your favorite movies.
3. If you are a new user, it asks you to enter 2 or 3 favorite movies and saves them.
4. Then it finds the user with the **most shared movies** with you.
5. Finally, it recommends the movies that the matched user likes but you haven't watched yet.


## 🧪 Recommendation Logic
- Users are stored as:  
  ```json
  {
    "Ali": ["Inception", "Matrix"],
    "Sara": ["Titanic", "Inception"]
  }
  ```

* Similarity is computed by set intersection of movie titles (case-insensitive).
* If multiple users have the same similarity score, the one with lexicographically smaller name is chosen.
 
## ▶️ Run
```bash
python recommender.py
```

Then follow the prompts in the terminal.


## 🗄 Data Persistence
* If users.json exists → it loads it.
* If it does not exist → it uses default users defined in the code and will create the file after first new user is added.

## 🛠 Requirements
* Python 3.8+
* No external libraries (only json, pathlib, time from stdlib)

