# Symfony Backend ETL Project

## Overview
This project is a Symfony backend that performs a daily ETL workflow:

1. Extracts data from a remote API and saves it as JSON (`data_[YYYYMMDD].json`).
2. Transforms the JSON into CSV files (`ETL_[YYYYMMDD].csv` and `summary_[YYYYMMDD].csv`).
3. Saves summary data into a MySQL database.
4. Encrypts CSV files and uploads them to an SFTP server.

---
