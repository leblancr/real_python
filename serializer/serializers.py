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
    def serialize(self, serializable, format):
        serializer = factory.get_serializer(format)  # retrieve the serializer from the object factory
        serializable.serialize(serializer)  #
        return serializer.to_str()


class SerializerFactory:
    format_to_class = {'JSON': JsonSerializer, 'XML': XmlSerializer}

    def get_serializer(self, output_format):
        try:
            return self.format_to_class[output_format]()  # make instance of class
        except KeyError:
            raise ValueError(output_format)
        # if format == 'JSON':
        #     return JsonSerializer()
        # elif format == 'XML':
        #     return XmlSerializer()
        # else:
        #     raise ValueError(format)


factory = SerializerFactory()