# VulnScan 🔒

A Python-based vulnerability scanner that uses Nmap for service and version detection and correlates detected software with publicly disclosed CVEs from the National Vulnerability Database (NVD) REST API.

---

## Features

- Detects open TCP ports
- Identifies running services and versions
- Retrieves relevant CVEs from the NVD API
- Displays results in a Flask web interface
- Generates a JSON report
- Prevents duplicate CVE lookups
- Handles network and API errors gracefully

---

## Technologies Used

- Python
- Flask
- Nmap
- Requests
- HTML
- CSS
- JSON
- NVD REST API

---

## Project Structure

```
VulnScan/
│
├── app.py
├── scanner.py
├── cve_lookup.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/styke.css
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/VulnScan.git
```

### Navigate into the project

```bash
cd VulnScan
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate it

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## Usage

1. Enter an IP address or domain.
2. Click **Scan**.
3. View detected services and related CVEs.
4. Review the generated JSON report.

---

## Example Output

| Port | Product | Version | CVEs |
|------|----------|----------|------|
| 22 | OpenSSH | 9.2 | 3 |
| 80 | Apache httpd | 2.4.7 | 12 |

---

## Skills Demonstrated

- Python Programming
- Network Scanning
- REST API Integration
- JSON Parsing
- Flask Web Development
- Secure Coding Practices
- Error Handling
- Modular Software Design

---

## Future Improvements

- CSV export
- PDF report generation
- Severity filtering
- Dark mode
- Scan history
- SQLite integration
- Docker deployment

---

## Disclaimer

This tool correlates detected software versions with publicly available CVEs from the National Vulnerability Database (NVD). It does **not** verify whether a vulnerability is exploitable on the target system.

---

## Author

**Gagan HS**

LinkedIn: *(your profile)*

GitHub: *(your profile)*
