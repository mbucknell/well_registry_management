# Well Registry Management System

[![Build Status](https://travis-ci.org/ACWI-SOGW/well_registry_management.svg?branch=master)](https://travis-ci.org/ACWI-SOGW/well_registry_management)
[![codecov](https://codecov.io/gh/ACWI-SOGW/well_registry_management/branch/master/graph/badge.svg)](https://codecov.io/gh/ACWI-SOGW/well_registry_management)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6af41d5963ee48c1bb9f8a83ea338b46)](https://www.codacy.com/gh/ACWI-SOGW/well_registry_management?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ACWI-SOGW/well_registry_management&amp;utm_campaign=Badge_Grade)


Application for management of groundwater monitoring locations.

## Local Environment Setup
A local development environment can be setup by running:

```bash
make env
```

## Development Server
To run the development server, create a `local_settings.py` file as a sibling of `settings.py`. Add a `SECRET_KEY` value
with some random stuff (e.g `SECRET_KEY = 'sjfio3u903RaggleFraggle'` and see "Environment Variables" section).

The Django local development can be run via:

```bash
make watch
```

## Environment Variables

    This project has a private companion config project where environment variable
    files for each deployment tier are maintained. The values in the config files are
    applied to the docker container for each teir at deployment. 
    The following sub sections will describe the various variables used.

General

    DEBUG: boolean - true for debug level logging

Cloud

    These environment variables are required for the cloud deployment.
    They are not used for local development.

        SECRET_KEY: AWS secret key
        ALLOWED_HOSTS: mapped URL
        CIDR_RANGES: IP ranges allowed to connect

Database (root)

    The DATABASE values are defined to connect to cloud RDS or local DB installation.
    These values are used by the initial Django migrations *only* to configure the application.

        DATABASE_NAME: posgres database name
        DATABASE_HOST: posgres host url 
            - use 'localhost' for local development database
            - use the actual tier database host URL for cloud deployment
        DATABASE_PORT: optional posgres port - if not specified then default is '5432' 
        DATABASE_USERNAME: postgres root user name
        DATABASE_PASSWORD: postgres root password

Database (app)

    The following should be set to initial values for a new database configuration.
    Once the database initial migration scripts are run then they need to be set to 
    expected values. While these can be arbitrarily configurable for local database 
    development, some example values are mentioned.

    The application database ensures that application data is not stored in the postgres 
    system database. It also enables multiple application to share a database instance.
        APP_DATABASE_NAME:     name for the applicaiton database within postgres
        APP_DB_OWNER_USERNAME: user name for the database owner
        APP_DB_OWNER_PASSWORD: database owner password

    The application schema ensure that applicaiton data is not stored in the default public
    schema. The configuration assigns this schema as the primary search_path.
        APP_SCHEMA_NAME:           name for the application schema
        APP_SCHEMA_OWNER_USERNAME: owner user name for the application schema
        APP_SCHEMA_OWNER_PASSWORD: schema owner password

    This connection will allow maitainance of all registry entries in support of user issues.
    It has less restricted table CRUD roles than the application user.
        APP_ADMIN_USERNAME: user name for the connection used by the registry administration
        APP_ADMIN_PASSWORD: administration login password

    This connecton is the standard or default applicaiton user connection.
    It has limited table CRUD roles.
        APP_CLIENT_USERNAME: user name for the connection used by the registry users
        APP_CLIENT_PASSWORD: user level login password
