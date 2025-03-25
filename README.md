# Google Docs API - Meeting Notes Formatter

## Description
This project demonstrates how to use the Google Docs API to automate the generation and formatting of meeting notes. It fetches meeting data, processes it, and creates a well-formatted Google Doc with various elements like headings, bullet points, checkboxes, and styled text.

## Setup Instructions
1. **Clone the repository**:
git clone https://github.com/StephinAntonio7/google-docs-api-practice-meeting-notes.git

2. **Install dependencies**:
Use the following command to install all required Python packages:
pip install -r requirements.txt

3. **Google Cloud API Credentials**:
You will need to authenticate using Google Cloud credentials to interact with the Google Docs API. Follow these steps:
- Go to the [Google Cloud Console](https://console.cloud.google.com/).
- Enable the **Google Docs API**.
- Create a **service account** and download the credentials file.
- Set up the environment variable to use your credentials file by running:
  ```
  export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
  ```

## Required Dependencies
- `google-auth`
- `google-api-python-client`
- `google-auth-httplib2`
- `google-auth-oauthlib`
- `google-colab` (for using Google Colab)

You can install them via:
pip install google-auth google-api-python-client google-auth-httplib2 google-auth-oauthlib google-colab

## How to Run in Colab
To run the notebook in Google Colab:
1. Upload the Python script and the credentials file to your Google Drive.
2. Open a new Google Colab notebook and run the following commands:

   ```python
   from google.colab import drive
   drive.mount('/content/drive')

   # Follow the rest of the steps in the Colab notebook to authenticate and run the code

Running the Script:
Once the authentication is complete, follow the instructions in the Colab notebook to run the script and create your formatted Google Doc. Make sure to check the resulting Google Doc for your meeting notes formatted with headings, bullet points, checkboxes, and styled text.
