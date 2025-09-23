# import unittest
# import os
# from unittest.mock import patch
# from main import (
#     read_file, preprocess, lcs_ratio, cosine_similarity,
#     hybrid_similarity, write_result,process_file_pair
# )
#
# class TestFileExceptions(unittest.TestCase):
#
#     def test_write_result_ioerror(self):
#         """测试 write_result 在 IOError 情况下的处理"""
#         orig_path = "orig.txt"
#         plag_path = "plag.txt"
#         ans_path = "results"
#
#         # 模拟 open 抛出 IOError
#         with patch("builtins.open", side_effect=IOError):
#             # 调用 process_file_pair，观察是否能捕获异常或不崩溃
#             try:
#                 process_file_pair(orig_path, plag_path, ans_path)
#             except IOError:
#                 self.fail("process_file_pair 不应抛出 IOError")
#
# class TestTextSimilarity(unittest.TestCase):
#
#     def setUp(self):
#         """在测试前创建临时文件"""
#         with open("temp_orig.txt", "w", encoding="utf-8") as f:
#             f.write("今天我去了图书馆，看了一本书。")
#         with open("temp_plag.txt", "w", encoding="utf-8") as f:
#             f.write("我今天去图书馆读书了。")
#
#     def tearDown(self):
#         """测试结束后清理临时文件"""
#         if os.path.exists("temp_orig.txt"):
#             os.remove("temp_orig.txt")
#         if os.path.exists("temp_plag.txt"):
#             os.remove("temp_plag.txt")
#         if os.path.exists("temp_result.txt"):
#             os.remove("temp_result.txt")
#
#     def test_read_file_exists(self):
#         """测试文件读取：存在文件"""
#         content = read_file("temp_orig.txt")
#         self.assertIn("图书馆", content)
#
#     def test_read_file_not_exists(self):
#         """测试文件读取：不存在文件"""
#         content = read_file("not_exist.txt")
#         self.assertEqual(content, "")
#
#     def test_preprocess_with_stopwords(self):
#         """测试分词（含停用词过滤）"""
#         tokens = preprocess("今天是一个好日子。", use_stopwords=True)
#         self.assertNotIn("今天", tokens)  # "今天" 在停用词表里
#
#     def test_preprocess_without_stopwords(self):
#         """测试分词（不去停用词）"""
#         tokens = preprocess("今天是一个好日子。", use_stopwords=False)
#         self.assertIn("今天", tokens)
#
#     def test_lcs_ratio_similarity(self):
#         """测试 LCS 相似度"""
#         ratio = lcs_ratio(["今天", "图书馆"], ["今天", "书店"])
#         self.assertGreaterEqual(ratio, 0.3)
#
#     def test_cosine_similarity_basic(self):
#         """测试余弦相似度"""
#         sim = cosine_similarity(["图书馆", "书"], ["图书馆", "阅读"])
#         self.assertGreater(sim, 0.0)
#
#     def test_hybrid_similarity_normal(self):
#         """测试混合相似度"""
#         sim = hybrid_similarity("我去图书馆学习", "今天我去图书馆看书")
#         self.assertGreater(sim, 30.0)  # 应该有一定相似度
#
#     def test_hybrid_similarity_empty(self):
#         """测试混合相似度：空文本"""
#         sim = hybrid_similarity("", "")
#         self.assertEqual(sim, 0.0)
#
#     def test_write_result_file(self):
#         """测试结果写入"""
#         write_result("temp_result.txt", "temp_orig.txt", "temp_plag.txt", 85.5)
#         self.assertTrue(os.path.exists("temp_result.txt"))
#         with open("temp_result.txt", "r", encoding="utf-8") as f:
#             content = f.read()
#         self.assertIn("85.5%", content)
#
#     def test_hybrid_similarity_identical(self):
#         """测试混合相似度：相同文本"""
#         sim = hybrid_similarity("测试文本", "测试文本")
#         self.assertEqual(sim, 100.0)
#
#
# if __name__ == "__main__":
#     unittest.main()

















#
# import unittest
# import os
# from unittest.mock import patch
# from main import (
#     read_file, preprocess, lcs_ratio, cosine_similarity,
#     hybrid_similarity, write_result, process_file_pair
# )
#
#
#
# # class TestFileExceptions(unittest.TestCase):
# #     def test_write_result_ioerror(self):
# #         """测试 write_result 在 IOError 情况下的处理"""
# #         orig_path = "orig.txt"
# #         plag_path = "plag.txt"
# #         ans_path = "results"
# #
# #         # 模拟 open 抛出 IOError，但 process_file_pair 不应崩溃
# #         with patch("builtins.open", side_effect=IOError):
# #             try:
# #                 process_file_pair(orig_path, plag_path, ans_path)
# #             except IOError:
# #                 self.fail("process_file_pair 不应抛出 IOError")
#
#
#
#
#
#
#
#
#
# class TestFileExceptions(unittest.TestCase):
#
#     def test_write_result_ioerror(self):
#         """测试 write_result 在 IOError 情况下的处理"""
#         orig_path = "temp_orig.txt"
#         plag_path = "temp_plag.txt"
#         ans_path = "results"
#
#         # 先创建临时原文和抄袭文件
#         with open(orig_path, "w", encoding="utf-8") as f:
#             f.write("测试内容")
#         with open(plag_path, "w", encoding="utf-8") as f:
#             f.write("抄袭内容")
#
#         # 模拟 write_result 抛出 IOError
#         with patch("main.write_result", side_effect=IOError):
#             try:
#                 process_file_pair(orig_path, plag_path, ans_path)
#             except IOError:
#                 self.fail("process_file_pair 不应抛出 IOError")
#
#         # 清理临时文件
#         if os.path.exists(orig_path):
#             os.remove(orig_path)
#         if os.path.exists(plag_path):
#             os.remove(plag_path)
#
#
# class TestTextSimilarity(unittest.TestCase):
#
#     def setUp(self):
#         """在测试前创建临时文件"""
#         with open("temp_orig.txt", "w", encoding="utf-8") as f:
#             f.write("今天我去了图书馆，看了一本书。")
#         with open("temp_plag.txt", "w", encoding="utf-8") as f:
#             f.write("我今天去图书馆读书了。")
#
#     def tearDown(self):
#         """测试结束后清理临时文件"""
#         for file in ["temp_orig.txt", "temp_plag.txt", "temp_result.txt"]:
#             if os.path.exists(file):
#                 os.remove(file)
#
#     def test_read_file_exists(self):
#         """测试文件读取：存在文件"""
#         content = read_file("temp_orig.txt")
#         self.assertIn("图书馆", content)
#
#     def test_read_file_not_exists(self):
#         """测试文件读取：不存在文件"""
#         content = read_file("not_exist.txt")
#         self.assertEqual(content, "")
#
#     def test_preprocess_with_stopwords(self):
#         """测试分词（含停用词过滤）"""
#         tokens = preprocess("今天是一个好日子。", use_stopwords=True)
#         self.assertNotIn("今天", tokens)  # "今天" 在停用词表里
#
#     def test_preprocess_without_stopwords(self):
#         """测试分词（不去停用词）"""
#         tokens = preprocess("今天是一个好日子。", use_stopwords=False)
#         self.assertIn("今天", tokens)
#
#     def test_lcs_ratio_similarity(self):
#         """测试 LCS 相似度"""
#         ratio = lcs_ratio(["今天", "图书馆"], ["今天", "书店"])
#         self.assertGreaterEqual(ratio, 0.3)
#
#     def test_cosine_similarity_basic(self):
#         """测试余弦相似度"""
#         sim = cosine_similarity(["图书馆", "书"], ["图书馆", "阅读"])
#         self.assertGreater(sim, 0.0)
#
#     def test_hybrid_similarity_normal(self):
#         """测试混合相似度"""
#         sim = hybrid_similarity("我去图书馆学习", "今天我去图书馆看书")
#         self.assertGreater(sim, 30.0)  # 应该有一定相似度
#
#     def test_hybrid_similarity_empty(self):
#         """测试混合相似度：空文本"""
#         sim = hybrid_similarity("", "")
#         self.assertEqual(sim, 0.0)
#
#     def test_write_result_file(self):
#         """测试结果写入"""
#         write_result("temp_result.txt", "temp_orig.txt", "temp_plag.txt", 85.5)
#         self.assertTrue(os.path.exists("temp_result.txt"))
#         with open("temp_result.txt", "r", encoding="utf-8") as f:
#             content = f.read()
#         self.assertIn("85.5%", content)
#
#     def test_hybrid_similarity_identical(self):
#         """测试混合相似度：相同文本"""
#         sim = hybrid_similarity("测试文本", "测试文本")
#         self.assertEqual(sim, 100.0)
#
# if __name__ == "__main__":
#     unittest.main()




































































#
# import unittest
# import os
# import sys
# from unittest.mock import patch
# from main import (
#     read_file, preprocess, lcs_ratio, cosine_similarity,
#     hybrid_similarity, write_result, process_file_pair, main, tokenize
# )
#
# class TestFileExceptions(unittest.TestCase):
#     from unittest.mock import patch, mock_open
#
#     def test_process_file_pair_with_mock(self):
#         mock_orig = "原文内容"
#         mock_plag = "抄袭内容"
#         with patch("builtins.open", mock_open(read_data=mock_orig)) as m_open:
#             with patch("main.write_result") as mock_write:
#                 process_file_pair("orig.txt", "plag.txt", "results")
#                 mock_write.assert_called_once()
#
#     def setUp(self):
#         # 创建临时原文和抄袭文件
#         with open("temp_orig.txt", "w", encoding="utf-8") as f:
#             f.write("今天我去了图书馆，看了一本书。")
#         with open("temp_plag.txt", "w", encoding="utf-8") as f:
#             f.write("我今天去图书馆读书了。")
#
#     def tearDown(self):
#         # 清理临时文件
#         for file in ["temp_orig.txt", "temp_plag.txt", "temp_result.txt"]:
#             if os.path.exists(file):
#                 os.remove(file)
#
#     def test_write_result_ioerror(self):
#         """测试 write_result 异常分支"""
#         with patch("main.write_result", side_effect=IOError):
#             try:
#                 process_file_pair("temp_orig.txt", "temp_plag.txt", "results")
#             except IOError:
#                 self.fail("process_file_pair 不应抛出 IOError")
#
#     def test_read_file_not_exist(self):
#         """测试 read_file 文件不存在分支"""
#         content = read_file("not_exist.txt")
#         self.assertEqual(content, "")
#
#     def test_process_file_pair_with_not_exist_file(self):
#         """测试 process_file_pair 跳过不存在文件"""
#         # 原文不存在
#         process_file_pair("not_exist.txt", "temp_plag.txt", "results")
#         # 抄袭文件不存在
#         process_file_pair("temp_orig.txt", "not_exist.txt", "results")
#
# class TestTextSimilarity(unittest.TestCase):
#     def test_tokenize_empty_text(self):
#         """测试 tokenize 空文本"""
#         no_stop, full = tokenize("")
#         self.assertEqual(no_stop, [])
#         self.assertEqual(full, [])
#
#     def test_hybrid_similarity_empty_text(self):
#         """测试 hybrid_similarity 空文本"""
#         sim = hybrid_similarity("", "")
#         self.assertEqual(sim, 0.0)
#
# class TestMainFunction(unittest.TestCase):
#     # def test_main_single_arg(self):
#     #     """测试 main 单组参数分支"""
#     #     sys.argv = ["main.py", "temp_orig.txt", "temp_plag.txt", "results"]
#     #     # patch write_result 避免文件写入
#     #     with patch("main.write_result") as mock_write:
#     #         main()
#     #         self.assertTrue(mock_write.called)
#
#     # def test_main_batch_branch(self):
#     #     """测试 main 批量分支"""
#     #     sys.argv = ["main.py"]  # 无额外参数触发批量
#     #     with patch("main.process_file_pair") as mock_process:
#     #         main()
#     #         self.assertTrue(mock_process.called)
#     #         self.assertEqual(mock_process.call_count, 6)  # 文件列表长度
#
#     def test_main_single_branch(self):
#         """测试 main 单文件分支"""
#         sys.argv = ["main.py", "orig.txt", "plag.txt", "results"]
#         with patch("main.process_file_pair") as mock_process:
#             main()
#             mock_process.assert_called_once_with("orig.txt", "plag.txt", "results")
#
#     def test_main_batch_branch(self):
#         """测试 main 批量分支，不访问真实文件"""
#         sys.argv = ["main.py"]  # 无参数触发批量
#         with patch("main.process_file_pair") as mock_process, \
#                 patch("builtins.print") as mock_print:
#             main()
#             # 文件列表长度是6
#             self.assertEqual(mock_process.call_count, 6)
#             # 确保打印了“批量计算模式”
#             printed = [args[0] for args, _ in mock_print.call_args_list]
#             self.assertTrue(any("批量计算模式" in p for p in printed))
#
#
# if __name__ == "__main__":
#     unittest.main()
#


























































































#
# import unittest
# import os
# from unittest.mock import patch, mock_open
# import sys
# from main import (
#     read_file, preprocess, lcs_ratio, cosine_similarity,
#     hybrid_similarity, write_result, process_file_pair, main
# )
#
# class TestFileExceptions(unittest.TestCase):
#     """测试文件异常处理"""
#
#     def test_write_result_ioerror(self):
#         """模拟 write_result 抛出 IOError，但 process_file_pair 不应崩溃"""
#         with patch("builtins.open", mock_open()) as m_open:
#             with patch("main.write_result", side_effect=IOError):
#                 try:
#                     process_file_pair("orig.txt", "plag.txt", "results")
#                 except IOError:
#                     self.fail("process_file_pair 不应抛出 IOError")
#
# class TestTextSimilarity(unittest.TestCase):
#     """测试文本处理及相似度函数"""
#
#     def setUp(self):
#         """每个测试前创建临时文件"""
#         self.orig_file = "temp_orig.txt"
#         self.plag_file = "temp_plag.txt"
#         with open(self.orig_file, "w", encoding="utf-8") as f:
#             f.write("今天我去了图书馆，看了一本书。")
#         with open(self.plag_file, "w", encoding="utf-8") as f:
#             f.write("我今天去图书馆读书了。")
#
#     def tearDown(self):
#         """每个测试后删除临时文件"""
#         for file in [self.orig_file, self.plag_file, "temp_result.txt"]:
#             if os.path.exists(file):
#                 os.remove(file)
#
#     def test_read_file_exists(self):
#         """测试文件读取：存在文件"""
#         content = read_file(self.orig_file)
#         self.assertIn("图书馆", content)
#
#     def test_read_file_exists(self):
#         """测试文件读取：存在文件"""
#         m = mock_open(read_data="今天我去了图书馆")
#         with patch("builtins.open", m):
#             content = read_file("temp.txt")
#             self.assertIn("图书馆", content)
#
#     def test_read_file_not_exists(self):
#         """测试文件读取：不存在文件"""
#         with patch("os.path.exists", return_value=False):
#             content = read_file("not_exist.txt")
#             self.assertEqual(content, "")
#
#     def test_preprocess_with_stopwords(self):
#         tokens = preprocess("今天是一个好日子。", use_stopwords=True)
#         self.assertNotIn("今天", tokens)
#
#     def test_preprocess_without_stopwords(self):
#         tokens = preprocess("今天是一个好日子。", use_stopwords=False)
#         self.assertIn("今天", tokens)
#
#     def test_lcs_ratio_similarity(self):
#         ratio = lcs_ratio(["今天", "图书馆"], ["今天", "书店"])
#         self.assertGreaterEqual(ratio, 0.3)
#
#     def test_cosine_similarity_basic(self):
#         sim = cosine_similarity(["图书馆", "书"], ["图书馆", "阅读"])
#         self.assertGreater(sim, 0.0)
#
#     def test_hybrid_similarity_normal(self):
#         sim = hybrid_similarity("我去图书馆学习", "今天我去图书馆看书")
#         self.assertGreater(sim, 30.0)
#
#     def test_hybrid_similarity_empty(self):
#         sim = hybrid_similarity("", "")
#         self.assertEqual(sim, 0.0)
#
#     def test_hybrid_similarity_identical(self):
#         sim = hybrid_similarity("测试文本", "测试文本")
#         self.assertEqual(sim, 100.0)
#
# class TestProcessFilePair(unittest.TestCase):
#     """测试 process_file_pair 函数"""
#
#     @patch("main.write_result")
#     @patch("main.read_file", return_value="测试内容")
#     def test_process_file_pair_basic(self, mock_read, mock_write):
#         process_file_pair("orig.txt", "plag.txt", "results")
#         mock_read.assert_any_call("orig.txt")
#         mock_read.assert_any_call("plag.txt")
#         mock_write.assert_called_once()
#
#     @patch("main.read_file", return_value="")
#     @patch("main.write_result")
#     def test_process_file_pair_empty_file(self, mock_write, mock_read):
#         process_file_pair("orig.txt", "plag.txt", "results")
#         mock_write.assert_not_called()  # 空文件不会写入结果
#
# class TestMainFunction(unittest.TestCase):
#     """测试 main() 两条分支"""
#
#     @patch("main.process_file_pair")
#     def test_main_single_file_branch(self, mock_process):
#         test_args = ["main.py", "orig.txt", "plag.txt", "results"]
#         with patch.object(sys, "argv", test_args):
#             main()
#         mock_process.assert_called_once()
#
#     @patch("main.process_file_pair")
#     def test_main_batch_branch(self, mock_process):
#         test_args = ["main.py"]
#         with patch.object(sys, "argv", test_args):
#             main()
#         # 批量处理列表长度为 6
#         self.assertEqual(mock_process.call_count, 6)
#
# if __name__ == "__main__":
#     unittest.main()




















































































import unittest
import os
from unittest.mock import patch, mock_open
import sys
from main import (
    read_file, preprocess, lcs_ratio, cosine_similarity,
    hybrid_similarity, write_result, process_file_pair, main
)

class TestFileExceptions(unittest.TestCase):
    """测试文件异常处理"""

    def test_write_result_ioerror(self):
        """模拟 write_result 抛出 IOError，但 process_file_pair 不应崩溃"""
        with patch("builtins.open", mock_open()) as m_open:
            with patch("main.write_result", side_effect=IOError):
                try:
                    process_file_pair("orig.txt", "plag.txt", "results")
                except IOError:
                    self.fail("process_file_pair 不应抛出 IOError")


class TestTextSimilarity(unittest.TestCase):
    """测试文本处理及相似度函数"""

    def setUp(self):
        """每个测试前创建临时文件"""
        self.orig_file = "temp_orig.txt"
        self.plag_file = "temp_plag.txt"
        with open(self.orig_file, "w", encoding="utf-8") as f:
            f.write("今天我去了图书馆，看了一本书。")
        with open(self.plag_file, "w", encoding="utf-8") as f:
            f.write("我今天去图书馆读书了。")

    def tearDown(self):
        """每个测试后删除临时文件"""
        for file in [self.orig_file, self.plag_file, "temp_result.txt"]:
            if os.path.exists(file):
                os.remove(file)

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data="今天我去了图书馆")
    def test_read_file_exists(self, mock_file, mock_exists):
        """测试文件读取：存在文件"""
        content = read_file("temp.txt")
        self.assertIn("图书馆", content)
    # @patch("builtins.open", new_callable=mock_open, read_data="今天我去了图书馆")
    # def test_read_file_exists(self, mock_file):
    #     """测试文件读取：存在文件"""
    #     content = read_file("temp.txt")
    #     self.assertIn("图书馆", content)

    @patch("os.path.exists", return_value=False)
    def test_read_file_not_exists(self, mock_exists):
        """测试文件读取：不存在文件"""
        content = read_file("not_exist.txt")
        self.assertEqual(content, "")

    def test_preprocess_with_stopwords(self):
        tokens = preprocess("今天是一个好日子。", use_stopwords=True)
        self.assertNotIn("今天", tokens)

    def test_preprocess_without_stopwords(self):
        tokens = preprocess("今天是一个好日子。", use_stopwords=False)
        self.assertIn("今天", tokens)

    def test_lcs_ratio_similarity(self):
        ratio = lcs_ratio(["今天", "图书馆"], ["今天", "书店"])
        self.assertGreaterEqual(ratio, 0.3)

    def test_cosine_similarity_basic(self):
        sim = cosine_similarity(["图书馆", "书"], ["图书馆", "阅读"])
        self.assertGreater(sim, 0.0)

    def test_hybrid_similarity_normal(self):
        sim = hybrid_similarity("我去图书馆学习", "今天我去图书馆看书")
        self.assertGreater(sim, 30.0)

    def test_hybrid_similarity_empty(self):
        sim = hybrid_similarity("", "")
        self.assertEqual(sim, 0.0)

    def test_hybrid_similarity_identical(self):
        sim = hybrid_similarity("测试文本", "测试文本")
        self.assertEqual(sim, 100.0)


class TestProcessFilePair(unittest.TestCase):
    """测试 process_file_pair 函数"""

    @patch("main.write_result")
    @patch("main.read_file", return_value="测试内容")
    def test_process_file_pair_basic(self, mock_read, mock_write):
        process_file_pair("orig.txt", "plag.txt", "results")
        mock_read.assert_any_call("orig.txt")
        mock_read.assert_any_call("plag.txt")
        mock_write.assert_called_once()

    @patch("main.read_file", return_value="")
    @patch("main.write_result")
    def test_process_file_pair_empty_file(self, mock_write, mock_read):
        process_file_pair("orig.txt", "plag.txt", "results")
        mock_write.assert_not_called()  # 空文件不会写入结果


class TestMainFunction(unittest.TestCase):
    """测试 main() 两条分支"""

    @patch("main.process_file_pair")
    def test_main_single_file_branch(self, mock_process):
        test_args = ["main.py", "orig.txt", "plag.txt", "results"]
        with patch.object(sys, "argv", test_args):
            main()
        mock_process.assert_called_once()

    @patch("main.process_file_pair")
    def test_main_batch_branch(self, mock_process):
        test_args = ["main.py"]
        with patch.object(sys, "argv", test_args):
            main()
        # 批量处理列表长度为 6
        self.assertEqual(mock_process.call_count, 6)


if __name__ == "__main__":
    unittest.main()
