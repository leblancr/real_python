import json
import xml.etree.ElementTree as et

from serializer.base import JsonSerializer, XmlSerializer


# gets a serializer object based on format type then passes it to serializable
class ObjectSerializer:
    def serialize(self, serializable, output_format):
        serializer = factory.get_serializer(output_format)  # retrieve the serializer from the object factory
        serializable.serialize(serializer)  #
        return serializer.to_str()


# the object factory, registers new format types and returns serializer objects
class SerializerFactory:
    def __init__(self):
        self._creators = {}

    # creator is class name
    def register_format(self, output_format, creator):
        self._creators[output_format] = creator # store class name

    # return a serializer object based on format
    def get_serializer(self, output_format):
        creator = self._creators.get(output_format)  # just a class name, no parenthesis
        if not creator:
            raise ValueError(output_format)
        return creator()  # instantiate object here, notice parenthesis

factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)
