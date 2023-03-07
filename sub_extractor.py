import subprocess
import os
import asstosrt


def show_tracks():
    for file_ in os.listdir():
        if file_.endswith('.mkv'):
            subprocess.call(f'mkvmerge -i "{file_}"', shell=True)
            return


def ass_to_srt(fn):
    ass_file = open(fn)
    srt_string = asstosrt.convert(ass_file)
    open(fn, 'w', encoding='utf-8').write(srt_string)
    print('--> Converted to srt')


def create_subtitle():
    track_id = input('--> Enter track id: ')

    for file_ in os.listdir():
        if file_.endswith('.mkv'):
            sub_fn = file_.replace(".mkv", ".srt")
            args = f'mkvextract tracks "{file_}" {track_id}:"{sub_fn}"'
            subprocess.call(args, shell=True)

            sub_content = open(sub_fn).read()

            if sub_content.count('-->') < 10:
                ass_to_srt(sub_fn)


print('01) Show tracks')
print('02) Create subtitle')

select = input('--> Enter an options: ')

if int(select) == 1:
    show_tracks()
elif int(select) == 2:
    create_subtitle()
