import yaml
print(f"__name__ = {__name__}")
print(f"__package__ = {__package__}")

from serializer.base import JsonSerializer
from serializer.serializers import factory

class YamlSerializer(JsonSerializer):
    def to_str(self):
        return yaml.dump(self._current_object)


factory.register_format('YAML', YamlSerializer)