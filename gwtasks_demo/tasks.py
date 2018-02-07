import click

from .decorator import augmented_task
from . import types


@augmented_task
@click.option('--name', type=types.String(), help="Your pet's name")
@click.option('--age', type=types.Integer(min=1, max=20),
              help='An interger between 1 and 2)')
@click.option('--animal', type=types.Choice(['cat', 'dog', 'monkey']))
def add_pet(name, age, animal='dog'):
    """Demo of a task with several different argument types."""
    print('You have a %d year old %s named %s' % (age, animal, name))


@augmented_task
@click.option('--guess', type=types.Range(min=1, max=20),
              help="Pick a number between 1 and 20 (hint: it's 4)")
def guess_a_number(guess=1):
    """Try to guess the number I picked."""
    if guess != 4:
        raise Exception('WRONG!')

    print('You guessed correctly!')
