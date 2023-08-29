"""
_summary_
https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python
https://pypi.org/project/screeninfo/

:return: _description_
:rtype: _type_
"""


from screeninfo import get_monitors


def get_size_primary_monitor():
    """
    Function to get the size os primary monitor.
    To be used within tkinter
    """
    for monitor in get_monitors():
        print(monitor)
        if monitor.is_primary:
            return monitor.height, monitor.width


if __name__ == '__main__':
    print('Módulo Size Monitor\n')
    screen_height, screen_width = get_size_primary_monitor()
    print(screen_height)
    print(screen_width)
