# resumen
Mi Resumen

## Binance Bot

Este repositorio incluye un script opcional (`binance_bot.py`) para conectarse a Binance utilizando la biblioteca [ccxt](https://github.com/ccxt/ccxt).

### Requisitos
- Python 3
- `ccxt` (`pip install ccxt`)
- Variables de entorno `BINANCE_API_KEY` y `BINANCE_API_SECRET` con tus credenciales.

### Uso
```bash
export BINANCE_API_KEY="<tu_api_key>"
export BINANCE_API_SECRET="<tu_api_secret>"
python binance_bot.py           # Muestra balance y precio de BTC/USDC
python binance_bot.py --trade   # Ejecuta una orden de compra de ejemplo
```

Ejecutar operaciones reales implica riesgo financiero. Asegúrate de revisar y entender el código antes de habilitar la opción `--trade`.
