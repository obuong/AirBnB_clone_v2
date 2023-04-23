from datetime import datetime
from models.state import State
state = State(name='California', created_at=datetime.now())
from models import storage

storage.new(state)
storage.save()

