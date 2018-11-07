# soocii-cli

Soocii CLI for Soocii's backend developers.

## For CLI User

```console
$ pip install soocii-cli
Collecting soocii-cli
...

$ soocii
Type:        Pipeline
String form: <cli.Pipeline object at 0x10cffa588>

Usage:       soocii
             soocii redis

$ soocii redis db pepper
Pepper Shared Redis: 9
Pepper Celery: 10
Pepper Cache: 11
```

## For CLI Developer

### Setup

`$ pip install -e .[dev]`

### Distribute

`$ python -m setup upload`