from collections import Counter, defaultdict
from math import log2


class Solution:
    def compute_tf_idf(self, docs: list[str]) -> list[dict[str, float]]:
        tf_idf_list = []
        token_docs_count = defaultdict(int)

        for doc in docs:
            doc_tokens = doc.lower().split()
            if not doc_tokens:  # защита от пустого документа
                tf_idf_list.append({})
                continue

            doc_counter = Counter(doc_tokens)

            for token in doc_counter:
                doc_counter[token] /= len(doc_tokens)
                token_docs_count[token] += 1

            tf_idf_list.append(doc_counter)

        for doc in tf_idf_list:
            for token in doc:
                doc[token] *= log2((len(docs) + 1) / (token_docs_count[token] + 1)) + 1

        return tf_idf_list
