from src.graph import GraphRepository
import spacy
from src.kpe import KeyPhraseExtraction
import spacy
import pandas as pd
from spacy.lang.vi import Vietnamese
from pandas import DataFrame
from typing import List
from src.textrank.textrank import TextRank

nlp: spacy.Language = spacy.load("vi_core_news_lg")

# # def sample_nlp_paragraph_similarity():
# #     questions = nlp(
# #         "Hành vi gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn bị xử phạt vi phạm hành chính như thế nào?".lower()
# #     )
# #     answers = [
# #         "Hành động dẫn đến nạn giao thông và không dừng lại, không giữ nguyên hiện trạng, trốn đi và không đến trình báo với công an sẽ bị xử phạt dựa trên mức độ nghiêm trọng của người bị nạn",
# #         "Hành vi không chấp hành hiệu lệnh của đèn tín hiệu giao thông; không chấp hành hiệu lệnh, hướng dẫn của người điều khiển giao thông hoặc người kiểm soát giao thông bị xử phạt vi phạm hành chính như thế nào?",
# #         "Hành vi điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn vượt quá 80 miligam/100 mililít máu hoặc vượt quá 0,4 miligam/1 lít khí thở và không chấp hành yêu cầu kiểm tra về nồng độ cồn của người thi hành công vụ bị xử phạt vi phạm hành chính như thế nào?"
# #         "Bấm còi, rú ga liên tục; bấm còi trong thời gian từ 22 giờ đến 5 giờ, bấm còi hơi, sử dụng đèn chiếu xa trong đô thị và khu đông dân cư, trừ các xe được quyền ưu tiên đang đi làm nhiệm vụ theo quy định của Luật này",
# #         "Phạt tiền từ 800.000 đồng đến 1.000.000 đồng đối với người điều khiển xe bấm còi, rú ga liên tục; bấm còi hơi, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định (điểm b khoản 3 Điều 5). Vi phạm quy định trên mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng (điểm c khoản 11 Điều 5)",
# #         "Phạt tiền từ 100.000 đồng đến 200.000 đồng đối với người điều khiển xe bấm còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau, sử dụng đèn chiếu xa trong đô thị, khu đông dân cư, trừ các xe ưu tiên đang đi làm nhiệm vụ theo quy định (điểm n khoản 1 Điều 6). Vi phạm quy định trên mà gây tai nạn giao thông thì bị tước quyền sử dụng Giấy phép lái xe từ 02 tháng đến 04 tháng (điểm c khoản 10 Điều 6)."
# #         "Phạt tiền từ 3.000.000 đồng đến 5.000.000 đồng đối với người điều khiển xe dừng xe, đỗ xe trên đường cao tốc không đúng nơi quy định; không có báo hiệu để người lái xe khác biết khi buộc phải dừng xe, đỗ xe trên đường cao tốc không đúng nơi quy định (điểm a khoản 6 Điều 7)",
# #         "Phạt tiền từ 800.000 đồng đến 1.000.000 đồng đối với người Điều khiển xe thực hiện hành vi Lùi xe ở đường một chiều, đường có biển “Cấm đi ngược chiều”, khu vực cấm dừng, trên phần đường dành cho người đi bộ qua đường, nơi đường bộ giao nhau, nơi đường bộ giao nhau cùng mức với đường sắt, nơi tầm nhìn bị che khuất; lùi xe không quan sát hoặc không có tín hiệu báo trước",
# #         "Sử dụng đèn chiếu xa khi tránh xe đi ngược chiều (điểm e khoản 3 Điều 7)",
# #         "Tín hiệu vàng là phải dừng lại trước vạch dừng, trừ trường hợp đã đi quá vạch dừng thì được đi tiếp; trong trường hợp tín hiệu vàng nhấp nháy là được đi nhưng phải giảm tốc độ, chú ý quan sát, nhường đường cho người đi bộ qua đường",
# #         "Tại Điều 30, 31 Luật Giao thông đường bộ năm 2008 quy định: Với người điều khiển xe mô tô hai bánh, xe mô tô ba bánh, xe gắn máy, xe đạp không được sử dụng ô, điện thoại di động, thiết bị âm thanh, trừ thiết bị trợ thính.",
# #         "Việt nam vô địch",
# #     ]
# #     for i in range(len(answers)):
# #         print(i, questions.similarity(nlp(answers[i].lower())))


# path = "../../applications/law_modeling/resources/keyphrase-extraction.csv"


# def read_csv(file_path: str) -> DataFrame:
#     data = pd.read_csv(file_path)
#     return data


# data = read_csv(path)


# def split_keyphrase(row):
#     row = str(row).replace("-", "")

#     res = list(
#         filter(
#             lambda keyphrase: len(keyphrase) != 0,
#             list(map(lambda item: item.strip().lower(), row.split("\n"))),
#         )
#     )

#     return res


# def tagging_keyphrase(keyphrases: List[str]):
#     result = []
#     for keyphrase in keyphrases:
#         tag_result = []
#         doc = nlp(keyphrase)
#         for token in doc:
#             tag_result.append(token.text + "|" + token.tag_)
#         result.append(tag_result)
#     print(result)
#     return result


# raw_keyphrases = data["Keyphrase"].map(lambda row: split_keyphrase(row))
# data["Cleanse Keyphrases"] = raw_keyphrases

# keyphrases = [keyphrases for keyphrases in data["Cleanse Keyphrases"]]
# data["Keyphrases Tagging"] = [tagging_keyphrase(
#     keyphrase) for keyphrase in keyphrases]


graphRepository = GraphRepository("bolt://localhost:7687")

question = "Hành vi gây tai nạn giao thông không dừng lại, không giữ nguyên hiện trường, bỏ trốn không đến trình báo với cơ quan có thẩm quyền, không tham gia cấp cứu người bị nạn bị xử phạt vi phạm hành chính như thế nào?"
# print(KeyPhraseExtraction.yake(question))

KeyPhraseExtraction.textrank(nlp, question)

# KeyPhraseExtraction.phobert(question)

t = TextRank(question)
# Reference: https://github.com/lukhnos/textrank-study-python/blob/master/Key%20Phrase%20Extraction%20with%20Python.ipynb
print(t.keywords(10))
