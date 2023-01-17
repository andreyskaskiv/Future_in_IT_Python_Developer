from screeninfo import get_monitors

monitor = get_monitors().pop()
WIDTH = monitor.width
HEIGHT = monitor.height
