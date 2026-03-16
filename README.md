# Modelace průniku 2 kružnic

 Krátký přehled projektu pro cvičení 6.

## Co skript dělá

 - Přijímá dvě kružnice s danýmými souřadnicemi středu x,y a poloměrem
 - Určí počet průniků obou kružnic
 - Podá výstup zdali mají průnik a vykreslí jejich vzájemnou polohu na grafu

## Dependencies

```powershell
uv add matplotlib pytest
```

## Spuštění
```powershell
uv run python \\src\\circle\_intersection.py
```

## Spuštění testů
```powershell
uv run pytest tests/test\_circle\_stats.py
```
