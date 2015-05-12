__author__ = 'charlie'

import logging
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO )
log = logging.getLogger(__name__)

from config import get_config
from twisted.web import server
from twisted.internet import reactor, task
from collect_metrics import MetricsCollectorFactory
from http_endpoint import MetricsCollectorResults
from graphite_report import graphite_looping_task


if __name__=='__main__':

    cfg = get_config()

    # Pickle listen endpoint
    listen_pickle = cfg["listen_pickle_port"]
    log.info("Listening for pickles on port %i" % listen_pickle)
    reactor.listenTCP(listen_pickle, MetricsCollectorFactory())

    # HTTP Debug endpoint
    listen_http = cfg["listen_http_report_port"]
    log.info("Debug report port at %i" % listen_http)
    reactor.listenTCP(listen_http, server.Site(MetricsCollectorResults()))

    # Graphite Looping Task
    graphite_host = cfg["report_graphite_host"]
    graphite_port = cfg["report_graphite_port"]
    looping_time = cfg["report_send_interval"]
    log.info("Scheduling report task %s:%i every %i seconds" % (graphite_host, graphite_port, looping_time))
    graphite_task = task.LoopingCall(graphite_looping_task, graphite_host, graphite_port)
    graphite_task.start(looping_time, now=True)

    # Start the reactor loop
    log.info("Starting Reactor")
    reactor.run()
    log.info("Reactor Stopped?!?")