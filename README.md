# Pubic Medical Paper fetcher

A Python command-line tool that fetches research papers from PubMed based on a query, identifies papers with at least one author affiliated with a pharmaceutical or biotech company, and exports the result as CSV.

## Features

- Accepts queries via CLI
- Filters non-academic authors using heuristics
- Outputs CSV or console print
- Debug and file save options
- Typed Python with Poetry support

## Tools Used
| Tool         | Purpose                             |
| ------------ | ----------------------------------- |
| Python 3.10+ | Core programming language           |
| Poetry       | Dependency and packaging management |
| Git + GitHub | Version control and hosting         |
| PubMed API   | Data source for research papers     |
| xml.etree    | XML parsing of PubMed results       |

## LLMs Used:
✅ ChatGPT (OpenAI GPT-4) — for idea assistance, filtering heuristics, and code drafting.

## Setup Instructions (to be completed after Python install)
Installation & Setup

1. Install Poetry
Check if Poetry is installed:
poetry --version

3. Clone the Repository

git clone https://github.com/Anusha6882/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher

3. Install Dependencies
poetry install

4. Run the Program
poetry run python main.py -q "covid vaccine" -f covid_results.csv

## Filtering Logic
To identify non-academic authors:
Affiliations not containing common academic keywords like:"University", "College", "Institute", "Hospital", "School", "Center", "Department".

If author affiliation includes keywords like: "Pharma", "Biotech", "Inc", "Ltd", "Corp", "Company" — it is considered pharmaceutical/biotech.

## Tools Used

- [Poetry](https://python-poetry.org/) for packaging
- [Requests](https://docs.python-requests.org/) for HTTP API calls

## conclusion

This project was developed as part of a home exercise assignment to demonstrate the ability to build a modular, command-line Python tool for fetching and filtering PubMed research papers. The task involved not only implementing functional logic using public APIs but also showcasing real-world development practices such as clean code structuring, packaging with Poetry, and documenting with clarity.

Through this assignment, I aimed to:
- Break down a complex API problem into simpler components.
- Leverage modern Python packaging and CLI design.
- Integrate basic NLP-inspired logic to identify relevant papers based on author affiliations.
- Produce a complete, beginner-friendly, and easily extensible solution.
