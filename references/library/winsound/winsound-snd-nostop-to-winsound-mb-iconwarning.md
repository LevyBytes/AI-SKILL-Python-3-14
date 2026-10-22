# winsound: Sound playback flags and message-beep constants

winsound.SND_NOSTOP

Leave any sounds already underway uninterrupted.

 winsound.SND_NOWAIT

Hand control back at once whenever the sound driver is occupied.

Note

This flag finds no support on present-day Windows platforms.

 winsound.SND_APPLICATION

Here the *sound* parameter is a registry alias specific to one application. You may pair this flag with the `SND_ALIAS` flag to point at an application-defined sound alias.

 winsound.SND_SENTRY

Fires off a SoundSentry event at the moment the sound sounds.

Added in version 3.14.

 winsound.SND_SYNC

Playback of the sound happens synchronously. That is what occurs by default.

Added in version 3.14.

 winsound.SND_SYSTEM

Route the sound into the audio session reserved for system notification sounds.

Added in version 3.14.

 winsound.MB_ICONASTERISK

Play the `SystemDefault` sound.

 winsound.MB_ICONEXCLAMATION

Play the `SystemExclamation` sound.

 winsound.MB_ICONHAND

Play the `SystemHand` sound.

 winsound.MB_ICONQUESTION

Play the `SystemQuestion` sound.

 winsound.MB_OK

Play the `SystemDefault` sound.

 winsound.MB_ICONERROR

Play the `SystemHand` sound.

Added in version 3.14.

 winsound.MB_ICONINFORMATION

Play the `SystemDefault` sound.

Added in version 3.14.

 winsound.MB_ICONSTOP

Play the `SystemHand` sound.

Added in version 3.14.

 winsound.MB_ICONWARNING

Play the `SystemExclamation` sound.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](winsound-beep-to-winsound-snd-nodefault.md) · [Owning module, declaration or section: winsound](winsound-beep-to-winsound-snd-nodefault.md)
