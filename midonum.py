from mido import MidiFile


def midinum(musicfile):

    mid = MidiFile(musicfile)

    midinum = ""

    for i, track in enumerate(mid.tracks):
        midinum = midinum + str('Track {}:{}'.format(i, track.name))
        for msg in track:
            midinum = midinum + str(msg)

    return midinum
