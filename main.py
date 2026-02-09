from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8591463797:AAFBYkF-cgVs3pJhHRufccbHxWXw8WZQUCs"  # توکن جدیدت

FREE_ACCOUNTS = """
🎁 **اکانت‌های رایگان:**

1. cazorlaluiscarlos@hotmail.com | Luiscarlos2023
2. mohamad.ahmadi6855@gmail.com | 09138692885a
3. juan23ciprian@gmail.com | Nancy2304
4. mrsumantap@gmail.com | $P@l2020
5. hsankhezri1389@gmail.com | hasan1389
6. bashirri.mahan1@gmail.com | Mahan@#1354
7. amirmahdish12@gmail.com | amirmahdish12
8. vsgevehen@gmail.com | mahdi1383
9. amirufc19@gmail.com | Amir5530114581
10. kasra.safari.9890@gmail.com | kasra2232
11. ghaffarmohamadrezasamadi1368@gmail.com | 09191072857gh
12. mobinn.razavii@gmail.com | mobin1387!
13. santiagocasji55@hotmail.com | Lucianita7
14. kauak2403@gmail.com | 40028922tfcvbhyg
15. fatemehaliakbarzadeh52@gmail.com | klhor09352865271
16. mahdimalke55@gmail.com | mahdi11228
17. kazem0011kazemm@gmail.com | kazem00kazem
18. sebastijansentigar16@gmail.com | FireFox001
19. ftahzadhesina@gmail.com | sina09339924416

🔥 **بفرما گل 👆**
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎁 اکانت رایگان", callback_data='free_accounts')],
        [InlineKeyboardButton("🛒 شاپ ما", callback_data='shop')],
        [InlineKeyboardButton("👤 ایدی پشتیبانی", callback_data='support')],
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = (
        "👋 **به ربات خوش آمدید!**\n\n"
        "🌟 با استفاده از دکمه‌های زیر می‌توانید به خدمات دسترسی پیدا کنید:\n\n"
        "1️⃣ 🎁 اکانت رایگان - دریافت لیست اکانت‌ها\n"
        "2️⃣ 🛒 شاپ ما - ورود به فروشگاه\n"
        "3️⃣ 👤 ایدی پشتیبانی - ارتباط با پشتیبانی"
    )
    
    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'free_accounts':
        await query.message.reply_text(
            FREE_ACCOUNTS,
            parse_mode='Markdown',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 بازگشت به منو", callback_data='back_to_menu')]
            ])
        )
        
    elif query.data == 'shop':
        await query.message.reply_text(
            "🛒 **فروشگاه ما:**\n\n"
            "🔗 https://t.me/shopalizord\n\n"
            "برای خرید به لینک بالا مراجعه کنید.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔗 رفتن به فروشگاه", url='https://t.me/shopalizord')],
                [InlineKeyboardButton("🔙 بازگشت", callback_data='back_to_menu')]
            ])
        )
        
    elif query.data == 'support':
        await query.message.reply_text(
            "👤 **پشتیبانی:**\n\n"
            "📍 ایدی: @AliZord_yt\n\n"
            "📞 برای ارتباط مستقیم روی ایدی بالا کلیک کنید.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📞 پیام به پشتیبانی", url='https://t.me/AliZord_yt')],
                [InlineKeyboardButton("🔙 بازگشت", callback_data='back_to_menu')]
            ])
        )
        
    elif query.data == 'back_to_menu':
        await query.edit_message_text(
            text="👋 **به ربات خوش آمدید!**\n\n"
                 "🌟 با استفاده از دکمه‌های زیر می‌توانید به خدمات دسترسی پیدا کنید:\n\n"
                 "1️⃣ 🎁 اکانت رایگان - دریافت لیست اکانت‌ها\n"
                 "2️⃣ 🛒 شاپ ما - ورود به فروشگاه\n"
                 "3️⃣ 👤 ایدی پشتیبانی - ارتباط با پشتیبانی",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🎁 اکانت رایگان", callback_data='free_accounts')],
                [InlineKeyboardButton("🛒 شاپ ما", callback_data='shop')],
                [InlineKeyboardButton("👤 ایدی پشتیبانی", callback_data='support')],
            ]),
            parse_mode='Markdown'
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("🤖 ربات روشن شد...")
    app.run_polling()

if __name__ == '__main__':
    main()
