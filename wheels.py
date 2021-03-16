import csv
import io
import json
import pandas as pd
import plotly.graph_objects as go

from collections import defaultdict

def test():
    df = pd.read_csv (r'Needs.csv')
    df.to_json (r'Needs.json')
 
if __name__ == "__main__":
    test()
    #needs = load_csv_rows("NVC  - Needs.csv")
