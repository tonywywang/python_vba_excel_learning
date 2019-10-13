import threading
def hello():
     print("hello, world")

class RepeatingTimer(threading.Timer): 
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)
t = RepeatingTimer(10.0, hello)
t.start()