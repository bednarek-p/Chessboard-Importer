# ♟︎ ChessBoard Importer Backend ♟︎

Repository for backend project "Chessboard Importer". The project is realized by the team of 4 students of Control Engineering and Robotics on specialization Information Technologies in Control Engineering as part of the Team Project Conference on Faculty of Electronics for the Company NetworkedAssets. Application was written in FastAPI framework used to recognize images taken with a mobile application. The machine learning models for the recognition pieces of chess were written using Keras and OpenCV libraries. The frontend of the application was written in Kotlin as a mobile application. To read more about the frontend part of the project visit the [frontend application repository](https://gitlab.com/kpz-2021-chessboard-importer-team/chessboard-importer-mobile). For more information visit the [wiki page](https://gitlab.com/kpz-2021-chessboard-importer-team/chessboard-importer-backend/-/wikis/home).

---
## Application Demo - Youtube 
[![Application Demo](https://i.imgur.com/Le2E452.png)](https://www.youtube.com/watch?v=HXiuUF98saY)

## Linter usage

### First time

Install

```shell
foo@bar:~$ pip install pre-commit
```

### Before commit

Run

```shell
foo@bar:~$ pre-commit run --all-files
```

---

## Add new packages

1. Install and configure Poetry
2. In directory containing pyproject.toml. Example add:

```shell
foo@bar:~$ poetry add numpy
```

3. Example remove:

```shell
foo@bar:~$ poetry remove numpy
```

---

## Authentication

Before running the app, you have to generate an environment variable in the command line.

Run:

```shell
foo@bar:~$ cp example.env .env
```

In .env file change SECRET variable to your own key.
This key is needed to generate access token and refresh token.

---

## Run app in a container - Linux

### 1. Running API server

1. Install Docker & Docker-Compose
2. Create Docker group in order not to use 'sudo' command **[link](https://docs.docker.com/engine/install/linux-postinstall/)**
3. To start server run the following commands in directory containing docker-compose.yml:

```shell
foo@bar:~$ docker-compose up
```

4. To stop server:

```shell
foo@bar:~$ ^C
foo@bar:~$ docker-compose down
```

Important! Always stop this way.

### 2. Accessing API with curl

1. Install curl:

```shell
sudo apt install curl
```

2. Run API server

3. Check if the server is running:

```shell
curl http://127.0.0.1:8000
```

You will see a JSON response as:

```json
{"Hello":"World"}
```

---

### 3. Logging in to get a token and be able to send a photo with curl

1. Send your username and password to get a token, where:

- "username": "here write your username"
- "password": "here write your password"

Below is a command on how to get a token, for this example values of username and password, are "test" but they are not truly values:

```shell
curl -H "Content-Type: application/json" -X POST \
  -d '{"username":"test","password":"test"}' http://localhost:8000/login
```

If your username and password are incorrect will see a JSON response as:

```json
{"detail":"Incorrect username or password"}
```

If your username and password are correct you will see access token and refresh token as JSON response, where:

- access token is valid for 15 minutes
- refresh token is valid for 30 days

2. export access token to variable TOKEN:

```shell
export TOKEN='here is access token'
```

Remember access token is the only combination of numbers without apostrophes ('').

---

### 4. Sending an image with curl

1. Post your image with token:

```shell
curl -H "Authorization: Bearer $TOKEN" -X POST -F 'file=@/path/to/your/image.png' http://127.0.0.1:8000/photo
```

If your token is incorrect you will see:

```json
{"detail":"Invalid crypto padding"}
```

If the recognition model does not recognize chessboard you will see 422 Error:

```json
{"detail":"Unprocessable Entity"}
```

If your token and path to your image are correct you will see the Forsyth–Edwards Notation.

---

### 6. Refreshing access token

1. After 15 minutes access token will be invalid and you will see a JSON response:

```json
{"detail":"Signature has expired"}
```

2. Export refresh token to variable TOKEN:

```json
export TOKEN='here is refresh token'
```

Remember access token is the only combination of numbers without apostrophes ('').

3. refresh token using refresh token, which is valid for 30 days:

```shell
curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:8000/refresh
```

If your refresh token is correct you will see an access token.

---

## Demo

Demonstration of a backend connected to a mobile application:

<img src="/demo/demo.gif" width="300">

## Authors

- Piotr Kowalski - Team leader
- Piotr Bednarek - Machine learning
- Kajetan Zdanowicz - DevOps
- Adam Bednorz - API, improving chess recognition
- Marcin Gruchała - Mobile application
