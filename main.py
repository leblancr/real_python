from serializer.songs import Song
from serializer.serializers import ObjectSerializer
import serializer.yaml_serializer

if __name__ == '__main__':
    song = Song('123', 'Imagine', 'John Lennon')
    serializer = ObjectSerializer()  #

    try:
        print(serializer.serialize(song, 'JSON'))
        print(serializer.serialize(song, 'XML'))
        print(serializer.serialize(song, 'YAML'))
    except ValueError as e:
        print(e, "not supported")

