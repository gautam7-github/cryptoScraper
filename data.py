# essential modules
import pandas as pd
import json
import lxml
def getData():
    dfs = pd.read_html("https://finance.yahoo.com/cryptocurrencies")
    df = dfs[0]
    df.set_index("Symbol", inplace=True)
    df = df.drop(["Volume in Currency (Since 0:00 UTC)", "Total Volume All Currencies (24Hr)",
                  "Circulating Supply", "52 Week Range", "1 Day Chart"], axis=1)
    js = df.to_json(orient='index')
    js = json.loads(js)
    return js




if __name__ == "__main__":
    print(getData())
