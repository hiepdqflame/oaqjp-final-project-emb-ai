# Huong dan nop 16 cau

Da co du file cho 16 cau. Cac file `.txt` la noi dung de copy/paste,
khong phai anh terminal. Cau 2 dung code buoc dau (tra ve response.text),
cac cau source con lai dung code ban cuoi.

## Danh sach theo thu tu

1. URL README: https://github.com/hiepdqflame/oaqjp-final-project-emb-ai/blob/main/README.md
2. Copy toan bo `2a_emotion_detection.txt`.
3. Copy toan bo `2b_application_creation.txt`.
4. Copy toan bo `3a_output_formatting.txt`.
5. Copy toan bo `3b_formatted_output_test.txt`.
6. URL package: https://github.com/hiepdqflame/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py
7. Copy toan bo `4b_packaging_test.txt`.
8. Copy toan bo `5a_unit_testing.txt`.
9. Copy toan bo `5b_unit_testing_result.txt` (5 test Watson that deu pass).
10. Copy toan bo `6a_server.txt`.
11. Upload `6b_deployment_test.png`: anh giao dien co ket qua Watson that.
12. Copy toan bo `7a_error_handling_function.txt`.
13. Copy toan bo `7b_error_handling_server.txt`.
14. Upload `7c_error_handling_interface.png`: anh gui input rong va hien loi.
15. Copy toan bo `8a_server_modified.txt`.
16. Copy toan bo `8b_static_code_analysis.txt` (Pylint 10/10).

## Ket qua da xac minh ngay 2026-09-26

- Log cac cau 3, 5, 7, 9 va 16 duoc thu truc tiep trong Skills Network Cloud IDE.
- Ca 5 test goi API Watson that deu pass; Pylint cua `server.py` dat 10/10.
- Hai anh PNG duoc chup truc tiep tren Chrome tu ung dung Flask trong lab.
- Cau mau `I think I am having fun` tra ve `joy` voi diem 0.876574.
- Input rong hien dung `Invalid text! Please try again!`.
- `offline_contract_tests.txt` la 11 test logic bo sung, khong dung thay cau 9.

Mo trang Mark, dien tung cau theo danh sach tren va upload hai anh PNG vao
cau 11 va 14. Kiem tra lai noi dung truoc khi bam Submit assignment.

## Thu thap lai bang chung khi can

Trong terminal cua lab, sau khi dua project vao va cai dependencies:

```bash
python scripts/collect_evidence.py --live
python server.py
```

Mo cong 5000 bang cong cu Launch Application cua lab. Nhap
`I think I am having fun` va bam Run Sentiment Analysis; luu anh ket qua
voi ten `6b_deployment_test.png`. Xoa het noi dung, bam lai va luu anh loi
voi ten `7c_error_handling_interface.png`.

Lab chan `cdn.playwright.dev`, vi vay khong can cai Playwright trong lab.
Dung chuc nang chup anh cua trinh duyet de luu hai anh.

## Chay project trong Cloud IDE

Repository cua ban:
https://github.com/hiepdqflame/oaqjp-final-project-emb-ai

```bash
git clone https://github.com/hiepdqflame/oaqjp-final-project-emb-ai.git final_project
cd final_project
python3 -m pip install -r requirements-dev.txt
python3 scripts/collect_evidence.py --live
python3 server.py
```

Neu thu muc `final_project` da ton tai, dung terminal trong thu muc project
hien co thay vi clone de len file cua ban. Khong push `.venv`, PDF de bai,
hoac thu muc `tmp`.
