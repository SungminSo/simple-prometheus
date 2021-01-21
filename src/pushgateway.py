import time
import random

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

if __name__ == '__main__':
    registry = CollectorRegistry()

    duration = Gauge('test_job_duration_seconds', 'Duration of test job in seconds', registry=registry)

    try:
        with duration.time():
            time.sleep(random.uniform(10, 60))

        g = Gauge('last_success_seconds', 'Last time batch job successfully finished', registry=registry)
        g.set_to_current_time()

        g_test = Gauge('test_gauge', 'This is for testing gauge type', registry=registry)
        g_test.set(random.uniform(100, 300))
    finally:
        push_to_gateway('localhost:9090', job='test_batch', registry=registry)
