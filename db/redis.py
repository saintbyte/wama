import os

import redis

redis_db = redis.from_url(os.environ.get("REDIS_URL"))
