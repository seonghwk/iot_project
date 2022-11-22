from pynput import keyboard

class MyException(Exception): pass

def on_press(key):
    try:
        if key.char == 'w':
            print("GO")
        if key.char == 'a':
            print("LEFT")
        if key.char == 's':
            print("BACK")
        if key.char == 'd':
            print("RIGHT")
    except AttributeError:
        pass
    # try:
    #     print('alphanumeric key {0} pressed'.format(wwadddddddasddaswwwwwwwwwwwwww
    #         key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))


def on_release(key):
    try:
        if key.char == 'w' or key.char == 's':
            print("STOP")
        if key.char == 'a' or key.char == 'd':
            print("MIDDLE")
      # print('{0} released'.format(
      #     key))
        if key == keyboard.Key.esc:
          # Stop listener
          raise MyException(key)
    except AttributeError:
        pass


# ...or, in a non-blocking fashion:wwwwwwwad
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

while True:
    try:
        pass
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))

