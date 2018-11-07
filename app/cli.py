import subprocess

import boto3
import fire

redis = boto3.client('elasticache')


class ElasticCache:
    """ElasticCache utils"""

    db_map = {
        'Jarvis Celery': 0,
        'Jarvis Game history': 1,
        'Jarvis User Cache': 2,
        'Jarvis API Stats': 3,
        'Jarvis Notification Records': 4,
        'Jarvis Streaming Records': 5,
        'Available Streaming server list': 6,
        'Pym Celery': 7,
        'Pym Cache': 8,
        'Pepper Shared Redis': 9,
        'Pepper Celery': 10,
        'Pepper Cache': 11,
        'Arsenal Celery': 12,
        'Arsenal Cache': 13,
        'Vision/Thor Cache': 14,
        'Vision Celery': 15,
    }

    def db(self, name):
        """Search Redis DB number by service name"""
        match = filter(lambda x: name.lower() in x.lower(),
                       [k for k in self.db_map])
        return [f'{m}: {self.db_map[m]}' for m in match]

    def _get_cluster_id(self, stage, service):
        if stage == 'staging':
            return 'api-staging-cache'
        if stage == 'integ':
            return 'soocii-integration'
        if stage != 'prod':
            raise ValueError('Support stage: integ, staging, prod')

        # stage is prod
        if service == 'jarvis':
            return 'jarvis-prod-cache-001'

        if service == 'thor':
            return 'thor-prod-cache-001'

        return 'api-prod-cache'

    def connect(self, stage, service, db=None):
        """Connect to ElastiCache by redis-cli"""

        cluster_id = self._get_cluster_id(stage, service)

        print('Getting ElastiCache node info...')
        resp = redis.describe_cache_clusters(
            CacheClusterId=cluster_id, ShowCacheNodeInfo=True)

        assert len(resp['CacheClusters']) == 1
        cluster = resp['CacheClusters'][0]
        node = cluster['CacheNodes'][0]
        endpoint = node['Endpoint']
        host, port = endpoint['Address'], endpoint['Port']

        print(f'Connecting to {host}:{port}...')
        cmd = ['redis-cli', '-h', host, '-p', str(port)]
        if db:
            cmd += ['-n', str(db)]
            print(f'Selected DB {db}')
        return subprocess.run(cmd)


class Pipeline:
    # https://github.com/google/python-fire/blob/master/docs/guide.md#grouping-commands
    def __init__(self):
        self.redis = ElasticCache()


def main():
    fire.Fire(Pipeline)


if __name__ == '__main__':
    main()
