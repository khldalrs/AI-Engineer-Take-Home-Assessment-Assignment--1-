# GreenThumb Goods AI Assistant - README

## Overview
This project implements an AI assistant for GreenThumb Goods, a company specializing in gardening and sustainable products. The assistant is designed to handle complex multi-intent customer queries that combine product inquiries with policy questions.

## Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher
- OpenAI API key

### 2. Installation
1. Ensure you have Python installed on your system
2. Install the required packages:
   ```
   pip install openai pandas streamlit
   ```



## Running the Project

The project includes a convenient runner script that provides a menu to access all sections:

```
python run.py
```

Alternatively, you can run each section individually:

### Section 1: Dataset Creation
```
python section1_dataset.py
```
This generates a dataset of 50 complex multi-intent customer queries with appropriate responses.

### Section 2: Streamlit Interface
```
streamlit run section2_streamlit_app.py
```
This launches a web interface where you can interact with the AI assistant using different prompt strategies.

### Section 3: Prompt Engineering
```
python section3_prompt_engineering.py
```
This tests two distinct prompt engineering strategies (zero-shot and few-shot) on challenging queries.

### Section 4: Summary Report
The summary report is available in `section4_summary_report.md`.

### Section 5: Google Analytics Integration
The Google Analytics integration document is available in `section5_google_analytics.md`.

## Project Structure
- `config.py` - Configuration file for API key
- `run.py` - Main runner script with menu interface
- `section1_dataset.py` - Dataset creation script
- `section2_streamlit_app.py` - Streamlit interface
- `section3_prompt_engineering.py` - Prompt engineering implementation
- `section4_summary_report.md` - Summary report and recommendations
- `section5_google_analytics.md` - Google Analytics integration plan
