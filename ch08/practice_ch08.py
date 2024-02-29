# p.213 ~ 214
# 메시지를 출력하는 메소드
def show_messages(msg):
    for i in msg:
        print(i)

# 출력된 메시지를 다른 list변수에 저장하는 메소드
def send_messages(msg, sent_message):
    while msg:
        current_msg = msg.pop()
        print(current_msg)
        sent_message.append(current_msg)

message = ["hello", "world", "Good", "bad"]
sent_messages = []
message_copy = message[:]

send_messages(message_copy, sent_messages)
show_messages(sent_messages)

print(f"message: {message}")
print(f"message_copy: {message_copy}")
print(f"sent_messages: {sent_messages}")