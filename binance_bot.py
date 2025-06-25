import os
import ccxt
import argparse


def main():
    parser = argparse.ArgumentParser(description="Ejemplo simple de conexión a Binance usando ccxt")
    parser.add_argument("--trade", action="store_true", help="Ejecuta una orden de prueba")
    args = parser.parse_args()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    if not api_key or not api_secret:
        print("Faltan credenciales. Define BINANCE_API_KEY y BINANCE_API_SECRET en variables de entorno.")
        return

    exchange = ccxt.binanceusdm({
        'apiKey': api_key,
        'secret': api_secret,
        'enableRateLimit': True,
        'options': {'defaultType': 'future'},
    })

    exchange.load_markets()

    balance = exchange.fetch_balance()
    usdc_total = balance.get('total', {}).get('USDC', 0.0)
    print(f"Balance total USDC: {usdc_total}")

    symbol = 'BTC/USDC'
    ohlcv = exchange.fetch_ohlcv(symbol, '1h', limit=1)
    last_close = ohlcv[-1][4]
    print(f"Precio actual {symbol}: {last_close}")

    if args.trade:
        amount = 0.001  # cantidad ejemplo
        print(f"Enviando orden de compra market de {amount} {symbol}")
        order = exchange.create_market_buy_order(symbol, amount)
        print("Orden ejecutada:", order)


if __name__ == "__main__":
    main()
