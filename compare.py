class PQ:
    def __init__(self, dist, id, info):
        self.dist=dist
        self.id=id
        self.info=info
    def __gt__(self, other):
        return self.dist>other.dist
    def __ge__(self, other):
        return self.dist>=other.dist
    def __eq__(self, other):
        return self.dist==other.dist
    def __le__(self, other):
        return self.dist<=other.dist
    def __lt__(self, other):
        return self.dist<other.dist