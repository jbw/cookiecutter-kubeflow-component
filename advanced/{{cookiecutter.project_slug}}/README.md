## Kubeflow Python Component Bootstrap :boot: :rocket:

This starter project should be used when developing new Kubeflow components. It implements
well accepted standards, development practices, and libraries. It's also to promote
consistent development and deployment experience from component to component to allow for ease of support, testing, and updating.

### Highlights :sparkles:

- Bootstraps the typical boilerplate when starting something new
- Solution layout for source and test code following best practices from Kubeflow and others
- Consistent code formatting and linting
- Bitbucket CI integration for running test suite, style checks, component builds and deployments

### Getting Started

### Implementation 


See [Kubeflow component example](https://bitbucket.org/caspianlearning/kubeflow-python-component-starter-example/src/master/)

```py
from dotenv import load_dotenv

from caspian_ml_kit.pipeline.workflow.builder import ComponentWorkflowBuilder
from example.components.trainer.src.handler import YourIAComponentHandler
from example.components.trainer.src.train import YourIAComponentTrainer
from example.components.common.logger import get_logger
from example.components.trainer.args import get_args

load_dotenv()

# fmt: off
(
    ComponentWorkflowBuilder()
        .add_logger(get_logger())
        .add_component_args(get_args())
        .add_trainer(YourIAComponentTrainer)
        .add_handler(YourIAComponentHandler)
        .build()
        .run()
)
# fmt: on
```

#### Running tests

```sh
pip install -r test_requirements.txt
pip install -r requirements.txt
python -m pytest components/<component_name>/tests/
```

### Building

#### Build Docker image

```sh
chmod +x ./ci/build.sh
./ci/build.sh <dockerfile> . <image_name>
```

#### Docker image naming convention

Use the following convention: `${container_registry_url}/kubeflow/ia/${ia-name}-${component_name}-component`

e.g. `eu.gcr.io/fip-project/kubeflow/ia/transaction-parties-predictor-component`

### Configuration

There is a .env.development file in the root of the project. Rename that file to .env so it will be
automatically loaded. Set the values in the file to match your environment or deployment environment. 

#### S3

Minio example: 
```
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_S3_ENDPOINT_URL=http://localhost:9000
AWS_MAX_ATTEMPTS=5
```

Modify the above for any other S3 instance e.g. AWS S3

#### CI 

##### Repository variables

Set up your CI environment variables. 

| Name                  | Value example |
| --------------------- | ------------- |
| DOCKER_PASS           |               |
| DOCKER_USER           | _json_key     |
| CONTAINER_REPOSITORY  |               |
| SONAR_TOKEN           |               |
| AWS_ACCESS_KEY_ID     |               |
| AWS_SECRET_ACCESS_KEY |               |
| AWS_DEFAULT_REGION    | eu-west-1     |
                                                             
### Dependencies
* Python 3.8

### Practices

- [Standards](./docs/standards.md)
- [Solution layout](./docs/layout.md)

### Learn More

- https://github.com/kubeflow
- https://www.kubeflow.org/docs/pipelines/overview/pipelines-overview/
- https://www.kubeflow.org/docs/pipelines/sdk/sdk-overview/
- https://www.kubeflow.org/docs/pipelines/sdk/build-component/
- https://www.kubeflow.org/docs/pipelines/sdk/component-development/
- https://www.kubeflow.org/docs/pipelines/sdk/python-function-components/
- https://www.kubeflow.org/docs/pipelines/sdk/best-practices/

### Related Projects

- [Kubeflow component example](https://bitbucket.org/caspianlearning/kubeflow-python-component-starter-example/src/master/)
- [Kubeflow pipeline starter](https://bitbucket.org/caspianlearning/kubeflow-pipeline-starter/src/master/)
- [Caspian ML Kit](https://bitbucket.org/caspianlearning/caspian-ml-kit/src/master/)
