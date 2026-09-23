from telebot import TeleBot
from telebot.types import InlineKeyboardButton , InlineKeyboardMarkup 
#-------Token----------------
bot = TeleBot("7797171877:AAGNI0kyGBko96z0huiKrUROsoPsJSXA_nc")
chanel_userid = '-1004482197052'
#--------------------------------------
def is_member(user_id):
    try :
        member = bot.get_chat_member(chat_id = chanel_userid , user_id = user_id)
        if member.status in ['member' , 'administrator' , 'creator'] :
            return True
    except Exception as e :
        print('خطا : ' , e)
    return False
#-------------------------------
def back_up():
    ba = InlineKeyboardButton(text = '👤 پشتیبانی ' , url = 'https://t.me/Bot_cola')
    backk = InlineKeyboardButton(text = 'back🔙' , callback_data = 'back')
    mae = InlineKeyboardMarkup(row_width = 1)
    mae.add(ba , backk)
    return mae
#-------------------------------
def nemone():
    hoko = InlineKeyboardButton(text = 'ایران باستان 🎉' , url = 'https://t.me/emperatoryiran_bot')
    new = InlineKeyboardButton(text = 'نمونه کار فروشگاهی ساده 🛒' , url = 'https://t.me/newbot_10_bot')
    back = InlineKeyboardButton(text = 'back🔙' , callback_data = 'back')
    mark = InlineKeyboardMarkup(row_width = 1)
    mark.add (hoko , new , back)
    return mark
#------------------------------
def ozv():
    butom1 = InlineKeyboardButton(text='عضو شدن در کانال ✅' , url = 'https://t.me/Level_up_code10')
    butom2 = InlineKeyboardButton(text = 'عضو شدم  ✅' , callback_data = 'membership')
    butm = InlineKeyboardMarkup(row_width = 1)
    butm.add(butom1,butom2)
    return butm
#-------------------------------------------
def btn_org ():
    button = InlineKeyboardButton(text = 'سفارش و خدمات 🔧', callback_data = 'services')
    button1 = InlineKeyboardButton(text = 'ارتباط با ما😇' , callback_data = 'call')
    button2 = InlineKeyboardButton(text = 'نمونه کار ها 📁' , callback_data = 'port_folio')
    robot = InlineKeyboardMarkup(row_width = 1)
    robot.add(button , button1 , button2)
    return robot
def back_btn():
    back = InlineKeyboardButton(text = 'بازگشت به منوی اصلی🔙' , callback_data = 'menu')
    markup = InlineKeyboardMarkup(row_width = 1)
    markup.add(back)
    return markup
#--------------------------------------
@bot.message_handler(commands = ['start'])
def welcome(message):
    welcome_text = (
    f"سلام {message.from_user.first_name} عزیز! 👋\n\n"
    "به ربات خدمات برنامه‌نویسی من خوش اومدی. 💻\n\n"
    "من اینجا هستم تا در پروژه‌هابه شما کمک کنم:\n\n"
    "برای شروع، یکی از گزینه‌های زیر رو انتخاب کن: 👇"
)
    user_id = message.from_user.id
    if is_member(user_id) :
        bot.send_message(message.chat.id, welcome_text  , reply_markup = btn_org())
    else :
        bot.send_message(message.chat.id , text = 'لطفا در این کانال عضو شوید بعد از ربات استفاده کنید ⚠' , reply_markup = ozv())
# موقع ارسال حتما پارامتر parse_mode='Markdown' رو اضافه کن   
@bot.callback_query_handler(func = lambda call : True)
def call_back(call):
    try :
        if call.data == 'services':
            bot.edit_message_text(chat_id = call.message.chat.id , message_id = call.message.message_id ,text = 'ربات  تلگرامی : از ساده تا پیشرفته 🤖 \n 🖥پروژه های Tkinter  : طراحی رابط  کاربری (GUI) ' , reply_markup = back_btn())
        elif call.data == 'membership':
            user_id = call.from_user.id
            if is_member(user_id) :
                bot.edit_message_text(chat_id = call.message.chat.id  , message_id = call.message.message_id , text = f"سلام {call.from_user.first_name} عزیز! 👋\n\n"
    "به ربات خدمات برنامه‌نویسی من خوش اومدی. 💻\n\n"
    "من اینجا هستم تا در پروژه‌هابه شما کمک کنم:\n\n"
    "برای شروع، یکی از گزینه‌های زیر رو انتخاب کن: 👇"  , reply_markup = btn_org())
        elif call.data == 'call':
            bot.edit_message_text(chat_id = call.message.chat.id , message_id = call.message.message_id , text = ' برای ثبت درخواست، طرح پروژه یا پرسیدن سوالات خود، لطفاً پیام خود را به آیدی زیر ارسال نمایید:' , reply_markup = back_up())
        elif call.data == 'port_folio':
            bot.edit_message_text(chat_id = call.message.chat.id , message_id = call.message.message_id , text = "📁 نمونه کار ها :👇" , reply_markup = nemone())
        elif call.data == 'menu':
            bot.edit_message_text(chat_id = call.message.chat.id , message_id = call.message.message_id , text = ' به منوی اصلی برگشتید 🔙'  , reply_markup = btn_org())
        elif call.data == 'back' :
            bot.edit_message_text(chat_id = call.message.chat.id , message_id = call.message.message_id , text = ' به منوی اصلی برگشتید 🔙'  , reply_markup = btn_org())

    except Exception as e :
        print('خطا : ' , e)
#---------------------------------------------------------------------
print('bot starting 🤖 . . . ')
bot.polling()

