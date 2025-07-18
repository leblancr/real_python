import yaml
print(f"__name__ = {__name__}")
print(f"__package__ = {__package__}")
from serializer import serializers

class YamlSerializer(serializers.JsonSerializer):
    def to_str(self):
        return yaml.dump(self._current_object)


serializers.factory.register_format('YAML', YamlSerializer)  # pass in class name
