// Вписать запрос в поле чата NotebookLM (заменить ТЕКСТ_ЗАПРОСА). Кнопка «Отправить» от JS-клика НЕ срабатывает:
// после этого скрипта — find «Поле для запросов» → left_click по ref → key "End space BackSpace Return".
const q = `ТЕКСТ_ЗАПРОСА`;
const ta = document.querySelector('textarea[aria-label="Поле для запросов"]');
ta.focus(); ta.value = q; ta.dispatchEvent(new Event('input', {bubbles: true}));
ta.value.length
