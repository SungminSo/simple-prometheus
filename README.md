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