import objects
import operator
import score

def write(caches, outputFile):
    outputFile.write("{}\n".format(len(caches.caches)))
    for cache in caches:
        string = " ".join([str(video.id) for video in cache.videos])
        outputFile.write("{} {}\n".format(cache.id, string))

with open("../input/kittens.in") as f:
    caches, endpoints, videos, requests = objects.read(f)

# get requests per video per endpoint
endpointsList = [None] * len(endpoints.endpoints)
for i in range(0, len(endpointsList)):
    endpointsList[i] = {}
for req in requests.requests:
    endpointsList[req.endpoint.id][req.video.id] = req.weight

# get for each endpoint which cahces are avail and the ms improved
connectionList = [None] * len(endpoints.endpoints)
for i in range(0, len(endpoints.endpoints)):
    connectionList[i] = {}
    for j in range(0, len(endpoints.endpoints[i].latencies)):
        improvement = endpoints.endpoints[i].dataLatency.ms - endpoints.endpoints[i].latencies[j].ms
        connectionList[endpoints.endpoints[i].id][endpoints.endpoints[i].latencies[j].cache.id] = improvement

# compute video preference for each endpoint
endpointsSorted = [None] * len(endpoints.endpoints)
for i in range(0, len(connectionList)):
    endpointsSorted[i] = []
    for key, value in sorted(endpointsList[i].iteritems(), key=lambda (k,v): (v,k)):
        endpointsSorted[i].append(key)
    endpointsSorted[i].reverse()

#
for endp in range(0, len(endpointsSorted)):
    #print endp
    #print connectionList[endp]
    #print endpointsSorted[endp]
    #print "---"
    videosPushed = 0

    #print connectionList[endp].keys()
    for cache in connectionList[endp].keys():
        try:
            #print "Trying to add video ", endpointsSorted[endp][videosPushed], " to cache ", cache
            caches.caches[cache].addVideo(videos.videos[endpointsSorted[endp][videosPushed]])
            videosPushed += 1
        except:
            #print "Cache full"
            continue

# klaar
with open("../output/maartenben3.txt", "w+") as f:
    write(caches, f)

with open("../output/maartenben3.txt") as f:
    print score.score(f, caches, endpoints, videos, requests)


