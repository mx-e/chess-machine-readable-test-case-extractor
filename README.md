# Extractor for chess test cases from any text

This extractor extracts FEN strings from chess documentation text and generates machine readble test case descriptions in json format as such:
- Regex search for fen strings in text
- Generating boards from fen (with [chess-python library](https://github.com/niklasf/python-chess))
- Generating legal moves from boards (with [chess-python library](https://github.com/niklasf/python-chess))
- Generating subsequent boards from moves (with [chess-python library](https://github.com/niklasf/python-chess))

The extractor reads full FEN strings and partial FEN strings (only the board and to_move parts) and generates two output files. One only from fully readable FEN strings and one from all matches.
