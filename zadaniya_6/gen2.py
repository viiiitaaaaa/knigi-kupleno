import os,re
exec(open("gen.py",encoding="utf-8").read().split("tasks=[")[0])
def F(p,n): return [G+"%s_%02d.md"%(p,i) for i in range(1,n+1)]
tasks=[
("lean","Croll, Yoskovitz «Lean Analytics»",""," как выбрать ОДНУ главную метрику, стадии стартапа, модели бизнеса, пороги «хорошо/плохо», как мерить и решать по цифрам.",F("lean_analytics",17),"lean-analytics/SKILL.md",fm("lean-analytics","«какую метрику мерить», «главная метрика», «lean analytics», «воронка», «стадия бизнеса», «хорошая конверсия», «тщеславные метрики»"),350),
("minto","Minto «The Pyramid Principle»",""," как строить текст и доклад пирамидой: вывод первым, группы аргументов, порядок, вступление (ситуация–осложнение–вопрос), проверка логики.",F("minto_pyramid",12),"minto-pyramid/SKILL.md",fm("minto-pyramid","«принцип пирамиды», «структура отчёта», «вывод первым», «как изложить мысль», «ситуация осложнение вопрос», «структурировать текст»"),300),
("story","Knaflic «Storytelling with Data: Let's Practice / Makeovers»",""," как делать понятные графики и рассказ по данным: выбор вида графика, убрать лишнее, акцент, подписи, история.",F("storytelling_data_makeovers",10),"storytelling-with-data/SKILL.md",fm("storytelling-with-data","«график», «диаграмма», «рассказ по данным», «убрать лишнее с графика», «акцент на графике», «storytelling with data»"),300),
("stick","Brown, Roediger, McDaniel «Make It Stick»",""," как учиться так, чтобы запомнить: самопроверка, интервалы, перемешивание, трудности, ошибки, как проверять себя.",F("make_it_stick",12),"make-it-stick/SKILL.md",fm("make-it-stick","«как запомнить», «самопроверка», «интервальные повторения», «перемешивание», «make it stick», «как учиться»"),300),
("peak","Ericsson, Pool «Peak»",""," как достигать мастерства через осознанную практику: цель, фокус, обратная связь, выход из зоны комфорта, ментальные образы, наставник.",F("peak_ericsson",15),"peak-ericsson/SKILL.md",fm("peak-ericsson","«осознанная практика», «как стать мастером», «peak», «deliberate practice», «ментальные образы», «тренировка навыка»"),300),
("mind","Oakley «A Mind for Numbers»",""," как учиться трудному (математика, техника): фокус и рассеянный режим, чанкинг, повторение, откладывание, сон, тесты, иллюзии знания.",F("a_mind_for_numbers",11),"mind-for-numbers/SKILL.md",fm("mind-for-numbers","«a mind for numbers», «чанкинг», «помодоро», «прокрастинация», «рассеянное мышление», «учить сложное»"),300),
]
for key,book,part,goal,files,out,f,n in tasks:
    s=T.format(book=book,part=part,goal=goal,files="; ".join(files),out=O+out,fm=f,n=n)
    open(key+".md","w",encoding="utf-8").write(s)
    print(key,len(files),all(os.path.exists(x) for x in files))
