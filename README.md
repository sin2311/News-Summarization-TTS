News Summarization & TTS
This project provides a News Summarization, Sentiment Analysis, and Text-to-Speech (TTS) application using free tools. The app scrapes news articles about a company, analyzes the sentiment of the articles, summarizes them, and converts the summary into Hindi speech.
Features:
News Scraping: Fetches top news articles using Bing News RSS and processes them.

Sentiment Analysis: Analyzes sentiment (positive, negative, or neutral) using Hugging Face's free transformer models.

Text-to-Speech (TTS): Converts the sentiment summary into speech using Google's free gTTS library.

Web Interface: Users can interact with the app through a Gradio interface.

Project Repository:
GitHub: News-Summarization-TTS

Hugging Face Spaces: Deployed App

Requirements
The following libraries are required for running this project:

requests (for making HTTP requests)

beautifulsoup4 (for parsing HTML/XML content)

newspaper3k (for article scraping)

transformers (for sentiment analysis using Hugging Face models)

torch (required by transformers)

gradio (for the web interface)

nltk (for natural language processing tasks)

gtts (for text-to-speech conversion)

fastapi (for API creation)

uvicorn (for serving the API)

Installation and Setup
Step 1: Clone the Repository
Clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/sin2311/News-Summarization-TTS.git
cd News-Summarization-TTS
Step 2: Set Up a Virtual Environment
If you don’t have a virtual environment set up, create one by running:

bash
Copy
Edit
python -m venv venv
Activate the virtual environment:

Windows:

bash
Copy
Edit
venv\Scripts\activate

Step 3: Install the Requirements
Install all the dependencies listed in the requirements.txt file:

bash
Copy
Edit
pip install -r requirements.txt
Running the Project Locally
Step 4: Run the FastAPI Backend
The project includes an API that scrapes news articles, performs sentiment analysis, and generates TTS. You can run the FastAPI server with Uvicorn:

bash
Copy
Edit
uvicorn api:app --reload
The API will be accessible at http://127.0.0.1:8000.

Step 5: Run the Web Interface
To run the Gradio web interface, use the following command:

bash
Copy
Edit
python app.py
This will start a Gradio interface at http://127.0.0.1:7860, where you can input a company name and get the sentiment analysis along with the Hindi TTS.

Deploying to Hugging Face Spaces
Step 6: Create a Hugging Face Spaces Account
Go to Hugging Face Spaces and create an account if you don’t have one.

After logging in, create a new Space.

Choose the Gradio template for your space.

Push the repository to your Hugging Face Space by following the instructions in your newly created space.

Step 7: Deploy the App
Once the repository is pushed to Hugging Face, the app should automatically deploy.

The entry point for the app is app.py.

The dependencies in the requirements.txt file will be automatically installed during the deployment process.

You can access the deployed application through the following link:

Deployed App

Usage
Once the app is deployed:

Go to the deployed app link.

Enter the name of a company in the input field.

The app will fetch the latest news articles about the company, perform sentiment analysis on them, and provide a summary of the sentiment.

You can listen to the summary in Hindi using the text-to-speech functionality.

License
This project is licensed under the MIT License - see the LICENSE file for details.



