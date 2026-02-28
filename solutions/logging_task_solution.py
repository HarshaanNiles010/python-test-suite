import logging
from typing import List, Optional


def task_0() -> logging.Logger:
    """
        Write a program that creates and returns a logger named "app".
    """
    return logging.getLogger("app")


def task_1() -> logging.Logger:
    """
        Write a program that creates a logger named "app" and sets its
        level to DEBUG. Return the logger.
    """
    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG)
    return logger


def task_2(logger: logging.Logger) -> None:
    """
        Write a program that adds a StreamHandler to the given logger.
    """
    logger.addHandler(logging.StreamHandler())


def task_3(logger: logging.Logger) -> None:
    """
        Write a program that adds a StreamHandler with a Formatter to the logger.
        The format string should be: "%(levelname)s:%(name)s:%(message)s"
    """
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(levelname)s:%(name)s:%(message)s"))
    logger.addHandler(handler)


def task_4(logger: logging.Logger, message: str) -> None:
    """
        Write a program that logs the message at DEBUG level using the logger.
    """
    logger.debug(message)


def task_5(logger: logging.Logger, message: str) -> None:
    """
        Write a program that logs the message at INFO level using the logger.
    """
    logger.info(message)


def task_6(logger: logging.Logger, message: str) -> None:
    """
        Write a program that logs the message at WARNING level using the logger.
    """
    logger.warning(message)


def task_7(logger: logging.Logger, message: str) -> None:
    """
        Write a program that logs the message at ERROR level using the logger.
    """
    logger.error(message)


def task_8(logger: logging.Logger, message: str) -> None:
    """
        Write a program that logs the message at CRITICAL level using the logger.
    """
    logger.critical(message)


def task_9(logger: logging.Logger) -> None:
    """
        Write a program that adds a filter to the logger that only allows
        records with level WARNING or above.
    """
    logger.addFilter(lambda record: record.levelno >= logging.WARNING)


def task_10(logger: logging.Logger, filepath: str) -> None:
    """
        Write a program that adds a FileHandler to the logger that writes
        to the given filepath.
    """
    logger.addHandler(logging.FileHandler(filepath))


def task_11() -> logging.Logger:
    """
        Write a program that creates a logger named "child" that is a child
        of a logger named "parent". Return the child logger.
    """
    return logging.getLogger("parent.child")


def task_12(logger: logging.Logger) -> None:
    """
        Write a program that logs a message with extra contextual data.
    """
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(levelname)s:%(name)s:%(message)s:%(user)s:%(action)s"))
    logger.addHandler(handler)
    logger.info("User action", extra={"user": "alice", "action": "login"})


def task_13(logger: logging.Logger) -> None:
    """
        Write a program that logs an exception using logger.exception().
    """
    try:
        raise ValueError("test error")
    except ValueError:
        logger.exception("An error occurred")


def task_14(name: str, level: int) -> logging.Logger:
    """
        Write a program that creates a logger with the given name, sets its
        level, adds a StreamHandler with level set to the same level, and
        applies the format "%(levelname)s - %(message)s". Return the logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
    logger.addHandler(handler)
    return logger


def task_15() -> logging.Logger:
    """
        Write a program that creates a logger named "no_propagate" and sets
        propagate to False. Return the logger.
    """
    logger = logging.getLogger("no_propagate")
    logger.propagate = False
    return logger


def task_16(logger: logging.Logger) -> None:
    """
        Write a program that removes all handlers from the given logger.
    """
    logger.handlers.clear()


def task_17(logger: logging.Logger) -> int:
    """
        Write a program that returns the number of handlers attached
        to the given logger.
    """
    return len(logger.handlers)


def task_18(logger: logging.Logger) -> int:
    """
        Write a program that returns the effective level of the logger.
    """
    return logger.getEffectiveLevel()


def task_19(logger: logging.Logger) -> bool:
    """
        Write a program that returns True if the logger is enabled for
        DEBUG level messages, False otherwise.
    """
    return logger.isEnabledFor(logging.DEBUG)
