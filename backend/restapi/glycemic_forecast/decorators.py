import logging
import time
from functools import wraps

from .apps import GlycemicForecastConfig

logger = logging.getLogger(__name__)


def log_view(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        app_name = GlycemicForecastConfig.name
        method_name = view_func.__name__
        logger.info(f'[{app_name}] -> {method_name} started')
        start_time = time.time()

        try:
            response = view_func(request, *args, **kwargs)
            if response.exception:
                logger.error(f'[{app_name}] -> {method_name} failed with error: {str(response.exception)}')
        except Exception as e:
            logger.error(f'[{app_name}] -> {method_name} failed with error: {str(e)}')
            raise

        logger.info(f'[{app_name}] -> {method_name} finished in {time.time() - start_time:.3f}s')
        return response

    return wrapped_view
