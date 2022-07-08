#!/usr/bin/env python3
import click
import example.random


@click.group()
def cli():
    """
    A random number generator.
    """
    pass


@cli.command("number")
@click.option("--min", default=0, help="Smallest number to return")
@click.option("--max", default=100, help="Largest number to return")
def number(min: int, max: int) -> None:
    """
    Returns a random number.
    """
    click.echo(f"Generating a random number between {min} and {max}")
    rnd = example.random.Random()
    num = rnd.number(min, max)

    click.echo(f"Number is: {num}")


@cli.command("password")
@click.option("-l", "--length", default=32, help="Password length to use")
@click.option("-n", "--numbers/--no-numbers", is_flag=True, help="Use numbers in the password")
@click.option("-s", "--special/--no-special", is_flag=True, help="Use special characters in the password")
def password(length: int, numbers: bool, special: bool) -> None:
    """
    Returns a password
    """
    rnd = example.random.Random()
    pw = rnd.password(length, numbers, special)
    click.echo(f"{pw}")


if __name__ == "__main__":
    cli()
