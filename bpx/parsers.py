from .schema import BPX


def parse_bpx_obj(bpx: dict, v_tol: float = 0.001) -> BPX:
    """
    A convenience function to parse a bpx dict into a BPX model.

    Parameters
    ----------
    bpx: dict
        a dict object in bpx format
    v_tol: float
        absolute tolerance in [V] to validate the voltage limits, 1 mV by default

    Returns
    -------
    BPX: :class:`bpx.BPX`
        a parsed BPX model
    """
    if v_tol < 0:
        error_msg = "v_tol should not be negative"
        raise ValueError(error_msg)

    BPX.Settings.tolerances["Voltage [V]"] = v_tol

    return BPX.model_validate(bpx)


def parse_bpx_file(filename: str, v_tol: float = 0.001) -> BPX:
    """
    A convenience function to parse a bpx file into a BPX model.

    Parameters
    ----------
    filename: str
        a filepath to a bpx file
    v_tol: float
        absolute tolerance in [V] to validate the voltage limits, 1 mV by default

    Returns
    -------
    BPX: :class:`bpx.BPX`
        a parsed BPX model
    """

    from pathlib import Path

    bpx = ""
    if filename.endswith((".yml", ".yaml")):
        import yaml

        with Path(filename).open(encoding="utf-8") as f:
            bpx = yaml.safe_load(f)
    else:
        import json

        with Path(filename).open(encoding="utf-8") as f:
            bpx = json.loads(f.read())

    return parse_bpx_obj(bpx, v_tol)


def parse_bpx_str(bpx: str, v_tol: float = 0.001) -> BPX:
    """
    A convenience function to parse a json formatted string in bpx format into a BPX
    model.

    Parameters
    ----------
    bpx: str
        a json formatted string in bpx format
    v_tol: float
        absolute tolerance in [V] to validate the voltage limits, 1 mV by default

    Returns
    -------
    BPX:
        a parsed BPX model
    """
    import json

    bpx = json.loads(bpx)
    return parse_bpx_obj(bpx, v_tol)
