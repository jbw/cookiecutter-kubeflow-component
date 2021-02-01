#!/usr/bin/env python
import os
from shutil import rmtree

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


if __name__ == '__main__':

    if '{{ cookiecutter.create_preprocessor }}' != 'y':
        rmtree(os.path.join(PROJECT_DIRECTORY, 'components/preprocessor'))
    
    if '{{ cookiecutter.create_trainer }}' != 'y':
        rmtree(os.path.join(PROJECT_DIRECTORY, 'components/trainer'))

    if '{{ cookiecutter.create_predictor }}' != 'y':
        rmtree(os.path.join(PROJECT_DIRECTORY, 'components/predictor'))

    if '{{ cookiecutter.create_validation }}' != 'y':
        rmtree(os.path.join(PROJECT_DIRECTORY, 'components/validation'))

    if '{{ cookiecutter.create_train_test_split }}' != 'y':
        rmtree(os.path.join(PROJECT_DIRECTORY, 'components/train_test_split'))

    if '{{ cookiecutter.create_explainability }}' != 'y':
        rmtree(os.path.join(PROJECT_DIRECTORY, 'components/explainability'))

    if '{{ cookiecutter.create_pipeline }}' != 'y':
        rmtree(os.path.join(PROJECT_DIRECTORY, 'pipeline/'))
