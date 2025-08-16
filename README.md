# LiveKit AI Voice Assistant

A simple voice assistant built with [LiveKit Agents](https://github.com/livekit/agents) and OpenAI to provide weather information.

## Prerequisites

- Python 3.12+
- LiveKit and OpenAI API credentials.

## Quick Start

1.  **Clone, Setup Venv, and Install Dependencies**
    ```bash
    git clone https://github.com/your-username/voiceAgent.git
    cd voiceAgent
    python -m venv .venv && source .venv/bin/activate
    pip install -e .
    ```

2.  **Configure Credentials**
    Copy `sample.env` to `.env` and add your API keys.
    ```bash
    cp sample.env .env
    ```

3.  **Run the Agent**
    ```bash
    python main.py dev
    ```
