# ✨ GitFlow for developers

- clone repo to local machine:

```
https://github.com/Andrets/crypto_bot.git
```

- make a new branch (kind of dev_nickname)

```
git checkout -b dev_nickname main
```

- add changes

```
git add .
```

- commit changes

```
git commit -m "message"
```

- push

```
git push origin dev_nickname
```

- go to github and create a pull request, if it is a great commit and github does agree with merge, merge it

- wait for success job from workflow

# ✨ Local developing

- clone repo to local machine:

```
https://github.com/Andrets/crypto_bot.git
```

- enter that command to command line

```
docker compose -f docker-compose.dev.yaml -p crypto up -d --build
```

- urls

api - http://localhost:9088/api/v.1.0
client - http://localhost:9088
swagger - http://localhost:9088/api/v.1.0/Q29Cryptonashka

Made by dmitriyjunior<br/>
telegram: @dmitriy_junior<br/>
