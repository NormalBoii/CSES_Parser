import argparse
from csesfetch.fetch_problem import fetch_problem


def run():
    parser = argparse.ArgumentParser(description="CSES Fetcher")
    parser.add_argument("target", help="Problem ID")

    args = parser.parse_args()

    fetch_problem(args.target)
