# trimtr-api

[![Build Status](https://travis-ci.com/tjmtmmnk/trimtr-api.svg?branch=master)](https://travis-ci.com/tjmtmmnk/trimtr-api)

## Features
- Insert new line after sentence
```
How are you? I am fine thank you.
↓
How are you?
I am fine thank you.
```

- Remove unnecessary white space or new line
```
I am  fine thank   you
↓
I am fine thank you.
```

```
I am fine
thank you.
↓
I am fine thank you.
```

- Even if the sentences are next to each other without white spaces, it can insert new line properly
```
How are you?I am fine thank you.
↓
How are you?
I am fine thank you.
```

- Retain sentence blocks
  - It becomes easy to understand sentences with chunks of meaning
```
Power Wireless Personal Area Networks (6LoWPANs) often have high packet error rates and a typical throughput of 10s of kbit/s.
The protocol is designed for machine- to-machine (M2M) applications such as smart energy and building automation.

CoAP provides a request/response interaction model between application endpoints, supports built-in discovery of services and resources, and includes key concepts of the Web such as URIs and Internet media types.
↓
[nochange]
```

## Routes
`POST https://trimtr.herokuapp.com/trim` Get shaped text from your raw text

Request
- header: `Content-Type: text/plain; charset=UTF-8`
- data: `{"body":[YOUR TEXT]}`

Responce:
- data: `[{"text":"{"body":[SHAPED TEXT]},200]`

e.g.
``` bash
curl -X POST -H "Content-Type: text/plain; charset=UTF-8" -d '{"body":"I am tjmtmmnk. I want to show you e.g."}' "https://trimtr.herokuapp.com/trim"
[{"text":"{\"body\":\"I am tjmtmmnk.\nI want to show you e.g.\"}"},200]
```

## Attention
I don't log your input data, so I know nothing about the input information.

## Licence
Apache 2.0

## Author
tjmtmmnk
