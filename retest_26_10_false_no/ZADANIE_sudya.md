# Task for JUDGE (Sonnet). Brief in English; write in Russian.
Goal: judge 15 answers. Per folder C:\Users\User\knigi_kupleno\retest_26_10_false_no\<v|h|m|k|w>\ : read vhod.md, klyuch.md (truth), otvety.md (answers).
Format of verdicts: see C:\Users\User\knigi_kupleno\retest_23_10_fresh\w\sud.md (first 12 lines only).
Rules: PASS / FAIL per G-situation, with reason citing otvety line and book line. Re-verify every disputed citation yourself with sed/grep on the book txt in C:\Users\User\knigi_kupleno\txt13\ (never trust the key blindly; the key writer's note: Klaff old keys used other line numbers).
Special column "ложное нет": yes/no — did the answer wrongly say "в книге нет" about something the book covers (check each "нет"/"не из книги" in otvety against book by grep)? Also flag invented facts or fake quotes.
Output: sud.md in each folder, plus C:\Users\User\knigi_kupleno\retest_26_10_false_no\SVODKA.md: table of 15 rows (book, G, PASS/FAIL, ложное нет yes/no, one-line reason) and totals X of 15, ложных «нет» N. Max 70 tool steps; stuck = stop and report. Final reply in Russian: the totals and the FAIL lines.
