def evaluate(target, guess):
    result = ["gray"] * len(guess)
    left = {}
    for i, ch in enumerate(guess):
        if ch == target[i]:
            result[i] = "green"
        else:
            left[target[i]] = left.get(target[i], 0) + 1
    for i, ch in enumerate(guess):
        if result[i] == "green":
            continue
        if left.get(ch, 0) > 0:
            result[i] = "yellow"
            left[ch] -= 1
    return result