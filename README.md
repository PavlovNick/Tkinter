# Tkinter

It is a program which written with Tkinter (Python GUI)

### gmail_enter_send.pyw

It is a primitive mail transfer agent  

Програма використовує протоколи SMTP для відправки повідомлень, 
та протокол IMAP, протокол POP3 не використовується.

Використовується лише один SMTP сервер та один IMAP: smtp.gmail.com, 
imap.gmail.com - тому зайти під іншим доменом неможливо.

Авторизація, надсилання та отримання повдомлень - реалізовані.

Щоб отримати таке повідомлення, потрібно увімкнути дозвіл IMAP (доступ
до Gmail з інших клієнтів через протокол IMAP, або POP, якщо б ми вико-
ристали протокол та сервер pop)
Щоб увімкнути дозвіл IMAP, потрібно зайти в своєму поштовому клієнті в
"Налаштування" -> "Переглянуи всі налаштування" -> "Пересилання та POP/
IMAP" -> "Доступ IMAP\Завантаження POP" (На прикладі Gmail)

Авторизуватись просто так також не вийде, Gmail заблокує спробу входу
навіть якщо пароль і пошта вірні, тому що як вважає Google - програма не
надійна. Щоб дозволити авторизацію, потрібно перейти за посиланням:
https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4MCw41tSNsJr
IZjeNdAJTEwhHorMYpOsCJX2V0Se6EJJ0Pf42VQMToUeWTvs-UYk6FV0R0GNAhm5qjJYc52-XOZLLc9Ug
та включити доступ для менш безпечних додатків.

Додаток запускається як звичайний .exe файл (я за те, що достатньо просто двічі 
клацнути мишкою по ньому) (на Windows), це при умові, якщо встановлений python.

### tkinter_2.pyw

A simple program for calculating room reservations
