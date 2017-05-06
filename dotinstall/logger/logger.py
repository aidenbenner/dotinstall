from level import Level

class Logger(object):
    def log(self, level, message):
        print('{}{}{}'.format(level, message, Level.END))

    def error(self, message):
        self.log(Level.ERROR, message)

    def warning(self, message):
        self.log(Level.WARNING, message)

    def success(self, message):
        self.log(Level.SUCCESS, message)

    def info(self, message):
        self.log(Level.INFO, message)

    def header(self, message):
        self.log(Level.HEADER, message)
