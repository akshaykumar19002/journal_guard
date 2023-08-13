# JournalGuard - A Secure Journalling Web Application

JournalGuard is a journalling website that allows users to create, view, edit, and delete journal entries securely. With added encryption key management, your entries are not only stored but also encrypted for additional security.

## Features
1. **User Registration and Authentication**: Securely register and log in to your personal journal space.
2. **Create a New Journal Entry**: Craft new memories and save them for posterity.
3. **Viewing Journal Entries**: Browse through your journal entries in a user-friendly interface.
4. **Editing Existing Journal Entries**: Modify your memories as and when you need.
5. **Delete Journal Entries**: Choose to delete entries that no longer resonate.
6. **Encryption Key Management**: Manage your encryption keys ensuring that your entries remain private and secure.

## Local Setup

### Pre-requisites

- Python (3.8 or higher)
- pip
- Virtual environment (recommended)

### Steps

1. Clone the repository:

```
git clone https://github.com/your_username/JournalGuard.git
cd JournalGuard
```

2. (Recommended) Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate  # For Windows, use: .\venv\Scripts\activate
```

3. Install required packages:

```
pip install -r requirements.txt
```

4. Migrate and run the application:

```
python manage.py migrate
```

To run the application in HTTP mode:

```
python manage.py runserver
```

To run the application in HTTPS mode:

```
python manage.py runserver_plus 443 --cert-file certs/cert.pem --key-file certs/key.pem
```

Now, navigate to the appropriate URL (`http://127.0.0.1:8000/` for HTTP or `https://127.0.0.1:443/` for HTTPS) in your browser.

## Docker Setup

### Pre-requisites

- Docker
- Docker Compose (if using docker-compose.yml)

### Steps

1. Build the Docker image:

```
docker build -t journalguard:latest .
```

2. Run the container:

```
docker run -d -p 8000:8000 journalguard:latest
```

Now, navigate to `http://localhost:8000/` in your browser.

## HTTPS Setup for journalguard.com

To access the website using `https://journalguard.com`:

1. Edit your hosts file:

- On Linux/macOS: `/etc/hosts`
- On Windows: `C:\Windows\System32\drivers\etc\hosts`

Add the following line:

```
127.0.0.1 journalguard.com
```

2. Make sure you have a valid SSL certificate setup for the domain in your Django settings. If testing locally, you can use tools like [mkcert](https://github.com/FiloSottile/mkcert) to create local trusted certificates.

3. Navigate to `https://journalguard.com` in your browser.
