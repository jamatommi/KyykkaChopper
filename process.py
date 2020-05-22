import argparse
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

def parse_cuts(filename):
    """Parse file with the following format:
    >clip start (in seconds)
    <clip end (in seconds)
    """
    cuts = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for n in range(0, len(lines), 2):
            start = lines[n]
            end = lines[n+1]
            assert start.startswith(">") and end.startswith("<")
            start = float(start[1:].strip())
            end = float(end[1:].strip())
            cuts.append([start, end])
    return cuts
                
def process_with_moviepy(filenames, datafiles, outfile):
    clips = []

    for video_file, data_file in zip(filenames, datafiles):
        input_vid = VideoFileClip(video_file)
        cuts = parse_cuts(data_file)
        for cut in cuts:
            clips.append(input_vid.subclip(cut[0], cut[1]))

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(outfile)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--input", type=str)
    args.add_argument("--output", type=str, default="out.mp4")

    args = args.parse_args()

    input_dir = args.input
    files = os.listdir(input_dir)

    videofiles = []
    datafiles = []
    for fname in files:
        if fname.lower().endswith("mp4"):
            videofiles.append(os.path.join(input_dir, fname))
            datafiles.append(os.path.join(input_dir, f"{fname.split('.')[0]}.txt"))


    process_with_moviepy(videofiles, datafiles, args.output)
