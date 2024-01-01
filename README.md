# Pomodoro Timer Bot

This is a discord bot that I wrote for personal use which acts as a Pomodoro timer

### Prerequisites

What things you need to install the software and how to install them

```
Python
Discord
```

### Installation, And Setup

A step by step series of examples that tell you how to get a development env running


Step 1
```
Download Python, Discord, and the files in the repository.
```

Step 2
```
Access the discord developer portal online, and create a new bot. After creating it
go to the bot section and generate the bots secret token key, and paste it
into the config.py file.When you open it you will know where to 
paste it.
```

Step 3
```
From the developer portal generate a url, and give the scope of bot, and the permission
of Send Messages.Generate a url to copy paste into your browser which will prompt
you for which server you want to invite the bot. Have a text channel ready for the bot
to use.
```

Step 4
```
Go to your user setting in the discord app, and in the advanced section enable developer mode.
With developer mode now enabled go back to the discord server of which you invited the bot.
```

Step 5
```
right click on the text channel you want to add the bot, and copy the channel id.
Paste the channel id into the bot.py file where the comment is specifying the location.
```

## Usage, And Commands
The pomodoro timer will go for 4 loops with 5 minute breaks in between, and will
stop once 4 loops have been done. You can start it again after the longer break.
You can also end it if you get tired during it.

!Start
```
Starts the pomodoro timer
```

!End
```
Ends the pomodoro timer
```

## Acknowledgements

Inspiration to make this bot came from pixegami
