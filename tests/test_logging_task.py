import pytest
import logging
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from problems.logging_task import (
    task_0, task_1, task_2, task_3, task_4, task_5, task_6, task_7,
    task_8, task_9, task_10, task_11, task_12, task_13, task_14,
    task_15, task_16, task_17, task_18, task_19,
)


@pytest.fixture(autouse=True)
def cleanup_loggers():
    """Clean up loggers after each test to avoid state leakage."""
    yield
    for name in ["app", "parent", "parent.child", "no_propagate", "test_logger"]:
        logger = logging.getLogger(name)
        logger.handlers.clear()
        logger.filters.clear()
        logger.setLevel(logging.WARNING)
        logger.propagate = True


@pytest.fixture
def logger():
    lg = logging.getLogger("test_logger")
    lg.handlers.clear()
    lg.filters.clear()
    lg.setLevel(logging.DEBUG)
    return lg


# --- task_0: create logger ---

def test_task_0():
    result = task_0()
    assert isinstance(result, logging.Logger)
    assert result.name == "app"


# --- task_1: create logger with DEBUG level ---

def test_task_1():
    result = task_1()
    assert result.name == "app"
    assert result.level == logging.DEBUG


# --- task_2: add StreamHandler ---

def test_task_2(logger):
    task_2(logger)
    assert any(isinstance(h, logging.StreamHandler) for h in logger.handlers)


# --- task_3: add StreamHandler with Formatter ---

def test_task_3(logger):
    task_3(logger)
    stream_handlers = [h for h in logger.handlers if isinstance(h, logging.StreamHandler)]
    assert len(stream_handlers) >= 1
    handler = stream_handlers[-1]
    assert handler.formatter is not None
    assert "%(levelname)s" in handler.formatter._fmt
    assert "%(name)s" in handler.formatter._fmt
    assert "%(message)s" in handler.formatter._fmt


# --- task_4: log DEBUG ---

def test_task_4(logger, caplog):
    with caplog.at_level(logging.DEBUG, logger="test_logger"):
        task_4(logger, "debug message")
    assert "debug message" in caplog.text


# --- task_5: log INFO ---

def test_task_5(logger, caplog):
    with caplog.at_level(logging.DEBUG, logger="test_logger"):
        task_5(logger, "info message")
    assert "info message" in caplog.text


# --- task_6: log WARNING ---

def test_task_6(logger, caplog):
    with caplog.at_level(logging.DEBUG, logger="test_logger"):
        task_6(logger, "warning message")
    assert "warning message" in caplog.text


# --- task_7: log ERROR ---

def test_task_7(logger, caplog):
    with caplog.at_level(logging.DEBUG, logger="test_logger"):
        task_7(logger, "error message")
    assert "error message" in caplog.text


# --- task_8: log CRITICAL ---

def test_task_8(logger, caplog):
    with caplog.at_level(logging.DEBUG, logger="test_logger"):
        task_8(logger, "critical message")
    assert "critical message" in caplog.text


# --- task_9: add warning-only filter ---

def test_task_9(logger, caplog):
    task_9(logger)
    with caplog.at_level(logging.DEBUG, logger="test_logger"):
        logger.debug("should be filtered")
        logger.info("should be filtered too")
        logger.warning("should pass")
    assert "should be filtered" not in caplog.text
    assert "should pass" in caplog.text


# --- task_10: add FileHandler ---

def test_task_10(logger, tmp_path):
    filepath = str(tmp_path / "test.log")
    task_10(logger, filepath)
    file_handlers = [h for h in logger.handlers if isinstance(h, logging.FileHandler)]
    assert len(file_handlers) >= 1
    logger.warning("file test")
    for h in logger.handlers:
        h.flush()
    with open(filepath) as f:
        content = f.read()
    assert "file test" in content


# --- task_11: child logger ---

def test_task_11():
    result = task_11()
    assert result.name == "parent.child"
    assert result.parent.name == "parent"


# --- task_12: log with extra data ---

def test_task_12(logger, capsys):
    # Clear existing handlers
    logger.handlers.clear()
    task_12(logger)
    captured = capsys.readouterr()
    assert "User action" in captured.err or "User action" in captured.out


# --- task_13: log exception ---

def test_task_13(logger, caplog):
    with caplog.at_level(logging.DEBUG, logger="test_logger"):
        task_13(logger)
    assert "An error occurred" in caplog.text
    assert "test error" in caplog.text


# --- task_14: create configured logger ---

def test_task_14():
    result = task_14("test_configured", logging.ERROR)
    assert result.level == logging.ERROR
    assert len(result.handlers) >= 1
    handler = result.handlers[-1]
    assert handler.level == logging.ERROR
    assert "%(levelname)s" in handler.formatter._fmt
    # cleanup
    result.handlers.clear()


# --- task_15: no propagate ---

def test_task_15():
    result = task_15()
    assert result.name == "no_propagate"
    assert result.propagate is False


# --- task_16: remove all handlers ---

def test_task_16(logger):
    logger.addHandler(logging.StreamHandler())
    logger.addHandler(logging.StreamHandler())
    assert len(logger.handlers) >= 2
    task_16(logger)
    assert len(logger.handlers) == 0


# --- task_17: count handlers ---

def test_task_17(logger):
    logger.addHandler(logging.StreamHandler())
    logger.addHandler(logging.StreamHandler())
    assert task_17(logger) == 2


# --- task_18: effective level ---

def test_task_18(logger):
    logger.setLevel(logging.ERROR)
    assert task_18(logger) == logging.ERROR


# --- task_19: is enabled for DEBUG ---

def test_task_19_enabled(logger):
    logger.setLevel(logging.DEBUG)
    assert task_19(logger) is True

def test_task_19_disabled(logger):
    logger.setLevel(logging.ERROR)
    assert task_19(logger) is False
