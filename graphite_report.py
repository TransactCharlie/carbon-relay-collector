__author__ = 'charlie'

from logging import getLogger
log = getLogger(__name__)

from stats import STATS, topX_graphite_format
from twisted.internet.protocol import Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from twisted.internet import reactor

class GraphiteReportSender(Protocol):
    def sendMessage(self, msg):
        log.debug(msg)
        for m in msg:
            self.transport.write("%s\n" % m)


def send_to_graphite(p, stats, x):
    """Sends the message (assuming we have stats!)"""
    if stats:
        log.info("sending report to graphite....")
        p.sendMessage(topX_graphite_format(stats, x))


def graphite_looping_task(graphite_host, graphite_port):
    point = TCP4ClientEndpoint(reactor, graphite_host, graphite_port)
    d = connectProtocol(point, GraphiteReportSender())
    d.addCallback(send_to_graphite, STATS, 100)