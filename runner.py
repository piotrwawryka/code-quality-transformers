#!/usr/bin/env python
import argparse
import inspect

from codequality import reader, model


def get_available_models():
    return {name: cls for (name, cls) in inspect.getmembers(model)
            if inspect.isclass(cls)
            and cls is not model.BaseModel
            and issubclass(cls, model.BaseModel)}


def create_parser(available_models):
    parser = argparse.ArgumentParser()
    parser.add_argument('model', choices=available_models)
    parser.add_argument('dataset')
    return parser


def main():
    available_models = get_available_models()
    parser = create_parser(available_models=available_models.keys())
    args = parser.parse_args()


if __name__ == '__main__':
    main()
