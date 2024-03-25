"""Generic class for reading imaging data from a binary file."""

import numpy
from pydantic import FilePath
from roiextractors import ImagingExtractor


# TODO: propagate
class BinaryImagingExtractor(ImagingExtractor):
    """A generic class for reading binary imaging data."""

    def __init__(
        self,
        *,
        file_path: FilePath,
        sampling_frequency: float,
        dtype: str,
        shape: Tuple[int, int, int],
        offset: int = 0,
        order: Literal["C", "F"] = "C"
    ) -> None:
        super().__init__(
            file_path=file_path,
            sampling_frequency=sampling_frequency,
            dtype=dtype,
            shape=shape,
            offset=offset,
            order=order,
        )
        self._memmap = numpy.memmap(filename=file_path, dtype=dtype, shape=shape, offset=offset, order=order, mode="r")

    def get_image_size(self) -> Tuple[int, int]:
        return self._kwargs["shape"][1:]

    def get_num_frames(self) -> int:
        return self._kwargs["shape"][0]

    def get_sampling_frequency(self) -> float:
        return self._kwargs["sampling_frequency"]

    def get_channel_names(self) -> list:
        raise NotImplementedError

    def get_num_channels(self) -> int:
        return 1

    def get_dtype(self) -> str:
        return self._kwargs["dtype"]

    def get_video(
        self, start_frame: Optional[int] = None, end_frame: Optional[int] = None, channel: int = 0
    ) -> np.ndarray:
        return self._memmap[start_frame:end_frame, ...]
