import pafy 

url = "https://www.youtube.com/watch?v=g_HN50TLuaI"
video = pafy.new(url) 
print(video.title) 
  
# print rating 
print(video.rating) 
  
# print viewcount 
print(video.viewcount) 
  
# print author 
print(video.author) 
  
# print duration, likes, dislikes & description 
print(video.duration)

# print likes
print(video.likes)

# print dislikes
print(video.dislikes)

streams = video.streams 
for i in streams: 
	print(i) 
	
# get best resolution regardless of format 
best = video.getbest() 

print(best.resolution, best.extension) 

# Download the video 
best.download() 
