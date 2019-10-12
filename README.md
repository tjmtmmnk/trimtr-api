# trimtr-api

[![Build Status](https://travis-ci.com/tjmtmmnk/trimtr-api.svg?branch=master)](https://travis-ci.com/tjmtmmnk/trimtr-api)

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
