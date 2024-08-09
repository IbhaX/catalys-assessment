  The server will start on `http://localhost:5000`.

  ## API Endpoints

  - `/`: Home endpoint
  - `/logs`: View application logs
  - `/health`: Health check endpoint
  - `/fetch-data`: Fetch raw product data
  - `/get-processed-data`: Get processed product data

  ## Project Structure

  - `app/`: Main application package
    - `__init__.py`: Application factory and route registration
    - `config.py`: Configuration settings
    - `models.py`: Pydantic models for data validation
    - `services.py`: Business logic and data processing
    - `logging_setup.py`: Logging configuration
  - `run.py`: Script to run the application
  - `requirements.txt`: List of Python dependencies

  ## Dependencies

  - Flask
  - Flask-RESTful
  - Pydantic
  - Requests
  - Python-dotenv

  ## Setup and Running the Server

  1. Clone the repository:
   
```bash
    git clone https://github.com/IbhaX/catalys-assessment.git
    cd catalys-assessment
```
   

  2. Create a virtual environment:
   
   ```bash
   python -m venv venv
   ```
   

  3. Activate the virtual environment:
   - On Windows:
     
     ```bash
     venv\Scripts\activate
     ```
     
   - On macOS and Linux:
     
     ```bash
     source venv/bin/activate
     ```
     

  4. Install the dependencies:
   
   ```bash
    pip install -r requirements.txt
   ```

  5. Set up environment variables:
   - Create a `.env` file in the project root directory
   - Add necessary environment variables (e.g., `API_KEY=c18753ee-4361-4fa7-90af-e236aec0cd99`)
        - API_KEY is the API key for the product data API. It is same as the pantry id

  6. Run the server:
   ```bash
    python run.py
   ```
## Run with Docker:
   - Build the Docker image:
     ```bash
     docker build -t catalys-assessment .
     ```
   - Run the Docker container:
     ```bash
     docker run -p 5000:5000 catalys-assessment
     ```


  The server will start on `http://localhost:5000`.
