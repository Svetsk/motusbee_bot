import telebot
import threading
import time

from telebot import types
from telebot.types import InlineKeyboardMarkup

bot = telebot.TeleBot('6868071421:AAEhmOf8RH_F3a0u028UulATrUz_E0Mz7fM')

file_path = 'test.jpg'

# Глобальная переменная для хранения имени пользователя
global username
username = None

# Переменная для отслеживания активных таймеров
active_timers = {}  # Словарь для хранения активных таймеров для каждого чата

# ============================================================ #
textOne = ('<b>Уже через несколько минут ты поймешь, как долго не кончать, укрепить эрекцию и сделать сексуальную жизнь яркой</b>\n\n '
            '<u>Это мини-курс из 3 уроков, который поможет тебе разобраться в своих sex-проблемах и найти для них решения. </u><b>Ты можешь пройти его бесплатно.</b>\n\n '
            '<b>Здесь ты также узнаешь, как повысить свое либидо 💪🏻</b>\n\n '
            '<b>Здесь поделюсь с тобой своей уникальной методикой по контролю эякуляции и восстановлению крепкой эрекции,</b>\n\n'
            'Меня зовут Сергей Пчелинцев. Я кинезиолог с 13-летним опытом. Помогаю обрести уверенность и здоровье в сексуальной жизни мужчинам по всему миру от Нью-Йорка до Пекина\n\n'
            '<b>Здесь поделюсь с тобой своей уникальной методикой по контролю эякуляции и восстановлению крепкой эрекции,</b> которая когда-то выручила меня самого. А уже сейчас помогла 3 000+ клиентов.'
            'Я не буду давать тебе скучную теорию или делиться нерабочими методами. Здесь я объясню, как просто, быстро, безопасно и с удовольствием решить проблему быстрого финиша навсегда.\n\n'
            '<b>ГОТОВ?</b> Жми на кнопку ниже и смотри видео.')
lessonTwo = ('⚡️<b>Урок 2/3. Не будь, как молния. Научись держаться с ней в постели намного дольше и увереннее</b>\n\n'
              'Если сейчас ты постоянно чувствуешь вину, стыд, стесняешься, и в итоге не можешь получить наслаждения от секса — можешь выдохнуть.\n\n'
              '<b>Я уже подготовил разбор трех самых главных причин, из-за которых парни быстро кончают</b>\n\n'
              'Посмотрев это видео, тебе никогда не придется пользоваться такой ерундой, как «подумать о чем-то мерзком», «выпить таблетки», «брызнуть лидокаина»…\n\n'
              'Узнай ТОП-3 причины быстрого финиша и пойми, что ты можешь исправить самостоятельно, в домашних условиях\n\n'
              '<b>Все это поможет тебе избавиться от самой проблемы и начать управлять продолжительностью процесса</b>👇🏻')
lessonThree = ('🥵 <b>Урок 3/3. Все решения sex-проблем в одном видео.</b>\n\n'
               'Пора перейти от разбора своих проблем к разбору конкретных решений. Если до этого я объяснял тебе, ПОЧЕМУ:\n\n'
               '— Ты быстро кончаешь, не можешь продержаться и стесняешься из-за этого…\n'
               '— Тебе то хочется, то не хочется, то легко возбуждаешься, то даже не можешь думать о соитии с девушками\n'
               '— То все получается, то в самые важные моменты боец тебя подводит…\n\n'
               '<b>Теперь пора РЕШИТЬ всё это!</b>\n\n'
               'Нажимай на кнопку ниже. В этом коротком видео я разбираю все самые популярные решения и даю самый рабочий способ обрести уверенность в сексуальной жизни.')

inline_keyboard = types.InlineKeyboardMarkup()
inline_keyboard_two = types.InlineKeyboardMarkup()
inline_keyboard_three = types.InlineKeyboardMarkup()
inline_keyboard_buy = types.InlineKeyboardMarkup()
inline_keyboard_prot = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('СМОТРЕТЬ ПЕРВЫЙ УРОК', callback_data='button1')
button2 = types.InlineKeyboardButton('СМОТРЕТЬ ВТОРОЙ УРОК', callback_data='button2')
button3 = types.InlineKeyboardButton('СМОТРЕТЬ ТРЕТИЙ УРОК', callback_data='button3')
button4 = types.InlineKeyboardButton('ОПЛАТИТЬ', callback_data='button4')
button7 = types.InlineKeyboardButton('У МЕНЯ НЕТ ПРОТИВОПОКАЗАНИЙ, ОПЛАТИТЬ', callback_data='button7')
button5 = types.InlineKeyboardButton('ОСТАЛИСЬ ВОПРОСЫ', callback_data='button5')
inline_keyboard.row(button1)
inline_keyboard_two.row(button2)
inline_keyboard_three.row(button3)
inline_keyboard_buy.row(button4)
inline_keyboard_prot.row(button7)
quOne = types.InlineKeyboardButton('Первый вопрос', callback_data='quOne')
quTwo = types.InlineKeyboardButton('Второй вопрос', callback_data='quTwo')
quThree = types.InlineKeyboardButton('Третий вопрос', callback_data='quThree')
quFour = types.InlineKeyboardButton('Четвертый вопрос', callback_data='quFour')
quFive = types.InlineKeyboardButton('Пятый вопрос', callback_data='quFive')
quSix = types.InlineKeyboardButton('Противопоказания', callback_data='quSix')
keyboardQu = InlineKeyboardMarkup()
keyboardQu.row(quOne, quTwo)
keyboardQu.row(quThree, quFour)
keyboardQu.row(quFive, quSix)





@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    if call.data == 'button1':
        bot.send_message(chat_id, 'https://youtu.be/hbeovCEUrD8')
        stop_timers(chat_id, message_id)  # Остановка таймеров при нажатии кнопки 1


        # Запуск двух новых таймеров при нажатии кнопки 1
        timer_3 = threading.Timer(5, send_privat_message, args=(chat_id, message_id))
        timer_21 = threading.Timer(10, send_but_two, args=[chat_id, message_id])
        timer_22 = threading.Timer(15, send_but_three, args=[chat_id, message_id])
        active_timers[chat_id] = [timer_21, timer_22]  # Добавление новых таймеров в список активных таймеров
        timer_21.start()
        timer_22.start()
        timer_3.start()
    elif call.data == 'button2':
        bot.send_message(chat_id, 'https://youtu.be/kXJRyjnrSmg')
        stop_timers(chat_id, message_id)  # Остановка таймеров при нажатии кнопки 2
        # Запуск двух новых таймеров при нажатии кнопки 2
        timer_31 = threading.Timer(5, lesson_Three_bot, args=[chat_id, message_id])
        timer_32 = threading.Timer(10, send_button__three, args=[chat_id, message_id])
        timer_33 = threading.Timer(15, bet_three, args=[chat_id, message_id])
        active_timers[chat_id] = [timer_31, timer_32]  # Добавление новых таймеров в список активных таймеров
        timer_31.start()
        timer_32.start()
        timer_33.start()
    elif call.data == 'button3':
        bot.send_message(chat_id, 'https://youtu.be/iBv0hlz-yPE')
        stop_timers(chat_id, message_id)  # Остановка таймеров при нажатии кнопки 3

        timer_41 = threading.Timer(5, buyer, args=[chat_id, message_id])
        timer_buy = threading.Timer(10, buyer_doj, args=[chat_id, message_id])
        timer_buyer = threading.Timer(15, buyer_dojim, args=[chat_id, message_id])
        timer_buys = threading.Timer(20, buyers_d, args=[chat_id, message_id])
        timer_qaa = threading.Timer(25, qaa, args=[chat_id, message_id])
        timer_qaa.start()
        timer_41.start()
        timer_buy.start()
        timer_buyer.start()
        timer_buys.start()
    elif call.data == 'quOne':
        bot.send_message(chat_id, '<b>Твоя сексуальная жизнь выйдет на новый уровень, ты научишься контролировать свою эякуляцию и заниматься сексом столько, сколько этого хочешь ты. Эракция станет крекой и стабильной в любом возрасте. Либидо будет бить ключом ярче, чем это было у тебя раньше. И так, как организм единое целое, а курс “Мужской фокус” придуман мной, кинезиологом с 13и летним стажем, попутно ты избавишься от лишнего живота, проблем с поясницей, чувствовать себя будешь бодрей, а спать будешь как младенец, даже во время сложных жизненных периодов. Скорее всего ты заведешь новые знакомства, а твой доход на работе или в бизнесе непременно пойдет вверх. P.S. Ты можешь написать в службу заботы и оперативно получить ответ на другой вопрос @motusbee_sup</b>', parse_mode='HTML', reply_markup=inline_keyboard_buy)
    elif call.data == 'quTwo':
        bot.send_message(chat_id, '<b>Первые результаты в подавляющем большинстве случаев ты получишь через всего 2е недели, занимаясь три раза в неделю по 1.5 - 2 часа. Стабильный эффект в 95% случаев получают за 1.5 - 2 месяца. Будешь заниматься реже, все равно получишь желанный эффект, только чуть дольше, чем за 2 месяца.</b>\n\n'
                                       '<b>P.S. Ты можешь написать в службу заботы и оперативно получить ответ на другой вопрос @motusbee_sup</b>', parse_mode='HTML', reply_markup=inline_keyboard_buy)
    elif call.data == 'quThree':
        bot.send_message(chat_id, '<b>Курс “Мужской фокус” подходит для мужчин от 18и до 50и лет. При отсутствие противопоказаний. Таких, как острая стадия воспаления предстательной железы, 2 года после полостных операций, открытые раны на теле и голове, температура тела выше 37и градусов, простудные заболевания, рак в стадии метастазирования, варикоцели, острые нарушения психики, аутоиммунные заболевания. При наличии больших грыж любого характера требуется консультация со специалистом перед началом курса.</b>\n\n'
                                  '<b>P.S. Ты можешь написать в службу заботы и оперативно получить ответ на другой вопрос @motusbee_sup </b>', parse_mode='HTML', reply_markup=inline_keyboard_buy)
    elif call.data == 'quFour':
        bot.send_message(chat_id, '<b>Потому что мой курс “Мужской фокус” известен по всему миру, его прошло огромное количество мужчин и оставили свой положительный отзыв о достижении желаемого результата. А так же я, Пчелинцев Сергей, автор курса, имею высшее образование в сфере реабилитации и восстановления, вылечил за 13 лет работы методами массажа, мануальной терапии, остеопатии и кинезиотерапии от проблем интимного характера, проблем в суставах и спине около 4000 человек. Мне 30 лет и да, работать официально массажистом я стал с 17и, тогда как в 15 лет прошел первые курсы оздоровительного массажа и начал практиковаться. Все это потому, что в 14 лет на футбольном поле я получил травму, с которой не могли справиться врачи, я решил справиться сам. Такая жестокая мотивация, всегда творит чудеса.</b>\n\n'
                                  '<b>P.S. Ты можешь написать в службу заботы и оперативно получить ответ на другой вопрос @motusbee_sup</b>', parse_mode='HTML', reply_markup=inline_keyboard_buy)
    elif call.data == 'quFive':
        bot.send_message(chat_id, '<b>Все данные клиента абсолютно конфиденциальны. Курс покупают и проходят мужчины по всему миру уже больше года. Никто не раскрыт, все отзывы и публикации исключительно с разрешения мужчины. Я понимаю тебя как никто другой, ведь и интимная проблема на моем пути меня коснулась.</b>\n\n'
                                  'P.S. Ты можешь написать в службу заботы и оперативно получить ответ на другой вопрос @motusbee_sup', parse_mode='HTML', reply_markup=inline_keyboard_buy)
    elif call.data == 'quSix':
        bot.send_message(chat_id, '<b>Противопоказания к прохождению курса без предварительной консультации:</b>\n\n'
                                  '1. Острая стадия воспаления предстательной железы\n'
                                  '2. Температура тела выше 37 - и градусов\n'
                                  '3. В течении двух лет после полостных операций\n'
                                  '4. Остеопороз\n'
                                  '5. Язвы желудка и кишечника\n'
                                  '6. Наркотические и алкогольные состояния\n'
                                  '7. Болезнь Бехтерева\n'
                                  '8. Аутоиммунные заболевания\n'
                                  '9. Варикоцеле\n'
                                  '10. Варикозное расширение вен в острой стадии\n'
                                  '11. Аденома простаты\n'
                                  '12. Рак в стадии метастазирования\n'
                                  '13. Период простудных заболеваний\n'
                                  '14. Грыжи позвоночника в стадии секвестирования\n'
                                  '15. Паховые и пупочные грыжи\n'
                                  '16. Острая стадия любых заболеваний почек\n'
                                  '17. Острая стадия любых заболеваний мочевого пузыря\n\n'
                                  '<b>P.s Чтобы попасть на курс “Мужской фокус” при наличии хотя бы одного противопоказания, пожалуйста, запишитесь на платную консультацию - разбор, для записи, пишите свой запрос в службу заботы @motusbee_sup (телеграм)</b>', parse_mode='HTML', reply_markup=inline_keyboard_prot)


def qaa(chat_id, message_id):
    bot.send_message(chat_id, '<b>👉🏻 ОТВЕТЫ НА ТВОИ ВОПРОСЫ</b>\n\n'
                              'Моя личка разрывается от сообщений смелых и достойных мужчин, ребята из службы заботы тоже уже вскипают 🥵\n\n'
                              'Как много желающих обрести здоровье и уверенность в сексуальной сфере…\n\n'
                              '<b>Я собрал ответы на самые частые вопросы ниже</b>\n\n'
                              '1. Что именно изменится после курса?\n\n'
                              '2. Сколько его проходить и когда будут первые результаты?\n\n'
                              '3. Для какого возраста подходит курс?\n\n'
                              '4. Почему я должен тебе доверять?\n\n'
                              '5. Кто-то узнает, что я прохожу такой курс?', parse_mode='HTML', reply_markup=keyboardQu
                     )

def buyer_dojim(chat_id, message_id):
    bot.send_message(chat_id, '<b>🔥 Бонусы сгорят через 5 минут</b>\n\n'
                              'Курс «Мужской фокус» помог уже 3 000+ мужчин. И в 100% случаев он сработал безупречно, за счет того, что:\n\n'
                              '— я даю простые способы решить проблему. Простые упражнения, которые можно делать дома, в командировке, у друзей, в отеле, где хочешь. Хватит двух квадратных метров, чтобы сделать упражнения.\n\n'
                              '— все упражнения максимально приятные и простые. Тебе будет нравится их делать и они без труда станут привычкой.\n\n'
                              '— на курсе есть поддержка от кураторов, если вдруг у тебя будет что-то не получаться.', parse_mode='HTML', reply_markup=inline_keyboard_buy)
def buyers_d(chat_id, message_id):
    bot.send_message(chat_id, '<b>🔥 БОНУСЫ СГОРЕЛИ, но не все потеряно.</b> Ты еще можешь воспользоваться скидкой и решить свои sex-проблемы максимально выгодно.\n\n'
                              '<em>Поверь мне, это будет лучшая инвестиция в себя, ведь…</em>\n\n'
                              'Здоровье в сексуальной сфере = ментальное здоровье. Ведь сексуальные проблемы порой проявляются в жизни: в отношениях, в общении с девушками, да даже на работе.\n\n'
                              'Мне понадобилось 13 лет непрерывно пахать и экспериментировать с методиками, чтобы научиться решать сексуальные проблемы у клиентов.', parse_mode='HTML')

    bot.send_message(chat_id, '<b>Но сейчас ты можешь просто купить курс с проверенными упражнениями по цене от 9 990 и можешь 100% получить результат</b>\n\n'
                              '— Ты поймешь, как влиять на либидо\n\n'
                              '— Сможешь сделать эрекцию сильнее\n\n'
                              '— Научишься продлевать половой акт без вреда для здоровья\n\n'
                              '— Получишь техники, которые нормализуют кровообращение в органах малого таза\n\n'
                              '— Научишься расслаблять психику и за счет техник по укреплению тканей внутренних органов продлишь свою жизнь и будешь энергичным мачо до старости\n\n'
                              '<b>Курс может пройти любой мужчина в возрасте до 50 лет.</b> Проходить курс можно в своем темпе, в неделю понадобится до 250 минут. В НЕДЕЛЮ! И все.\n\n'
                              'Ты можешь сделать свою сексуальную жизнь ярче и насыщеннее прямо сейчас. Я уверен, что уже через неделю занятий ты скажешь мне «спасибо».\n\n'
                              '👇🏻 ОТКРЫВАЙ САЙТ, чтобы выбрать свой тариф и попасть на курс.\n\n'
                              '<s>от 13 990</s>\n\n'
                              '<b>от 9 990</b>\n\n'
                              '❗Если платеж не прошел, пиши в службу заботы: @motusbee_sup', parse_mode='HTML', reply_markup=inline_keyboard_buy)
def buyer_doj(chat_id, message_id):
    bot.send_message(chat_id, '🔥 <b>Бонусы сгорят через 10 минут</b>', parse_mode='HTML', reply_markup=inline_keyboard_buy)
def buyer(chat_id, message_id):
    bot.send_message(chat_id, '<b>Ты дошел до конца...</b>\n\n'
                              'Поэтому я с огромной радостью представляю тебе свой интенсив "Мужской фокус" 🎯\n\n'
                              '<b>Он точечно направлен на решение одной задачи: </b>формирование крепкой, здоровой эрекции и умение контролировать свою эякуляцию, чтобы заниматься сексом столько, сколько этого хочется тебе и получать ощущения более высокого качества, чем это было раньше.\n\n'
                              '<b>Никаких врачей, таблеток, обследований! Только ты и мои упражнения, направленные на улучшение интимного здоровья.</b>'
                              'В течение 48 часов ты можешь купить мой курс “Мужской фокус” по цене…\n\n'
                              '<s>от 13 990 руб</s>\n'
                              'от 9 990 руб', parse_mode='HTML')

    bot.send_message(chat_id, '🔥<b>Если ты оплатишь интенсив в течение 15 минут,</b> в подарок получишь от меня бонусы ценностью 50 000 рублей.\n\n'
                              '<b>Кроме этого:</b> каждый мой ученик может выиграть до 15 000 рублей, за простое выполнение упражнений. Я провожу такие розыгрыши в каждом потоке!\n\n'
                              '▶️ Нажимай на кнопку «ОПЛАТИТЬ», чтобы перейти на сайт и выбрать свой формат курса.\n\n'
                              '▶️ Можешь выбрать VIP формат, чтобы работать лично со мной и гарантированно прийти к результату максимально быстро\n\n'
                              '❗Если платеж не прошел, пиши в службу заботы: @motusbee_sup\n\n'
                              '❗Платежи принимаются с ЛЮБОЙ КАРТЫ МИРА, если у тебя не получилось, пиши в службу заботы: @motusbee_sup всегда найдем комфортное для тебя решение\n\n', parse_mode='HTML', reply_markup=inline_keyboard_buy)

def send_button_foure(chat_id, message_id):
    bot.send_message(chat_id, '', parse_mode='HTML')
    bot.send_message('https://youtu.be/iBv0hlz-yPE')
def send_button__three(chat_id, message_id):
    bot.send_message(chat_id, '😱 <b>Один мой клиент 3 года не чувствовал ничего во время секса.</b> Знаешь, почему?\n\n'
                              'Потому что он до этого решал проблему с эякуляцией путем мазей и лидокаина. Если тебе сейчас подумалось:\n\n'
                              '<em>«Ого, как круто, ничего не чувствуешь, можно хоть два часа в постели провести!»</em>\n\n'
                              'То вот он так не думал. Он вообще потерял интерес к сексу. И вот это «два часа» — только на словах звучит круто и страстно.\n\n'
                              '<b>По факту, и парень, и девушка, после 30-40 минут уже утомляются и никто не хочет доводить дело до конца.</b>\n\n'
                              'Я рассказываю, ПОЧЕМУ НАДО СРОЧНО перестать использовать мази и таблетки во втором уроке 👇🏻\n\n'
                              'В нем же ты узнаешь, что именно будет работать и безопасно поможет тебе решить свою проблему. Никаких сложностей, никаких побочек.\n\n'
                              'Просто открой урок. Несколько минут могут перевернуть жизнь на 180°.', parse_mode='HTML', reply_markup=inline_keyboard_three)
def lesson_Three_bot(chat_id, message_id):
    bot.send_message(chat_id, lessonThree, parse_mode='HTML', reply_markup=inline_keyboard_three)
def send_but_two(chat_id, message_id):
    global username
    message_text = (f'✍🏻<b>Записываю: {username} согласен быстро кончать. Или ты не согласен?</b>\n\n'
                    'Нажимай на кнопку, чтобы посмотреть второй урок и понять, как тебе избавиться от проблемы быстрого финиша:\n\n'
                    '- что именно нужно проработать или изменить, чтобы научиться контролировать длительность секса\n')
    bot.send_message(chat_id, message_text, parse_mode='HTML', reply_markup=inline_keyboard_two)
def send_but_three(chat_id, message_id):
    bot.send_message(chat_id, '📹 <b>Так и быть, отправляю тебе урок прямо в диалог</b>\n\n'
                              'Смотри его сейчас: \n\n'
                              '— Пойми, как избавиться от стеснения и стыда и почувствовать себя аполлоном\n'
                              '— Разбереись, из-за чего ты быстро финишируешь\n\n'
                              '— Узнай, как ты сможешь решить это дома, без напрягов\n\n'
                              '🏆<b>Смотри и победи свою эякуляцию</b>', parse_mode='HTML')
    bot.send_message(chat_id, 'https://youtu.be/kXJRyjnrSmg')
def send_reminder(chat_id, message_id):
    bot.send_message(chat_id, '🙄 <em>Бросила меня, потому что еле встал. Так я еще и быстро кончил…</em>\n\n'
                              'История клиента. Анонимно.\n\n'
                              '«<em>Я помню, как однажды жестко влюбился в девушку. Крышу сносило, в гормонах тонул, ни о чем кроме нее не думал. И я тоже ей нравился.</em>\n\n'
                              '<em>Первый раз — не встал. А на второй раз я продержался 3 минуты После этого она со мной не общалась»</em>\n\n'
                              'Вот так за 3 минуты можно потерять отношения мечты. Но ты практически <b>за это же время</b> можешь понять, как обрести титанический стояк и долго не кончать\n\n'
                              '<b>Нажимай на кнопку 👇🏻</b>'
                              'За 3 минуты узнаешь, как навсегда избавиться от быстрого финиша и слабой эрекции', parse_mode='HTML', reply_markup=inline_keyboard)
def send_reminders(chat_id, message_id):
    bot.send_message(chat_id, '<b>Урок 1/3. Представь, что ты всегда готов к бою. Можешь за ночь сколько хочешь раз, с любой продолжительностью</b>\n\n'
                              'Представил? Это хорошо. Только вот теперь пора перейти к действиям и воплотить давнюю мечту в реальность ☝🏻\n\n'
                              'Я собрал 13 лет опыта работы с sex-проблемами в одно видео длительностью 2 минуты 33 секунды.\n\n'
                              'Отправил его в чат, так как у тебя не получается нажать на кнопку. Открывай и смотри прямо сейчас — там есть подробное объяснение, как избавиться от быстрой эякуляции и слабой эрекции\n\n', parse_mode='HTML')
    bot.send_message(chat_id, 'https://youtu.be/hbeovCEUrD8')


def bet_three(chat_id, message_id):
    bot.send_message(chat_id, '<b>📹 Урок 3/3 уже в чате: узнай о единственном рабочем способе избавиться от низкого либидо, слабой эрекции и быстрого финиша. </b>\n\n'
                              'Смотри его отсюда прямо сейчас.\n\n'
                              '<b>Тут ты поймешь:</b>'
                              '— Почему не работают мази и таблетки\n'
                              '— Что будет, если затягивать с решением проблем\n'
                              '— Как, уделяя 20 минут в день, имея только коврик и 2 квадратных метра, можно ЛЕГКО и с УДОВОЛЬСТВИЕМ избавиться от сексуальных проблем за счет простых упражнений\n\n'
                              '☝🏻 Смотри прямо сейчас. Сможешь встать на быстрый путь исправления уже сегодня', parse_mode='HTML')
    bot.send_message(chat_id, 'https://youtu.be/iBv0hlz-yPE')
def send_privat_message(chat_id, message_id, message=None):
    bot.send_message(chat_id, lessonTwo, parse_mode='HTML' , reply_markup=inline_keyboard_two)

# Функция для запуска всех таймеров
def start_timers(chat_id, message_id):
    timer_1 = threading.Timer(5, send_reminder, args=[chat_id, message_id])
    timer_2 = threading.Timer(10, send_reminders, args=[chat_id, message_id])
    timer_4 = threading.Timer(86400, send_but_three, args=[chat_id, message_id])
    timer_5 = threading.Timer(160000, send_reminders, args=[chat_id])
    active_timers[chat_id] = [timer_1, timer_2, timer_4]  # Сохранение активных таймеров для данного чата
    timer_1.start()
    timer_2.start()
    timer_4.start()
    timer_5.start()
text_prize = ('🎁<em>После мини-курса ты получишь подарок — <b>секретное упражнение для управления и усиления оргазма X2.</b></em>')
# Функция для остановки всех таймеров
def stop_timers(chat_id, message_id):
    if chat_id in active_timers:
        for timer in active_timers[chat_id]:
            timer.cancel()  # Остановка каждого активного таймера
        del active_timers[chat_id]  # Удаление записи о таймерах для данного чата

@bot.message_handler(commands=['start'])
def start(message):
    global username
    username = message.from_user.first_name
    with open(file_path, 'rb') as file:
        bot.send_photo(message.chat.id, file, textOne, parse_mode='HTML', reply_markup=inline_keyboard)
    with open(file_path, 'rb') as file:
        bot.send_photo(message.chat.id, file, text_prize, parse_mode='HTML', reply_markup=inline_keyboard)

    # Запуск всех таймеров при старте
    start_timers(message.chat.id, message.message_id)

@bot.message_handler(func=lambda message: True)
def stop_timer(message):
    chat_id = message.chat.id
    message_id = message.message_id

    # Остановка таймеров, если они активны
    stop_timers(chat_id, message_id)

bot.polling()