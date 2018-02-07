import click


def augmented_task(func):
    func.main = click.command()(func)
    params = func.main.params

    for param in params:
        # we only handle option instances (at least for now)
        assert isinstance(param, click.Option)

    return func
