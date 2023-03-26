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

| Module        | Version | Link                                                                               |
|---------------|---------|------------------------------------------------------------------------------------|
| pytest        | 7.2.1   | [https://pypi.org/project/pytest/](https://pypi.org/project/pytest/)               |
| black         | 23.1.0  | [https://pypi.org/project/black/](https://pypi.org/project/black/)                 |
| coverage      | 7.2.0   | [https://pypi.org/project/coverage/](https://pypi.org/project/coverage/)           |
| pre-commit    | 3.1.0   | [https://pypi.org/project/pre-commit/](https://pypi.org/project/pre-commit/)       |
| pylint        | 2.16.2  | [https://pypi.org/project/pylint/](https://pypi.org/project/pylint/)               |
| pylint-django | 2.5.3   | [https://pypi.org/project/pylint-django/](https://pypi.org/project/pylint-django/) |



#### Evaluation Modules

| Module       | Version | Link                                                                             |
|--------------|---------|----------------------------------------------------------------------------------|
| requests     | 2.28.2  | [https://pypi.org/project/requests/](https://pypi.org/project/requests/)         |
| pandas       | 1.5.3   | [https://pypi.org/project/pandas/](https://pypi.org/project/pandas/)             |
| seaborn      | 0.12.2  | [https://pypi.org/project/seaborn/](https://pypi.org/project/seaborn/)           |
| scikit-learn | 1.2.2   | [https://pypi.org/project/scikit-learn/](https://pypi.org/project/scikit-learn/) |


### Node Dependencies

_This project makes use of multiple node packages some of which are in general,
and some are used for development only and have been listed as such in the following._

#### Production Packages

| Module                                | Version | Link                                                                                                                                       |
|---------------------------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------|
| @fortawesome/fontawesome-svg-core     | 6.3.0   | [https://www.npmjs.com/package/@fortawesome/fontawesome-svg-core](https://www.npmjs.com/package/@fortawesome/fontawesome-svg-core)         |
| @fortawesome/free-regular-svg-icons   | 6.3.0   | [https://www.npmjs.com/package/@fortawesome/free-regular-svg-icons](https://www.npmjs.com/package/@fortawesome/free-regular-svg-icons)     |
| @fortawesome/free-solid-svg-icons     | 6.3.0   | [https://www.npmjs.com/package/@fortawesome/free-solid-svg-icons](https://www.npmjs.com/package/@fortawesome/free-solid-svg-icons)         |
| @fortawesome/react-fontawesome        | 0.2.0   | [https://www.npmjs.com/package/@fortawesome/react-fontawesome](https://www.npmjs.com/package/@fortawesome/react-fontawesome)               |
| axios                                 | 1.3.4   | [https://www.npmjs.com/package/axios](https://www.npmjs.com/package/axios)                                                                 |
| moment                                | 2.29.4  | [https://www.npmjs.com/package/moment](https://www.npmjs.com/package/moment)                                                               |
| npm-check-updates                     | 16.7.10 | [https://www.npmjs.com/package/npm-check-updates](https://www.npmjs.com/package/npm-check-updates)                                         |
| react                                 | 18.2.0  | [https://www.npmjs.com/package/react](https://www.npmjs.com/package/react)                                                                 |
| react-cookie                          | 4.1.1   | [https://www.npmjs.com/package/react-cookie](https://www.npmjs.com/package/react-cookie)                                                   |
| react-dom                             | 18.2.0  | [https://www.npmjs.com/package/react-dom](https://www.npmjs.com/package/react-dom)                                                         |
| react-dropzone                        | 14.2.3  | [https://www.npmjs.com/package/react-dropzone](https://www.npmjs.com/package/react-dropzone)                                               |
| react-router-dom                      | 6.8.2   | [https://www.npmjs.com/package/react-router-dom](https://www.npmjs.com/package/react-router-dom)                                           |
| react-scripts                         | 5.0.1   | [https://www.npmjs.com/package/react-scripts](https://www.npmjs.com/package/react-scripts)                                                 |
| web-vitals                            | 3.1.1"  | [https://www.npmjs.com/package/web-vitals](https://www.npmjs.com/package/web-vitals)                                                       |

#### Development Packages

| Module                                | Version | Link                                                                                                                                       |
|---------------------------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------|
| @testing-library/jest-dom             | 5.16.5  | [https://www.npmjs.com/package/@testing-library/jest-dom](https://www.npmjs.com/package/@testing-library/jest-dom)                         |
| @testing-library/react                | 14.0.0  | [https://www.npmjs.com/package/@testing-library/react](https://www.npmjs.com/package/@testing-library/react)                               |
| @testing-library/user-event           | 14.4.3  | [https://www.npmjs.com/package/@testing-library/user-event](https://www.npmjs.com/package/@testing-library/user-event)                     |
| @trivago/prettier-plugin-sort-imports | 4.1.1   | [https://www.npmjs.com/package/@trivago/prettier-plugin-sort-imports](https://www.npmjs.com/package/@trivago/prettier-plugin-sort-imports) |
| eslint                                | 8.35.0  | [https://www.npmjs.com/package/eslint](https://www.npmjs.com/package/eslint)                                                               |
| eslint-plugin-react                   | 7.32.2  | [https://www.npmjs.com/package/eslint-plugin-react](https://www.npmjs.com/package/eslint-plugin-react)                                     |
| prettier                              | 2.8.4   | [https://www.npmjs.com/package/prettier](https://www.npmjs.com/package/prettier)                                                           |

### Docker Images

As Part of this project a number of docker images have been used as a base and thn either built onto of or used as is. They are here as follows:

| Image Name                            | Image Tag | Link                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ubuntu                                | 20.04     | [https://hub.docker.com/layers/library/ubuntu/20.04/images/sha256-b39db7fc56971aac21dee02187e898db759c4f26b9b27b1d80b6ad32ff330c76?context=explore](https://hub.docker.com/layers/library/ubuntu/20.04/images/sha256-b39db7fc56971aac21dee02187e898db759c4f26b9b27b1d80b6ad32ff330c76?context=explore)                 |
| python                                | 3.8       | [https://hub.docker.com/layers/library/python/3.8/images/sha256-00af0878e19a32802037964268982b52425d0e8395cb61483baec3a28f89eeb5?context=explore](https://hub.docker.com/layers/library/python/3.8/images/sha256-00af0878e19a32802037964268982b52425d0e8395cb61483baec3a28f89eeb5?context=explore)                     |
| node                                  | latest    | [https://hub.docker.com/layers/library/node/latest/images/sha256-026026d98942438e4df232b3e8cd7ca32416b385918977ce5ec0c6333618c423?context=explore](https://hub.docker.com/layers/library/node/latest/images/sha256-026026d98942438e4df232b3e8cd7ca32416b385918977ce5ec0c6333618c423?context=explore)                   |
| postgres                              | latest    | [https://hub.docker.com/layers/library/postgres/latest/images/sha256-739e77524f4036dd45e09368cefed617780bb24eca6c4aa9b0b431c7c0b76bca?context=explore](https://hub.docker.com/layers/library/postgres/latest/images/sha256-739e77524f4036dd45e09368cefed617780bb24eca6c4aa9b0b431c7c0b76bca?context=explore)           |
| registry.hub.docker.com/grobid/grobid | 0.7.2     | [https://registry.hub.docker.com/layers/grobid/grobid/0.7.2/images/sha256-a318e685dbf597a9b6dd1c5e03cc6b41d9dcd2f6b43629a5ad41bb0ba5c238aa?context=explore](https://registry.hub.docker.com/layers/grobid/grobid/0.7.2/images/sha256-a318e685dbf597a9b6dd1c5e03cc6b41d9dcd2f6b43629a5ad41bb0ba5c238aa?context=explore) |


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
