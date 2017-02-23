from objects import read

def score(outputFile):
    next(outputFile)

def skip(file, n):
    for i in range(n):
        next(file)

if __name__ == "__main__":
    with open("../input/me_at_the_zoo.in") as inputFile, open("../output/score.out") as outputFile:
        caches, endpoints, videos, requests = read(inputFile)
        print requests.get(2)
        print score(outputFile)
