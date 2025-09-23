import sys
import os
from difflib import SequenceMatcher
import jieba
import numpy as np
import cProfile
import pstats

jieba.initialize()
COSINE_WEIGHT = 0.6
LCS_WEIGHT = 0.4
GLOBAL_STOPWORDS = {'，','。','！','？','、','的','了','我','是','今天'}

def read_file(file_path):
    # 读取文件内容
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}, 已跳过")
        return ""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().strip()

def preprocess(text, use_stopwords=True):
    # 文本预处理：小写 + 分词 + 去停用词
    text = text.lower()
    words = jieba.lcut(text)
    if use_stopwords:
        words = [w for w in words if w.strip() and w not in GLOBAL_STOPWORDS and not w.isdigit()]
    else:
        words = [w for w in words if w.strip() and not w.isdigit()]
    return words

def lcs_ratio(seq1, seq2):
    # 计算最长公共子序列相似度
    return SequenceMatcher(None, seq1, seq2).ratio()

def cosine_similarity(tokens1, tokens2):
    # 计算词频向量余弦相似度
    vocab = list(set(tokens1) | set(tokens2))
    vec1 = np.array([tokens1.count(w) for w in vocab])
    vec2 = np.array([tokens2.count(w) for w in vocab])
    norm = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    return np.dot(vec1, vec2)/norm if norm else 0.0

def hybrid_similarity(orig_text, plag_text):
    # 高精度混合相似度算法
    # 预处理
    orig_tokens_stop = preprocess(orig_text, use_stopwords=True)
    plag_tokens_stop = preprocess(plag_text, use_stopwords=True)

    if not orig_tokens_stop or not plag_tokens_stop:
        return 0.0

    # 计算 LCS（按去停用词分词）相似度
    lcs = lcs_ratio(orig_tokens_stop, plag_tokens_stop)

    # 计算 COSINE 相似度（按原文完整分词）
    orig_tokens_full = preprocess(orig_text, use_stopwords=False)
    plag_tokens_full = preprocess(plag_text, use_stopwords=False)
    cosine = cosine_similarity(orig_tokens_full, plag_tokens_full)

    # 加权融合
    similarity = COSINE_WEIGHT * cosine + LCS_WEIGHT * lcs
    return round(similarity * 100, 2)


def write_result(file_path, orig_path, plag_path, similarity):
    # 将重复率及文件信息写入文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"原文: {orig_path}\n")
        f.write(f"抄袭版: {plag_path}\n")
        f.write(f"重复率: {similarity}%\n")

def process_file_pair(orig_path, plag_path, ans_path):
    # 处理单组文件
    orig_text = read_file(orig_path)
    plag_text = read_file(plag_path)
    if not orig_text or not plag_text:
        print(f"跳过文件组: {orig_path} | {plag_path}")
        return

    similarity = hybrid_similarity(orig_text, plag_text)

    # 输出文件独立命名
    base_name = os.path.splitext(os.path.basename(plag_path))[0]
    if not os.path.exists(ans_path):
        os.makedirs(ans_path)
    ans_file = os.path.join(ans_path, f"{base_name}_ans.txt")

    write_result(ans_file, orig_path, plag_path, similarity)
    print(f"原文: {orig_path} | 抄袭版: {plag_path} | 重复率: {similarity}% | 输出: {ans_file}")


def main():
    if len(sys.argv) == 4:
        # 单组命令行计算
        orig_path, plag_path, ans_path = sys.argv[1], sys.argv[2], sys.argv[3]
        process_file_pair(orig_path, plag_path, ans_path)
    else:
        # 批量处理文件组
        file_list = [
            ("orig.txt", "orig_0.8_add.txt", "results"),
            ("orig.txt", "orig_0.8_del.txt", "results"),
            ("orig.txt", "orig_0.8_dis_1.txt", "results"),
            ("orig.txt", "orig_0.8_dis_10.txt", "results"),
            ("orig.txt", "orig_0.8_dis_15.txt", "results"),
        ]
        print("批量计算模式：")
        for orig_path, plag_path, ans_path in file_list:
            process_file_pair(orig_path, plag_path, ans_path)

# if __name__ == "__main__":
#     main()

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    main()

    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats(20)  # 输出前20个耗时函数