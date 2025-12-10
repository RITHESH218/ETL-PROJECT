# ETL-PROJECT

A Python-based Extract, Transform, and Load (ETL) pipeline for processing NASA data using Supabase as the data storage backend.

## Overview

This project implements an ETL workflow to extract data from NASA APIs, transform it into a structured format, and load it into a Supabase database. The pipeline is designed to be modular and scalable, with separate scripts for each stage of the ETL process.

## Project Structure

```
ETL-PROJECT/
├── SCRIPTS/
│   ├── extract_nasa.py      # Extract data from NASA APIs
│   ├── transform_nasa.py    # Transform and process the extracted data
│   ├── load_nasa.py         # Load processed data into Supabase
├── DATA/                  # Directory for storing data files
├── .github/workflows/     # GitHub Actions workflow configurations
├── .gitignore             # Git ignore rules
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Features

- **Extract**: Fetch data from NASA APIs
- **Transform**: Process and structure the data according to business requirements
- **Load**: Store data in Supabase database
- **Environment Management**: Secure handling of sensitive credentials using environment variables
- **Automated Workflows**: GitHub Actions integration for automated ETL execution

## Technologies Used

- **Language**: Python 3
- **Database**: Supabase (PostgreSQL)
- **Data Processing**: Pandas
- **HTTP Requests**: Requests
- **Environment Management**: python-dotenv
- **CI/CD**: GitHub Actions

## Dependencies

The project requires the following Python packages:

```
requests
pandas
supabase
python-dotenv
```

All dependencies are listed in `requirements.txt`.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- A Supabase account and project

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/RITHESH218/ETL-PROJECT.git
   cd ETL-PROJECT
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   - Create a `.env` file in the project root
   - Add your Supabase credentials:
     ```
     SUPABASE_URL=your_supabase_project_url
     SUPABASE_KEY=your_supabase_api_key
     NASA_API_KEY=your_nasa_api_key
     ```

## Usage

### Running the ETL Pipeline

Execute the scripts in the following order:

1. **Extract Data**:
   ```bash
   python SCRIPTS/extract_nasa.py
   ```

2. **Transform Data**:
   ```bash
   python SCRIPTS/transform_nasa.py
   ```

3. **Load Data to Database**:
   ```bash
   python SCRIPTS/load_nasa.py
   ```

Alternatively, you can run the complete pipeline using the GitHub Actions workflow.

## Environment Variables

The project uses the following environment variables (configured in `.env`):

| Variable | Description |
|----------|-------------|
| `SUPABASE_URL` | Your Supabase project URL |
| `SUPABASE_KEY` | Your Supabase API key |
| `NASA_API_KEY` | Your NASA API key (get from [nasa.gov](https://api.nasa.gov)) |

Make sure to add `.env` to your `.gitignore` file to avoid exposing sensitive credentials.

## Project Scripts

### extract_nasa.py
Extracts data from NASA APIs. Handles API requests and data fetching.

### transform_nasa.py
Transforms the extracted raw data into a structured format suitable for database storage. Includes data cleaning and validation.

### load_nasa.py
Loads the transformed data into the Supabase database. Handles connection management and error handling.

## GitHub Actions Workflow

The project includes automated workflow configurations in `.github/workflows/` that enable:

- Automated ETL execution on schedule
- Error notifications
- Data validation checks

## Contributing

Contributions are welcome! Please feel free to:

- Report bugs and issues
- Suggest improvements
- Submit pull requests

## License

This project is open source and available under the MIT License.

## Contact

For questions or support, please contact the project maintainer at [GitHub Profile](https://github.com/RITHESH218).

---

**Last Updated**: December 2025
