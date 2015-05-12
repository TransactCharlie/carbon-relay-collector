__author__ = 'charlie'

import logging
log = logging.getLogger(__name__)
from stats import STATS, topX_json_format
from twisted.web import resource
import json


class MetricsCollectorResults(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        request.setHeader("Content-Type", "application/json; charset=utf-8")
        log.info("http report request received")
        top100 = topX_json_format(STATS, 100)
        return json.dumps(top100, indent=4)
