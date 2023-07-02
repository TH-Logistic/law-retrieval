# Task Report

## Đã làm

- [x] Thu thập các câu hỏi và rút trích keyphrases bằng tàng các câu hỏi đó.
- Có 2 loại chính:
  - Xử phạt (phạt, mức phạt)
  - Quy định (nguyên tắc, hành vi)
- [x] Tìm hiểu về KGE và ampligraph.

=> Mục tiêu: Tìm ra phương pháp để so khớp 2 đồ thị keyphrase => từ đó đưa ra xếp hạng kết quả

> Ampligraph chủ yếu là đánh giá và xếp hạng dựa trên các triple đã có sẵn `(C,R,C)` Vì thế nó không phù hợp khi bài toán yêu cầu đưa ra kết quả điều luật phù hợp.

> Từ đó, việc sử dụng ampligraph hiện tại vẫn chưa mang lại hiệu quả. Khi so sánh hai graph với nhau thay vì là 2 node trong cùng 1 graph

## Đang làm

> Sử dụng thư viện spacy

- [x] Sử dụng thư viện spacy để so khớp đoạn văn bản với nhau, Từ đó đưa ra similarity giữa 2 câu. Độ chính xác tương đối.
- [x] Để sử dụng spacy hiệu quả và các thư viện graph khác, cần 1 graph database để truy vấn => `NEO4J (Hiện tại khoảng 591 Node & 844 Relations)`
- [ ] Tuy nhiên spacy chỉ hỗ trợ tiếng anh chứ chưa có tiếng việt
- [ ] Sử dụng pyvi để làm tiếng việt cho spacy. Hiện tại đã có thể so khớp 2 câu đơn giản với nhau. Tuy nhiên chưa ổn vì pretrained model là cho cho news thay vì law
- [ ] Có thể sẽ sử dụng model pretrain khác
  - [ ] Nếu không có model law đã pretraind => Tiến hành tự train
  - [ ] Nếu không ổn có thể sử dụng so khớp các từ trong đồ thị keyphrase theo cách anh Dương
- [ ] Từ keyphrase => Tiến hành gắn tag và phân loại từ keyphrase
  > Một số keyphrase là tổ hợp của nhiều loại từ và phủ định. Ví dụ: người - điều khiển,
  > không - chấp hành. Cần gộp các keyphrase này lại thay vì tách tiêng

## Mục tiêu hiện tại

- Phân tích tương đồng giữa các đồ thị keyphrase.

1. So sánh đồ thị Keyphrase của câu hỏi và đồ thị keyphrase của điều luật trong DB

- Hiện tại đang sử dụng phương pháp đánh trọng số
- Sử dụng networkX

2. Lưu giá trị/vector của điều luật trong DB và so sánh độ tương đồng giữa 2 vector

- Cần tìm ra phương pháp embedding các đồ thị keyphrase

## Sẽ làm

- [ ] Tiếp tục làm tiếp rút trích keyphrase lên các câu hỏi
- [ ] Tìm hiểu về 1 số KGE lib khác để so sánh các đồ thị keyphrase

---

<details>
<summary>Note</summary>
> Note: Trong keyphrase extraction.csv, từ câu 59->73 nằm ở trang [này](http://tuphapdienban.gov.vn/2021/09/22/hoi-dap-phap-luat-ve-luat-giao-thong-duong-bo/)
> Từ câu 74 -> 104 nằm ở trang [này](https://hoatieu.vn/tai-lieu/cau-hoi-tim-hieu-luat-giao-thong-duong-bo-127936)
</details>
