#!/usr/bin/env python
import os
from shutil import rmtree

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_dir(filepath):
    os.removedirs(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.create_preprocessor }}' != 'y':
        rmtree(os.path.join(PROJECT_DIRECTORY, 'components/preprocessor'))
        remove_file("preprocessor.py")

    if '{{ cookiecutter.create_trainer }}' != 'y':
        rmtree(os.path.join(PROJECT_DIRECTORY, 'components/trainer'))
        remove_file("trainer.py")

    if '{{ cookiecutter.create_predictor }}' != 'y':
        rmtree(os.path.join(PROJECT_DIRECTORY, 'components/predictor'))
        remove_file("predictor.py")

    if '{{ cookiecutter.create_validation }}' != 'y':
        rmtree(os.path.join(PROJECT_DIRECTORY, 'components/model_validatior'))
        remove_file("model_validatior.py")

    if '{{ cookiecutter.create_train_test_split }}' != 'y':
        rmtree(os.path.join(PROJECT_DIRECTORY, 'components/train_test_splitter'))
        remove_file("train_test_splitter.py")

    if '{{ cookiecutter.create_explainability }}' != 'y':
        rmtree(os.path.join(PROJECT_DIRECTORY, 'components/explainer'))
        remove_file("explainer.py")

    if '{{ cookiecutter.create_pipeline }}' != 'y':
        rmtree(os.path.join(PROJECT_DIRECTORY, 'pipeline/'))
