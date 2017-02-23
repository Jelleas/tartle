from objects import *

with open("../input/bullshit.in") as inputFile, open("../output/score.out") as outputFile:
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