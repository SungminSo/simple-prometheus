from prometheus_client import delete_from_gateway


if __name__ == '__main__':
    delete_from_gateway('localhost:9091', job='test_batch')
