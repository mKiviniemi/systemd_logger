import signal
import time
from datetime import datetime


class SignalHandler:
    exit = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        self.exit = True


if __name__ == '__main__':
    '''Log every second to a file, when the service receives a signal, exit gracefully and log the exit event'''
    signal = SignalHandler()

    path = "/opt/logger/logfile.txt"

    while not signal.exit:
        with open(path, "a") as file:
            file.write(f"Service was running at {datetime.now()}\n")
        time.sleep(1)

    with open(path, "a") as file:
        file.write(f"Service exited at {datetime.now()}\n")
