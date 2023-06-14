# vim:fenc=utf-8
from click.testing import CliRunner
import diabetes
from diabetes import cli


def test_true():
    assert 1 == 1


def test_click_cli():
  runner = CliRunner(mix_stderr=False)
  result = runner.invoke(cli.cli, ['--help'])
  assert result.exit_code == 0
  assert 'Start nutrion in server mode' in result.output
  assert 'Start nutrion in server mode' in result.stdout
  assert '' == result.stderr
