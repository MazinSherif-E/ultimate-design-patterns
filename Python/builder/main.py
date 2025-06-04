from .MessengerNotificationBuilder import MessengerNotificationBuilder

builder = MessengerNotificationBuilder()
builder.set_content("Hello, World!")
builder.set_sender("John Doe")
builder.set_recipient("Jane Doe")
builder.set_time_stamp("2021-01-01")
builder.set_attachments(["attachment1", "attachment2"])
builder.set_theme("Light")

notification = builder.build()