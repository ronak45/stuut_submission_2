from flask import Flask, jsonify, request
import yfinance as yf
from datetime import datetime, timedelta

app = Flask(__name__)




@app.route('/api/stock/<symbol>/historical')
def get_stock_historical(symbol):
    try:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        
        stock = yf.Ticker(symbol)
        hist = stock.history(start=start_date, end=end_date)
        
        historical_data = []
        for date, row in hist.iterrows():
            historical_data.append({
                'date': date.strftime('%Y-%m-%d'),
                'open': row['Open'],
                'high': row['High'],
                'low': row['Low'],
                'close': row['Close'],
                'volume': row['Volume']
            })
        
        print(f"Historical data for {symbol}:", historical_data)
        return jsonify(historical_data)
    except Exception as e:
        print(f"Error fetching historical data: {str(e)}")
        return jsonify({'error': str(e)}), 400


@app.route('/api/search')
def search_stocks():
    query = request.args.get('query', '')
    if not query:
        return jsonify([])
    
    try:
        # Use yfinance to search for stocks
        tickers = yf.Tickers(query)
        search_results = []
        
        for symbol, ticker in tickers.tickers.items():
            info = ticker.info
            search_results.append({
                'symbol': symbol,
                'name': info.get('longName', 'N/A'),
                'exchange': info.get('exchange', 'N/A')
            })
        
        return jsonify(search_results)
    except Exception as e:
        print(f"Error in search: {str(e)}")
        return jsonify([]), 500

@app.route('/api/stock/<symbol>')
def get_stock_details(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        
        # Format the stock details
        stock_details = {
            'symbol': info.get('symbol'),
            'name': info.get('longName'),
            'currentPrice': info.get('currentPrice'),
            'previousClose': info.get('previousClose'),
            'open': info.get('open'),
            'dayHigh': info.get('dayHigh'),
            'dayLow': info.get('dayLow'),
            'volume': info.get('volume'),
            'marketCap': info.get('marketCap'),
            'fiftyTwoWeekHigh': info.get('fiftyTwoWeekHigh'),
            'fiftyTwoWeekLow': info.get('fiftyTwoWeekLow')
        }
        
        return jsonify(stock_details)
    except Exception as e:
        print(f"Error in stock details: {str(e)}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)