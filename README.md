## Rain Sensor MQTT Listener
This project is a Rain Sensor MQTT Listener that listens to MQTT messages from a rain sensor, processes the data, and sends notifications via Telegram. The application is containerized using Docker and orchestrated with Docker Compose for easy deployment.

### Features
**MQTT Listener**: Subscribes to a specific MQTT topic and processes incoming messages.
**Telegram Notifications**: Sends alerts to a Telegram chat when rain is detected.
**Environment Configuration**: Uses .env files for secure and flexible configuration.
**Containerized Deployment**: Runs seamlessly in Docker containers with Docker Compose.
### Requirements
**Docker**: Ensure Docker is installed on your system.
**Docker Compose**: Required for orchestrating the containers.
### Environment Variables
The application uses a .env file 

### How to Run
1. Clone the Repository
2. Create the .env File
Create a .env file in the root directory and populate it with the required environment variables following .env.exemple template.

3. Build and Run with Docker Compose
```bash
docker-compose up --build
```
This will build the Docker image and start the application.

Docker Compose Configuration
The docker-compose.yml file defines the services:

### How It Works
The application connects to the MQTT broker and subscribes to the specified topic.
When a message is received, the handle_message function processes the payload.
If rain is detected, a notification is sent to the configured Telegram chat using the TelegramBot class.
### Logs
Logs are displayed in the console and provide information about:

- MQTT connection status
- Received messages
- Telegram notification status
### Extending the Project
- Cloud deployment
- Add support for other notification services (e.g., email, SMS).
- Integrate with a database to store received messages.
- Add more advanced message filtering or processing.
### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contributing
Feel free to open issues or submit pull requests to improve the project.