# Chapter 08 - Environment Variables

I have done some modification of my own as I do not want to store sensitive information in `docker-compose` file either. The author suggest use of `.env` file as a best practice, but for the book he decided the to use `docker-compose.yml` instead. I am taking the suggested way of doing it by using `.env`

### Setup

You will need two files in the project directory:
1. `.db.env`: Settings for db. This needs to set minimum:
    - `POSTGRES_PASSWORD`
2. `.web.env`: Settings for web. This needs to set minimum:
    - `SECRET_KEY`
    - `ENV` (`development` or `production`)
    - `POSTGRES_PASSWORD`

Leave the value if you have them set in your shell profile.

```powershell
SECRET_KEY    # shell will provide the value
ENV
DEBUG=1       # explicitly giving the value
```
