try:
    # Requires python3.8
    from functools import cached_property
except:
    from property_cached import cached_property

from functools import lru_cache