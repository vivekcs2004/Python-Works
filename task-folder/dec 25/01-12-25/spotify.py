import csv

file_path = "task-folder/dec 25/01-12-25/spotify_data clean.csv"

fr = open(file_path, "r", encoding="utf-8")
reader = csv.DictReader(fr)
data = list(reader)

# Q1 First 5 track names  (UPDATED)
# for t in data[:5]:
#     print(t["track_name"])

# # Q2 Total tracks
# print("Total tracks =", len(data))

# # Q3 Unique artist names
# unique_artists = list({t["artist_name"] for t in data})
# print(unique_artists)

# # Q4 Count explicit songs
# explicit_count = len([t for t in data if t["explicit"] == "TRUE"])
# print(explicit_count)

# # Q5 Tracks with popularity > 50
# popular_tracks = [t["track_name"] for t in data if int(t["track_popularity"]) > 50]
# print(popular_tracks)

# # Q6 Most popular track
# top_track = max(data, key=lambda x: int(x["track_popularity"]))
# print(top_track["track_name"], top_track["track_popularity"])

# # Q7 Average popularity
# avg_pop = sum(int(t["track_popularity"]) for t in data) / len(data)
# print(avg_pop)

# # Q8 Count tracks per album
# album_count = {}
# for t in data:
#     album = t["album_name"]
#     album_count[album] = album_count.get(album, 0) + 1
# print(album_count)

# # Q9 Tracks by artist name
# artist = input("Enter artist name: ")
# artist_tracks = [t["track_name"] for t in data if artist.lower() in t["artist_name"].lower()]
# print(artist_tracks)

# # Q10 Longest duration track
longest = max(data, key=lambda x: float(x["track_duration_min"]))
print(longest["track_name"], longest["track_duration_min"])
