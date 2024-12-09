# Project Setup Guide

## Prerequisites
- Python 3.x
- pip (Python package manager)

## Setup Instructions

### 1. Virtual Environment (Recommended)

#### For Linux/Ubuntu:
```bash
# Create virtual environment
python3 -m venv myenv

# Activate virtual environment
source ./myenv/bin/activate
```

### 2. Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt
```

### 3. Launch Application
```bash
# Run Streamlit application
streamlit run Assignment_better.py
```

### API Key Configuration
To use the Hugging Face API, you need to provide your API key. A dedicated section in the frontend allows you to securely input your Hugging Face API key. Ensure the key is entered correctly to enable functionality.

```

## Accessing the App
- The app will automatically open in your default web browser
- If not, use the URL displayed in the terminal (typically `http://localhost:8501`)

### Troubleshooting
- Ensure all dependencies are installed correctly
- Check Python and Streamlit versions
- Verify virtual environment activation

