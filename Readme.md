# Light API and Live data stream

Very light fast api on top of sql light database, and live stream via SSE (server side events)

## Installation

1. Clone the repository.
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the FastAPI server using Uvicorn, run the following command:
```
uvicorn main:app --reload
```