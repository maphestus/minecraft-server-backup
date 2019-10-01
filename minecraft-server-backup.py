import os
import shutil
import time
import zlib

server_dir = "C:/Minecraft Server/Scholomance"
backup_dir = "D:/MinecraftBackups/Scholomance_bak_"
time = time.strftime("%Y%m%d-%H%M%S")


# def backup():


def main():

    backup = backup_dir + time
    print(backup)
    shutil.make_archive(backup, 'zip', server_dir)


main()
