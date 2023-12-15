# Modified from transformers/models/gpt_neox/__init__.py

from typing import TYPE_CHECKING

from ...file_utils import _LazyModule, is_torch_available
from ...utils import OptionalDependencyNotAvailable

_import_structure = {"configuration_mamba": ["MAMBA_PRETRAINED_CONFIG_ARCHIVE_MAP", "MambaConfig"]}

try:
    if not is_torch_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["modeling_mamba"] = [
        "Mamba",
        "MambaModel",
        "MambaForCausalLM",
        "MambaPreTrainedModel",
    ]

if TYPE_CHECKING:
    from .configuration_mamba import MAMBA_PRETRAINED_CONFIG_ARCHIVE_MAP, MambaConfig

    try:
        if not torch_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .modering_mamba import (
            Mamba,
            MambaModel,
            MambaForCausalLM,
            MambaPreTrainedModel,
        )

else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure, module_spec=__spec__)
