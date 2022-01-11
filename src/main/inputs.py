try:
    import tty, sys, termios
    OS = "linux"
except:
    import msvcrt
    OS = "windows"

def build_keyboard():
    if OS == "linux":
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
