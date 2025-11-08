#  omnicart-pipeline

**A production-ready CLI data pipeline tool** that fetches, enriches, and analyzes seller performance data from multiple APIs.  
Built using Python, Poetry, and a modular architecture — this project demonstrates real-world software packaging, dependency management, and command-line interface (CLI) design.

---

##  Project Overview

**OmniCart Pipeline** is a command-line tool designed to automate the extraction, enrichment, and analysis of product and seller data for OmniCart Analytics.

The tool:
- Fetches data from multiple REST APIs (`/products`, `/users`) with pagination.
- Enriches product data with seller information.
- Computes seller performance metrics (e.g., total revenue, number of products, average price).
- Outputs a structured JSON report ready for BI or analytics teams.

Anyone can install and run it from the command line — no manual scripts, no setup hassle.

---

##  Learning Goals

This project demonstrates:
- **End-to-End Software Development** — from raw Python logic to an installable, versioned CLI package.  
- **Robust OOP Design** — with reusable, testable, and modular classes.  
- **Advanced Data Engineering Concepts** — including pagination, enrichment joins, and analytics aggregation.  
- **Professional Packaging & Distribution** — using Poetry and PyPI best practices.  

---

##  Core Components

| Module | Description |
|:-------|:-------------|
| **`config.py`** | Reads and manages configuration values from `pipeline.cfg` using `importlib.resources` for cross-environment compatibility. |
| **`api_client.py`** | Handles API communication and pagination for both `/products` and `/users`. |
| **`data_enricher.py`** | Merges and enriches product data with seller information; calculates `revenue = price * rating['count']`. |
| **`data_analyzer.py`** | Generates per-seller performance statistics (total revenue, product count, average price). |
| **`pipeline.py`** | Orchestrates the full workflow — from config loading to final JSON report generation. |
| **`cli.py`** | Defines the CLI entry point for the `omnicart-pipeline` command. |

---

##  Installation

###  From PyPI (recommended)

```bash
pip install pip install omnicart-pipeline-sallie==0.1.0
```
---
 
# Configuration Management (The .cfg Challenge)

One major packaging challenge was ensuring the tool could access its configuration file (pipeline.cfg) regardless of where it was installed.

To solve this, the project uses Python’s modern approach:

from importlib import resources

````
if config_path is None:
            base_dir = resources.files("omnicart_pipeline")  # goes up one folder
            config_path = os.path.join(base_dir, "pipeline.cfg")
````


And in pyproject.toml, we explicitly include non-code files:

```
[tool.poetry.include]
"omnicart_pipeline/pipeline.cfg" = "omnicart_pipeline/pipeline.cfg"
```
---
# Repository Structure

de-capstone-packaging-salome/
├── omnicart_pipeline/
│   ├── __init__.py
│   ├── api_client.py
│   ├── config.py
│   ├── data_enricher.py
│   ├── data_analyzer.py
│   ├── pipeline.py
│   ├── cli.py
│   └── pipeline.cfg
│
├── tests/
│   ├── test_config.py
│   ├── test_api_client.py
│   ├── test_data_enricher.py
│   ├── test_data_analyzer.py
│   └── test_pipeline.py
│
├── pyproject.toml
├── poetry.lock
├── README.md
└── .gitignore

