__author__ = 'charlie'

from protocols import CollectorProtocol
from twisted.internet.protocol import Factory
from twisted.web import server, resource
from twisted.internet import reactor
from globals import STATS
from collections import Counter
import json

class CollectorFactory(Factory):
    protocol = CollectorProtocol

    def startFactory(self):
        print "Starting Factory"

    def stopFactory(self):
        print "Stopping Factory"
        self.fp.close()


class CollectorResults(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        top100 = Counter(STATS).most_common(100)
        print top100
        mgen = (m for m in top100)
        output = [dict([m]) for m in mgen]
        return json.dumps(output)


if __name__=='__main__':

    # collector endpoint
    reactor.listenTCP(8889, CollectorFactory())

    #results endpoint
    site = server.Site(CollectorResults())
    reactor.listenTCP(8080, site)
    reactor.run()