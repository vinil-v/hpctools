import time
import fcntl
import sys

name = sys.argv[1]
lockfile = sys.argv[2]

with open(lockfile, 'w') as f:

    hold_locks_for = 20
    time_to_wait = 30
    time_waited = 0
    start_time = time.time()
    lock_acquired = None
    print(f"{name}: trying to get lock on {lockfile}")
    while time_waited < time_to_wait:
        try:
            fcntl.lockf(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            lock_acquired = time.time()
            print(f"{name}: acquired lock; holding {lockfile} for {hold_locks_for} sec...")
            time.sleep(hold_locks_for)
            break
        except IOError as e:
            # Errno 11 is "Resource temporarily unavailable" i.e. the file is locked already
            if e.errno == 11:
                time_remaining = time_to_wait - time_waited
                print(f"{name}: could not get lock, waiting {time_remaining:0.0f} more sec...")
                sleep = 2
                time.sleep(sleep)
                time_waited = time.time() - start_time
                continue
            else:
                raise

    if lock_acquired:
        held_for = time.time() - lock_acquired
        print(f"{name}: lock released after {held_for:0.0f} sec")
    else:
        print(f"{name}: failed to get lock")
