import base64

css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

# style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />
        <span class="material-symbols-outlined" style="font-size:38px;">
            robot_2
        </span>
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <span class="material-symbols-outlined" style="font-size:38px;">
        person
        </span>
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
            </style>"""

filepath = "pics/ucwdc_without_words.png"

with open(filepath, "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
data_ucwdc = "data:image/png;base64," + encoded.decode("utf-8")

filepath2 = "pics/immigration_without_words.png"

with open(filepath2, "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
data_immigration = "data:image/png;base64," + encoded.decode("utf-8")

filepath3 = "pics/cloud_without_words.png"

with open(filepath3, "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
data_cloud = "data:image/png;base64," + encoded.decode("utf-8")