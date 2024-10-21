"""Utility to determine whether the provided object is a valid SMILES string."""

from typing import Any
from rdkit.Chem import MolFromSmiles  # pylint: disable=import-error,no-name-in-module
from rdkit import RDLogger  # pylint: disable=import-error


def is_valid_smiles(smiles: Any) -> bool:
    """Determine whether the provided object is a valid SMILES string."""
    if not isinstance(smiles, str):
        return False

    RDLogger.DisableLog("rdApp.error")
    mol = MolFromSmiles(smiles)
    RDLogger.EnableLog("rdApp.error")
    return mol is not None
