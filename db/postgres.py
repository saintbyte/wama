import os

import databases

db = databases.Database(os.environ.get("DATABASE_URL"))
