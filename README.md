# Text-to-SQL Application

This project is a **Text-to-SQL Application** that utilizes Google Gemini to convert natural language queries into SQL commands, retrieving data from a SQLite database. It is built using Python and Streamlit, providing a user-friendly interface for interacting with the student database.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Example Queries](#example-queries)
- [Database Structure](#database-structure)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Natural Language Processing**: Converts English questions into SQL queries.
- **Database Interaction**: Uses SQLite to store and retrieve student data.
- **User-Friendly Interface**: Built with Streamlit for an interactive experience.
- **Complex Query Handling**: Efficiently processes a variety of SQL queries.

## Getting Started

### Prerequisites

Make sure you have the following installed:
- Python 3.x
- Streamlit
- SQLite3
- Google Generative AI (Gemini) API Key

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/text-to-sql-app.git
   cd text-to-sql-app

2. Create a virtual environment:

    python -m venv venv
    Activate the virtual environment:

    On Windows:

    venv\Scripts\activate

    On macOS/Linux:

    source venv/bin/activate

3. Install required packages:

    Create a requirements.txt file with the following content:


    streamlit
    google-generativeai
    python-dotenv
    Then, run:

    pip install -r requirements.txt

4. Set up your environment variables:

    Create a .env file in the project root directory and add your Google API key:

    GOOGLE_API_KEY=your_google_api_key
    
5. Run the application:

streamlit run app.py
Open your browser: Go to http://localhost:8501 to access the application.


## Database Structure
The SQLite database student.db contains a table named STUDENT with the following columns:

NAME: Name of the student (VARCHAR)
CLASS: Class the student is enrolled in (VARCHAR)
SECTION: Section of the class (VARCHAR)
MARKS: Marks obtained by the student (INTEGER)