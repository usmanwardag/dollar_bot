# For Developers: By the Developers of DollarBot

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#testing">Testing</a></li>
    <li><a href="#code-coverage">Code Coverage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#code-documentation">Code Documentation</a></li>
    <li><a href="#how-to-contribute">How to Contribute</a></li>
    <li><a href="#future-roadmap">Future RoadMap</a></li>
  </ol>
</details>

## Testing

We use pytest to perform testing on all unit tests together. The command needs to be run from the home directory of the project. The command is:
```
python run -m pytest test/
```

## Code Coverage

Code coverage is part of the build. Every time new code is pushed to the repository, the build is run, and along with it, code coverage is computed. This can be viewed by selecting the build, and then choosing the codecov pop-up on hover.

Locally, we use the coverage package in python for code coverage. The commands to check code coverage in python are as follows:

```
coverage run -m pytest test/
coverage report
```

## License

This project is licensed under the terms of the MIT license. Please check [License](https://github.com/usmanwardag/dollar_bot/blob/main/LICENSE) for more details.


## Code Documentation

Checkout the [docs](https://github.com/aditikilledar/dollar_bot_SE23/tree/main/docs) for a detailed explanation of each functionality and the expected working along with code file location.

## How to Contribute

We would be happy to receive contributions! If you'd like to, please go through our [CONTRIBUTING.md](https://github.com/aditikilledar/dollar_bot_SE23/blob/main/CONTRIBUTING.md)

For any feedback, issues, or bug reports, please create an issue [here](https://github.com/aditikilledar/dollar_bot_SE23/issues/new/choose).

## Future RoadMap

- More content can be added for the way notifications can be displayed on the user front. This can be done to make the UI more interactive.
- Recurring expenses feature can be added for faster addition of expenses instead of following the whole process of everytime.
