from .LogLevel import LogLevel

class Logger:
    def __init__(self, log_level: LogLevel):
        self.log_level = log_level

    def set_log_level(self, log_level: LogLevel):
        self.log_level = log_level

    def log_debug(self, message: str):
        if self.log_level == LogLevel.DEBUG:
            print(f"{self.log_level}: {message}")

    def log_info(self, message: str):
        if self.log_level == LogLevel.INFO:
            print(f"{self.log_level}: {message}")
            


