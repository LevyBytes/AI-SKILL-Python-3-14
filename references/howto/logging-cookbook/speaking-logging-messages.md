# Speaking logging messages

### Speaking logging messages

There may be cases where you'd prefer logging messages delivered audibly rather than visibly. This is straightforward when text-to-speech (TTS) capability exists on your system, even without a Python binding for it. The majority of TTS systems offer a command line program you can launch, and a handler can call it through [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess). We assume here that TTS command line programs neither expect to interact with users nor take long to finish, that logged messages won't arrive often enough to overwhelm the user, and that having the messages spoken one after another rather than at once is acceptable, The sample implementation below waits for each message to finish being spoken before processing the next, which could leave other handlers waiting. Here's a brief example of the approach, presuming the `espeak` TTS package is on hand:

```python
import logging
import subprocess
import sys

class TTSHandler(logging.Handler):
    def emit(self, record):
        msg = self.format(record)
        # Speak slowly in a female English voice
        cmd = ['espeak', '-s150', '-ven+f3', msg]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        # wait for the program to finish
        p.communicate()

def configure_logging():
    h = TTSHandler()
    root = logging.getLogger()
    root.addHandler(h)
    # the default formatter just returns the message
    root.setLevel(logging.DEBUG)

def main():
    logging.info('Hello')
    logging.debug('Goodbye')

if __name__ == '__main__':
    configure_logging()
    sys.exit(main())

```

Once run, this script should pronounce “Hello” and afterward “Goodbye” in a female voice.

The approach above can, naturally, be adjusted to other TTS systems and even to wholly different systems able to process messages through external programs launched from a command line.

[Subject index](INDEX.md) · [Previous source context](customized-exception-formatting.md) · [Following source context](buffering-logging-messages-and-outputting-them-conditionally.md)
