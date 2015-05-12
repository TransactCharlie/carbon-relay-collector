__author__ = 'charlie'

import logging
log = logging.getLogger(__name__)
import yaml
import os
import json

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
DEFAULT_CONF_FILE = "{p}/config/carbon-relay-collector.yaml".format(p=ROOT_DIR)

def get_config(config_file=DEFAULT_CONF_FILE):
    """reads config from file"""
    log.info("Loading config from %s" % config_file)

    try:
        with open(config_file, "r") as cfile:
            cfg = yaml.load(cfile)
            log.debug("--CONFIG--")
            log.debug(json.dumps(cfg, indent=4))

        log.info("Config Loaded")

    except Exception as e:
        log.warn("Couldn't load config %s" % e)
        log.warn("Returning base config")
        cfg = {
            "report_send_interval": 60,
            "listen_pickle_port": 6006,
            "report_graphite_host": "localhost",
            "report_graphite_port": 2003,
            "listen_http_report_port": 8086
        }

    return cfg