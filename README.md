# Briefly PDF 📚

## Overview

The Briefly PDF application is a web-based tool for processing and summarizing PDF documents. Users can upload PDF files along with a text prompt. The application extracts text from the uploaded PDFs, processes the prompt and PDF text using a generative AI model, and provides a summarized response. The summarized response can be viewed, copied, and listened to via text-to-speech. Users can also view the full response in a separate page.

## Features

- **Upload PDFs:** Users can upload multiple PDF files.
- **Enter Prompt:** Users can enter a prompt to guide the summarization.
- **Generate Summary:** The application processes the prompt and extracted text from PDFs to generate a summarized response.
- **View Response:** The summarized response is displayed with options to copy the text or listen to it via text-to-speech.
- **Full Response Page:** Users can view the full response on a separate page.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/shahram8708/Briefly-PD
   cd Briefly PDF
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Environment Variables**

   Make sure to set the `API_KEY` environment variable for the Generative AI API:

   ```bash
   export API_KEY=<your-api-key>
   ```

   On Windows, you can use:

   ```bash
   set API_KEY=<your-api-key>
   ```

## Usage

1. **Run the Flask Application**

   ```bash
   python app.py
   ```

2. **Open Your Browser**

   Navigate to `http://localhost:5000` to access the application.

## Application Structure

- **`app.py`**: The main Flask application file.
- **`templates/`**:
  - **`index.html`**: The main page for uploading PDFs and entering prompts.
  - **`fullresponse.html`**: The page for viewing the full response.
- **`uploads/`**: Directory for storing uploaded PDF files.

## Endpoints

- **`/`**: Main page where users can upload PDFs and enter prompts.
- **`/upload`**: Endpoint for handling file uploads and prompt submission.
- **`/fullresponse`**: Page for displaying the full response.
- **`/save/<filename>`**: Endpoint for serving saved files.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. Make sure to follow the coding standards and include tests with your changes.
