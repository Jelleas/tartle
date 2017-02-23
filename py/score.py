from objects import read

def score(outputFile, caches, endpoints, videos, requests):
    next(outputFile)
    for line in outputFile:
        cacheId = int(line.split(" ")[0])
        cache = caches.get(cacheId)
        for vidId in [int(i) for i in line.split(" ")[1:]]:
            video = videos.get(vidId)
            cache.addVideo(video)

    score = 0
    nRequests = 0

    for request in requests:
        endpoint = request.endpoint
        video = request.video
        nRequests += request.weight

        minMs = endpoint.dataLatency.ms
        for latency in endpoint.latencies:
            if video in latency.cache and latency.ms < minMs:
                minMs = latency.ms


        score += (endpoint.dataLatency.ms - minMs) * 1000 * request.weight

    return score / nRequests

if __name__ == "__main__":
    with open("../input/bullshit.in") as inputFile, open("../output/score.out") as outputFile:
        caches, endpoints, videos, requests = read(inputFile)
        print requests.get(2)
        print caches
        print score(outputFile, caches, endpoints, videos, requests)
