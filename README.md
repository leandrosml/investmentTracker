# Investment Tracker

Investment Tracker is an investment and portfolio management platform built with Django, React, MySQL, and Docker. It uses external APIs to fetch information and currently implements mock transactions as a virtual trading game. This project is part of a diploma thesis by Leandros Malliaroudakis and is licensed under the MIT license.

## Features
- Portfolio management
- Mock trading with virtual transactions
- Data fetching from external APIs
- Dockerized deployment for ease of setup

## Installation

### Prerequisites
- Docker
- Docker Compose
- mkcert (for local SSL certificates)

### Setup Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/leandrosml/investmentTracker.git
    cd investmentTracker
    ```

2. Create local SSL certificates with privileged rights and PowerShell:
    ```bash
    ./create_certs.ps1
    ```

3. Build and start the Docker containers:
    ```bash
    docker-compose up --build
    ```

### Accessing the Application
- **Backend:** https://localhost:8081
- **Frontend:** https://localhost:3000
- **phpMyAdmin:** http://localhost:8085

## Usage

1. Ensure Docker and Docker Compose are installed on your system.
2. Follow the setup instructions above to get the application running.
3. Access the frontend, backend, and phpMyAdmin using the URLs provided.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please reach out to Leandros Malliaroudakis.

---

