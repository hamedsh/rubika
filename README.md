<p align="center">
    <a href="github.address">
        <img src="https://raw.githubusercontent.com/shayanheidari01/rubika/master/icon.png" alt="Rubpy" width="128">
    </a>
    <br>
    <b>Rubika API Framework for Python</b>
    <br>
    <a href="https://github.com/shayanheidari01/rubika">
        Homepage
    </a>
    •
    <a href="https://github.com/shayanheidari01/rubika/tree/master/docs">
        Documentation
    </a>
    •
    <a href="https://pypi.org/project/rubpy/#history">
        Releases
    </a>
    •
    <a href="https://t.me/rubika_library">
        News
    </a>
</p>

## Rubpy

> Elegant, modern and asynchronous Rubika API framework in Python for users and bots

### Async Accounts
```python
from rubpy import Client, filters, utils
from rubpy.types import Updates

bot = Client(name='rubpy')

@bot.on_message_updates(filters.text)
async def updates(update: Updates):
    print(update)
    await update.reply(utils.Code('hello') + utils.Underline('from') + utils.Bold('rubpy'))

bot.run()
```

**Async Another Example:**
```python
from rubpy import Client

bot = Client(name='rubpy')

async def main():
    async with bot:
        result = await bot.send_message('me', '`hello` __from__ **rubpy**')
        print(result)

bot.run(main())
```

### Sync Accounts
```python
from rubpy.sync import Client, handlers, Message

with Client(session='rubpy') as client:
    @client.on(handlers.MessageUpdates())
    def updates(message: Message):
        message.reply('`hello` __from__ **rubpy**')
    client.run_until_disconnected()
```

**Sync Another Example:**
```python
from rubpy import Client

with Client(session='rubpy') as client:
        result = client.send_message('me', '`hello` __from__ **rubpy**')
        print(result)
```

**Rubpy** is a modern, elegant and asynchronous framework. It enables you to easily interact with the main Rubika API through a user account (custom client) or a bot
identity (bot API alternative) using Python.


### Key Features

- **Ready**: Install Rubpy with pip and start building your applications right away.
- **Easy**: Makes the Rubika API simple and intuitive, while still allowing advanced usages.
- **Elegant**: Low-level details are abstracted and re-presented in a more convenient way.
- **Fast**: Boosted up by pycryptodome, a high-performance cryptography library written in C.
- **Async**: Fully asynchronous (also usable synchronously if wanted, for convenience).
- **Powerful**: Full access to Rubika's API to execute any official client action and more.

### Installing

``` bash
pip3 install -U rubpy
```

### Thanks to
- [Milad Heidari](https://github.com/IRMilad/rubika)
