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

### 3. **Working Colab Notebook (.ipynb)**
In the final step, create a **Colab notebook** that demonstrates how to use your script. Here's how you can proceed:

#### Steps to Create and Share the Colab Notebook:
1. Go to [Google Colab](https://colab.research.google.com/).
2. Create a new notebook by selecting **File** -> **New notebook**.
3. Paste the entire Python script (the one you've already written) into separate code cells.
4. Add detailed comments and instructions for each code block to explain what it does.
5. Save the notebook by selecting **File** -> **Save a copy in GitHub** to save it directly into your repository (this step ensures the notebook is included in your GitHub repository).
6. Share the Colab notebook URL as part of your submission.

---

### Final Checklist for Deliverables:
- **GitHub Repository**: A public GitHub repo with your code, README.md, and Colab notebook.
- **README.md**: Detailed instructions for setting up and running the project, including how to authenticate with Google APIs.
- **Colab Notebook**: A working Colab notebook demonstrating the use of your Python script.

Once these steps are completed, you’ll be ready to submit your application. Let me know if you need more help with any of the steps!



