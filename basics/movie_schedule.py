current_movies = {"The Grinch":"11:00AM",
                  "Rudolph":"1:00PM",
                  "Frostly the Snowman":"3:00PM",
                  "Christmas Vacation":"5:00PM"}

print("We're showing the following movies:")
for movie in current_movies:
    print(movie)

your_movie = str(input("Enter which movie you would like to watch:\n"))
is_available = current_movies.get(your_movie)

if is_available:
    print(is_available)
else:
    print("The entered movie doesn't exist")
