from .action_scheme import ActionScheme
from .dynamic_orders import DynamicOrders
from .managed_risk_orders import ManagedRiskOrders
from .future_action_strategy import FutureActionStrategy
from .future_position_strategy import FuturePositionStrategy

_registry = {
    'dynamic': DynamicOrders,
    'future': FutureActionStrategy(),
    'managed-risk': ManagedRiskOrders,
}


def get(identifier: str) -> ActionScheme:
    """Gets the `ActionScheme` that matches with the identifier.

    Arguments:
        identifier: The identifier for the `ActionScheme`

    Raises:
        KeyError: if identifier is not associated with any `ActionScheme`
    """
    if identifier not in _registry.keys():
        raise KeyError(f'Identifier {identifier} is not associated with any `ActionScheme`.')

    return _registry[identifier]()
