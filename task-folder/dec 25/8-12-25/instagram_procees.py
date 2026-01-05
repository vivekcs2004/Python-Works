file_path = "task-folder\\dec 25\\8-12-25\\Instagram_Analytics.csv"

import csv

fr = open(file_path,"r",encoding="utf8")

reader = csv.DictReader(fr)
data = list(reader)

#  Q1: Total number of posts 
total_posts = len(data)
# print("Total posts:", total_posts)


#  Q2: Media type with most posts 
media_list = [row.get("media_type") for row in data]
media_count = {m: media_list.count(m) for m in set(media_list)}
most_common_media = [m for m, c in media_count.items() if c == max(media_count.values())]
# print("Media type with most posts:", most_common_media)


#  Q3: Post with highest engagement_rate 
eng_rates = [float(row["engagement_rate"]) for row in data]
max_eng = max(eng_rates)
top_eng_posts = [row["post_id"] for row in data if float(row["engagement_rate"]) == max_eng]
# print("Post with highest engagement rate:", top_eng_posts)


#  Q4: Average likes per content category 
category_likes = {}

for row in data:
    cat = row["content_category"]
    likes = float(row["likes"])
    category_likes.setdefault(cat, []).append(likes)

avg_likes_per_cat = {cat: sum(values) / len(values) for cat, values in category_likes.items()}
# print("Average likes per category:", avg_likes_per_cat)


#  Q5: Posts where impressions > reach 
impression_higher = [
    row["post_id"]
    for row in data
    if float(row["impressions"]) > float(row["reach"])
]
# print("Posts where impressions > reach:", impression_higher[:20], "...")  # printing first 20 only


#  Q6: Post with longest caption 
max_caption = max(int(row["caption_length"]) for row in data)
longest_caption_posts = [row["post_id"] for row in data if int(row["caption_length"]) == max_caption]
# print("Post(s) with longest caption:", longest_caption_posts)


#  Q7: Top 5 posts by engagement (likes+comments+shares+saves) 
engagement_scores = []

for row in data:
    score = (
        float(row["likes"]) +
        float(row["comments"]) +
        float(row["shares"]) +
        float(row["saves"])
    )
    engagement_scores.append((row["post_id"], score))

top5_engagement = sorted(engagement_scores, key=lambda x: x[1], reverse=True)[:5]
# print("Top 5 posts by engagement:", top5_engagement)


#  Q8: Avg followers gained per media type 
followers_media = {}

for row in data:
    m = row["media_type"]
    gained = float(row["followers_gained"])
    followers_media.setdefault(m, []).append(gained)

avg_followers_per_media = {m: sum(v)/len(v) for m, v in followers_media.items()}
# print("Average followers gained per media type:", avg_followers_per_media)


#  Q9: Posts with zero hashtags 
zero_hashtag_posts = [row["post_id"] for row in data if int(row["hashtags_count"]) == 0]
# print("Posts with 0 hashtags:", zero_hashtag_posts[:20], "...")  # first 20


#  Q10: Highest reachtolike efficiency 
efficiency_scores = []

for row in data:
    likes = float(row["likes"])
    reach = float(row["reach"])
    efficiency = reach / (likes + 1)  # avoid division by zero
    efficiency_scores.append((row["post_id"], efficiency))

best_efficiency_post = max(efficiency_scores, key=lambda x: x[1])
print("Post with highest reach/like efficiency:", best_efficiency_post)



