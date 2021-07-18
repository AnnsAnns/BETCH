FROM archlinux:latest

RUN pacman -Syu

WORKDIR /app
COPY . .

RUN pacman -Ss python38 rustup


CMD ["cargo", "run"]