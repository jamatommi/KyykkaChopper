import vlc
import keyboard
import argparse
import os

set_timestamp_start = 'x'
set_timestamp_end = 'c'
pause_player = 'space'
go_forward = 'right'
go_backward = 'left'
time_step = 5000 #ms

def get_time_frame_start(timestamp, player):
    time = player.get_time()/1000
    # print(time)
    timestamp["start"] = time

def get_time_frame_end(timestamp, timestamps, player):
    time = player.get_time()/1000
    # print(time)
    timestamp["end"] = time
    timestamps.append(timestamp.copy())

def pause(player):
    player.pause()

def move_forward(player, time_step):
    if (player.get_time() + time_step) <= player.get_length():
        player.set_time(player.get_time() + time_step)

def move_backward(player, time_step):
    if (player.get_time() - time_step) >= 0:
        player.set_time(player.get_time() - time_step)

def edit_video(file):
    timestamps = []
    timestamp = {"start" : 0, "end": 0}
    player = vlc.MediaPlayer(file)
    player.play()
    keyboard.add_hotkey(set_timestamp_start, get_time_frame_start, args=[timestamp, player])
    keyboard.add_hotkey(set_timestamp_end, get_time_frame_end, args=[timestamp, timestamps, player])
    keyboard.add_hotkey(pause_player, pause, args=[player])
    keyboard.add_hotkey(go_forward, move_forward, args=[player, time_step])
    keyboard.add_hotkey(go_backward, move_backward, args=[player, time_step])
    # keyboard.add_hotkey('esc', cut_video, args=[timestamps, file])
    print("Hätä tilanteessa paina ESC.")
    keyboard.wait('esc')
    write_file(timestamps, file)
    # print(timestamps)

def write_file(timestamps, file):
    with open(file + "_timestamps.txt", "w") as f:
        for i in timestamps:
            f.write(">clip start " + str(i["start"]) + "\n" + "<clip end " + str(i["end"]) + "\n")


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--input", type=str)

    args = args.parse_args()

    input_dir = args.input
    files = os.listdir(input_dir)
    videofiles = []
    print("Mitä tiedostoa haluat editoita?")
    for fname in files:
        if fname.lower().endswith("mp4"):
            if not input_dir:
                videofiles.append(os.path.join(fname))
            else:
                videofiles.append(os.path.join(input_dir, fname))
            print(str(len(videofiles)) + "." + fname)
    if len(videofiles) == 0:
        print("yhtään tiedostoa ei ole")
    else:
        edit_video(videofiles[int(input("=")) - 1])
