"""cli.py unit tests."""
from pathlib import Path
from unittest.mock import patch

import pytest

import pypyr.cli


def test_main_pass_with_sysargv_context_positional():
    """Invoke from cli sets sys.argv, check assigns correctly to args."""
    arg_list = ['pypyr',
                'blah',
                'ctx string',
                '--loglevel',
                '50',
                '--dir',
                'dir here',
                '--groups',
                'group1',
                'group 2',
                'group3',
                '--success',
                'sg',
                '--failure',
                'f g']

    with patch('sys.argv', arg_list):
        with patch('pypyr.pipelinerunner.run') as mock_pipeline_run:
            with patch('pypyr.log.logger.set_root_logger') as mock_logger:
                pypyr.cli.main()

    mock_logger.assert_called_once_with(log_level=50,
                                        log_path=None)

    mock_pipeline_run.assert_called_once_with(
        pipeline_name='blah',
        args_in=['ctx string'],
        parse_args=True,
        py_dir='dir here',
        groups=['group1', 'group 2', 'group3'],
        success_group='sg',
        failure_group='f g'
    )


def test_main_pass_with_sysargv_single_group():
    """Invoke from cli sets sys.argv, check assigns correctly to group."""
    arg_list = ['pypyr',
                'blah',
                'ctx string',
                '--loglevel',
                '50',
                '--dir',
                'dir here',
                '--groups',
                'group1',
                '--success',
                'sg',
                '--failure',
                'f g']

    with patch('sys.argv', arg_list):
        with patch('pypyr.pipelinerunner.run') as mock_pipeline_run:
            with patch('pypyr.log.logger.set_root_logger') as mock_logger:
                pypyr.cli.main()

    mock_logger.assert_called_once_with(log_level=50,
                                        log_path=None)

    mock_pipeline_run.assert_called_once_with(
        pipeline_name='blah',
        args_in=['ctx string'],
        parse_args=True,
        py_dir='dir here',
        groups=['group1'],
        success_group='sg',
        failure_group='f g'
    )


def test_main_pass_with_sysargv_context_multiple_positional():
    """Multiple positional arguments."""
    arg_list = ['pypyr',
                'blah',
                'ctx string',
                'arg 2',
                'arg 3',
                'arg4=hello',
                '--loglevel',
                '50',
                '--dir',
                'dir here',
                '--groups',
                'group1',
                'group 2',
                'group3',
                '--success',
                'sg',
                '--failure',
                'f g']

    with patch('sys.argv', arg_list):
        with patch('pypyr.pipelinerunner.run') as mock_pipeline_run:
            with patch('pypyr.log.logger.set_root_logger') as mock_logger:
                pypyr.cli.main()

    mock_logger.assert_called_once_with(log_level=50,
                                        log_path=None)

    mock_pipeline_run.assert_called_once_with(
        pipeline_name='blah',
        args_in=['ctx string', 'arg 2', 'arg 3', 'arg4=hello'],
        parse_args=True,
        py_dir='dir here',
        groups=['group1', 'group 2', 'group3'],
        success_group='sg',
        failure_group='f g'
    )


def test_main_pass_with_sysargv_context_positional_log_alias():
    """Invoke from cli sets sys.argv with log alias."""
    arg_list = ['pypyr',
                'blah',
                'ctx string',
                '--log',
                '50',
                '--dir',
                'dir here']

    with patch('sys.argv', arg_list):
        with patch('pypyr.pipelinerunner.run') as mock_pipeline_run:
            with patch('pypyr.log.logger.set_root_logger') as mock_logger:
                pypyr.cli.main()

    mock_logger.assert_called_once_with(log_level=50,
                                        log_path=None)

    mock_pipeline_run.assert_called_once_with(
        pipeline_name='blah',
        args_in=['ctx string'],
        parse_args=True,
        py_dir='dir here',
        groups=None,
        success_group=None,
        failure_group=None
    )


def test_main_pass_with_sysargv_context_positional_abbreviations():
    """Invoke from cli sets sys.argv with log abbreviations."""
    arg_list = ['pypyr',
                'blah',
                'ctx string',
                '--logl',
                '50',
                '--dir',
                'dir here',
                '--logp',
                '/blah']

    with patch('sys.argv', arg_list):
        with patch('pypyr.pipelinerunner.run') as mock_pipeline_run:
            with patch('pypyr.log.logger.set_root_logger') as mock_logger:
                pypyr.cli.main()

    mock_logger.assert_called_once_with(log_level=50,
                                        log_path='/blah')

    mock_pipeline_run.assert_called_once_with(
        pipeline_name='blah',
        args_in=['ctx string'],
        parse_args=True,
        py_dir='dir here',
        groups=None,
        success_group=None,
        failure_group=None
    )


def test_main_pass_with_sysargv_context_positional_flags_last():
    """Check assigns correctly to args when positional last not first."""
    arg_list = ['pypyr',
                '--loglevel',
                '50',
                '--dir',
                'dir here',
                'blah',
                'ctx string', ]

    with patch('sys.argv', arg_list):
        with patch('pypyr.pipelinerunner.run') as mock_pipeline_run:
            with patch('pypyr.log.logger.set_root_logger') as mock_logger:
                pypyr.cli.main()

    mock_logger.assert_called_once_with(log_level=50,
                                        log_path=None)

    mock_pipeline_run.assert_called_once_with(
        pipeline_name='blah',
        args_in=['ctx string'],
        parse_args=True,
        py_dir='dir here',
        groups=None,
        success_group=None,
        failure_group=None
    )


def test_main_pass_with_sysargv_context_multiple_positional_flags_last():
    """Check assigns correctly to multiple args when positional last."""
    arg_list = ['pypyr',
                '--loglevel',
                '50',
                '--dir',
                'dir here',
                'blah',
                'ctx string',
                'arb 2',
                'arb3=arbvalue']

    with patch('sys.argv', arg_list):
        with patch('pypyr.pipelinerunner.run') as mock_pipeline_run:
            with patch('pypyr.log.logger.set_root_logger') as mock_logger:
                pypyr.cli.main()

    mock_logger.assert_called_once_with(log_level=50,
                                        log_path=None)

    mock_pipeline_run.assert_called_once_with(
        pipeline_name='blah',
        args_in=['ctx string', 'arb 2', 'arb3=arbvalue'],
        parse_args=True,
        py_dir='dir here',
        groups=None,
        success_group=None,
        failure_group=None
    )


def test_main_pass_with_defaults_context_positional():
    """Default values assigned - log 25 and cwd."""
    arg_list = ['blah',
                'ctx string']

    with patch('pypyr.pipelinerunner.run') as mock_pipeline_run:
        with patch('pypyr.log.logger.set_root_logger') as mock_logger:
            pypyr.cli.main(arg_list)

    mock_logger.assert_called_once_with(log_level=None,
                                        log_path=None)

    mock_pipeline_run.assert_called_once_with(
        pipeline_name='blah',
        args_in=['ctx string'],
        parse_args=True,
        py_dir=Path.cwd(),
        groups=None,
        success_group=None,
        failure_group=None
    )


def test_main_pass_with_no_context():
    """No context is None."""
    arg_list = ['blah']

    with patch('pypyr.pipelinerunner.run') as mock_pipeline_run:
        with patch('pypyr.log.logger.set_root_logger') as mock_logger:
            pypyr.cli.main(arg_list)

    mock_logger.assert_called_once_with(log_level=None,
                                        log_path=None)

    mock_pipeline_run.assert_called_once_with(
        pipeline_name='blah',
        args_in=[],
        parse_args=True,
        py_dir=Path.cwd(),
        groups=None,
        success_group=None,
        failure_group=None
    )


def test_main_pass_with_no_context_other_flags_set():
    """No context is None and other flag still work."""
    arg_list = ['blah',
                '--loglevel',
                '11']

    with patch('pypyr.pipelinerunner.run') as mock_pipeline_run:
        with patch('pypyr.log.logger.set_root_logger') as mock_logger:
            pypyr.cli.main(arg_list)

    mock_logger.assert_called_once_with(log_level=11,
                                        log_path=None)

    mock_pipeline_run.assert_called_once_with(
        pipeline_name='blah',
        args_in=[],
        parse_args=True,
        py_dir=Path.cwd(),
        groups=None,
        success_group=None,
        failure_group=None
    )


def test_pipeline_name_required():
    """Error expected if no pipeline name."""
    arg_list = ['--dir',
                'blah']

    with patch('pypyr.pipelinerunner.run'):
        with pytest.raises(SystemExit) as exit_err:
            pypyr.cli.main(arg_list)

        assert exit_err.value.code == 2


def test_interrupt_signal():
    """Interrupt signal handled."""
    arg_list = ['blah',
                'ctx string']

    with patch('pypyr.pipelinerunner.run') as mock_pipeline_run:
        mock_pipeline_run.side_effect = KeyboardInterrupt()
        val = pypyr.cli.main(arg_list)
        assert val == 130


def test_arb_error():
    """Arbitrary error should return 255."""
    arg_list = ['blah',
                'ctx string']

    with patch('pypyr.pipelinerunner.run') as mock_pipeline_run:
        mock_pipeline_run.side_effect = AssertionError('Test Error Mock')
        val = pypyr.cli.main(arg_list)
        assert val == 255


def test_trace_log_level_less_10():
    """Log Level < 10 produces traceback on error."""
    arg_list = ['blah',
                'ctx string',
                '--loglevel',
                '5']

    with patch('pypyr.pipelinerunner.run') as mock_pipeline_run:
        with patch('traceback.print_exc') as mock_traceback:
            mock_pipeline_run.side_effect = AssertionError('Test Error Mock')
            val = pypyr.cli.main(arg_list)
            assert val == 255

    mock_traceback.assert_called_once()


def test_trace_log_level_over_10():
    """Log Level > 10 doesn't produce traceback on error."""
    arg_list = ['blah',
                'ctx string',
                '--loglevel',
                '11']

    with patch('pypyr.pipelinerunner.run') as mock_pipeline_run:
        with patch('traceback.print_exc') as mock_traceback:
            mock_pipeline_run.side_effect = AssertionError('Test Error Mock')
            val = pypyr.cli.main(arg_list)
            assert val == 255

    mock_traceback.assert_not_called()


def test_trace_log_level_none():
    """Log Level None doesn't produce traceback on error."""
    arg_list = ['blah',
                'ctx string']

    with patch('pypyr.pipelinerunner.run') as mock_pipeline_run:
        with patch('traceback.print_exc') as mock_traceback:
            mock_pipeline_run.side_effect = AssertionError('Test Error Mock')
            val = pypyr.cli.main(arg_list)
            assert val == 255

    mock_traceback.assert_not_called()


def test_main_pass_with_logpath():
    """The logpath set to tempfile."""
    arg_list = ['blah',
                '--logpath',
                'tmp.log']

    with patch('pypyr.pipelinerunner.run') as mock_pipeline_run:
        with patch('pypyr.log.logger.set_root_logger') as mock_logger:
            pypyr.cli.main(arg_list)

    mock_logger.assert_called_once_with(log_level=None,
                                        log_path='tmp.log',)
    mock_pipeline_run.assert_called_once_with(
        pipeline_name='blah',
        args_in=[],
        parse_args=True,
        py_dir=Path.cwd(),
        groups=None,
        success_group=None,
        failure_group=None
    )
