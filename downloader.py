from subprocess import run, check_output

def get_name(url, file_type):
    cmd = ["youtube-dl",
           "--skip-download",
           "-e",
           "-o",
           "%(title)s.%(ext)s",
           url
           ]

    title = check_output(cmd).decode("utf-8").rstrip() + "." + file_type
    return title

def download_audio(url):
    cmd = ["youtube-dl",
           "--extract-audio",
           "--audio-format",
           "mp3",
           "-o",
           "%(title)s.%(ext)s",
           url
           ]

    run(cmd)


def download_video(url):
    cmd = ["youtube-dl",
           "--format",
           "mp4",
           "-o",
           "%(title)s.%(ext)s",
           url
           ]

    run(cmd)


def download_videohd(url):
    cmd = ["youtube-dl",
           "-o",
           "%(title)s.%(ext)s",
           url
           ]

    run(cmd)