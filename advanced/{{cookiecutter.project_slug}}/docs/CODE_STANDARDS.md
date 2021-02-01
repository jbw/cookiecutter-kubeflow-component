## Standards

### Testing

- Test expected behaviour
- uses `unittest` framework and `pytest` as a test runner
- Files prefixed with `test_`
- But any test data in a folder called `testdata`
- Test files should be grouped logically into folders to keep it tidy and readable
- Test method names follow `should_expected_behavior_when_state_under_test`

```py
def test_should_throw_exception_when_source_data_is_missing():
    # given
    # when
    # then

```

### Development

#### Component Code

- Components should be testable.
- Component data should come through inputs and not anywhere else.
- Consider upstream and downstream impact and test against it.
- Module code should be runnable from the CLI and not only as a Kubeflow component
- Components are language agnostic but most of our code will use Python3.
- Do not use hard-coded parameters and isntead make the component configurable.
- We should separate the Kubeflow component concerns from our code module.

  By code module we mean the business logic we are implementing e.g.a trainer or predictor. This means our code module should not know anything about Kubeflow. Inputs should be handled elsewhere and passed into the module. Outputs should be returned in standard ways.

### requirements.txt

Amend this file in the root of the project to the requirements of your component.

### Component YAML

- All inputs and outputs must be defined in the YAML
- Fill in name and description

### Dockerfile

[Follow best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices).

You might need to modify the Dockerfile if a more appropriate base image is available e.g. Tensorflow

### Logging

This project uses the `python-json-logger` package to standardise logging for use with log aggregators.

In your code use

```py
from logger import get_logger
logger = get_logger()
logger.info("Hello")
```

Which outputs

```json
{
  "asctime": "2020-11-13 17:14:46,669",
  "created": 1605287686.669351,
  "levelname": "INFO",
  "module": "main",
  "funcName": "<module>",
  "message": "Hello"
}
```

### Tooling

| File   | Description       |
| ------ | ----------------- |
| pytest | Testing framework |
| black  | Code formatter    |
