import click


class String(click.types.StringParamType):
    def gw_type_json(self):
        return {
            'type': 'string'
        }


class Range(click.types.IntRange):
    def gw_type_json(self):
        return {
            'type': 'range',
            'min': self.min,
            'max': self.max,
            'step': 1
        }


class Integer(click.types.IntRange):
    def gw_type_json(self):
        return {
            'type': 'integer',
            'min': self.min,
            'max': self.max,
            'step': 1
        }


class Choice(click.types.Choice):
    def gw_type_json(self):
        return {
            'type': 'string-enumeration',
            'values': self.choices
        }
