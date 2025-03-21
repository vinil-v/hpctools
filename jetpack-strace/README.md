# Jetpack Strace Script

This script helps capture system call traces from the Jetpack daemon (`jetpackd`). It is useful for diagnosing issues related to Jetpack convergence and analyzing the system calls made during the process.

## Prerequisites
1. Ensure you have uploaded the `jetpack-strace` script to a shared location for easy access.
2. Obtain the IP address of the node where you want to capture the trace.

## Usage

### Step 1: Access the Node
Log in as the `cyclecloud` user once you have the node's IP address.

### Step 2: Switch to Root
Switch to the root user to manage the Jetpack daemon:

```
sudo su -
```

### Step 3: Stop the Jetpack Daemon
Before the Jetpack daemon (`jetpackd`) starts converging, stop it using the following command:

```
systemctl stop jetpackd.service
```

### Step 4: Start Jetpack Daemon and Run Strace
Immediately after starting the Jetpack daemon, run the `jetpack-strace` script to capture system calls:

```
systemctl start jetpackd.service
./jetpack-strace
```

## Output
The script will start outputting system calls as shown below:

```
20533<jetpack> rt_sigprocmask(SIG_BLOCK, ~[RTMIN RT_1 RT_2], [], 8) = 0
20533<jetpack> rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
20533<jetpack> rt_sigprocmask(SIG_BLOCK, ~[RTMIN RT_1 RT_2], [], 8) = 0
20533<jetpack> rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
20533<jetpack> munmap(0x7eff232af000, 32768) = 0
20533<jetpack> munmap(0x7eff232c5000, 32768) = 0
20533<jetpack> munmap(0x7eff22c74000, 32768) = 0
20533<jetpack> exit_group(0) = ?
20533<jetpack> +++ exited with 0 +++
No child processes found for PID 20521; waiting for converge to start...
```

## Troubleshooting
If you encounter issues or unexpected behavior, please share the trace log for further analysis. Feel free to reach out for assistance or open an issue on GitHub.

