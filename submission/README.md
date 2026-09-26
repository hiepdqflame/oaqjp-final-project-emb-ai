# Huong dan nop 16 cau

Code da duoc chuan bi theo PDF. Cac file `.txt` la noi dung de copy/paste,
khong phai anh terminal. Cau 2 dung code buoc dau (tra ve response.text),
cac cau source con lai dung code ban cuoi.

## Danh sach theo thu tu

1. URL README: https://github.com/hiepdqflame/oaqjp-final-project-emb-ai/blob/main/README.md
2. Copy toan bo `2a_emotion_detection.txt`.
3. Copy `2b_application_creation.txt` sau khi chay Watson that thanh cong.
4. Copy toan bo `3a_output_formatting.txt`.
5. Copy `3b_formatted_output_test.txt` sau khi chay Watson that thanh cong.
6. URL package: https://github.com/hiepdqflame/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py
7. Copy `4b_packaging_test.txt` sau khi chay mau "I hate working long hours".
8. Copy toan bo `5a_unit_testing.txt`.
9. Copy `5b_unit_testing_result.txt` sau khi ca 5 test Watson that pass.
10. Copy toan bo `6a_server.txt`.
11. Upload `6b_deployment_test.png`: anh giao dien co ket qua Watson that.
12. Copy toan bo `7a_error_handling_function.txt`.
13. Copy toan bo `7b_error_handling_server.txt`.
14. Upload `7c_error_handling_interface.png`: anh gui input rong va hien loi.
15. Copy toan bo `8a_server_modified.txt`.
16. Copy toan bo `8b_static_code_analysis.txt` (Pylint 10/10).

## Ket qua chua the thu thap

Watson bi timeout tu may local. Cac cau 3, 5, 7, 9 va anh ket qua o cau 11 can
chay trong moi truong co ket noi den Watson. Khong dung `offline_contract_tests.txt`
thay cho cau 9: day la test logic co mock HTTP, khong phai 5 du doan that.

Trong terminal cua lab, sau khi dua project vao va cai dependencies:

```bash
python scripts/collect_evidence.py --live
python server.py
```

Mo cong 5000 bang cong cu Launch Application cua lab. Nhap
`I think I am having fun` va bam Run Sentiment Analysis; luu anh ket qua
voi ten `6b_deployment_test.png`. Xoa het noi dung, bam lai va luu anh loi
voi ten `7c_error_handling_interface.png`.

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
