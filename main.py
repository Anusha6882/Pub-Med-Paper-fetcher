import argparse
from pubmed_fetcher.fetcher import fetch_pubmed_data, save_to_csv

def main():
    # Define CLI arguments
    parser = argparse.ArgumentParser(description="Fetch non-academic research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results as CSV")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug output during fetch")

    args = parser.parse_args()

    # Fetch data from fetcher module
    papers = fetch_pubmed_data(args.query, debug=args.debug)

    if not papers:
        print("No relevant papers found.")
        return

    # Output to CSV file if specified, else print to terminal
    if args.file:
        save_to_csv(papers, args.file)
        print(f"Saved results to {args.file}")
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()