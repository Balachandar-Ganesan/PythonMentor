class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Aggregation

    def start(self):
        self.engine.start()