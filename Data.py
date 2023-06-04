from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
**مرحبا بك {}

في بوت استخراج جلسات تيرمكس

• البوت يقوم بأستخراج كود تيليثون

• ويقوم بأستخراج كود بايروجرام 

━━━━━━━━━━━━━━━━━━━━━━━━

**
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("بـدء انشـاء جلسة", callback_data="generate")],
        [InlineKeyboardButton(text=" رجــوع ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("بـدء انشـاء جلسة", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("بـدء انشـاء جلسة", callback_data="generate")],
        
        [
            InlineKeyboardButton("مسـاعدة", callback_data="help"),
            InlineKeyboardButton("حول البوت", callback_data="about")
        ],
        
    ]

    # Help Message
    HELP = """
**- اوامـر البـوت الاخـرى ⌨:**

/about - حـول البـوت
/help - اوامـر المسـاعده
/start - بـدء تشغيـل البـوت
/generate - بـدء انشـاء جلسـه
/cancel - الغـاء
/restart - اعـادة تشغيـل
"""

    # About Message
    ABOUT = """
**معلومات البوت : 

• تم انشاء البوت من قبل مطور سورس سايثون

• يستخدم هذا البوت لأستخراج جلسة تيرمكس

• ( كود تيليثون و كود بايروجرام )

• المطور : @T_4_Z

• قناة السورس : @saythonh**
    """
