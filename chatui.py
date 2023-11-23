css = '''
<style>
.chat-message {
    min-height: 1rem; padding: 1.25rem; border-radius: 0.25rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 10%;
}
.chat-message .avatar img {
  max-width: 50px;
  max-height: 50px;
  border-radius: 3px;
  object-fit: cover;
}
.chat-message .message {
  width: 90%;
  padding: 0 0.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmc1GiL7UwyP8TeEu3uKIU-MKuO1rUO5VdXs0mrWqsF6Yk4MSovtJAAMVywWv-0Sz7LN0">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://w7.pngwing.com/pngs/469/1003/png-transparent-avatar-businessman-male-person-suit-user-user-avatars-icon.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''