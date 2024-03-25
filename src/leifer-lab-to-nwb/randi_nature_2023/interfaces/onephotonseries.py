"""Specific class for reading raw imaging data from the binary files of the pumpprobe format from the Leifer lab."""

from typing import Literal, Union

from neuroconv.datainterfaces.ophys.baseimagingextractorinterface import \
    BaseImagingExtractorInterface
from pynwb import NWBFile


class OnePhotonSeriesInterface(BaseImagingExtractorInterface):
    """Custom interface for automatically setting metadata and conversion options for this experiment."""

    ExtractorModuleName = "leifer_lab_to_nwb.randi_nature_2023.interfaces.binaryimagingextractor"  # TODO: propagate
    ExtractorName = "BinaryImagingExtractor"

    def get_metadata(self) -> dict:
        return super().get_metadata(photon_series_type="OnePhotonSeries")

    def get_metadata_schema(self) -> dict:
        return super().get_metadata(photon_series_type="OnePhotonSeries")

    def add_to_nwbfile(
        self,
        nwbfile: NWBFile,
        metadata: Union[dict, None] = None,
        photon_series_index: int = 0,
        stub_test: bool = False,
        stub_frames: int = 100,
    ) -> None:
        super().add_to_nwbfile(
            nwbfile=nwbfile,
            metadata=metadata,
            photon_series_index=photon_series_index,
            stub_test=stub_test,
            stub_frames=stub_frames,
            photon_series_type="OnePhotonSeries",
            parent_container="acquisition",
        )
