"""Submodule to generate a BRICS DAG from a list of SMILES strings."""

from typing import Iterable
from multiprocessing import Pool
import pandas as pd
from tqdm.auto import tqdm
from rdkit.Chem import MolFromSmiles  # pylint: disable=import-error,no-name-in-module
from rdkit.Chem.BRICS import (
    BRICSDecompose,
)  # pylint: disable=import-error,no-name-in-module




class BRICSDAG:
    """Class to generate a BRICS DAG from a list of SMILES strings."""

    def __init__(
        self,
        include_smiles: bool = False,
        verbose: bool = False,
        n_jobs: int = 1,
    ):
        """Initialize the BRICS-DAG object.

        Parameters
        ----------
        include_smiles : bool = False
            Whether to include the SMILES strings in the output, by default False,
            which means we only include the BRICS fragments. Depending on the use
            cases and the dataset, SMILES strings may exactly match the BRICS fragments
            of other molecules.
        verbose : bool = False
            Whether to display a progress bar, by default False.
        n_jobs : int = 1
            Number of parallel jobs to run, by default 1.
        """
        self._include_smiles = include_smiles
        self._verbose = verbose
        self._n_jobs = n_jobs

    def fit(self, smiles: Iterable[str]):
        """Fit the BRICS-DAG to the provided SMILES strings."""

    def fit_path(self, path: str):
        """Creates an iterator from the provided path and fits the BRICS-DAG."""

    @classmethod
    def from_path(cls, path: str, verbose: bool = False):
        """Create a BRICS-DAG from a file containing SMILES strings."""

    @classmethod
    def from_version(cls, version: str, verbose: bool = False):
        """Create a BRICS-DAG froms a pre-rendered version."""
