# addons/my_module/models/my_model.py
import logging
_logger = logging.getLogger(__name__)

class MyModel(models.Model):
    _name = 'my.model'

    def create(self, vals):
        _logger.info("MyModel 생성: %s", vals)
        return super().create(vals)
