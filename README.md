# Final Year Project Repo for William Holbrook

## Deployment Instructions

### Development Deployment

### Production Deployment

## External Dependencies and Acknowledgements

- Python - 3.8.10
- Node - 18.12.1

### Python Dependencies

_This project makes use of multiple python modules some of which are in general,
some are used for development only and some are used for evaluation only and
have been listed as such in the following._

#### Production Modules


#### Production Code Adapted For Use
#### Development Modules
#### Evaluation Modules
### Node Dependencies

_This project makes use of multiple node packages some of which are in general,
and some are used for development only and have been listed as such in the following._

#### Production Packages
#### Development Packages
### Docker Images
### GitHub Actions
### Pre-Commit Hooks


## Development Tools

### Pre-commit Hooks

This project makes use of pre-commit hooks.
To install them first download pre-commit using pip:

```pip install pre-commit```

Then install the hooks specified in `.pre-commit-config.yaml` by running `pre-commit install`

Further details can be found [here](https://pre-commit.com/)

Python pre-commit hooks are set up to only run on the "backend" directory and "JavaScript" are only set up for the frontend directory

### Postman Collection

This project comes with a [postman collection](./resources/FYP.postman_collection.json)
and a [postman environment](./resources/FYP%20Environment.postman_environment.json)
which can be used for testing and development of the Web App.
These files are found in `./resources`
