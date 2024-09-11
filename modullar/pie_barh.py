import pandas as pd 
import matplotlib.pyplot as plt


data = pd.read_csv("videos.csv")

total_views1 = data["Video views"].sum()

data = data.sort_values(by="Video views", ascending=False).head(5)
total_views2 = data["Video views"].sum()


video_names = data["Video names"].to_list()
video_names.append("Digər videolar")

video_views = data["Video views"].to_list()
video_views.append(total_views1 - total_views2)

colors = ["#6439FF","#6C48C5","#2E073F","#FABC3F","#6A9C89","#16423C"]

plt.figure(figsize=(10, 6))
plt.pie(video_views, labels=[name[0:15]+"..." for name in video_names], colors=colors,
        explode=[0,0,0,0,0,0.1], startangle=180, shadow=True)
plt.title("Top 5 video")
plt.tight_layout()
plt.savefig("pie.png")

# plt.figure(figsize=(10, 6))
# plt.barh([name[0:15]+"..." for name in video_names], video_views)
# plt.title("Top 5 video")
# plt.xlabel("Görüntüləmə sayı")
# plt.ylabel("Video adı")
# plt.yticks(rotation=45)
# plt.tight_layout()
# plt.savefig("barh.png")