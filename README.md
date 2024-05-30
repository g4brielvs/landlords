# Leveraging NYC Open Data to Identify Potential Potential Housing Maintenance Code in New York City

The New York Attorney General (NYAG) is actively combating various harmful landlord practices such as tenant harassment, deed theft, and bank fraud, which adversely impact tenants and homeowners. By leveraging open data publicly available through [NYC Open Data](https://opendata.cityofnewyork.us), this notebook uses data analysis tools to identify, describe, and visualize characteristics of landlords engaging in harmful behaviors.

## Installation

**landlords** can installed using `pip`:

### From Source

1. Clone or download this repository to your local machine. Then, navigate to the root directory of the repository:

    ```shell
    git clone https://github.com/g4brielvs/landlords.git
    cd landlords
    ```

2. Create a virtual environment (optional but recommended):

    ```shell
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the package with dependencies:

    ```shell
    pip install .
    ```

    Install the package **in editable** mode with dependencies:

    ```shell
    pip install -e .
    ```

    The `-e` flag stands for "editable," meaning changes to the source code will immediately affect the installed package.

### Building Documentation Locally

To build the documentation locally, after (1) and (2) above, please follow these steps:

- Install the package with documentation dependencies:

  ```shell
    pip install -e .[docs]
  ```

- Build the documentation:

  ```shell
    jupyter-book build . --config docs/_config.yml --toc docs/_toc.yml
  ```

The generated documentation will be available in the `_build/html` directory. Open the `index.html` file in a web browser to view it.
