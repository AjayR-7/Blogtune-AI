# Blogtune AI

## Description
Blogtune AI is a web application that allows users to generate blog content based on a title they provide. It uses Flask for the backend and LangChain to interact with the OpenAI model.

## Features
- Generate blog content based on user-provided titles.
- User-friendly interface with Tailwind CSS styling.
- Responsive design for mobile and desktop users.

## Installation Steps

### Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### Install Python Dependencies
Make sure you have Python and pip installed. Then, install Flask and LangChain:
```bash
pip install Flask langchain
```

### Install Node.js Dependencies
Make sure you have Node.js and npm installed. Then, install Tailwind CSS:
```bash
npm install
```

### Run Tailwind CSS
To compile the Tailwind CSS, run:
```bash
npm run tw
```

### Run the Flask Application
Start the Flask server:
```bash
python main.py
```

### Access the Application
Open your web browser and go to `http://localhost:5500`.

## Usage
1. Enter the title of the blog in the provided text area.
2. Click the "Submit" button to generate the blog content.
3. The generated content will be displayed below the input area.
