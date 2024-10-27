# solution_ps2_ex3_database

This is the solution to PS 2, ex3 database.

# Setup

## Envrionment

Install the required packages by running:

```bash
conda env create -f environment.yml
```

Activate the environment by running:

```bash
conda activate solution_ps2_ex3_database
```

## Pre-commit

This repository uses pre-commit to run some checks before each commit. To install pre-commit, run:

```bash
pre-commit install
```

To run the checks manually, run:

```bash
pre-commit run --all-files
```

# Getting the data

1. create kaggle account: https://www.kaggle.com/
2. get API keys and user name
   - Go to your account, and click on your profile in the top right
   - Then click on "Settings"
   - Scroll down to the API section and click on "Create New Token"
   - Get your username and API key from there

Then run the following command in the terminal being at the root of the repository. Replace
"your_user_name" and "your_api_key" with your username and API key. This creates a json file at
"~/.kaggle/kaggle.json" with your username and API key. This is used to authenticate your account
and download the data.

```bash
python nba/data_loader.py --user_name "your_user_name" --api_key "your_api_key"
```
