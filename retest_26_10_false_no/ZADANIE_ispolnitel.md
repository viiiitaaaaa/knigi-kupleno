# Task for ANSWERER (Sonnet). Brief in English; write answers in Russian.
Goal: answer 15 situations as the skill `dogovorennosti` would answer Vita.
Read first: C:\Users\User\.claude\skills\dogovorennosti\SKILL.md and C:\Users\User\.claude\skills\dogovorennosti\references\retest_2310_pravila.md (rules 42-54; rule 50: before writing "the book has nothing on this", grep the book text by 2-3 keywords of the situation) and the card for the book in references\karty\<book>\ .
Inputs: C:\Users\User\knigi_kupleno\retest_26_10_false_no\<v|h|m|k|w>\vhod.md (G-1..G-3 each).
FORBIDDEN: do NOT open any klyuch.md or sud.md anywhere under knigi_kupleno (blind test). 
Books for grep: C:\Users\User\knigi_kupleno\txt13\ never_split_difference.txt (Voss), users_manual_brain1_full.txt/users_manual_brain2_full.txt (Hall), mom_test.txt, pitch_anything.txt (Klaff), million_dollar_consulting.txt (Weiss).
Answer format per situation as in C:\Users\User\knigi_kupleno\retest_23_10_fresh\w\otvety.md (look at its first 40 lines only): short plain-Russian answer, mark [Из книги X] with line number, mark own ideas "наше". Any claim "в книге нет" must be preceded by a grep you actually ran; write in the answer which words you grepped.
Output: <code>\otvety.md in each folder (writing only there). Max 80 tool steps; stuck = stop and report. Final reply in Russian: for each situation, one line "said 'нет в книге'? yes/no; grep words".
