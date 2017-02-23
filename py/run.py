import objects
import operator

with open("../input/me_at_the_zoo.in") as f:
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

print endpointsSorted



