from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_MESSAGE = '''**Hi, {}**
I am EZ4Short bot, bulk link converter with your posts/messages. I can convert & earn money directly from your links.
'''

HELP_MESSAGE = '''**Hi, {}**
A bot to short link support bulk link conversion. I can convert links directly from your shrinkme.ioaccount.
    
1. Go To 👉 https://shrinkme.io/api
2. Then Copy API Key
3. Then long press /api command then paste your API Key (43158cd2de15fd89738b02619a33de9ec093e47b)

**/api Your API Key 
(See Example.👇)
Example:** `/api de303d5270f481aec928f39883da7b7f9a8812ac `

**➕ Hit** 👉 /features To know more features of this bot.
**💁‍♀️ Hit** 👉 /help To get help.
**➕ Hit** 👉 /footer Adding your custom footer to bot.

**Contact** 👉 @Jakeedot (For support)
'''

ABOUT_TEXT = '''**Hey! My name is 68985.**

**⚡Features⚡**

• I can **Convert any** links or posts to your **68985** link / post. (Button Links Posts, Hidden links/Hyperlinks All Are Supported)

• I Can **auto** add custom **footer text** to your every post. Hit 👉 /footer To know more...

• I Can **auto** add custom **Header text** to your every post. Hit 👉 /header To know more...

• I Can **Automatically Replace** Your **Banner** Image To images in the post. Hit  👉/banner_image To Know More... 

• **No** need to share **password or email** to convert links.**

 **Contact** 👉 @Jakeedot (For support)

**Click On Custom Alias To Create Custom Link**
'''

CUSTOM_ALIAS_MESSAGE = """For Custom Alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex:  Updates"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""

ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('Custom Alias', callback_data=f'alias_conf')
        
    ],


])

HELP_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('More Features', callback_data=f'about_command')
        
    ],


])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Get Api', url=f'https://bit.ly/EZ4Short')
    ]
])



BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Back', callback_data=f'about_command')
    ],

])

USER_ABOUT_MESSAGE = """
- Website: [{base_site}](https://shrinkme.io/ref/Hs534415)

- Site Link {base_site} Current Linked API: {shortener_api}

- Replace Channel Username: @layersyetem

- Header Text: 
{header_text}

- Footer Text: 
{footer_text}

- Banner Image: {banner_image}
"""


SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/api [Your API Token]`
            
Ex: `/api de303d5270f481aec928f39883da7b7f9a8812ac `

Get API From [{base_site}](https://shrinkme.io/ref/Hs534415)

Current API: `{43158cd2de15fd89738b02619a33de9ec093e47b}`"""

HEADER_MESSAGE = """**Reply to the Header Text You Want**

This Text will be added to the top of every message **caption** or text

For adding **line break** use \n
To Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """**Reply to the Footer Text You Want**

This Text will be added to the **bottom** of every message **caption** or text

For adding **line break** use \n
To Remove Footer Text: `/footer remove`"""

USERNAME_TEXT = """**Hi! {}, I am EZ4Short bot, bulk link converter bot From Linked Your 68985 Account,**

**🌟 Type** /channel (channel link or username)

**example:**
/channel @layersyetem
Or
/channel https://t.me/layersyetem

**🤘 Hit** 👉 /features To Know More Features Of This Bot.

**- Message @Jakeedot For More Help -**"""

BANNER_IMAGE = """
**Usage:** `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://telegra.ph/file/5e96340a91470256b387a.jpg`"""


BANNED_USER_TXT = """
Usage: `/ban [User ID]`

Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
