import objects

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
        connectionList[endpoints.endpoints[i].id][endpoints.endpoints[i].latencies[j].cache.id] = endpoints.endpoints[i].latencies[j].ms
