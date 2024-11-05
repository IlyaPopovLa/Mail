import smtplib
import os
from dotenv import load_dotenv

website = "https://dvmn.org/referrals/Je6wQwphD1Ntg2hjgimqAkwx0CrWcDmesAwIfSB8/"
friend_name = "Александр"
my_name = "Илья"

from_address = "ilyadvmn@yandex.ru"
to_address = "il.popov@lamoda.ru"

msg = f"""From: {from_address} 
To: {to_address}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""\
    .format(website=website, friend_name=friend_name, my_name=my_name).encode("utf-8")


load_dotenv()
login = os.environ["LOGIN"]
password = os.environ["PASSWORD"]


server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail(from_address, to_address, msg)
server.quit()