# carbon-relay-collector

A simple python-twisted applcation that listens for pickled objects coming from carbon-relay. Collects simple statistics about the metrics received (just counting the first part of the metric path for now)

## Configuration
YAML config file at `config/carbon-relay-collector.yaml` (TODO - take a command line args and parse them / config file location)

```
# Config file for Carbon Relay Collector

listen_pickle_port: 6006
listen_http_report_port: 8086

report_graphite_host: "localhost"
report_graphite_port: 2003
report_send_interval: 60
```



