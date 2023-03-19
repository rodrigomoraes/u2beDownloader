from pytube import YouTube
from moviepy.editor import *
import os
import shutil
import sys


def main():
    while True:
        print("-" * 20)
        print("ut downloader")
        print("-" * 20)
        print("")
        print("Selecione uma opção")
        print("[0] - Baixar Video")
        print("[1] - Baixar Audio")
        print("[2] - Sair")

        opt = int(input("Voce selecionou a opção:"))

        if opt == 0:
            print("Baixar Video")
            print("Cole abaixo o link do video do youtube")
            link = (input())
            if link == "":
                print("O campo não pode ficar vazio")
            else:
                downloadVideo(link)

        elif opt == 1:
            print("Baixar Audio")
            print("Cole abaixo o link do video do youtube")
            link = (input())
            if link == "":
                print("O campo não pode ficar vazio")
            else:
                downloadAudio(link)
        elif opt == 2:
            sys.exit()


def downloadVideo(link):

    video = YouTube(link)
    video = video.streams.get_highest_resolution()
    title = video.title

    try:
        print(title)
        video_path = video.download(output_path="./videos")
        video.download(output_path="./videos")
        print("Sucesso")
    except:
        print("Ocorreu um erro")


def downloadAudio(link):

    video = YouTube(link)
    video = video.streams.get_audio_only(subtype="mp4")
    title = video.title

    try:
        print(title)
        video.download(output_path="./tmp/")
        video_path = video.download(output_path="./tmp/")

        print("Exatraindo audio do video")
        mp3_path = './audios/' + title + '.mp3'
        tmp_path = "./tmp/"
        AudioFileClip(video_path).write_audiofile(mp3_path)

        cleanTempDir(tmp_path)

        print("Sucesso!")
    except OSError:
        print(OSError)


def cleanTempDir(path):

    file_list = os.listdir(path)

    for file_name in file_list:
        file_path = os.path.join(path, file_name)

        if os.path.isfile(file_path):
            os.remove(file_path)
            print("Arquivo excluido")


if __name__ == '__main__':
    main()
