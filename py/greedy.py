from objects import *
import score

def greedy(fileName):
    with open(fileName) as inputFile:
        caches, endpoints, videos, requests = read(inputFile)

        for request in requests:
            for cache in [latency.cache for latency in request.endpoint.latencies]:
                try:
                    cache.addVideo(request.video)
                except ValueError:
                    pass

        print caches
        fullCaches = [cache for cache in caches if cache.overCapicity()]
        print fullCaches

        while fullCaches:
            cache = fullCaches[0]
            video = max(cache.videos, key = lambda v : v.size)
            cache.removeVideo(video)

            if not cache.overCapicity():
                fullCaches.remove(cache)

    return caches

def write(caches, outputFile):
    outputFile.write("{}\n".format(len(caches.caches)))
    for cache in caches:
        string = " ".join([str(video.id) for video in cache.videos])
        outputFile.write("{} {}\n".format(cache.id, string))

if __name__ == "__main__":
    for name in ["me_at_the_zoo", "kittens", "trending_today", "videos_worth_spreading"]:
        inputFilename = "../input/{}.in".format(name)
        outputFilename = "../output/{}.out".format(name)

        caches = greedy(inputFilename)
        with open(outputFilename, "w+") as outputFile:
            write(caches, outputFile)


        with open(inputFilename) as inputFile, open(outputFilename) as outputFile:
            print score.score(outputFile, *read(inputFile))