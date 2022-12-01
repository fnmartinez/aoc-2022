import importlib
import os
import pkgutil

import click


def get_commands_from_pkg(pkg) -> dict:
    pkg_obj = importlib.import_module(pkg)

    pkg_path = os.path.dirname(pkg_obj.__file__)

    commands = {}
    for module in pkgutil.iter_modules([pkg_path]):
        module_obj = importlib.import_module(f"{pkg}.{module.name}")
        if not module.ispkg:
            module_obj.command.name = module.name
            commands[module_obj.command.name] = module_obj.command

        else:
            commands[module.name.replace('_', '-')] = click.Group(
                context_settings={'help_option_names': ['-h', '--help']},
                help=module_obj.__doc__,
                commands=get_commands_from_pkg(f"{pkg}.{module.name}")
            )

    return commands


@click.group(commands=get_commands_from_pkg("aoc2022.solutions"))
def cli():
    pass
