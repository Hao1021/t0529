from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction
from linebot.models import TemplateSendMessage,ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn
from linebot.models import ImagemapSendMessage, BaseSize, MessageImagemapAction, URIImagemapAction, ImagemapArea, TemplateSendMessage, ButtonsTemplate, DatetimePickerTemplateAction
from linebot.models import TextSendMessage, AudioSendMessage, VideoSendMessage
from linebot.models import TextSendMessage, BubbleContainer, ImageComponent, BoxComponent, TextComponent, IconComponent, ButtonComponent, SeparatorComponent, FlexSendMessage, URIAction

import datetime
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
baseurl = "https://github.com/lowenchi0509/st2/tree/master/media/"
def sendText(event):  #傳送文字
    try:
        message = TextSendMessage(  
            text = "我是 Linebot，\n您好！"
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


def sendMulti(event):  #多項傳送
    try:
        message = [  #串列

            TextSendMessage(  #傳送y文字
                text = "何謂洗錢??"
            ),
            ImageSendMessage(  #傳送圖片
                original_content_url ="https://img.itw01.com/images/2018/03/05/20/4828_rb0nUb_C75LEGQ.jpeg!r800x0.jpg",
                preview_image_url = "https://img.itw01.com/images/2018/03/05/20/4828_rb0nUb_C75LEGQ.jpeg!r800x0.jpg"
            ),

	   TextSendMessage(  #傳送y文字
                text = "洗錢:\n將其不法行為活動獲得的資金或財產，透過各種交易管道掩飾或隱匿， 轉換成為合法的資金或財產。"
            ),
	   TextSendMessage(  #傳送y文字
                text = "洗錢的架構:1.特定罪犯行為 2.取得不法利益 3.洗清黑錢"
            ),


            TextSendMessage(  #傳送y文字
                text ="https://www.youtube.com/watch?v=F-ESYoE0w0k"
	    ),

        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))



def sendQuickreply(event):  #快速選單
    try:
        message = TextSendMessage(
            text='請選擇想要查詢的國內相關組織',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="行政院防制洗錢辦公室", text="https://www.amlo.moj.gov.tw/")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="法務部調查局洗錢防制處", text="https://www.mjib.gov.tw/mlpc")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="金管會", text="https://www.fsc.gov.tw/ch/index.jsp")
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


def sendButton(event):  #按鈕樣版
    try:
        message = TemplateSendMessage(
            alt_text='防制洗錢小知識',
            template=ButtonsTemplate(
                thumbnail_image_url='https://cnews.com.tw/wp-content/uploads/%E5%8F%B0%E7%81%A3%E5%8F%8D%E6%B4%97%E9%8C%A2%E9%98%B2%E5%88%B6%E3%80%8C%E8%90%BD%E5%BE%8C%E3%80%8D-%E9%87%91%E7%AE%A1%E6%9C%83%E7%A0%94%E8%AD%B0%E7%9B%B8%E9%97%9C%E6%8E%AA%E6%96%BD.jpg',  #顯示的圖片
                title=' ',  #主標題
                text='國外相關組織：',  #副標題
                actions=[
                    MessageTemplateAction(  #顯示文字計息
                        label='FATF',
                        text='https://www.fatf-gafi.org/home/'
                    ),
                    MessageTemplateAction( 
                        label='APG',
                        text='http://www.apgml.org/'
                    ),
                     MessageTemplateAction( 
                        label='艾格蒙聯盟',
                        text='https://egmontgroup.org/en'
                  

                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

  
def sendCarousel(event):  #轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='轉盤樣板',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',
                        title='這是樣板一',
                        text='第一個轉盤樣板',
                        actions=[
                            MessageTemplateAction(
                                label='文字訊息一',
                                text='賣披薩'
                            ),
                            URITemplateAction(
                                label='連結文淵閣網頁',
                                uri='http://www.e-happy.com.tw'
                            ),
                            PostbackTemplateAction(
                                label='回傳訊息一',
                                data='action=sell&item=披薩'
                            ),
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/qaAdBkR.png',
                        title='這是樣板二',
                        text='第二個轉盤樣板',
                        actions=[
                            MessageTemplateAction(
                                label='文字訊息二',
                                text='賣飲料'
                            ),
                            URITemplateAction(
                                label='連結台大網頁',
                                uri='http://www.ntu.edu.tw'
                            ),
                            PostbackTemplateAction(
                                label='回傳訊息二',
                                data='action=sell&item=飲料'
                            ),
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))



