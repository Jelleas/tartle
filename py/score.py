from objects import read

def score(outputFile, caches, videos):
    next(outputFile)
    for line in outputFile:
        cacheId = int(line.split(" ")[0])
        cache = caches.get(cacheId)
        for vidId in [int(i) for i in line.split(" ")[1:]]:
            video = videos.get(vidId)
            cache.capacity = 0
            cache.addVideo(video)

if __name__ == "__main__":
    with open("../input/me_at_the_zoo.in") as inputFile, open("../output/score.out") as outputFile:
        caches, endpoints, videos, requests = read(inputFile)
        print requests.get(2)
        print caches
        print score(outputFile, caches, videos)
