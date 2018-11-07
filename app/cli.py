import fire

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
        match = filter(lambda x: name.lower() in x.lower(), [k for k in self.db_map])
        return [f'{m}: {self.db_map[m]}' for m in match]


class Pipeline:
    # https://github.com/google/python-fire/blob/master/docs/guide.md#grouping-commands
    def __init__(self):
        self.redis = ElasticCache()

def main():
    fire.Fire(Pipeline)

if __name__ == '__main__':
    main()
