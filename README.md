# simple-prometheus

## Docker로 띄우기
```
$ docker run -p 9090:9090 prom/prometheus
```

## Local에서 띄우기
1. <a href="https://prometheus.io/download/">prometheus 다운로드</a>
```
$ ./prometheus --config.file=prometheus.yml
```

### Node-exporter
```
$ docker pull prom/node-exporter
$ docker run -p 9100:9100 prom/node-exporter
```

### Pushgateway
```
$ docker pull prom/pushgateway
$ docker run -p 9091:9091 prom/pushgateway
```

## Grafana
```
$ docker pull grafana/grafana
$ docker run -p 3000:3000 grafana/grafana
```