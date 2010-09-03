"""
Check file timestamps and execute specified command if newer exist::

    $ python updater.py make html

"""

import os, sys, time

def loop(command, check_interval, update_duration):
    checked_at = time.time()
    while True:
        filelist = []
        for dirname, dirs, files in os.walk('.'):
            for f in files:
                filelist.append(os.path.join(dirname, f))
        lasts = reversed(sorted(os.stat(f).st_mtime for f in filelist))
        newest = lasts.next()
        if newest > checked_at:
            checked_at = time.time()
            print time.strftime('\n== run at %Y/%m/%d %H:%M:%S')
            print '== %s\n' % command
            status = os.system(command)
            print time.strftime('\n== complete at %Y/%m/%d %H:%M:%S'), '(status: %d, %.1f secs)' % (status, time.time() - checked_at)
        else:
            checked_at = time.time()
        time.sleep(check_interval)

def main():
    command = ' '.join(sys.argv[1:])
    loop(command, 2, 10)


if __name__ == '__main__':
    main()
