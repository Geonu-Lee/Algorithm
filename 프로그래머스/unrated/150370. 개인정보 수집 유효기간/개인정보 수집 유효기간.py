def solution(today, terms, privacies):
    def split_terms(terms):
        return terms.split()
    answer = []
    terms = list(map(split_terms, terms))
    terms = dict(terms)
    n_yy, n_mm, n_dd = list(map(int, today.split(".")))
    now_total = n_yy * 28 * 12 + n_mm * 28 + n_dd
    for index, p in enumerate(privacies):
        d, t_type = p.split()
        t = int(terms[t_type])
        yy, mm, dd = list(map(int, d.split(".")))
        total = yy * 28 * 12 + (mm + t) * 28 + dd
        if now_total >= total:
            answer.append(index + 1)
    return answer