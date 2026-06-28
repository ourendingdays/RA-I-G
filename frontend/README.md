# Frontend

This is the frontend application for the ra-i-g project, built with [Streamlit](https://streamlit.io/).

## Overview

The frontend provides an interactive user interface for the ra-i-g application using Streamlit, a fast and easy way to build data applications in Python.

## Installation

1. Install the required dependencies:

If you havent installed dependencies from [requiremetns.txt](../requirements.txt) yet, run:

```bash
pip install streamlit==1.30.0
```

## Testing the Streamlit

To test the Streamlit library and ensure everything is working correctly, run:

```bash
streamlit hello
```

This will run Streamlit's demo application, which showcases various Streamlit features and components.

## Running the Application

To start the Streamlit application, run:

```bash
streamlit run app.py
```

The application will start on `http://localhost:8501` by default.


## Project Structure

- `app.py` - Main Streamlit application entry point
- `pages/` - Additional pages for multi-page applications
- `components/` - Reusable Streamlit components
- `utils/` - Utility functions and helpers