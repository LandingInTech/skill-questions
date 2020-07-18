# opsdroid skill questions

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to work together with the Twitch Connector. 

Landing in Tech is using opsdroid and the Twitch Connector to interact with the chat. This skill allows viewers to trigger a `!question` command which will add the user question to a dashboard where we can chose which one to show on stream.

## Requirements

An active Twitch Connector.

## Configuration

```yaml
skills:
  questions: {}
```

## Usage

### `!question <user question>`

Opsdroid will reply to an hello message. It will choose from a few random messages.

> user: !question what is it like to work as a freelancer?
>
> opsdroid: Thank you for your question user! I will ask this question as soon as possible.

Then the question is added to the database so it can be fetched on the [Questions](https://github.com/LandingInTech/questions) dashboard.