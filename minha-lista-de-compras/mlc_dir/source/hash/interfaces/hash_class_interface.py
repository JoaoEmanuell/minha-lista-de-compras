from abc import ABC, abstractmethod


class HashInterface(ABC):
    """Class responsible to manage hash."""

    @abstractmethod
    def generate_hash(self, value: str) -> str:
        """Generate hash from value

        Args:
            value (str): Value to generate a hash

        Returns:
            str: Hash generated by value
        """
        raise NotImplementedError()

    @abstractmethod
    def compare_hash(self, value: str, hash: str) -> bool:
        """Compare hash generated by generate_hash

        Args:
            value (str): Value to generate a hash
            hash (str): Hash generated by generate_hash

        Returns:
            bool: true if value corresponding to hash, else false
        """
        raise NotImplementedError()
