
class Latency(object):
    def __init__(self, end, cache, ms):
        self.endpoint = end
        self.cache = cache
        self.ms = ms

    def __repr__(self):
        return "LATENCY: {}, {}, {}".format(self.endpoint.id, self.cache, self.ms)

class Requests(object):
    def __init__(self):
        self.requests = []

    def add(self, request):
        self.requests.append(request)

    def get(self, id):
        return self.requests[id]

    def __repr__(self):
        return "REQUESTS: {}".format(self.requests)

class Videos(object):
    def __init__(self):
        self.vidoes = {}

    def add(self, video):
        self.vidoes[video.id] = video

    def get(self, id):
        return self.vidoes[id]

    def __repr__(self):
        return "VIDEOS: {}".format(self.vidoes)

class Endpoints(object):
    def __init__(self):
        self.endpoints = {}

    def add(self, endpoint):
        self.endpoints[endpoint.id] = endpoint

    def get(self, id):
        return self.endpoints[id]

    def __repr__(self):
        return "ENDPOINTS: {}".format(self.endpoints)

class Caches(object):
    def __init__(self):
        self.caches = {}

    def get(self, id):
        if id not in self.caches:
            self.caches[id] = Cache(id)
        return self.caches[id]

    def __repr__(self):
        return "CACHES: {}".format(self.caches)

class Cache(object):
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return "CACHE: {}".format(self.id)


class Request(object):
    def __init__(self, video, endpoint, weight):
        self.video = video
        self.endpoint = endpoint
        self.weight = weight

    def __repr__(self):
        return "REQUEST: {} {} weight:{}".format(self.video, self.endpoint, self.weight)

class Video(object):
    def __init__(self, id, size):
        self.id = id
        self.size = size

    def __repr__(self):
        return "VIDEO: id:{} size:{}".format(self.id, self.size)

class Endpoint(object):
    def __init__(self, id, datacenterLatency):
        self.id = id
        self.dataLatency = Latency(self, datacenter, datacenterLatency)
        self.latencies = []

    def addLatency(self, latency):
        self.latencies.append(latency)

    def __repr__(self):
        return "ENDPOINT: id:{}".format(self.id)

datacenter = Cache(-1)


def read(inputFile):
    caches = Caches()
    endpoints = Endpoints()
    videos = Videos()
    requests = Requests()

    endpointN = 0
    cacheCount = 0
    endpoint = None
    endpointFlag = True

    next(inputFile)

    videoLine = next(inputFile)
    for i, vidSize in enumerate([int(size) for size in videoLine.split(" ")]):
        videos.add(Video(i, vidSize))

    for line in inputFile:
        if cacheCount == 0 and len(line.split(" ")) == 2:
            if endpoint:
                endpoints.add(endpoint)
            endpoint = Endpoint(endpointN, int(line.split(" ")[0]))
            cacheCount = int(line.split(" ")[1])
            endpointN += 1
        elif cacheCount > 0:
            latency = Latency(endpoint, caches.get(int(line.split(" ")[0])), int(line.split(" ")[1]))
            endpoint.addLatency(latency)
            cacheCount -= 1

        if len(line.split(" ")) == 3:
            if endpointFlag:
                endpointFlag = False
                endpoints.add(endpoint)

            videoId, endpointId, weight = [int(i) for i in line.split(" ")]
            video = videos.get(videoId)
            endpoint = endpoints.get(endpointId)
            request = Request(video, endpoint, weight)
            requests.add(request)

    return caches, endpoints, videos, requests