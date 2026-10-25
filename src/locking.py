from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime
from typing import Iterator, Optional
from uuid import uuid4


class LockBusy(RuntimeError):
    pass


class LockBackend:
    def set_if_absent(self, key: str, value: str, ttl_seconds: int) -> bool:
        raise NotImplementedError

    def delete_if_value(self, key: str, value: str) -> bool:
        raise NotImplementedError


class RedisMutex:
    def __init__(self, backend: LockBackend):
        self.backend = backend

    def acquire(self, key: str, ttl_seconds: int) -> Optional[str]:
        token = uuid4().hex
        if self.backend.set_if_absent(key, token, ttl_seconds):
            return token
        return None

    def release(self, key: str, token: str) -> bool:
        return self.backend.delete_if_value(key, token)

    @contextmanager
    def held(self, key: str, ttl_seconds: int) -> Iterator[str]:
        token = self.acquire(key, ttl_seconds)
        if token is None:
            raise LockBusy(key)
        try:
            yield token
        finally:
            self.release(key, token)


@dataclass(frozen=True)
class LeaseHandle:
    key: str
    token: str
    expires_at: datetime


class ExpiringSemaphore:
    def acquire(self, key: str, ttl_seconds: int) -> Optional[LeaseHandle]:
        raise NotImplementedError

    def release(self, handle: LeaseHandle) -> bool:
        raise NotImplementedError


class ReservationBroker:
    def reserve(self, key: str, ttl_seconds: int):
        raise NotImplementedError
