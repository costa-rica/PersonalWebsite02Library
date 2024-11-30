# PersonalWebsite02Library

![nick-rodriguez.info Logo](https://nick-rodriguez.info/website_assets_favicon/logo02_whiteBck-180x112.png)

This repository contains essential modules for the `PersonalWebsite02` Flask application.

## Components

- **Configuration**: The `config.py` file hosts the Configuration classes utilized by the main Flask application.

- **Models**: This module contains the data models for the application.

## Database

The application employs SQLite as its database, with SQLAlchemy acting as the ORM (Object Relational Mapper).

## Installation

There are two primary methods to install these modules:

1. **Direct Installation with pip**:
   You can clone this repository and then use pip to install:
   ```bash
   git clone https://github.com/costa-rica/PersonalWebsite02Library.git
   cd
   pip install .
   ```

## .env

- Ubuntu server

```env
DATABASE_ROOT = "/home/nick/applications/databases/PersonalWebsite02/"
PROJECT_ROOT = "/home/nick/applications/PersonalWebsite02/"
PROJECT_RESOURCES_ROOT = "/home/nick/applications/project_resources/PersonalWebsite02/"
CONFIG_ROOT="/home/nick/applications/_config_files/"
CONFIG_FILE_NAME="config_personalWebsite02.json"
FLASK_CONFIG_TYPE='prod'
DB_NAME_BLOGPOST = "BlogPosts.db"
CONFIG_FILE_NAME_SUPPORT="support20231118.json"
API_URL = "http://localhost:5001"
BACKUP_ROOT = "/home/nick/applications/_backups"
TEMPORARILY_DOWN=0
```

- local workstation

```env
DATABASE_ROOT = /Users/nick/Documents/_databases/PersonalWebsite02/
PROJECT_ROOT = /Users/nick/Documents/PersonalWebsite02/
PROJECT_RESOURCES_ROOT = "/Users/nick/Documents/_project_resources/PersonalWebsite02/PersonalWebsite02/"
CONFIG_ROOT=/Users/nick/Documents/_config_files/
CONFIG_FILE_NAME="config_personalWebsite02.json"
FLASK_CONFIG_TYPE='dev'
DB_NAME_BLOGPOST = "BlogPosts.db"
CONFIG_FILE_NAME_SUPPORT="support20231118.json"
API_URL = "http://localhost:5001"
BACKUP_ROOT = "/home/nick/applications/_backups"
TEMPORARILY_DOWN=0
```
