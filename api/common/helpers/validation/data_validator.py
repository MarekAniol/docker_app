from common.helpers.validation.validation_strategies import ValidationStrategy
from common.errors.custom_errors import StrategyNotSetError
from common.logs.loggers import log_validation_errors


class DataValidator:
    def __init__(self, strategy=None) -> None:
        self.strategy = strategy

    def set_strategy(self, strategy: ValidationStrategy) -> None:
        self.strategy = strategy

    @log_validation_errors
    def validate(self, *args, **kwargs) -> None:
        if self.strategy is None:
            raise StrategyNotSetError()
        self.strategy.validate(*args, **kwargs)

data_validator = DataValidator()
