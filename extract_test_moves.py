import chess, re, chess.variant, json

from numpy import full


def get_all_fen_strings(filename):
    with open(filename, 'r') as file:
        content = file.read()

    full_fens = []
    partial_fens = []
    
    full_fen_matches=re.findall('''(?:(?:(?:[rnbqkpRNBQKP1-8]+\/){7})[rnbqkpRNBQKP1-8]+)\s(?:[b|w])\s(?:-|[K|Q|k|q]{1,4})\s(?:-|[a-h][1-8])\s(?:\d+\s\d+)''', content)

    for fen in list(full_fen_matches):
        print(fen)
        content = content.replace(fen, '')
        full_fens.append(fen)

    partial_fen_matches = re.findall('''(?:(?:(?:[rnbqkpRNBQKP1-8]+\/){7})[rnbqkpRNBQKP1-8]+)\s(?:[b|w])\s''', content)

    for fen in list(partial_fen_matches):
        print(fen)
        partial_fens.append(fen)

    print(len(full_fens) + len(partial_fens))
    return full_fens, partial_fens

def full_fen_from_partial_fen(fen):
    board = chess.variant.KingOfTheHillBoard(fen)
    return board.fen()

def get_moves_from_fen(fen):
    board = chess.variant.KingOfTheHillBoard(fen)
    return list(board.legal_moves)

def get_uci_moves_from_fen(fen):
    moves = get_moves_from_fen(fen)
    uci_moves = []
    for move in moves:
        uci_moves.append(move.uci())
    return uci_moves

def get_subsequent_boards_from_fen(fen):
    moves = get_moves_from_fen(fen)
    subs_boards = []
    for move in moves:
        board = chess.variant.KingOfTheHillBoard(fen)
        board.push(move)
        subs_boards.append(board.fen())
    return subs_boards

def write_json_to_file(dict, filename):
    with open(filename, 'w') as file:
        str = json.dumps(dict, indent=2)
        file.write(str)


full_fens, partial_fens = get_all_fen_strings('chess_wiki.txt')
test_data = {}

for fen in full_fens:
    test_data[fen] = {
        "n_legal_moves": len(get_moves_from_fen(fen)),
        "legal_moves": get_uci_moves_from_fen(fen),
        "subsequent_boards": get_subsequent_boards_from_fen(fen)
    }

write_json_to_file(test_data, 'out/test_data_only_full_fen_matches.json')
for fen in partial_fens:
    full_fen = full_fen_from_partial_fen(fen)
    test_data[full_fen] = {
        "n_legal_moves": len(get_moves_from_fen(fen)),
        "legal_moves": get_uci_moves_from_fen(fen),
        "subsequent_boards": get_subsequent_boards_from_fen(fen)
    }


write_json_to_file(test_data, 'out/test_data_all_fen_matches.json')