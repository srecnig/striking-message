import dramatiq

@dramatiq.actor(queue_name='messages')
def shout_something(something):
    print(f"I am shouting something: {something.upper()}")
