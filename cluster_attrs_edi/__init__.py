# coding=utf-8
import sys

if sys.version_info > (3, 0):
    import importlib
    importlib.reload(sys)

    from .cluster_attrs_edi import *

    from .get_attr_names import *
    from .cluster_attr_names import *
else:
    reload(sys)
    sys.setdefaultencoding("UTF-8")

    from cluster_attrs_edi import *

    from get_attr_names import *
    from cluster_attr_names import *
