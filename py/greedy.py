from objects import *
import score

def greedy(caches, endpoints, videos, requests):
    for i, request in enumerate(requests):
        if i % 1000 == 0:
            print "{} / {}".format(i, len(requests.requests))
        for cache in (latency.cache for latency in request.endpoint.latencies):
            try:
                cache.addVideo(request.video)
                break
            except ValueError:
                cache.removeVideo(request.video)
    """
    print caches
    fullCaches = [cache for cache in caches if cache.overCapicity()]
    print fullCaches

    while fullCaches:
        cache = fullCaches[0]
        video = max(cache.videos, key = lambda v : v.size)
        cache.removeVideo(video)

        if not cache.overCapicity():
            fullCaches.remove(cache)
    """
    return caches

def write(caches, outputFile):
    nonEmptyCaches = [cache for cache in caches if cache.videos]
    outputFile.write("{}\n".format(len(nonEmptyCaches)))
    for cache in nonEmptyCaches:
        string = " ".join([str(video.id) for video in cache.videos])
        outputFile.write("{} {}\n".format(cache.id, string))

if __name__ == "__main__":
    for name in ["kittens", "me_at_the_zoo", "trending_today", "videos_worth_spreading"]:
        inputFilename = "../input/{}.in".format(name)
        outputFilename = "../output/{}.out".format(name)

        with open(inputFilename) as inputFile, open(outputFilename, "w+") as outputFile:
            caches, endpoints, videos, requests = read(inputFile)
            caches = greedy(caches, endpoints, videos, requests)
            write(caches, outputFile)

        with open(outputFilename) as outputFile:
            print score.score(outputFile, caches, endpoints, videos, requests)