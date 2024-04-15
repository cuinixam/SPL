from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from spl_core.test_utils.spl_build import SplBuild


@pytest.fixture
def spl_build():
    return SplBuild(variant="my_var", build_kit="defaultKit")


def test_build_dir(spl_build: SplBuild) -> None:
    """
    Test that the build directory is constructed correctly.
    """
    assert spl_build.build_dir == Path("build/my_var/defaultKit")


@patch("spl_core.common.command_line_executor.CommandLineExecutor.execute")
def test_execute_success(mock_execute: MagicMock, spl_build: SplBuild) -> None:
    """
    Test that execute returns 0 when the build succeeds.
    """
    mock_execute.return_value = MagicMock(returncode=0)

    # Call the method
    result = spl_build.execute(target="all")

    # Assertions
    mock_execute.assert_called_once()
    assert result == 0


@patch("time.sleep")
@patch("spl_core.common.command_line_executor.CommandLineExecutor.execute")
def test_execute_failure_due_to_license_issue(mock_execute: MagicMock, mock_sleep: MagicMock, spl_build: SplBuild) -> None:
    """
    Test that execute retries on specific license failure messages.
    """
    # Setup mock outputs to simulate license failure and then success
    failure_output = MagicMock(returncode=1, stdout="No valid floating license")
    success_output = MagicMock(returncode=0)
    mock_execute.side_effect = [failure_output, success_output]

    # Call the method
    result = spl_build.execute(target="all")

    # Assertions
    assert mock_execute.call_count == 2
    assert result == 0
    assert mock_sleep.call_count == 1


@patch("spl_core.common.command_line_executor.CommandLineExecutor.execute")
def test_execute_with_additional_args(mock_execute: MagicMock, spl_build: SplBuild) -> None:
    """
    Test that additional arguments are passed to the command line executor correctly.
    """
    # Setup mock
    mock_execute.return_value = MagicMock(returncode=0)

    # Call the method
    additional_args = ["-j", "4"]
    spl_build.execute(target="all", additional_args=additional_args)

    # Assertions
    mock_execute.assert_called_once_with(["build.bat", "-buildKit", "defaultKit", "-variants", "my_var", "-target", "all", "-reconfigure", "-j", "4"])
