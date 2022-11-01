def extract_key(
    key: str,
    d: dict,
    types: list,
    optional: bool = False,
    default_value=None,
):
    if key not in d:
        if optional:
            return default_value
        raise Exception(f"{key} missing from {d}")
    val = d[key]
    if type(val) not in types:
        raise Exception(f"Type of {key} <<{val}>> is not in {types}")
    return val


def extract_save(d: dict) -> bool:
    if "save" in d:
        val = d["save"]
        if type(val) is not bool:
            raise Exception(f"the key save from {d} should be bool")
        return val
    return False
