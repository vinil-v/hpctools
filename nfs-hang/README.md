# NFS Lock Test Script

This script helps diagnose issues related to file locking on NFS (Network File System). It mimics the behavior of Jetpack to identify potential problems with lock acquisition and release. The script can be used to observe how locks are held and released on a NetApp volume.

## Usage

### 1. Reproduce the Locking Behavior
To demonstrate the problematic behavior on a node that won't converge, run the following command:

```
python3 test.py test .jetpack.lock
```

#### Expected Output (if something holds the lock)
The script should run for 30 seconds and produce the following output:

```
test: trying to get lock on .jetpack.lock
test: could not get lock, waiting 30 more sec...
test: could not get lock, waiting 28 more sec...
...
test: could not get lock, waiting 1 more sec...
test: failed to get lock
```

#### Problematic Output (when the script hangs)
Instead of the expected output, you might see this:

```
test: trying to get lock on .jetpack.lock
```

At this point, the script hangs and does not proceed. This indicates an issue with NFS locking.

---

### 2. Alternative Locking Test
Try running the script with a different lock file that does not exist:

```
python3 test.py test newfile.lock
```

#### Expected Output
The script should acquire the lock immediately and display:

```
test: trying to get lock on .jetpack.lock
test: acquired lock; holding .jetpack.lock for 20 sec...
test: lock released after 20 sec
```

---

### 3. Simulate Multiple Locking Programs
To simulate two programs trying to acquire the same lock, use the following commands:

```
touch newfile.lock
python3 ~/test.py first .jetpack.lock & python3 ~/test.py second .jetpack.lock; wait
```

#### Example Output
```
first: trying to get lock on .jetpack.lock
first: acquired lock; holding .jetpack.lock for 20 sec...
second: trying to get lock on .jetpack.lock
second: could not get lock, waiting 30 more sec...
...
first: lock released after 20 sec
second: acquired lock; holding .jetpack.lock for 20 sec...
second: lock released after 20 sec
```

In this scenario, the first script acquires the lock, holds it for 20 seconds, and then releases it. The second script logs every 2 seconds while waiting, indicating it is actively trying to acquire the lock and not stuck.

---

## Troubleshooting
If your setup behaves differently, such as the script hanging indefinitely when trying to acquire a lock, it may indicate an issue with the NFS configuration or how the volume handles locks.

Feel free to open an issue or submit a pull request if you encounter any problems or have suggestions for improvements.

