import time
import sys

def rgb_cycle_text(text, delay=0.1):
    for i in range(1000):
        r = (i * 5) % 256
        g = (i * 3) % 256
        b = (i * 7) % 256
        sys.stdout.write(f"\033[38;2;{r};{g};{b}m{text}\r")
        sys.stdout.flush()
        time.sleep(delay)

try:
    rgb_cycle_text("🌈 Abdul Mateen 🌈")
except KeyboardInterrupt:
    print("\033[0m\nDone.")