"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Era5 Analysis."""


if __name__ == "__main__":
    main(prog_name="era5-analysis")  # pragma: no cover
