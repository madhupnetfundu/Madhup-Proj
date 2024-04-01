# disk_player.py

from enum import Enum, auto

class State(Enum):
    EMPTY = auto()
    STOPPED = auto()
    PAUSED = auto()
    PLAYING = auto()

class DiskPlayer:
    def __init__(self):
        self.state = State.EMPTY

    def insert_disk(self):
        if self.state is State.EMPTY:
            self.state = State.STOPPED
        else:
            raise ValueError("disk already inserted")

    def eject_disk(self):
        if self.state is State.EMPTY:
            raise ValueError("no disk inserted")
        else:
            self.state = State.EMPTY

    def play(self):
        if self.state in {State.STOPPED, State.PAUSED}:
            self.state = State.PLAYING

    def pause(self):
        if self.state is State.PLAYING:
            self.state = State.PAUSED
        else:
            raise ValueError("can't pause when not playing")

    def stop(self):
        if self.state in {State.PLAYING, State.PAUSED}:
            self.state = State.STOPPED
        else:
            raise ValueError("can't stop when not playing or paused")

if __name__ == "__main__":
    actions = [
        DiskPlayer.insert_disk,
        DiskPlayer.play,
        DiskPlayer.pause,
        DiskPlayer.stop,
        DiskPlayer.eject_disk,
        DiskPlayer.insert_disk,
        DiskPlayer.play,
        DiskPlayer.stop,
        DiskPlayer.eject_disk,
    ]
    player = DiskPlayer()
    for action in actions:
        action(player)
        print(player.state)

'''
 In the given code, `action(player)` is calling a method of the `DiskPlayer` class with `player` as an argument. The `actions` list contains references to methods of the `DiskPlayer` class.

Let's break down what happens at each iteration of the loop:

1. `action(player)` calls `DiskPlayer.insert_disk(player)`, which transitions the player's state from `State.EMPTY` to `State.STOPPED`.
2. `action(player)` calls `DiskPlayer.play(player)`, which transitions the player's state from `State.STOPPED` to `State.PLAYING`.
3. `action(player)` calls `DiskPlayer.pause(player)`, which transitions the player's state from `State.PLAYING` to `State.PAUSED`.
4. `action(player)` calls `DiskPlayer.stop(player)`, which transitions the player's state from `State.PAUSED` to `State.STOPPED`.
5. `action(player)` calls `DiskPlayer.eject_disk(player)`, which transitions the player's state from `State.STOPPED` to `State.EMPTY`.
6. `action(player)` calls `DiskPlayer.insert_disk(player)`, which transitions the player's state from `State.EMPTY` to `State.STOPPED`.
7. `action(player)` calls `DiskPlayer.play(player)`, which transitions the player's state from `State.STOPPED` to `State.PLAYING`.
8. `action(player)` calls `DiskPlayer.stop(player)`, which transitions the player's state from `State.PLAYING` to `State.STOPPED`.
9. `action(player)` calls `DiskPlayer.eject_disk(player)`, which transitions the player's state from `State.STOPPED` to `State.EMPTY`.

After each action, `print(player.state)` prints the current state of the player. So, the loop iterates through the list of actions, and at each step, it performs the action on the player and prints the player's state.
'''