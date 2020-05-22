# KyykkaChopper

Automatic video editor for quickly editing Kyykkä videos.

Usage:
``` python process.py --input <path-to-folder> --output <output-file> ```

The input folder should contain one or more mp4 videos, and input files corresponding to the video filename.

An example folder could contain files:
* vid1.mp4
* vid2.mp4
* vid1.txt
* vid2.txt

Input file format is the following:

```
> clip start (in seconds)
< clip end (in seconds)
```

## Automatic timestamps from VLC

To automatically get timestamps from VLC player, use VLC version 2.0.x and place the elapsed_time_to_file.lua script to the extension folder. Enable the extension and after this, press 'x' to start a clip, and 'c' to stop it.

Original script: https://addons.videolan.org/p/1154002/

## Known issues
* Automatic timestamp file generation doesn't work between hard drives: the video needs to be in the same drive as VLC player.
* When merging multiple videos, the order of the videos is only determined by the output of `os.listdir`

