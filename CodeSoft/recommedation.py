# USER-BASED RECOMMENDATION SYSTEM

# Combination of marathi and hindi movies Dataset 
user_data = {
    "A": ["Dangal", "PK", "3 Idiots"],
    "B": ["PK", "Lagaan"],
    "C": ["Dangal", "Bahubali"],
    "D": ["3 Idiots", "Chhichhore"],
    "E": ["Sairat", "Natsamrat", "Timepass"],
    "F": ["Sairat", "Duniyadari"],
}

# Collect ALL movies name
all_movies = set()
for movies in user_data.values():
    all_movies.update(movies)

print("Enter movie names (comma separated):")
user_input = input("> ")

movie_list = [m.strip() for m in user_input.split(",")]

valid_movies = []
invalid_movies = []

# Check each movie
for movie in movie_list:
    if movie in all_movies:
        valid_movies.append(movie)
    else:
        invalid_movies.append(movie)

# ---------- OUTPUT ----------
print("\nVALID Movies:")
if valid_movies:
    for m in valid_movies:
        print("Yes", m)
else:
    print("None")

print("\nINVALID Movies:")
if invalid_movies:
    for m in invalid_movies:
        print("No", m)
else:
    print("None")
