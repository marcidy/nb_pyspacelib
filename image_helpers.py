import subprocess


COMMANDS = {
    'convert': '/usr/bin/convert',
}


def run_cmd(cmd):
    return subprocess.run(cmd, stdout=subprocess.PIPE)


def pixelate(img_path, dest_path, width, height):
    cmd = [COMMANDS['convert'],
           img_path,
           "-resize",
           "{}x{}".format(width, height),
           "+dither",
           dest_path]

    return run_cmd(cmd)
