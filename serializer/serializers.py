import json
import xml.etree.ElementTree as et


class JsonSerializer:
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer:
    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')


#
class ObjectSerializer:
    def serialize(self, serializable, output_format):
        serializer = factory.get_serializer(output_format)  # retrieve the serializer from the object factory
        serializable.serialize(serializer)  #
        return serializer.to_str()


# the object factory
class SerializerFactory:
    def __init__(self):
        self._creators = {}

    # creator is class name
    def register_format(self, output_format, creator):
        self._creators[output_format] = creator # store class name

    # return a serializer object based on format
    def get_serializer(self, output_format):
        creator = self._creators.get(output_format)
        if not creator:

            raise ValueError(output_format)
        return creator()

factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)
factory.register_format('YAML', XmlSerializer)