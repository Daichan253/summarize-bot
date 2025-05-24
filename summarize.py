from janome.tokenizer import Tokenizer

def extract_keywords(text, top_n=5):
    tokenizer = Tokenizer()
    words = []
    for token in tokenizer.tokenize(text):
        part = token.part_of_speech.split(',')[0]
        if part in ['名詞', '動詞', '形容詞']:
            words.append(token.base_form)
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [w for w, _ in sorted_words[:top_n]]

def extract_summary(text, top_n=3):
    sentences = text.split('。')
    keywords = extract_keywords(text)
    scored = []
    for s in sentences:
        score = sum([s.count(k) for k in keywords])
        scored.append((score, s.strip()))
    top = sorted(scored, reverse=True)[:top_n]
    return '。'.join([s for _, s in top]) + '。'

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        text = f.read()
    summary = extract_summary(text)
    print("\n▼要約：")
    print(summary)