# stupid-password-manager

Silly password manager for low security uses.

## Uses

As this won't really have much going for it security wise,
it'll probably only suit storing passwords for things that don't really matter.
This will be great for the miscellaneous accounts that some sites want you to make,
sites where you won't care if anything happens to it.

Main point is so that you don't have to enter a secure password to retrieve it.
Much like how some browser in-built passwords managers work,
relying on the fact that no one but you should have physical access to your device.

## Design

Will probably be based around storing passwords locally, most likely with SQLite.
From there, whether the passwords are encrypted or not can be considered,
but probably won't be for some time.

## Improvements

Basic Encryption would be good to have.

At the moment the passwords are being placed on the clipboard.
Would be good to be able to clear the clipboard after it is done.
Could use something like this.

```python
from ctypes import windll
if windll.user32.OpenClipboard(None):
    windll.user32.EmptyClipboard()
    windll.user32.CloseClipboard()
```
