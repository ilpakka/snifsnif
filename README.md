# Snifsnif

## Legal Disclaimer
**Port scanning and network sniffing may be illegal in some countries or without explicit permission from the target network owner. This tool is intended strictly for educational purposes, security testing, and ethical use.** The developers and maintainers are not responsible for any misuse of this software.

## Features
- Multi-threaded scanning
- Supports both **IPv4** and **IPv6**
- Verbose mode to display closed ports and errors
- Option to save results to a CSV file with a custom filename
- Identifies known services running on open ports

## Installation

```sh
git clone https://github.com/yourusername/snifsnif.git
cd snifsnif
```

Ensure you have Python 3.x installed.

## Run and Examples

```sh
python snifsnif.py <target> <port-range> [options]
```

```sh
python snifsnif.py 192.168.1.1 20-100
```

```sh
python snifsnif.py 192.168.1.1 20-100 -v
```

```sh
python snifsnif.py 192.168.1.1 20-100 --save
```

```sh
python snifsnif.py 192.168.1.1 20-100 --save --filename=my_results.csv
```

```sh
python snifsnif.py 2001:db8::1 20-100 --ipv6
```

## Command-Line Arguments
| Argument | Description |
|----------|-------------|
| `<target>` | Target IP address or hostname |
| `<port-range>` | Port range to scan (e.g., 20-100) |
| `-v, --verbose` | Show closed ports and errors |
| `--ipv6` | Enable IPv6 scanning |
| `--save` | Save results to a CSV file |
| `--filename` | Specify a custom filename (default: Snifsnif_results_TARGET.csv) |
