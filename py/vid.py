
# TODO classname
class Endpoint:
    def __init__(self, list):
        """
        init
        """
        self.latency, self.cachesCount = map(int, list[0].split())
        self.caches = {}
        for i in range(1, self.cachesCount + 1):
            cache, latency = map(int, list[i].split())
            self.caches[cache] = latency
        self.videos = {}

    def addRequests(self, video, requests):
        """
        init requests section
        """
        self.videos[video] = requests

    def __str__(self):
        """
        print
        """
        t = "Latency to Youtube: " + str(self.latency) + "\n"
        t += "Caches: " + str(self.cachesCount) + "\n"
        for entry in self.caches.keys():
            t += "Cache " + str(entry) + ": latency " + str(self.caches[entry]) + "\n"
        return t

class Cache:
    def __init__(self, list):
        print "create cache"
        pass


class Youtube:
    def __init__(self, file):
        # generate Youtube object
        with open(file) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        self.videocnt, self.endp, self.req, self.cachecnt, self.cachesize = map(int, list(content[0].split()))
        self.videos = map(int, content[1].split())
        self.endpoints = []
        self.requests = []

        # generate Endpoint objects
        index = 2
        for amt in range(0, self.endp):
            toCreate = []
            for i in range(index, index + 1 + int(content[index].split()[1])):
                toCreate.append(content[i])
            self.endpoints.append(Endpoint(toCreate))
            index += int(content[index].split()[1]) + 1

        # parse requests
        for amt in range(index, len(content)):
            video, endpoint, requests = map(int, list(content[amt].split()))
            self.endpoints[endpoint].addRequests(video, requests)

        #print self.endpoints[9]


vid = Youtube("../input/me_at_the_zoo.in")