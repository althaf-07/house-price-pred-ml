import logging
from datetime import datetime
from pathlib import Path
from typing import Literal


def load_logger(
    name: str,
    filename: str,
    logs_dir: Path = Path("logs/"),
    file_logging: bool = True,
    console_logging: bool = True,
    logger_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "DEBUG",
    fh_log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "DEBUG",
    ch_log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "DEBUG",
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logger_level)

    if logger.handlers:
        return logger

    fmt = "{asctime}.{msecs:03.0f} | {levelname:<8} | {name}:{funcName}:{lineno} - {message}"
    datefmt = "%Y-%m-%d %H:%M:%S"
    style = "{"
    formatter = logging.Formatter(fmt, datefmt, style)

    if file_logging:
        logs_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_filename = logs_dir / f"{filename}_{timestamp}.log"
        fh = logging.FileHandler(log_filename, encoding="utf-8")
        fh.setLevel(fh_log_level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    if console_logging:
        ch = logging.StreamHandler()
        ch.setLevel(ch_log_level)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger
