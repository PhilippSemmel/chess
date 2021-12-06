for (int new_pos = this._pos + diff; new_pos < this._pos + ((m + 1) * diff); new_pos += diff)

for (int i = 0; i < min(diffs.length, max_moves.length); i++) {
    diff = diffs[i];
    m = max_moves[i];
    ...
}