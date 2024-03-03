# notification-api

## About

The `notification-api` is a specialized service designed to manage the sending of notifications through various channels, with initial support for Telegram. It offers a unified interface for dispatching messages, simplifying the integration of notification functionality into applications.

## Features

- Currently supports sending notifications via Telegram.
- Flexible DTOs for different message types, including generic and trade-related messages.
- Easy to extend to other notification platforms in the future.

## Getting Started

### Prerequisites

- Python 3.10
- Poetry for dependency management

### Installation and Setup

1. Clone the repository:
```
git clone https://github.com/felipesilvaibi/notification-api.git
```

2. Navigate to the project directory:
```
cd notification-api
```

3. Install dependencies using Poetry:
```
poetry install
```

### Configuration

Configure your Telegram bot token and other necessary details in a suitable configuration file or environment variables, as per your project's best practices.

### Running the Service

Using Poetry, you can run the service directly. Ensure you have configured the application correctly, including the environment variables for the Telegram API.
```
poetry run uvicorn src.main.config.app:app --host 0.0.0.0 --port 8080
```

## Usage

### Sending a Generic Message
To send a generic message through Telegram, an API client must construct a JSON payload specifying:

`type`: The type of notification, in this case, "TELEGRAM".
`recipient_id`: The identifier of the recipient on Telegram (e.g., a user or chat ID).
`message_type`: The type of message to be sent, which in this example is "GENERIC".
`message`: An object containing the content of the message, which is the text of the message to be sent.

#### Example Payload for a Generic Message
```json
{
  "type": "TELEGRAM",
  "recipient_id": "123456789",
  "message_type": "GENERIC",
  "message": {
    "content": "This is a generic message."
  }
}
```

### Sending a Trade Message
For notifications related to trade operations, the payload should include additional information about the trade action and relevant indicators. This includes:

`type`: The same as above, "TELEGRAM".
`recipient_id`: The recipient's ID on Telegram.
`message_type`: In this case, "TRADE".
`message`: A more complex object that includes `trade_action` (the trade action like "BUY", "SELL", or "HOLD") and indicators (an object containing relevant `indicators` for the trade decision, such as weekly RSI, monthly RSI, and MVRV Z-Score).

#### Example Payload for a Trade Message
```json
{
  "type": "TELEGRAM",
  "recipient_id": "987654321",
  "message_type": "TRADE",
  "message": {
    "trade_action": "BUY",
    "indicators": {
      "weekly_rsi": 70,
      "monthly_rsi": 60,
      "mvrv_z_score": 2
    }
  }
}
```

## Docker Deployment
Your provided Dockerfile is set up for a multi-stage build, optimizing dependencies installation and minimizing the final image size. Make sure to build and run your Docker container according to your operational environment requirements.

## CI/CD Configuration
CI/CD Configuration
You've outlined workflows for deployment, Terraform apply, plan, and destroy. Ensure these workflows are configured in your .github/workflows directory, adjusting for your specific project and operational needs.

## Google Cloud Integration

For the current project, we are utilizing Google Cloud to manage the infrastructure. To maximize the project's potential, the following configurations are necessary:

1. **Create a Google Cloud Account**: Begin by signing up for a Google Cloud account if you haven't already.

2. **Activate the Free Tier**: Take advantage of Google Cloud's free tier to access many services without incurring costs.

3. **Enable Necessary APIs**: Activate the following APIs in your Google Cloud project:
   - **Identity and Access Management (IAM) API**: Essential for managing access and identities.
   - **Cloud Resource Manager API**: Required for managing resources.
   - **Secret Manager API**: For storing and accessing secrets safely.
   - **Cloud Run API** (if necessary): If you're deploying applications with Cloud Run.

4. **Service Account for GitHub Actions**: Create a service account to be used by GitHub Actions with the following permissions:
   - Firebase Remote Config Administrator
   - App Engine Service Admin
   - App Engine Admin
   - Cloud Functions Admin
   - Cloud Run Admin
   - Cloud Scheduler Admin
   - Compute Storage Admin
   - Secret Manager Admin
   - Artifact Registry Repository Admin
   - Storage Admin
   - Pub/Sub Admin
   - App Engine Flexible Environment Service Agent
   - App Engine Creator
   - Cloud Build Editor
   - App Engine Deployer
   - Service Account User
   - Service Account Admin

5. **GitHub Actions Secrets**: Access the service account in GitHub Actions, generate a `GCP_SA_KEY` in JSON format, and add it to the GitHub repo's actions secrets. Also, add the `GH_TOKEN` (GitHub token) to the repo's secrets.

6. **Cloud Storage Bucket**: Create a bucket in Cloud Storage using the repository name and branch as the naming convention (e.g., `notification-api-main`).

7. **Cloud Build Repository Connection**: Create and authenticate a connection with your repository in Cloud Build.

8. **Secret Manager Configuration**: In Google Cloud's Secret Manager, configure a secret named `notification-api_main_telegram_bot_token`. This will be used to set the `TELEGRAM_BOT_TOKEN` environment variable.

**Note**: To obtain the Telegram bot token, you must first create a bot through Telegram's BotFather. For a step-by-step guide, you can refer to [this tutorial on YouTube](https://www.youtube.com/watch?v=UQrcOj63S2o).

This setup ensures your project is fully integrated with Google Cloud, leveraging its powerful infrastructure and services for optimal performance and scalability.
