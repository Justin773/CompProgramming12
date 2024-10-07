import sys, os
import KEY, CONTROLS

if os.name == "posix":
    import tty, termios
    POSIX = True
    WINDOWS = False
    fd = 1
    old_settings = None
    print("posix")
else:
    import msvcrt
    WINDOWS = True
    POSIX = False

render_buffer = ""

def init():
    global render_buffer

    # Posix systems  - i.e mac/linux
    if POSIX:
        global fd, old_settings
        fd = sys.stdin.fileno()
        print(sys.stdin.fileno())
        old_settings =  termios.tcgetattr(fd)

    render_buffer = ""

def clearRenderBuffer():
    global render_buffer
    render_buffer = ""

def render(command):
    global render_buffer
    render_buffer += command

def renderCopy():
    global render_buffer
    sys.stdout.write(render_buffer)
    sys.stdout.flush()
    clearRenderBuffer()

def moveCursor(direction: str, amount=1):
    amount = str(amount)
    render("\033["+amount+direction)

def screenClear():
    render("\033[2J")

class KeyboardInput:
    def __init__(self):
        self.pressed = -1

        if POSIX:
            tty.setraw(fd)

        # Control codes for POSIX/WINDOWS
        # UP DOWN RIGHT LEFT
            CONTROL_CODES = tuple(range(65,69))
        else:
            CONTROL_CODES = (72, 80, 77, 75)
        self.CONTROL_MAP = dict(zip(CONTROL_CODES, (CONTROLS.UP,
                                                    CONTROLS.DOWN,
                                                    CONTROLS.RIGHT,
                                                    CONTROLS.LEFT)))

    def _scan_in_control_codes(self, char):
        if char in self.CONTROL_MAP:
            return self.CONTROL_MAP[char]
        raise ValueError(f'Invalid control code: {char}')
        
    def keyIn(self):
        if POSIX:
            # Reads one chracter from input stream 
            char = ord(sys.stdin.read(1))
        else:
            # Gets keyboard input as UNICODE character
            # ord() converts to ascii
            key = msvcrt.getwch()
            char = ord(key)

        render(str(char))
        # ASCII a - ~
        if 32 <= char <= 126:
            self.pressed = char
            return

        elif char in {10, 13}:
            render("\033[1;5H CONTROL")
            self.pressed = KEY.ENTER
            return

        if POSIX:
            if char == 3: # CTRL-C
                self.pressed = KEY.QUIT
                return
            elif char == 27:
                next1, next2 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
                if next1 == 91:
                    self.pressed = self._scan_in_control_codes(next2)
                    render("\033[1;5H CONTROL"+ str(next2))
        # WINDOWS
        else:
            if char == 0x00 or char == 0xE0:
                next_ = ord(msvcrt.getwch())
                render("\033[1;5H CONTROL")
                self.pressed = self._scan_in_control_codes(next_)
                return
            elif char == 27: #ESC
                render("\033[2;5H ESCAPE")
                self.pressed = KEY.ESC
                return

        self.pressed = -1

if __name__ == "__main__":
    keyboard = KeyboardInput()

    screenClear()
    render("\033[;H")
    for i in range(10000000):
        keyboard.keyIn()
        if keyboard.pressed == KEY.QUIT:
            break
        elif keyboard.pressed == KEY.ESC:
             render("\033[5HClear")

        render("\033[100;H")
        renderCopy()