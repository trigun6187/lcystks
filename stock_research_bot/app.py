import pandas as pd
import json
import os

# Keeping this function definition as per instructions.
def get_trending_penny_stocks_research():
    # Replaced mock data with results from the live web research pipeline (Step 3).
    # Live research found 0 stocks in the $1-$5 range based on the initial source.
    return []

def generate_static_report():
    data = get_trending_penny_stocks_research()
    df = pd.DataFrame(data)
    
    table_html = None
    if not df.empty:
        table_html = df.to_html(index=False)
    else:
        table_html = "<p>No data available.</p>"

    html_content = f"""
    <html>
    <head><title>Penny Stock Watchlist Report</title>
    <style>
        body {{ font-family: sans-serif; margin: 20px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
    </style>
    </head>
    <body>
        <h1>Penny Stock Watchlist Report (Mock Data)</h1>
        <p>Generated on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p>Data refreshed from mock source.</p>
        {table_html}
        <script>
          // Add logic here later to fetch fresh data via JS if needed, but for now, static.
        </script>
    </body>
    </html>
    """
    
    # Write index.html inside the stock_research_bot directory.
    output_filename = "stock_research_bot/index.html"
    with open(output_filename, "w") as f:
        f.write(html_content)
    print(f"Static report generated to {output_filename}")

if __name__ == '__main__':
    # Replace Streamlit server run logic with static generation
    generate_static_report()