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

| Module                      | Version | Link                                                                                                           |
|-----------------------------|---------|----------------------------------------------------------------------------------------------------------------|
| Django                      | 4.1.7   | [https://pypi.org/project/Django/](https://pypi.org/project/Django/)                                           |
| Pillow                      | 9.4.0   | [https://pypi.org/project/Pillow/](https://pypi.org/project/Pillow/)                                           |
| django-cors-headers         | 3.13.0  | [https://pypi.org/project/django-cors-headers/](https://pypi.org/project/django-cors-headers/)                 |
| djangorestframework         | 3.14.0  | [https://pypi.org/project/djangorestframework/](https://pypi.org/project/djangorestframework/)                 |
| djangorestframework-api-key | 2.3.0   | [https://pypi.org/project/djangorestframework-api-key/](https://pypi.org/project/djangorestframework-api-key/) |
| nltk                        | 3.8.1   | [https://pypi.org/project/nltk/](https://pypi.org/project/nltk/)                                               |
| numpy                       | 1.24.2  | [https://pypi.org/project/numpy/](https://pypi.org/project/numpy/)                                             |
| requests                    | 2.28.2  | [https://pypi.org/project/requests/](https://pypi.org/project/requests/)                                       |
| psycopg2-binary             | 2.9.5   | [https://pypi.org/project/psycopg2-binary/](https://pypi.org/project/psycopg2-binary/)                         |
| bert-extractive-summarizer  | 0.10.1  | [https://pypi.org/project/bert-extractive-summarizer/](https://pypi.org/project/bert-extractive-summarizer/)   |
| tensorflow                  | 2.11.0  | [https://pypi.org/project/tensorflow/](https://pypi.org/project/tensorflow/)                                   |
| torch                       | 1.13.1  | [https://pypi.org/project/torch/](https://pypi.org/project/torch/)                                             |

#### Production Code Adapted For Use

Code in the package [`./backend/api/grobid_client`](./backend/api/grobid_client) has
sourced and adapted from the python package `grobid_client_python` which can be found
at [https://github.com/kermitt2/grobid_client_python](https://github.com/kermitt2/grobid_client_python)

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

Then install the hooks specified in [`.pre-commit-config.yaml`](./.pre-commit-config.yaml) by running `pre-commit install`

Further details can be found [here](https://pre-commit.com/)

Python pre-commit hooks are set up to only run on the "backend" directory and "JavaScript" are only set up for the frontend directory

### Postman Collection

This project comes with a [postman collection](./resources/FYP.postman_collection.json)
and a [postman environment](./resources/FYP%20Environment.postman_environment.json)
which can be used for testing and development of the Web App.
These files are found in [`./resources`](./resources)
