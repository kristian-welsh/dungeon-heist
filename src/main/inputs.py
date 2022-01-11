from src.main.os import OS
try:
    import tty, sys, termios
    system = OS.LINUX
except:
    import msvcrt
    system = OS.WINDOWS

def build_keyboard():
    if system is OS.LINUX:
        return LinuxKeyboard()
    else:
        return WindowsKeyboard()

class LinuxKeyboard():
    def getkey(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class WindowsKeyboard():
    def getkey(self):
        return msvcrt.getch().decode("utf-8")
