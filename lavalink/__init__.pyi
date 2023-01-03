"""
This type stub file was generated by pyright.
"""

import typing as t

from .client import Client as Client
from .errors import (
    AuthenticationError as AuthenticationError,
    InvalidTrack as InvalidTrack,
    LoadError as LoadError,
    NodeError as NodeError,
)
from .events import (
    Event,
    NodeChangedEvent as NodeChangedEvent,
    NodeConnectedEvent as NodeConnectedEvent,
    NodeDisconnectedEvent as NodeDisconnectedEvent,
    PlayerUpdateEvent as PlayerUpdateEvent,
    QueueEndEvent as QueueEndEvent,
    TrackEndEvent as TrackEndEvent,
    TrackExceptionEvent as TrackExceptionEvent,
    TrackLoadFailedEvent as TrackLoadFailedEvent,
    TrackStartEvent as TrackStartEvent,
    TrackStuckEvent as TrackStuckEvent,
    WebSocketClosedEvent as WebSocketClosedEvent,
)
from .filters import (
    ChannelMix as ChannelMix,
    Equalizer as Equalizer,
    Filter as Filter,
    Karaoke as Karaoke,
    LowPass as LowPass,
    Rotation as Rotation,
    Timescale as Timescale,
    Tremolo as Tremolo,
    Vibrato as Vibrato,
    Volume as Volume,
)
from .models import (
    AudioTrack as AudioTrack,
    BasePlayer as BasePlayer,
    DefaultPlayer as DefaultPlayer,
    DeferredAudioTrack as DeferredAudioTrack,
    LoadResult as LoadResult,
    LoadType as LoadType,
    PlaylistInfo as PlaylistInfo,
    Plugin as Plugin,
    Source as Source,
)
from .node import Node as Node
from .nodemanager import NodeManager as NodeManager
from .playermanager import PlayerManager as PlayerManager
from .stats import Penalty as Penalty, Stats as Stats
from .utils import (
    decode_track as decode_track,
    encode_track as encode_track,
    format_time as format_time,
    parse_time as parse_time,
    timestamp_to_millis as timestamp_to_millis,
)

_EventT = t.TypeVar('_EventT', bound=Event)
_EventT2 = t.TypeVar('_EventT2', bound=Event)
_EventT3 = t.TypeVar('_EventT3', bound=Event)

HookSig = t.Callable[[_EventT], None]
ListenerSig = t.Callable[[_EventT], None]

def enable_debug_logging(submodule: str = ...) -> None:
    """
    Sets up a logger to stdout. This solely exists to make things easier for
    end-users who want to debug issues with Lavalink.py.

    Parameters
    ----------
    module: :class:`str`
        The module to enable logging for. ``None`` to enable debug logging for
        the entirety of Lavalink.py.

        Example: ``lavalink.enable_debug_logging('websocket')``
    """
    ...

@t.overload
def listener() -> ListenerSig[Event]: ...
@t.overload
def listener(event: _EventT) -> ListenerSig[_EventT]: ...
@t.overload
def listener(event: _EventT, event2: _EventT2) -> ListenerSig[_EventT | _EventT2]: ...
@t.overload
def listener(
    event: _EventT, event2: _EventT2, event3: _EventT3
) -> ListenerSig[_EventT | _EventT2 | _EventT3]: ...
def listener(*events: _EventT) -> ListenerSig[_EventT]:
    """
    Marks this function as an event listener for Lavalink.py.
    This **must** be used on class methods, and you must ensure that you register
    decorated methods by using :func:`Client.add_event_hooks`.

    Example:

    ```py
    @listener()
    async def on_lavalink_event(self, event):  # Event can be ANY Lavalink event
        ...

    @listener(TrackStartEvent)
    async def on_track_start(self, event: TrackStartEvent):
        ...
    ```

    Note
    ----
    Track event dispatch order is not guaranteed!
    For example, this means you could receive a :class:`TrackStartEvent` before you receive a
    :class:`TrackEndEvent` when executing operations such as ``skip()``.

    Parameters
    ----------
    events: List[:class:`Event`]
        The events to listen for. Leave this empty to listen for all events.
    """
    ...

@t.overload
def add_event_hook(*hooks: HookSig[Event]) -> None: ...
@t.overload
def add_event_hook(*hooks: HookSig[_EventT], event: _EventT = ...) -> None: ...
def add_event_hook(*hooks: HookSig[_EventT], event: t.Optional[_EventT] = ...) -> None:
    """
    Adds an event hook to be dispatched on an event.

    Note
    ----
    Track event dispatch order is not guaranteed!
    For example, this means you could receive a :class:`TrackStartEvent` before you receive a
    :class:`TrackEndEvent` when executing operations such as ``skip()``.

    Parameters
    ----------
    hooks: :class:`function`
        The hooks to register for the given event type.
        If ``event`` parameter is left empty, then it will run when any event is dispatched.
    event: :class:`Event`
        The event the hook belongs to. This will dispatch when that specific event is
        dispatched. Defaults to ``None`` which means the hook is dispatched on all events.
    """
    ...
