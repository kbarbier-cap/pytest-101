# Python Unit Testing 101

This repository helps all people you want to write unit tests in Python. The unit tests are oriented for Data-Sciences/Data-Engineer activities. You can find some slides [here](UPDATE_LINK) about what are Unit Tests and why is so important to get the skill of integrating unit tests in any Data-Science projects.

# Prerequisites

- `make` command in order to run all make command from the Makefile
- A `python 3.10` environment. Python 3.9/3.8 should also work but not have been tested

# Understand the repository

The folder architecture is the following :

```bash
├── README.md
├── Makefile
├── setup.py                     ----- Used for building your package and the dependencies
├── requirements.txt             ----- Dependencies requirements
├── src                          ----- Source code
│   ├── python_unit_tests_101/   ----- Code of the learning
├── tests                        ----- Main test folder
│   ├── conftest.py              ----- Fixture that can be used in all of your tests
│   └── unit/                    ----- All of the unit tests
└── tests                        ----- Data folder with a simple example to make the tasks work
```

# Setup

- Activate your python environment (python3.10)
- Run in your shell `make install_env`
- Your env is ready (for some reasons when using a conda environment you may need to reactivate your env to have your own package properly intalled)

# Exercices

## Exercice 1 : run a simple test to see if you're development environment is ready

In this exercice, you won't test functions of the main code but just test a simple function to test your development setup

1. Look at the tests/unit/utils/test_simple.py script. There's a simple test here. That's how to write a unit test.
2. Run your unit test and valid that the test in test_simple.py passed. `make test`

## Exercice 2 : Understand the main code

This exercice helps you understand the main code of the Tasks / Pipeline

1. Look at the main code under src/python_unit_tests_101 and understand the structure.
2. Understand what is the link between the Task classes and the two Pipelines classes (preprocessing and feature engineering)

## Exercice 3 : Create tests for the PreprocessingPipeline

At the end of this exercice you'll have all of your unit tests from the PreprocessingPipeline. 

1. Look at the PreprocessingPipeline located in *src/python_unit_tests_101/pipelines.py*
2. Ask yourself what methods/classes/functions you need to test and what kind of test you want to implement. Remember, a test must help you to avoid code regression and document your code.
3. Code the tests of the PreprocessingPipeline class. Remember, test one thing at a time.
4. BONUS: train yourself ! Use a fixture a datraframe as input of your tests (Doc [here](https://docs.pytest.orting)).

hint 1: Your `tests` should mirror your main code. Create a class `TestPreprocessingPipeline` and put your tests inside.

hint 2: use [*pd.testing.assert_frame_equal*](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_frame_equal.html) method to test if two pandas dataframes are equal.

## Exercice 4 : Create tests for the FeaturesEngineeringPipeline

At the end of this exercice you'll have all of your unit tests from the FeaturesEngineeringPipeline

1. Look at the FeaturesEngineering located in *src/python_unit_tests_101/pipelines.py*
2. Ask yourself what methods/classes/functions you need to test and what kind of test you want to implement. Remember, a test must help you to avoid code regression and document your code.
3. Code the tests of the FeaturesEngineering class. Remember, test one thing at a time.
4. BONUS: use a `setup_class(cls)` method to define dataframe as input of your tests (Doc [here](https://docs.pytest.org/en/stable/how-to/xunit_setup.html)).

hints: use [*pd.testing.assert_frame_equal*](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_frame_equal.html) method to test if two pandas dataframes are equal.

## Exercice 5 : Create tests for the two PreprocesingTask and FeaturesEngineeringTask tasks

At the end of this exercice you'll have all of your unit tests of both Task (PreprocessingTask and FeatureEngineering Task)

1. Look at both Tasks located in *src/python_unit_tests_101/tasks/*
2. Ask yourself what methods/classes/functions you need to test and what kind of test you want to implement. Remember, a test must help you to avoid code regression and document your code.
3. Code the tests of the PreprocessingTask/FeatureEngineeringTask classes. Remember, test one thing at a time.

hints: the `pandas` library is already tested ;). It's not necessary to tests that kind of code.


# Correction 

Look at the branch to have the correction of each exercice. For example, to have all the correction of all exercices, look at the branch correction-exercice5