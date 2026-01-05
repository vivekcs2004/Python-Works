# all_movies_path = "task-folder/27-11-25/movies.csv"

# fr_all_movies = open(all_movies_path, "r")

# for index, line in enumerate(fr_all_movies):
#     if index == 5:
#         break
#     line = line.rstrip("\n")
#     print(line)


# 2 Count Lines

# Write a program to count how many movie records are present in movies.csv (excluding the header).


# total_number_of_movies = -1   # start at -1 to cancel header

# for line in fr_all_movies:
#     total_number_of_movies += 1

# print(f"Total number of movies = {total_number_of_movies}")


# 3 Print Column Names
# Write a program to read the header row and print all column names.

# for line in fr_all_movies:
#     line = line.rstrip("\n")
#     header_row = line.split(",")

#     for column in header_row:
#         print(column)
#     break

# 4 Filter by Year
# Accept a year from the user and display all movie titles released in that year.

# year = int(input("Enter year: "))
# movie_year = []

# for index, line in enumerate(fr_all_movies):
#     if index == 0:
#         continue
#     line = line.rstrip("\n")
#     row = line.split(",")
#     movie_year.append({row[0] : int(row[7])})

# for movie in movie_year:
#     for m, y in movie.items():
#         if y == year:
#             print(f"{m} : {y}")

# 5 Find Highest Rated Movie
# Read the CSV and print the movie with the highest rating.

# movie_audience_rating = {}

# print("Top rated movies: ", end="")

# for index, line in enumerate(fr_all_movies):
#     if index == 0:          
#         continue
#     line = line.rstrip("\n")
#     row = line.split(",")
#     movie_audience_rating[row[0]] = float(row[3])   

# max_rating = max(movie_audience_rating.values())

# for m, r in movie_audience_rating.items():
#     if r == max_rating:
#         print(m, end=" ")

# 6 List Movies by Genre
# Accept a genre from the user (e.g., Action, Drama) and print all matching movies
# genre = input("Enter genre : ")

# movie_genre = {}

# for index, line in enumerate(fr_all_movies):
#     if index == 0:
#         continue
#     line = line.rstrip("\n")
#     row = line.split(",")
#     movie_genre[row[0]] = row[1].strip()   # strip fixes the issue

# for m, g in movie_genre.items():
#     if g == genre:
#         print(m)


# Write to a New File
# Create a new CSV file named top_rated.csv and write all movies with rating greater than 8.0.

# top_rated_movies_path = "task-folder/27-11-25/top_rated_movies.csv"
# fw_top_rated_movies = open(top_rated_movies_path, "w")

# movie_audience_rating = {}

# for index, line in enumerate(fr_all_movies):
#     if index == 0:
#         continue
#     line = line.rstrip("\n")
#     row = line.split(",")
#     movie_audience_rating[row[0]] = float(row[3])

# for m, r in movie_audience_rating.items():
#     if r > 80:
#         fw_top_rated_movies.write(m + "\n")

# fw_top_rated_movies.close()


# 8 Count Movies by Genre
# Read the file, calculate how many movies are in each genre, and write the output into genre_count.txt.

# genre_count_path = "task-folder/27-11-25/genre_count.txt"
# fw_genre_count = open(genre_count_path, "w")

# genre_count = {}

# fr_all_movies = open("movies.csv", "r")   # <-- REQUIRED
# for index, line in enumerate(fr_all_movies):
#     if index == 0:
#         continue
#     line = line.rstrip("\n")
#     row = line.split(",")

#     if row[1] in genre_count:
#         genre_count[row[1]] += 1
#     else:
#         genre_count[row[1]] = 1

# for g, c in genre_count.items():
#     fw_genre_count.write(f"{g} : {c}\n")


# 9 Sort by Rating
# Read all movies and write them into sorted_movies.csv sorted in descending order of rating.

# sorted_movie_rating_path = "task-folder/27-11-25/sorted_movie_rating.csv"
# fw_sorted_movie_rating = open(sorted_movie_rating_path, "w")

# movie_audience_rating = {}

# fr_all_movies = open("task-folder/27-11-25/movies.csv", "r")

# for index, line in enumerate(fr_all_movies):
#     if index == 0:
#         continue
#     line = line.rstrip("\n")
#     row = line.split(",")
#     movie_audience_rating[row[0]] = float(row[3])

# sorted_movie_rating = sorted(
#     movie_audience_rating,
#     key=lambda k: movie_audience_rating[k],
#     reverse=True
# )

# for movie in sorted_movie_rating:
#     rating = movie_audience_rating[movie]
#     fw_sorted_movie_rating.write(f"{movie} : {rating}\n")



# 10 Find Movies with Missing Data
# Read the CSV and print all rows where any field is empty.

# fr_all_movies = open("task-folder/27-11-25/movies.csv", "r")

# for index, line in enumerate(fr_all_movies):
#     if index == 0:
#         continue                   

#     line = line.rstrip("\n")
#     row = line.split(",")

#     if "" in row:                    
#         print(line)


# 11 Search by Movie Name
# Ask the user for a keyword and print all movie titles containing that keyword (case-insensitive).
# title_keyword = input("Enter keyword to search movies: ").casefold()

# fr_all_movies = open("task-folder/27-11-25/movies.csv", "r")

# movies = []

# for index, line in enumerate(fr_all_movies):
#     if index == 0:
#         continue
#     line = line.rstrip("\n")
#     row = line.split(",")
#     movies.append(row[0])

# for title in movies:
#     if title_keyword in title.casefold():
#         print(title)





    
